# HTML

HTML definisce la **struttura e il significato** dei contenuti di una pagina. CSS ne controlla la presentazione, mentre JavaScript può aggiungere comportamento e interattività.

## Percorso consigliato

1. [Introduzione e struttura del documento](Introduzione%20HTML.md)
2. [HTML5 e struttura semantica](HTML5.md) · [Elementi semantici](Elementi%20semantici%20HTML5.md)
3. [Link, percorsi e immagini](Link%20percorsi%20e%20immagini%20HTML.md)
4. [Liste e tabelle](Liste%20e%20tabelle%20HTML.md)
5. [Form e validazione](Form%20e%20validazione%20HTML.md)
6. [Media e iframe](Media%20e%20iframe%20HTML.md)
7. [Classi, ID e layout](Classi%20ID%20e%20layout%20HTML.md)
8. [Canvas e SVG](Canvas%20e%20SVG%20HTML.md)
9. [Attributi globali e accessibilità](Attributi%20globali%20e%20accessibilit%C3%A0%20HTML.md)
10. [Collegare CSS a HTML](HTML-Usare%20CSS.md)

## Struttura minima

```html
<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>La mia pagina</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <header><h1>Titolo</h1></header>
  <main><p>Contenuto principale.</p></main>
  <footer>Informazioni finali</footer>
</body>
</html>
```

## Da ricordare

- I tag HTML descrivono contenuti e struttura; non sono comandi di programmazione.
- Gli attributi specificano proprietà dell'elemento, per esempio `href`, `src`, `alt`, `id` e `class`.
- Usa un elemento per il suo significato, non soltanto per l'aspetto grafico.
- La validazione HTML aiuta a individuare errori di struttura, ma non garantisce da sola accessibilità o qualità.

## Fonte di approfondimento

- [W3Schools — HTML Tutorial](https://www.w3schools.com/html/)
- [W3Schools — HTML Reference](https://www.w3schools.com/tags/)
