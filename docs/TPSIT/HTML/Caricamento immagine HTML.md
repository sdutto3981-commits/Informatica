# Caricamento delle immagini HTML

L'attributo `src` indica la risorsa immagine da caricare. Per immagini informative usa sempre un `alt` significativo; se l'immagine è puramente decorativa, `alt=""` permette alle tecnologie assistive di ignorarla.

```html
<img src="immagini/scheda.jpg"
     alt="Scheda elettronica con ESP32 e connettori"
     width="800" height="450"
     loading="lazy" decoding="async">
```

## Attributi utili

- `src`: URL o percorso della risorsa.
- `alt`: testo alternativo, non una didascalia generica.
- `width` e `height`: dimensioni intrinseche che permettono al browser di riservare lo spazio corretto e ridurre i salti del layout.
- `loading="lazy"`: ritarda il caricamento finché l'immagine è vicina all'area visibile; non è raccomandato per l'immagine principale visibile all'apertura della pagina.
- `decoding="async"`: suggerisce al browser una decodifica asincrona.

## Immagini responsive

```html
<img src="foto-800.jpg"
     srcset="foto-400.jpg 400w, foto-800.jpg 800w, foto-1200.jpg 1200w"
     sizes="(max-width: 600px) 100vw, 800px"
     width="800" height="600"
     alt="Il prototipo sul banco di lavoro">
```

`srcset` offre diverse risoluzioni e `sizes` comunica la larghezza di visualizzazione prevista. La scelta reale dipende anche dalla densità dello schermo e dalle condizioni di rete. Per layout fluidi, il CSS può aggiungere `max-width: 100%; height: auto;`.
