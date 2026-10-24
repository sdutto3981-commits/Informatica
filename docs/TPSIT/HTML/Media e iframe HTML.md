# Audio, video e iframe in HTML

HTML5 permette di inserire audio e video senza richiedere necessariamente un plugin esterno. L'elemento `iframe` incorpora un altro documento.

## Audio

```html
<audio controls>
  <source src="audio/podcast.mp3" type="audio/mpeg">
  Il browser non supporta l'audio HTML.
</audio>
```

## Video con didascalie

```html
<video controls width="640" poster="immagini/anteprima.jpg">
  <source src="video/lezione.mp4" type="video/mp4">
  <track src="sottotitoli/it.vtt" kind="subtitles" srclang="it" label="Italiano">
  Il browser non supporta il video HTML.
</video>
```

- `controls` mostra i comandi del browser.
- `source` permette di proporre risorse e formati differenti.
- `poster` è l'immagine mostrata prima della riproduzione.
- `track` può fornire sottotitoli o altre tracce testuali.
- Non avviare audio automaticamente senza una ragione valida; rispetta le preferenze dell'utente.

## Iframe

```html
<iframe
  src="https://example.com/embed"
  title="Contenuto incorporato: dimostrazione"
  loading="lazy"
  width="640"
  height="360">
</iframe>
```

Un `iframe` crea un contesto di navigazione separato. Fornisci un `title` descrittivo. Per contenuti di terze parti, valuta le opzioni di sicurezza e i permessi necessari; l'attributo `sandbox` può limitare alcune capacità, ma la configurazione va scelta in base all'uso previsto.

## Percorsi delle risorse

I percorsi relativi sono risolti rispetto alla pagina o alla base URL del documento; controlla maiuscole/minuscole e cartelle reali del progetto. Evita link a file che non esistono.
