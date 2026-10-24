# Canvas e SVG in HTML

Canvas e SVG permettono di rappresentare grafica nel browser, ma funzionano in modo diverso.

## Canvas

`canvas` crea un'area bitmap sulla quale si disegna tramite JavaScript. È adatto a giochi 2D, grafici dinamici e disegni con molti aggiornamenti.

```html
<canvas id="grafico" width="320" height="160">
  Grafico illustrativo: il browser non supporta canvas.
</canvas>
<script>
  const canvas = document.querySelector('#grafico');
  const ctx = canvas.getContext('2d');
  if (ctx) {
    ctx.fillStyle = '#2457a7';
    ctx.fillRect(20, 20, 100, 60);
  }
</script>
```

Il canvas non fornisce automaticamente una struttura semantica per ogni forma disegnata. Se il disegno comunica informazioni, prevedi un'alternativa testuale o una rappresentazione accessibile.

## SVG

SVG descrive grafica vettoriale tramite elementi XML-like che possono essere ridimensionati senza diventare sfocati.

```html
<svg viewBox="0 0 120 80" role="img" aria-labelledby="titolo-svg">
  <title id="titolo-svg">Cerchio blu</title>
  <circle cx="40" cy="40" r="25" fill="steelblue" />
</svg>
```

SVG è utile per icone, loghi, diagrammi e illustrazioni scalabili. Le forme SVG sono elementi della struttura del documento e possono essere stilizzati con CSS.

## Immagini responsive

`picture` e `source` possono offrire immagini alternative in base a media query o formato. Non è la stessa cosa di scalare un'immagine con CSS: possono essere inviati asset diversi al browser.

## Riferimento

[W3Schools — HTML Canvas](https://www.w3schools.com/html/html5_canvas.asp) · [HTML SVG](https://www.w3schools.com/html/html5_svg.asp)
