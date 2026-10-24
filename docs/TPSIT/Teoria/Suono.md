# Suono e audio digitale

Il suono è una variazione di pressione che si propaga in un mezzo materiale. Un microfono converte la variazione acustica in un segnale elettrico; per elaborarlo con un calcolatore il segnale viene campionato e quantizzato.

## Digitalizzazione

- **Campionamento:** misura il segnale a intervalli regolari. La frequenza di campionamento indica quante misure vengono effettuate al secondo, in hertz.
- **Quantizzazione:** assegna ogni campione a uno dei livelli digitali disponibili.
- **Profondità in bit:** determina il numero di livelli teorici: con `n` bit sono `2^n`.
- **Canali:** mono ha un canale; stereo ne usa normalmente due.

Per un PCM non compresso, il flusso dati nominale è:

\[
\text{bit/s} = f_s \times N_{bit} \times N_{canali}
\]

Ad esempio, audio stereo a 44.100 campioni/s e 16 bit richiede `44.100 × 16 × 2 = 1.411.200 bit/s`, esclusi overhead e metadati.

## Formati e compressione

WAV è un contenitore che spesso ospita audio PCM non compresso; MP3 e AAC sono codec con perdita; FLAC comprime senza perdita. Il formato/contenitore e il codec non sono sinonimi. Il bitrate influisce sul peso e, per i codec con perdita, spesso anche sulla qualità, ma il rapporto esatto dipende dal codec e dal contenuto.

Per il video consulta [Video](Video.md) e [Streaming](Streaming.md).
