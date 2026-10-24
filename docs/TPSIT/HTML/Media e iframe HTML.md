# Immagini, audio, video e iframe

## Immagini

```html
<img src="immagini/prototipo.jpg" alt="Prototipo elettronico montato su una basetta" width="640" height="360">
```

`src` indica il percorso della risorsa; `alt` comunica il contenuto o la funzione dell'immagine. Se l'immagine è puramente decorativa e non aggiunge informazione, usa `alt=""`. Specificare larghezza e altezza intrinseche aiuta il browser a riservare lo spazio corretto.

Per immagini responsive:

```css
img, video { max-width: 100%; height: auto; }
```

`picture` e `source` permettono di offrire varianti diverse in base a media query o formati supportati.

## Audio e video

```html
<video controls width="640" poster="anteprima.jpg">
  <source src="demo.mp4" type="video/mp4">
  Il browser non supporta il video incorporato.
</video>

<audio controls>
  <source src="suono.mp3" type="audio/mpeg">
  Il browser non supporta l'audio incorporato.
</audio>
```

`controls` mostra i controlli del browser. Fornisci, quando possibile, sottotitoli o trascrizioni per rendere il contenuto utilizzabile anche senza audio. Non avviare automaticamente media con suono senza una motivazione chiara.

## Iframe

`iframe` incorpora un altro documento. Deve avere un titolo significativo; va limitato a contenuti attendibili e si possono usare attributi come `loading="lazy"` e `sandbox` quando appropriato.

```html
<iframe
  src="https://example.com/embed"
  title="Demo incorporata"
  loading="lazy"
  width="640"
  height="360">
</iframe>
```

Usa URL e servizio realmente disponibili: `example.com` è soltanto un segnaposto. Le restrizioni di incorporamento del sito remoto possono impedire il rendering.

## Riferimento

[W3Schools — HTML Images](https://www.w3schools.com/html/html_images.asp) · [HTML Media](https://www.w3schools.com/html/html_media.asp) · [HTML Iframes](https://www.w3schools.com/html/html_iframe.asp)
