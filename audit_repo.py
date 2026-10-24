#!/usr/bin/env python3
"""Audit local Markdown/MkDocs documentation for broken links and migration remnants."""
from __future__ import annotations

import argparse
import os
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit


def key(text: str) -> str:
    text = re.sub(r"\s+\{#[^}]+\}\s*$", "", text.strip())
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def split_markdown_blocks(text: str):
    """Yield (line_number, line, in_fence) and leave fenced samples alone."""
    in_fence = False
    for number, line in enumerate(text.splitlines(), 1):
        if re.match(r"^\s*(```|~~~)", line):
            yield number, line, in_fence
            in_fence = not in_fence
        else:
            yield number, line, in_fence


def main() -> int:
    parser = argparse.ArgumentParser(description="Controlla link, immagini, ancore e residui Obsidian nel repository MkDocs.")
    parser.add_argument("--repo", default=".", help="Root locale del repository")
    parser.add_argument("--output", default="AUDIT_LINKS.md", help="Nome report Markdown relativo alla root")
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    docs = root / "docs"
    if not docs.is_dir():
        print(f"ERRORE: docs/ non trovata sotto {root}")
        return 2

    files = sorted(docs.rglob("*.md"))
    by_rel = {p.relative_to(root).as_posix(): p for p in files}
    headings: dict[str, set[str]] = {}
    explicit_ids: dict[str, set[str]] = {}
    for rel, path in by_rel.items():
        content = path.read_text(encoding="utf-8-sig", errors="replace")
        headings[rel] = set()
        explicit_ids[rel] = set()
        for _, line, in_fence in split_markdown_blocks(content):
            if in_fence:
                continue
            match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
            if not match:
                continue
            value = match.group(1).strip()
            id_match = re.search(r"\s+\{#([^}]+)\}\s*$", value)
            if id_match:
                explicit_ids[rel].add(id_match.group(1))
                value = value[:id_match.start()].strip()
            value = re.sub(r"\s+#+\s*$", "", value)
            headings[rel].add(key(value))

    broken_links: list[tuple[str, int, str]] = []
    broken_anchors: list[tuple[str, int, str, str]] = []
    broken_images: list[tuple[str, int, str]] = []
    unresolved_wiki: list[tuple[str, int, str]] = []
    obsidian_callouts: list[tuple[str, int, str]] = []
    odd_fences: list[str] = []
    placeholders: list[str] = []
    empty_refs: list[str] = []

    for rel, path in by_rel.items():
        content = path.read_text(encoding="utf-8-sig", errors="replace")
        lines = content.splitlines()
        if len(re.findall(r"^\s*(```|~~~)", content, flags=re.M)) % 2:
            odd_fences.append(rel)
        if "{{date}}" in content or re.search(r"(?im)^\s*(TODO|FIXME|TBD)\b", content):
            placeholders.append(rel)
        if re.search(r"(?im)^##\s+Riferimenti2?\s*\n\s*1\.\s*$", content):
            empty_refs.append(rel)

        for number, line, in_fence in split_markdown_blocks(content):
            if in_fence:
                continue
            if re.search(r"(?<!!)!?\[\[[^\]]+\]\]", line):
                for item in re.finditer(r"(?<!!)\[\[([^\]]+)\]\]", line):
                    unresolved_wiki.append((rel, number, item.group(1)))
            callout = re.match(r"^\s*>\s*\[!([A-Za-z]+)\]", line)
            if callout:
                obsidian_callouts.append((rel, number, callout.group(1)))

            for match in re.finditer(r"(!?)\[[^\]]*\]\(([^)]+)\)", line):
                is_image = bool(match.group(1))
                raw_target = match.group(2).strip().split()[0].strip("<>")
                if re.match(r"^(?:https?:|mailto:|tel:|data:|javascript:)", raw_target, re.I):
                    continue
                parsed = urlsplit(raw_target)
                target = unquote(parsed.path)
                fragment = unquote(parsed.fragment)
                candidate: Path
                if not target:
                    candidate = path
                    target_rel = rel
                else:
                    candidate = (path.parent / target).resolve()
                    try:
                        target_rel = candidate.relative_to(root).as_posix()
                    except ValueError:
                        (broken_images if is_image else broken_links).append((rel, number, raw_target))
                        continue
                if not candidate.exists():
                    (broken_images if is_image else broken_links).append((rel, number, raw_target))
                    continue
                if is_image and candidate.suffix.lower() == ".md":
                    broken_images.append((rel, number, raw_target + " (immagine collegata a Markdown)"))
                    continue
                if fragment and candidate.suffix.lower() == ".md":
                    target_rel = candidate.relative_to(root).as_posix()
                    anchors = explicit_ids.get(target_rel, set())
                    # Markdown heading slugs and explicit attr_list IDs are both accepted.
                    if fragment not in anchors and key(fragment) not in headings.get(target_rel, set()) and key(fragment) not in {key(a) for a in anchors}:
                        broken_anchors.append((rel, number, raw_target, target_rel))

    cfg_path = root / "mkdocs.yml"
    cfg = cfg_path.read_text(encoding="utf-8", errors="replace") if cfg_path.exists() else ""
    expand = bool(re.search(r"(?m)^\s*-\s*navigation\.expand\s*$", cfg))
    prune = bool(re.search(r"(?m)^\s*-\s*navigation\.prune\s*$", cfg))
    local_js = []
    for match in re.finditer(r"(?m)^\s*-\s*([\w./-]+\.js)\s*$", cfg):
        asset = docs / match.group(1)
        if not asset.exists():
            local_js.append(match.group(1))
    workflow_count = len(list((root / ".github/workflows").glob("*.yml"))) + len(list((root / ".github/workflows").glob("*.yaml"))) if (root / ".github/workflows").exists() else 0

    report = [
        "# Audit locale Markdown/MkDocs", "", f"Root: `{root}`", f"File Markdown: {len(files)}", "",
        f"Link Markdown relativi mancanti: {len(broken_links)}",
        f"Link con ancora potenzialmente mancante: {len(broken_anchors)}",
        f"Immagini problematiche: {len(broken_images)}",
        f"Link Obsidian residui: {len(unresolved_wiki)}",
        f"Callout Obsidian da migrare: {len(obsidian_callouts)}",
        f"Blocchi di codice con delimitatori dispari: {len(odd_fences)}",
        f"File con token/placeholder: {len(placeholders)}",
        f"File con sezione Riferimenti vuota: {len(empty_refs)}",
        f"Script JavaScript locali mancanti: {len(local_js)}", f"Workflow YAML attivi in .github/workflows: {workflow_count}", "",
        f"Polyfill.io in mkdocs.yml: {'sì' if 'polyfill.io' in cfg else 'no'}",
        f"navigation.expand presente: {'sì' if expand else 'no'}",
        f"navigation.prune presente: {'sì' if prune else 'no'}",
        f"Conflitto expand/prune: {'SÌ' if expand and prune else 'no'}", "",
    ]

    def section(title: str, items: list, fmt) -> None:
        report.extend([f"## {title}", ""])
        report.extend(fmt(item) for item in items) if items else report.append("- Nessun problema rilevato.")
        report.append("")

    section("Link relativi mancanti", broken_links, lambda x: f"- `{x[0]}:{x[1]}` → `{x[2]}`")
    section("Ancore da verificare", broken_anchors, lambda x: f"- `{x[0]}:{x[1]}` → `{x[2]}` (destinazione `{x[3]}`)")
    section("Immagini problematiche", broken_images, lambda x: f"- `{x[0]}:{x[1]}` → `{x[2]}`")
    section("Link Obsidian residui", unresolved_wiki, lambda x: f"- `{x[0]}:{x[1]}` → `[[{x[2]}]]`")
    section("Callout Obsidian residui", obsidian_callouts, lambda x: f"- `{x[0]}:{x[1]}` → `[!{x[2]}]`")
    section("Altri controlli", [("Fences dispari", odd_fences), ("Token/placeholder", placeholders), ("Riferimenti vuoti", empty_refs), ("Script locali mancanti", local_js)], lambda x: f"### {x[0]}: {len(x[1])}\n" + ("\n".join(f"- `{v}`" for v in x[1]) if x[1] else "- Nessuno"))

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"Audit salvato: {output}")
    print(f"Markdown={len(files)}, links={len(broken_links)}, anchors={len(broken_anchors)}, images={len(broken_images)}, wiki={len(unresolved_wiki)}, callouts={len(obsidian_callouts)}")
    return 1 if (broken_links or broken_anchors or broken_images or odd_fences or placeholders or (expand and prune) or local_js or unresolved_wiki or obsidian_callouts or empty_refs) else 0


if __name__ == "__main__":
    raise SystemExit(main())
