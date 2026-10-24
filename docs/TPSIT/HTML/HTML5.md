# HTML5 e semantica

HTML definisce la struttura del documento; la semantica aiuta browser, tecnologie assistive e sviluppatori a comprenderne le aree. Non è necessario usare un `div` per ogni contenitore: scegli un elemento in base alla funzione.

```html
<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Il mio sito</title>
</head>
<body>
  <header>
    <h1>Titolo del sito</h1>
    <nav aria-label="Navigazione principale">
      <a href="index.html">Home</a>
      <a href="contatti.html">Contatti</a>
    </nav>
  </header>
  <main>
    <article>
      <h2>Un articolo</h2>
      <p>Contenuto principale.</p>
    </article>
    <aside>Informazioni correlate.</aside>
  </main>
  <footer><p>Informazioni finali.</p></footer>
</body>
</html>
```

## Elementi semantici

- `header`: intestazione di una pagina o di una sezione.
- `nav`: area con collegamenti di navigazione importanti.
- `main`: contenuto principale della pagina; normalmente c'è un solo `main` visibile.
- `section`: sezione tematica, di norma con un titolo.
- `article`: contenuto autonomo, potenzialmente riutilizzabile o distribuibile separatamente.
- `aside`: contenuto complementare o correlato.
- `footer`: informazioni finali di una pagina o sezione.

Gli elementi semantici non assegnano automaticamente un layout: l'aspetto viene controllato con CSS. L'indentazione è una convenzione di leggibilità, non cambia il significato del codice.
