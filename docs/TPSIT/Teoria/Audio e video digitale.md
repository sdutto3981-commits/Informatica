# Audio e video digitale

## Audio

Un suono analogico varia in modo continuo. Per rappresentarlo digitalmente si campiona il segnale e si quantizza ogni campione.

- **Frequenza di campionamento:** numero di campioni al secondo, misurato in hertz (Hz).
- **Profondità in bit:** numero di bit usati per rappresentare ciascun campione; a parità di altre condizioni, più bit consentono più livelli di quantizzazione.
- **Canali:** mono ha un canale, stereo normalmente due.
- **Bitrate:** quantità di dati codificati al secondo; nei formati compressi è spesso espresso in kbit/s.

La compressione lossless conserva i dati originali; la lossy riduce maggiormente la dimensione eliminando informazioni considerate meno importanti. MP3 è un formato audio con compressione con perdita.

## Video

Un video digitale contiene una sequenza di fotogrammi accompagnata, spesso, da una traccia audio.

- **Risoluzione:** numero di pixel di ciascun fotogramma.
- **Frame rate:** fotogrammi al secondo (fps).
- **Codec:** metodo per codificare/decodificare audio o video (es. H.264 per video).
- **Contenitore:** struttura del file che può includere tracce audio, video, sottotitoli e metadati (es. MP4).
- **Bitrate:** quantità media di dati prodotti ogni secondo; incide su dimensione e qualità insieme a codec e contenuto.

## Dimensione non compressa, stima

Per un'immagine bitmap non compressa, una stima semplice è:

`dimensione in bit = larghezza × altezza × bit per pixel`.

Per un flusso video non compresso si moltiplica inoltre per i fotogrammi al secondo e per la durata. I file reali differiscono perché intervengono codec, compressione, audio e metadati.

## Domande di ripasso

- Perché aumentare la frequenza di campionamento può aumentare la quantità di dati?
- In cosa differiscono codec e contenitore?
- Perché la dimensione di un JPEG non si calcola soltanto moltiplicando larghezza, altezza e profondità?
