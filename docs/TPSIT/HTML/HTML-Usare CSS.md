# Collegare CSS a HTML

Ci sono tre modi comuni per applicare regole CSS, ma nei progetti organizzati è preferibile un foglio esterno.

## Stile in linea

```html
<h1 style="color: navy;">Titolo</h1>
```

È rapido per una prova, ma mescola contenuto e presentazione e rende più difficile mantenere uno stile coerente.

## Foglio interno

```html
<head>
  <style>
    body { font-family: sans-serif; }
    h1 { color: navy; }
  </style>
</head>
```

Le regole si applicano a quel documento.

## Foglio esterno (consigliato)

Nel file HTML:

```html
<link rel="stylesheet" href="styles.css">
```

Nel file `styles.css`:

```css
body { font-family: system-ui, sans-serif; }
h1 { color: navy; }
```

Il percorso `href` deve puntare al file corretto. Un foglio esterno può essere condiviso da più pagine e mantenere separate struttura e presentazione. Consulta la sezione [CSS](../CSS/index.md) per selettori, box model, Flexbox e responsive design.
