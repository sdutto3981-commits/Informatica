# Video digitale

Un video digitale è una sequenza temporale di immagini (*frame*), spesso accompagnata da audio. Per descriverne la qualità e il costo di memorizzazione bisogna distinguere risoluzione, frequenza dei fotogrammi, compressione, codec e contenitore.

## Parametri principali

- **Risoluzione:** numero di pixel del fotogramma, ad esempio 1920×1080.
- **Frame rate:** fotogrammi al secondo (fps); 25, 30 e 60 fps sono valori comuni.
- **Rapporto d'aspetto:** proporzione tra larghezza e altezza, ad esempio 16:9.
- **Bitrate:** quantità media di dati trasmessa o memorizzata al secondo.
- **Codec video:** algoritmo usato per codificare/decodificare i fotogrammi (ad esempio H.264 o AV1).
- **Contenitore:** formato che riunisce flussi video, audio e metadati (ad esempio MP4 o WebM).

## Compressione

Molti codec video usano compressione con perdita: sfruttano ridondanze spaziali e temporali per ridurre i dati. Un bitrate maggiore può preservare più dettaglio a parità di codec e impostazioni, ma non è l'unico fattore che determina la qualità. Una risoluzione superiore aumenta il numero di pixel per fotogramma, mentre un frame rate più alto registra più istanti per secondo.

## Video sul web

```html
<video controls width="640" poster="anteprima.jpg">
  <source src="dimostrazione.mp4" type="video/mp4">
  Il browser non supporta il video incorporato.
</video>
```

Aggiungi sottotitoli quando necessari, fornisci controlli accessibili e non avviare audio automaticamente senza una ragione chiara. Per la distribuzione adattiva si usano tecniche di streaming che selezionano varianti di qualità in funzione della rete e del dispositivo.
