---
tags: [studio, materia/sistemi, stato/bozza]
data_creazione: 2026-05-24
argomento: Tipologie di File System, Architetture FAT e Ext
priorità: alta
collegamenti: [introduzione-file-system]
---

# Tipologie di File System, Architetture FAT e Ext

## Concetti Chiave

- **FAT (File Allocation Table)**: architettura basata su una tabella globale strutturata come lista concatenata di blocchi.
- **Inode (Index Node)**: struttura dati dei sistemi Unix/Linux che raccoglie i metadati e i puntatori di un singolo file.
- **Journaling**: tecnica transazionale di tracciamento delle modifiche per prevenire la corruzione del File System a seguito di crash.

## Spiegazione Approfondita

Esistono diverse implementazioni di File System ottimizzate per specifici Sistemi Operativi. Tra le più rilevanti figurano la famiglia **FAT** di Microsoft e la famiglia **Ext** di Linux.

Il File System **FAT** deve il suo nome alla tabella posizionata all'inizio del volume. Si è evoluto in tre versioni principali in base ai bit usati per l'indirizzamento dei blocchi: FAT12, FAT16 (con limite strutturale di dimensione massima della partizione definito a 2 GB) e FAT32 (che supera tale limite). La struttura fisica sequenziale di una partizione FAT prevede: il settore di boot della partizione, la File Allocation Table primaria, un duplicato della FAT (per motivi di ridondanza e sicurezza), la Directory Root e infine l'area dati per file e sottodirectory.

> **Definizione**: L'Inode (Index Node) è la struttura dati fondamentale dei file system Ext che identifica univocamente un file o una directory sulla memoria di massa, contenendo tutti i metadati e l'albero dei puntatori ai blocchi di dati fisici, escludendo il nome del file.

Nei sistemi Linux (**Ext2/Ext3/Ext4**), la gestione dello spazio e l'indirizzamento dei blocchi si basano sulla struttura interna dell'**Inode**, che contiene campi critici quali *Mode* (tipo di oggetto e diritti d'accesso), *Owner Information*, *Size* (dimensione in byte) e i *Timestamps*. Per puntare ai blocchi dati fisici (**Data Blocks**), l'Inode implementa un sistema di puntatori ad albero:
- **12 Puntatori Diretti**: puntano direttamente ai primi 12 blocchi fisici del file (garantiscono un accesso immediato per file di piccole dimensioni).
- **1 Puntatore Indiretto Semplice**: realizza una redirezione, puntando a un intero blocco di memoria che contiene un elenco di puntatori diretti.
- **1 Puntatore Indiretto Doppio**: introduce due livelli di redirezione intermedi.
- **1 Puntatore Indiretto Triplo**: introduce tre livelli di redirezione gerarchici, permettendo al File System di mappare e gestire file di dimensioni enormi.

A partire dalla versione **Ext3**, è stata introdotta la tecnica del **journaling**: prima di effettuare qualsiasi modifica fisica nell'area dati, il File System annota le operazioni pianificate in un registro delle transazioni chiamato giornale. In caso di interruzione improvvisa della corrente o malfunzionamento hardware, al riavvio il sistema operativo esamina il giornale per completare o annullare le transazioni interrotte, ripristinando la coerenza del File System in pochi secondi senza dover scansionare l'intero disco.

## Schema Riassuntivo

| Caratteristica Architetturale | FAT32 | Ext3 / Ext4 |
|------------------------------|-------|-------------|
| **Struttura di Allocazione** | Tabella concatenata globale all'inizio del disco | Indici e puntatori distribuiti tramite Inode individuali |
| **Posizione del Nome File** | All'interno della directory insieme ai metadati | All'interno della directory (l'inode contiene solo i metadati fisici) |
| **Accesso a File Grandi** | Scansione sequenziale dei cluster della catena | Accesso quasi diretto tramite indici semplici, doppi e tripli |
| **Resistenza ai Crash** | Bassa (alto rischio di cluster persi o catene corrotte) | Alta (presenza del modulo di **Journaling** per il ripristino coerente) |

## Domande di Autovalutazione

1. Perché l'architettura a Inode con puntatori gerarchici è intrinsecamente più efficiente rispetto alla tabella FAT nell'accesso casuale (random access) a un byte posizionato a metà di un file di grandi dimensioni?
2. Descrivi la sequenza logica di eventi che si verifica grazie al Journaling se il computer si spegne improvvisamente a causa di un blackout mentre il sistema operativo sta salvando un file su un File System Ext3.

## Collegamenti

- [[Indice-sistemi]]
- [[struttura-attributi-operazioni-file]]