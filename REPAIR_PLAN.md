# Piano dettagliato delle correzioni

Il pacchetto applica le correzioni sotto. L'obiettivo è rendere le note affidabili in MkDocs senza appiattire le spiegazioni specialistiche.

## A. Configurazione e pubblicazione

- Rimuovere `polyfill.io` dalla configurazione; aggiungere configurazione MathJax locale e un caricamento CDN versionato.
- Usare i nomi correnti dei moduli emoji Material per PyMdown.
- Rimuovere l'opzione `navigation.expand` quando è attiva `navigation.prune`, incompatibili tra loro.
- Dichiarare le dipendenze dirette MkDocs con versioni fissate.
- Usare un solo workflow GitHub Pages per la documentazione MkDocs; archiviare il workflow Jekyll, mantenendone il contenuto per consultazione.

## B. Struttura editoriale e migrazione

- Migrare link di Obsidian in Markdown standard quando è possibile risolvere la destinazione e gli heading.
- Aggiungere ID espliciti alle intestazioni richieste dai vecchi link `[[#titolo]]`, senza cambiare il testo visibile dei titoli.
- Convertire callout `> [!note]` e simili in admonition PyMdown, mantenendo titolo e righe del corpo.
- Sostituire riferimenti vuoti e token di template come `{{date}}` con contenuto neutro oppure rimuoverli solo quando sono veramente vuoti.
- Correggere i diagrammi AND/OR/NOT che puntavano a file Markdown e sostituire immagini remote dei latch con SVG conservati nel repository.

## C. Note tecniche lunghe: conservazione della profondità

| Nota | Intervento |
|---|---|
| `Filesystem manager.md` | Riscrittura approfondita che conserva i concetti originari: metadati, funzioni del manager, formattazione, inizializzazione, mount/unmount, descrittori, lettura/scrittura, EOF, cancellazione, allocazione, NTFS, inode ed ext. Distingue responsabilità del sistema operativo e strutture specifiche dei file system. |
| `Memorie di massa.md` | Approfondimento di HDD, LBA, seek, latenza rotazionale, SSD/NAND, FTL, wear leveling, garbage collection, TRIM, unità decimali/binari e distinzione tra supporto, volume e file system. |
| `tipologie-file-system-fat-ext.md` | Corregge la generalizzazione dei puntatori classici a Ext4; distingue FAT, exFAT, inode, extents e modalità di journaling. |
| `partizionamento-disco-mbr-gpt.md` | Precisa i limiti MBR in relazione ai settori logici, la struttura GPT, Protective MBR, GUID, CRC e copia di backup; evita di promettere riparazione automatica. |
| `Immagini.md` | Corregge le formule di dimensione, la distinzione bitmap/vettoriale, la differenza tra metadati immagine e metadati HTML, PPI/DPI e l'esempio di dimensione di stampa. |
| `Lossy.md` | Spiega trasformata/quantizzazione, qualità JPEG, dipendenza dell'encoder e differenze con lossless, evitando valori e rapporti di compressione universali. |
| `W3C.md` | Chiarisce standard aperti, interoperabilità, accessibilità e rapporto tra W3C e WHATWG/HTML Living Standard. |
| `Variabili logiche e assiomi booleani.md` | Completa le tavole per AND, OR, XOR, NAND e NOR e spiega i valori logici. |
| `Proprietà e teoremi dell'algebra di Boole.md` | Organizza leggi, assorbimento, De Morgan, dualità e semplificazioni guidate. |
| `Flip Flop D.md`, `Flip Flop sr.md` | Chiarisce fronte attivo, stato memorizzato, tabella caratteristica, condizioni non ammesse, equazione caratteristica e differenza tra latch e flip-flop. |
| `Variabili logiche e assiomi booleani.md`, `Proprietà e teoremi dell'algebra di Boole.md` | Complete le tabelle AND/OR/XOR/NAND/NOR, le leggi fondamentali, l'assorbimento, De Morgan, dualità e gli esempi di verifica. |

## D. Note brevi da ampliare

Lo script completa note che prima contenevano quasi soltanto un titolo, una frase o un riferimento incompleto: tipi/variabili C, costanti C, array C#, conversioni di basi, rappresentazione numerica, UCS, clock, pipeline, note atomiche HTML e alcune note di audio/video/URL.

## E. Duplicazioni senza perdita di contenuto

- La mappa di storage separa il ruolo del file system manager, le proprietà dei dispositivi, la gerarchia cache, la formattazione/RAID, il partizionamento e i dettagli FAT/ext. L’indice di Sistemi di elaborazione viene aggiornato per rendere raggiungibili Cache e le note specialistiche che prima erano orfane. Le note restano separate perché hanno scopi differenti.
- La pagina `docs/Sistemi/C/index.md` chiarisce la differenza tra panoramica di tipi/variabili, tipi di dati, file e memoria dinamica. Non crea un file fantasma `File e memoria dinamica C.md`.
- La nota di base C# su classi/oggetti rimanda al corso OOP esteso senza sostituire gli esempi già presenti.
- Le due note JavaScript su variabili e dichiarazioni spiegano il loro ambito per ridurre la duplicazione senza eliminarle.

## F. Protezione contro la perdita di profondità

Le riscritture integrali di note esistenti vengono bloccate se il nuovo Markdown è più corto del testo attuale. Le note lunghe non elencate nella tabella sono lasciate inalterate a livello di spiegazione; vengono applicate soltanto migrazioni di link/ancore e correzioni puntuali. Prima di pubblicare, confronta sempre il backup `.repair-backup/` e il diff Git.
