# Elementi semantici HTML5

Gli elementi semantici comunicano il ruolo del contenuto sia alle persone sia agli strumenti che lo interpretano. Usarli correttamente migliora struttura, manutenzione e accessibilità.

## Elementi principali

- `header`: intestazione della pagina o di una sezione.
- `nav`: gruppo significativo di collegamenti di navigazione.
- `main`: contenuto principale della pagina; normalmente uno per pagina.
- `section`: sezione tematica, di norma con un titolo.
- `article`: contenuto autonomo, per esempio un articolo o una notizia.
- `aside`: contenuto correlato ma secondario.
- `footer`: informazioni finali della pagina o di una sezione.
- `figure` e `figcaption`: figura e relativa didascalia.
- `div`: contenitore generico senza significato semantico specifico.

## Esempio

```html
<body>
  <header>
    <h1>Blog di tecnologia</h1>
    <nav aria-label="Navigazione principale">
      <a href="index.html">Home</a>
      <a href="articoli.html">Articoli</a>
    </nav>
  </header>
  <main>
    <article>
      <h2>Un articolo</h2>
      <p>Contenuto principale.</p>
    </article>
    <aside>Approfondimenti correlati</aside>
  </main>
  <footer>Contatti e informazioni</footer>
</body>
```

Non scegliere un tag solo in base allo stile predefinito: CSS può cambiare la resa grafica. Scegli l'elemento in base al suo significato.

## Titoli e gerarchia

Organizza i titoli in modo logico (`h1`, `h2`, `h3`...). Non scegliere `h4` perché è più piccolo: per l'aspetto usa CSS. I titoli devono descrivere le sezioni e rendere chiara la struttura.
