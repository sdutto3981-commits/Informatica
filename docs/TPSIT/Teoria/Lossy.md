# Compressione lossy (con perdita)

La **compressione lossy** riduce la quantità di dati eliminando informazioni considerate meno importanti per la percezione umana. Dopo la decompressione il risultato può essere simile all'originale, ma non è identico e non è possibile ricostruire esattamente tutti i dati scartati.

## Quando si usa

È comune per fotografie, audio e video, perché può produrre file molto più piccoli di una rappresentazione non compressa. È meno adatta a testi, grafici tecnici, diagrammi e schermate con contorni netti, dove gli artefatti possono essere evidenti o rendere i dettagli illeggibili.

## JPEG/JPG

JPEG e JPG sono due estensioni comunemente usate per immagini codificate secondo la famiglia JPEG. Una tipica codifica JPEG per immagini fotografiche comprende, in forma semplificata:

1. conversione del colore in uno spazio adatto alla codifica, spesso YCbCr;
2. eventuale sottocampionamento delle componenti cromatiche, sfruttando la maggiore sensibilità visiva ai dettagli di luminanza rispetto a parte dei dettagli cromatici;
3. suddivisione dell'immagine in blocchi e trasformazione dei coefficienti, tradizionalmente mediante DCT;
4. **quantizzazione**, che riduce la precisione di alcuni coefficienti e costituisce una delle principali fasi con perdita;
5. codifica entropica dei valori risultanti.

Il dettaglio dell'implementazione varia. Un'immagine JPEG non è correttamente descritta come “una tabella RGB compressa in base alle zone uniformi” soltanto: il procedimento utilizza trasformazioni, quantizzazione e codifica, con parametri che incidono su qualità e dimensione.

## Qualità e dimensione del file

Molti programmi espongono un cursore di qualità, ad esempio da 0 a 100, ma **non esiste un significato numerico universale valido per tutti gli encoder**. In molti strumenti un valore maggiore significa meno perdita e un file generalmente più grande; la relazione non è lineare e dipende da immagine, encoder, sottocampionamento e impostazioni.

Non esiste una riduzione fissa del tipo “JPEG è sempre un terzo dell'originale”. Il risultato dipende dal contenuto e dalle impostazioni di compressione. Texture, rumore, dettagli fini e bordi possono comportarsi in modo differente.

## Altri esempi

- **MP3 e AAC:** compressione audio con perdita che usa modelli percettivi;
- **H.264/AVC e H.265/HEVC:** codec video che possono utilizzare compressione con perdita;
- **WebP lossy:** modalità di compressione con perdita per immagini.

Un'estensione non indica necessariamente un solo metodo di compressione. Occorre distinguere **formato/contenitore**, **codec** e impostazioni di codifica.

## Confronto con lossless

| Aspetto | Lossy | Lossless |
|---|---|---|
| Ricostruzione | Approssimata | Identica all'originale digitale |
| Dimensione | Spesso molto ridotta per media complessi | Riduzione dipendente dalla struttura dei dati |
| Esempi | JPEG, MP3, codifica video lossy | PNG, FLAC, ZIP |
| Uso tipico | Fotografie, streaming audio/video | Loghi, testo, archivi, dati da preservare esattamente |

Per scegliere un formato considera qualità richiesta, dimensione, possibilità di modifiche successive e necessità di conservare l'originale. Per immagini con testo e contorni netti, valuta PNG o SVG; per fotografie, JPEG o altri formati fotografici possono essere più efficienti.

- [W3Schools — Images](https://www.w3schools.com/html/html_images.asp)
- [W3C — PNG Specification](https://www.w3.org/TR/png/)
