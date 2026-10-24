# Elementi semantici HTML5

Un elemento semantico comunica il ruolo del contenuto sia a chi legge il codice sia alle tecnologie che ne interpretano la struttura. La semantica, da sola, non rende automaticamente una pagina accessibile: bisogna usare titoli, etichette e alternative testuali corrette.

| Elemento | Uso tipico |
|---|---|
| `header` | intestazione di pagina o sezione |
| `nav` | blocco con link di navigazione principali |
| `main` | contenuto centrale e distintivo della pagina |
| `section` | raggruppamento tematico, spesso con un titolo |
| `article` | contenuto autonomo, come un articolo o una scheda indipendente |
| `aside` | contenuto correlato o laterale |
| `footer` | informazioni finali, autore o collegamenti secondari |
| `figure` / `figcaption` | contenuto illustrativo e relativa didascalia |
| `time` | data o ora leggibile dalla macchina tramite `datetime` |

## Esempio

```html
<main>
  <article>
    <header>
      <h2>Il mio progetto</h2>
      <p>Pubblicato il <time datetime="2026-10-24">24 ottobre 2026</time></p>
    </header>
    <figure>
      <img src="robot.jpg" alt="Prototipo di robot su un banco di lavoro">
      <figcaption>Prototipo durante il test.</figcaption>
    </figure>
    <p>Descrizione del progetto.</p>
  </article>
</main>
```

## Errori da evitare

- Usare `section` come sostituto universale di `div` anche quando non c'è una sezione tematica.
- Usare `nav` per ogni singolo link: serve a raggruppare blocchi di navigazione.
- Saltare i livelli dei titoli soltanto per ottenere una dimensione diversa; l'aspetto va modificato con CSS.
- Inserire più elementi `main` visibili come contenuto principale dello stesso documento.

## Riferimento

[W3Schools — HTML Semantic Elements](https://www.w3schools.com/html/html5_semantic_elements.asp)
