# TPSIT — programma 3INF

## Obiettivi

Elaborare contenuti multimediali e realizzare pagine web semantiche, responsive e interattive con HTML5, CSS3, Bootstrap e JavaScript. Manipolare il DOM e gli eventi, valutando attendibilità delle fonti e accessibilità.

## 1. Elementi di multimedialità (7 ore)

**Appunti:** [teoria multimediale](../TPSIT/Teoria/index.md), [immagini digitali](../TPSIT/Teoria/Immagini.md), [compressione lossless](../TPSIT/Teoria/Lossless.md) e [lossy](../TPSIT/Teoria/Lossy.md).

- RGB è un modello additivo usato negli schermi; CMYK è sottrattivo e usato nella stampa.
- Immagini bitmap/raster: pixel; immagini vettoriali: forme geometriche.
- Risoluzione, profondità di colore e dimensione del file.
- Lossless: conserva tutte le informazioni (es. PNG e ZIP); lossy: ne scarta una parte (es. JPEG e MP3).
- Audio: campionamento, frequenza di campionamento, quantizzazione e profondità in bit.
- Video: fotogrammi, frame rate, risoluzione, codec e contenitore. MP4 è un contenitore, H.264 è un codec.

## 2. HTML5 (24 ore)

**Appunti:** [HTML](../TPSIT/HTML/index.md).

```html
<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pagina di esempio</title>
</head>
<body>
  <header><h1>Titolo</h1></header>
  <main>
    <section aria-labelledby="intro">
      <h2 id="intro">Introduzione</h2>
      <p>Contenuto della pagina.</p>
    </section>
  </main>
  <footer>Informazioni finali</footer>
</body>
</html>
```

Da conoscere: struttura del documento; tag semantici (`header`, `nav`, `main`, `section`, `article`, `footer`); gerarchia dei titoli; liste e link; immagini con `alt`; form con `label`, tipi di input e validazione; attributi globali; audio/video; iframe con titolo; URL assoluti e relativi.

## 3. CSS3 (34 ore)

**Appunti:** [CSS](../TPSIT/CSS/index.md), [box model](../TPSIT/CSS/Box-Model.md), [selettori](../TPSIT/CSS/Selettori.md).

- Selettori, cascata, specificità ed ereditarietà.
- Box model: contenuto, padding, bordo e margine; `box-sizing: border-box`.
- Dimensionamento, unità CSS e overflow.
- Flexbox: asse principale/trasversale, `justify-content`, `align-items`, `gap`, `flex-wrap`.
- Posizionamento: `static`, `relative`, `absolute`, `fixed`, `sticky`.
- Colori, tipografia, transizioni e animazioni.
- Media query e approccio mobile-first.

```css
* { box-sizing: border-box; }
.container { width: min(100% - 2rem, 1100px); margin-inline: auto; }
.cards { display: flex; flex-wrap: wrap; gap: 1rem; }
.card { flex: 1 1 240px; }
@media (max-width: 600px) {
  .container { width: min(100% - 1rem, 1100px); }
}
```

## 4. Bootstrap (8 ore)

**Appunti:** [Bootstrap](../TPSIT/Bootstrap/index.md).

Studiare inclusione della versione usata in laboratorio, container e breakpoint, grid system, classi responsive e componenti navbar, form, card, carosello e pulsanti. Realizzare un sito personale mobile-first, sapendo spiegare le classi utilizzate.

## 5. JavaScript lato client (55 ore)

**Appunti:** [JavaScript](../TPSIT/JavaScript/index.md), [introduzione](../TPSIT/JavaScript/Introduzione%20JavaScript.md), [DOM ed eventi](../TPSIT/JavaScript/DOM%20ed%20eventi.md).

- `const` e `let`, tipi, conversioni, operatori e scope.
- Condizioni, cicli, funzioni, parametri e valore restituito.
- Array e oggetti se previsti dal percorso della classe.
- DOM: selezione e modifica di elementi; eventi con `addEventListener`.
- Form: leggere e validare input, mostrare messaggi comprensibili.
- Timer: `setTimeout`, `setInterval`, `clearInterval`.
- Giochi semplici separando stato, logica e interfaccia.

## 6. Verifica fonti e inclusività (4 ore)

**Appunti:** [accessibilità e verifica delle fonti](../TPSIT/Accessibilita%20e%20verifica%20fonti.md).

Controllare autore, data, scopo, prove e riscontri indipendenti. Per l'accessibilità usare testi alternativi, etichette dei form, contrasto adeguato, gerarchia dei titoli e navigazione da tastiera. Non comunicare informazioni soltanto tramite il colore.

## Autoverifica

- [ ] Creare una pagina HTML semantica e un form accessibile.
- [ ] Spiegare box model, specificità e Flexbox.
- [ ] Rendere una pagina responsive.
- [ ] Usare griglia e componenti Bootstrap.
- [ ] Manipolare DOM ed eventi.
- [ ] Creare e fermare un timer JavaScript.
- [ ] Valutare fonti e accessibilità.
