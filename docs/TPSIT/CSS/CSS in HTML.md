# Collegare CSS a HTML

Il CSS può essere inserito in tre modi: inline (`style`), in un blocco `<style>` nel documento o in un foglio esterno. Per un sito con più pagine, il file esterno è normalmente la scelta più manutenibile.

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

```css
body {
  font-family: system-ui, sans-serif;
  line-height: 1.5;
}
```

Il percorso nel `href` deve essere corretto; un CSS caricato male può essere verificato nella scheda Network degli strumenti per sviluppatori del browser. Vedi [CSS](index.md) per cascata, selettori e layout.
