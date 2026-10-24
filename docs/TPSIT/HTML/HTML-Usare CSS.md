# Collegare CSS a HTML

Il CSS controlla la presentazione della pagina. HTML e CSS possono essere collegati in tre modi, ma per progetti multipagina il foglio esterno è normalmente la scelta più manutenibile.

## CSS esterno (consigliato)

Nel file HTML, all'interno di `head`:

```html
<link rel="stylesheet" href="styles.css">
```

Nel file `styles.css`:

```css
body {
  font-family: system-ui, sans-serif;
  line-height: 1.5;
}

h1 { color: #2457a7; }
```

Il percorso di `href` è relativo al file HTML. Se il foglio si trova in una cartella `css`, il percorso potrebbe essere `css/styles.css`.

## CSS interno

```html
<head>
  <style>
    body { margin: 0; }
    h1 { color: navy; }
  </style>
</head>
```

È adatto a dimostrazioni o a pagine molto piccole, ma rende più difficile condividere e mantenere lo stile tra più documenti.

## CSS inline

```html
<p style="color: navy;">Testo di esempio</p>
```

L'attributo `style` applica dichiarazioni a un singolo elemento. Per layout riutilizzabili, preferisci classi nel foglio di stile.

## Cascata

Se più regole applicano la stessa proprietà, il browser risolve i conflitti in base a cascata, specificità e ordine. L'attributo inline spesso prevale sulle normali regole di autore, perciò un abuso degli stili inline complica la manutenzione.

## Riferimento

[W3Schools — HTML CSS](https://www.w3schools.com/html/html_css.asp)
