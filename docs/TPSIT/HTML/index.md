# HTML e HTML5

HTML descrive la struttura e il significato dei contenuti di una pagina web; CSS ne definisce la presentazione e JavaScript aggiunge interattività.

## Percorso

- [Introduzione HTML](Introduzione%20HTML.md)
- [HTML5 e struttura semantica](HTML5.md)
- [Attributi HTML](Attributi%20HTML.md)
- [Paragrafi](Paragrafi%20HTML.md) e [intestazioni](Intestazioni%20HTML.md)
- [Link](Link%20HTML.md), [URL assoluti e relativi](URL%20assoluti%20vs%20URL%20relativi%20HTML.md)
- [Immagini](Immagini%20HTML.md) e [attributo alt](Attributo%20alt%20HTML.md)
- [Form](HTML%20Forms.md), [radio button](Radio%20button.md), [checkbox](Checkboxes%20button.md)
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
  <main>
    <p>Contenuto principale.</p>
  </main>
  <footer>Informazioni finali</footer>
</body>
</html>
```

## Regole essenziali

- Usa un solo titolo principale `h1` per identificare il contenuto della pagina e mantieni una gerarchia coerente dei sottotitoli.
- Le immagini informative devono avere un testo alternativo `alt` adeguato.
- Ogni campo di un form deve avere un'etichetta associata.
- Usa un link per navigare e un pulsante per compiere un'azione.
- Specifica `lang="it"` quando il contenuto principale è in italiano.

Confronta gli argomenti con il [programma TPSIT](../../Programmi/tpsit.md).
