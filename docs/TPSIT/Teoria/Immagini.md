---
date: 2025-10-02
time: 10:03
---
# Immagini digitali

Le immagini digitali rappresentano informazioni visive. Le due famiglie principali sono le **immagini raster/bitmap**, formate da una griglia di pixel, e le **immagini vettoriali**, descritte attraverso forme geometriche, tracciati e attributi grafici.

## Bitmap e immagini vettoriali

### Raster o bitmap

Una bitmap contiene un numero definito di pixel in larghezza e altezza. Ogni pixel memorizza un valore di colore o un indice a una palette. Fotografie e immagini acquisite da fotocamera sono normalmente raster.

- Aumentare l'ingrandimento oltre i pixel disponibili può rendere visibili blocchi o sfocatura.
- Il peso dipende da dimensioni in pixel, profondità colore, eventuale canale alfa, metadati e compressione.
- Formati comuni sono JPEG, PNG, GIF, TIFF e WebP.

### Vettoriale

Un'immagine vettoriale descrive elementi come linee, curve, rettangoli, testo e riempimenti usando coordinate e parametri. Può essere ridimensionata senza la tipica pixelizzazione di una bitmap, ma può contenere effetti o immagini raster incorporate.

SVG è un formato vettoriale usato sul Web. È adatto a loghi, icone, diagrammi e grafici; non è sempre la scelta più efficiente per fotografie complesse.

## Colore e profondità

Il modello **RGB** è additivo: combina rosso, verde e blu per generare colori sullo schermo. Con 8 bit per canale si hanno 256 livelli per canale e, senza considerare l'alfa, 24 bit per pixel (oltre 16 milioni di combinazioni teoriche).

| Esempio RGB | Significato |
|---|---|
| `(255, 0, 0)` | rosso massimo |
| `(0, 255, 0)` | verde massimo |
| `(0, 0, 255)` | blu massimo |
| `(255, 255, 255)` | bianco |
| `(0, 0, 0)` | nero |
| `(128, 128, 128)` | grigio intermedio |

Un'immagine RGBA include anche un canale alfa, spesso usato per la trasparenza. Il modello **CMYK** è sottrattivo ed è usato nei processi di stampa; la resa finale dipende da stampante, inchiostri, carta e profilo colore. RGB e CMYK non sono modelli intercambiabili senza conversione e possibili differenze cromatiche.

Approfondimento: [conversione concettuale RGB e CMYK](Conversione%20RGB%20to%20CMYK.md).

## Risoluzione e dimensione del file

La risoluzione in pixel si esprime come larghezza × altezza, per esempio `1920 × 1080` (Full HD). Il numero totale dei pixel è:

\[
N = larghezza_{px} \times altezza_{px}
\]

Per una bitmap non compressa con profondità costante, una stima grezza del contenuto è:

\[
Dimensione_{byte} \approx \frac{larghezza_{px} \times altezza_{px} \times bitPerPixel}{8}
\]

Ad esempio, un'immagine RGB da `1920 × 1080` a 24 bit per pixel richiede circa 6,22 MB decimali (circa 5,93 MiB) di dati pixel, senza contare intestazioni e metadati. Il file reale può essere molto più piccolo o più grande secondo formato, compressione, canali e contenuti. **La dimensione non si calcola sommando larghezza, altezza e byte per pixel.**

Il tempo ideale di trasferimento può essere stimato come `tempo = dimensione / velocità`, ma nella pratica intervengono overhead di protocollo, latenza, congestione e velocità effettiva del collegamento.

## Metadati: immagine e pagina Web

I metadati sono informazioni che descrivono un contenuto. Possono essere salvati nel file immagine, per esempio EXIF, IPTC o XMP, e includere orientamento, data, modello di fotocamera, posizione geografica o informazioni sul copyright. Non tutte le immagini contengono tutti questi campi; alcune applicazioni rimuovono i metadati per privacy o ridurre il file.

I metadati HTML sono un concetto diverso: sono elementi inseriti nella sezione `<head>` della pagina, ad esempio codifica caratteri, descrizione e viewport.

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Galleria fotografica del progetto">
  <title>Galleria</title>
</head>
```

`alt` non è un metadato tecnico del file: è un attributo HTML che fornisce un'alternativa testuale all'immagine per accessibilità e quando la risorsa non è disponibile.

## PPI e DPI

**PPI (pixels per inch)** indica quanti pixel dell'immagine sono collocati in un pollice della dimensione di stampa o visualizzazione. Un pollice misura **2,54 cm**. Se un'immagine è larga 2400 pixel e viene stampata a 300 PPI, la larghezza teorica è `2400 / 300 = 8` pollici, cioè circa 20,32 cm.

Cambiare il valore PPI nei metadati senza ricampionare l'immagine non aggiunge né rimuove pixel: modifica la dimensione fisica di stampa suggerita. Se invece si ricampiona, il numero di pixel viene cambiato tramite interpolazione o riduzione.

**DPI (dots per inch)** indica la densità di punti fisici che un dispositivo di stampa può depositare. I punti d'inchiostro non coincidono necessariamente uno a uno con i pixel dell'immagine: una stampante usa più punti e combinazioni di inchiostri per riprodurre un pixel e un colore. PPI riguarda i pixel dell'immagine rispetto alla dimensione fisica; DPI riguarda i punti del dispositivo.

La qualità di stampa dipende inoltre da risoluzione originale, dimensione finale, algoritmo di ricampionamento, processo di stampa, supporto e distanza di osservazione. Valori come 300 PPI sono una convenzione frequente per stampe di qualità osservate da vicino, non una regola universale per ogni supporto.

## Compressione

- [Lossless](Lossless.md): dopo la decompressione ricostruisce esattamente i dati originali. Esempi: PNG e TIFF con compressione lossless.
- [Lossy](Lossy.md): elimina parte dell'informazione per ottenere file generalmente più piccoli. Esempio: JPEG con compressione lossy.

Scegli il formato in base all'immagine. Fotografie spesso si prestano a JPEG o WebP; grafici, schermate e immagini con testo richiedono attenzione agli artefatti, quindi può essere preferibile un formato lossless. Per icone e loghi, SVG è spesso efficiente se l'immagine è vettoriale.

- [W3Schools — HTML Images](https://www.w3schools.com/html/html_images.asp)
- [W3Schools — HTML Canvas](https://www.w3schools.com/html/html5_canvas.asp)
- [MDN — Image file type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
