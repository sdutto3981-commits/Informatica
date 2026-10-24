# Introduzione a HTML

HTML significa **HyperText Markup Language**. È un linguaggio di marcatura, non un linguaggio di programmazione: usa elementi e attributi per descrivere la struttura e il significato dei contenuti. Il browser interpreta il documento e costruisce il DOM.

## Documento minimo

```html
<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Prima pagina</title>
</head>
<body>
  <h1>Ciao, web</h1>
  <p>Questa è la prima pagina.</p>
</body>
</html>
```

- `<!doctype html>` attiva la modalità standard HTML moderna.
- `<html lang="it">` è l'elemento radice e dichiara la lingua principale.
- `<head>` contiene metadati, titolo e riferimenti a risorse.
- `<body>` contiene i contenuti mostrati nella pagina.
- Un elemento di solito comprende tag di apertura, contenuto e tag di chiusura; alcuni elementi, come `img` e `meta`, sono void e non hanno tag di chiusura.

Il significato del tag va preferito alla scelta di elementi generici: per questo HTML5 comprende elementi semantici come `header`, `nav`, `main`, `article` e `footer`.
