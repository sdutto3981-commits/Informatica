# HTML e HTML5

HTML descrive la struttura e il significato dei contenuti; CSS cura la presentazione e JavaScript aggiunge interattività.

## Percorso

- [Introduzione HTML](Introduzione%20HTML.md)
- [Struttura e semantica HTML5](HTML5.md) e [elementi semantici](Elementi%20semantici%20HTML5.md)
- [Attributi HTML](Attributi%20HTML.md), [attributi globali e accessibilità](Attributi%20globali%20e%20accessibilit%C3%A0%20HTML.md)
- [Titoli](Intestazioni%20HTML.md), [paragrafi](Paragrafi%20HTML.md), [liste e tabelle](Liste%20e%20tabelle%20HTML.md)
- [Link](Link%20HTML.md), [URL assoluti e relativi](URL%20assoluti%20vs%20URL%20relativi%20HTML.md)
- [Immagini](Immagini%20HTML.md) e [attributo alt](Attributo%20alt%20HTML.md)
- [Form](HTML%20Forms.md), [form e validazione](Form%20e%20validazione%20HTML.md)
- [Audio, video e iframe](Media%20e%20iframe%20HTML.md)
- [CSS in HTML](HTML-Usare%20CSS.md)

## Struttura semantica minima

```html
<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Titolo descrittivo</title>
</head>
<body>
  <header><h1>Titolo della pagina</h1></header>
  <main><p>Contenuto principale.</p></main>
  <footer>Informazioni finali</footer>
</body>
</html>
```

## Regole essenziali

- Usa titoli in ordine gerarchico e landmark semantici appropriati.
- Le immagini informative hanno bisogno di un `alt` significativo; quelle decorative possono avere `alt=""`.
- Associa un'etichetta a ogni campo di un form.
- Usa un link per navigare e un pulsante per compiere un'azione.
- Specifica la lingua principale con `lang="it"` quando il testo è in italiano.

