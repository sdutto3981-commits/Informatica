# Appunti di informatica

Documentazione tecnica in italiano, organizzata in quattro aree: Informatica, Sistemi, TPSIT e Telecomunicazioni.

## Anteprima locale

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

Apri l'indirizzo locale mostrato da MkDocs nel terminale.

## Controlli prima del commit

```bash
python audit_repo.py --repo .
git diff --check
mkdocs build
```

L'audit segnala link interni, riferimenti Obsidian rimasti, asset mancanti e anomalie comuni. I risultati richiedono revisione: i collegamenti contenuti dentro esempi di codice non sono necessariamente link reali.

## Pubblicazione

Il workflow `.github/workflows/docs.yml` costruisce il sito e lo pubblica con GitHub Pages Actions. In **Settings → Pages → Build and deployment**, seleziona **GitHub Actions** come sorgente di pubblicazione.

## Modificare gli appunti

- Mantieni una pagina per argomento principale, ma non spezzare una trattazione specialistica in frammenti privi di contesto.
- Per una modifica editoriale preserva definizioni, casi limite, formule, tabelle ed esempi validi; migliora la struttura senza ridurre la profondità.
- Usa link Markdown relativi e immagini versionate in `docs/assets/`.
- Per schemi digitali semplici sono preferibili SVG o Mermaid conservati nel repository rispetto a immagini remote instabili.
