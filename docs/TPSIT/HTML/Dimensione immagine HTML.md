# Dimensioni delle immagini in HTML

Gli attributi `width` e `height` di `<img>` descrivono le dimensioni intrinseche dell'immagine, normalmente espresse in pixel CSS. Permettono al browser di riservare spazio prima del completamento del caricamento.

```html
<img src="prototipo.jpg"
     width="800" height="600"
     alt="Prototipo montato sul banco">
```

Per adattare l'immagine al contenitore senza deformarla, usa una regola CSS responsive:

```css
img {
  max-width: 100%;
  height: auto;
}
```

Se l'immagine deve ritagliare un riquadro di dimensioni fisse, si può usare un contenitore con dimensioni esplicite e `object-fit: cover`; questo comportamento è diverso dal semplice ridimensionamento proporzionale.

Non confondere la dimensione visualizzata con la risoluzione del file. Un'immagine di 1600×1200 pixel può essere visualizzata a 400×300 pixel, ma il file può conservare tutti i pixel originali. La scelta delle dimensioni e del formato influisce sulle prestazioni; `width` e `height` non comprimono il file.
