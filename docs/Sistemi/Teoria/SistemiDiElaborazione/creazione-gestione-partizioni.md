---
tags: [studio, materia/sistemi, stato/bozza]
data_creazione: 2026-05-24
argomento: Creazione e Gestione delle Partizioni
priorità: media
collegamenti: [partizionamento-disco-mbr-gpt]
---

# Creazione e Gestione delle Partizioni

## Concetti Chiave

- **Gestione Disco**: utilità di sistema in ambiente Windows per l'amministrazione logica delle memorie di massa.
- **Spazio Non Allocato**: porzione di spazio sul disco fisicamente disponibile ma non ancora associata ad alcuna partizione.
- **Volume Semplice**: tipologia di partizione di base che risiede interamente su un singolo disco fisico.

## Spiegazione Approfondita

La configurazione pratica delle partizioni avviene tramite appositi applicativi messi a disposizione dal sistema operativo. In ambiente Windows, l'interfaccia di riferimento è la console **Gestione Disco** (`diskmgmt.msc`), accessibile tramite gli strumenti di amministrazione o digitando "Crea e formatta le partizioni del disco rigido" nella barra di ricerca.

> **Definizione**: Il volume semplice è un'unità logica di memorizzazione creata all'interno di un disco di base che utilizza lo spazio disponibile provenienti da un unico disco fisico, agendo come una partizione primaria indipendente.

Il processo di inizializzazione e creazione di una nuova partizione segue una procedura guidata rigidamente sequenziale:
1. Identificazione visiva dello **spazio non allocato** (contrassegnato graficamente dal sistema).
2. Selezione dell'opzione "Nuovo volume semplice" tramite menu contestuale.
3. Specificazione della dimensione del volume espressa in MB (compresa tra il valore minimo e il massimo disponibile).
4. Assegnazione di una lettera di unità alfabetica (es. `C:`, `D:`, `E:`) o di un percorso di montaggio in una cartella vuota.
5. Scelta dei parametri di formattazione: selezione del File System desiderato (solitamente NTFS o FAT32), impostazione della dimensione dell'unità di allocazione (cluster) e dell'etichetta di volume. Viene generalmente applicata la formattazione rapida per inizializzare le tabelle logiche senza scansionare l'intera superficie del disco per settori danneggiati, accelerando l'attivazione.

## Schema Riassuntivo

| Fase Operativa | Azione Richiesta dall'Utente | Output di Sistema |
|----------------|------------------------------|-------------------|
| **Selezione** | Click destro su blocco Spazio Non Allocato | Apertura della procedura guidata "Nuovo volume semplice" |
| **Dimensionamento** | Input del quantitativo di MB da allocare | Allocazione logica e calcolo dello spazio residuo non allocato |
| **Assegnazione** | Scelta della lettera di unità o del mount point | Visibilità dell'unità logica all'interno del file manager del SO |
| **Formattazione** | Scelta del File System (NTFS/FAT) ed esecuzione | Scrittura delle strutture di controllo e del settore di boot sul volume |

## Domande di Autovalutazione

1. Qual è la differenza fondamentale tra lo stato di un disco contrassegnato come "Spazio non allocato" e uno contrassegnato come "Volume semplice"?
2. Durante la creazione di un volume, un tecnico seleziona l'opzione di formattazione rapida invece di quella completa. Cosa accade a livello logico sul disco?

## Collegamenti

- [[partizionamento-disco-mbr-gpt]]
- [[Indice-sistemi]]