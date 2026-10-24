---
tags: [studio, materia/sistemi, stato/bozza]
data_creazione: 2026-05-24
argomento: Struttura, Attributi e Operazioni sui File
priorità: media
collegamenti: [introduzione-file-system]
---

# Struttura, Attributi e Operazioni sui File

## Concetti Chiave

- **Directory**: file speciale interpretato dal sistema come tabella di corrispondenza per il reperimento dei documenti.
- **Attributi del File**: metadati gestiti dal File System che descrivono le proprietà e lo stato del file.
- **Handle**: identificatore numerico temporaneo assegnato dal sistema operativo a un file aperto da un processo.

## Spiegazione Approfondita

L'utente interagisce con la memoria di massa tramite una struttura ad albero logica abilitata dalle **directory** (o cartelle). Una directory non memorizza dati utente diretti, ma funge da contenitore organizzato di puntatori ad altri nodi dell'albero.

> **Definizione**: Una directory è un file speciale strutturato logicamente come una tabella, in cui ogni riga (record) contiene il nome logico di un oggetto (file o sottocartella) e i riferimenti indispensabili per reperire la sua posizione fisica sul disco.

Oltre al contenuto binario (flusso di byte), ogni file possiede degli **attributi** specifici gestiti dal descrittore del File System:
- Un nome logico ed un tipo (estensione del file).
- L'indirizzo logico al primo blocco fisico del disco (LBA).
- La dimensione corrente calcolata in byte.
- I timestamp temporali (data dell'ultimo accesso e dell'ultima modifica).
- L'ID dell'utente proprietario e i relativi diritti di accesso (permessi).

Le operazioni sui file seguono algoritmi rigorosi gestiti tramite chiamate di sistema (system call). Nell'operazione di **spostamento (move)**, i parametri essenziali includono l'handle e il nome delle directory sia di partenza che di destinazione. Se le due directory coincidono e i due nomi differiscono, l'operazione si riduce ad una *rinomina (rename)*.

Nella **copia di una directory**, il File System implementa un controllo preventivo navigando a ritroso verso la radice (`root`) a partire dalla directory di destinazione: questo serve a verificare che la destinazione non sia una sottocartella della directory sorgente, evitando un ciclo di ricorsione infinita (che farebbe diventare una directory figlia di se stessa). Quando un file viene aperto, il SO associa un descrittore e restituisce un **handle** all'applicazione. I blocchi fisici occupati e il descrittore vengono rilasciati solo alla chiusura dell'ultimo handle attivo, garantendo la consistenza dei file aperti da processi concorrenti.

## Schema Riassuntivo

| Tipo di Operazione | Parametri Richiesti | Meccanismo di Controllo del File System |
|---------------------|---------------------|-----------------------------------------|
| **Rinomina** | Stessa directory, nome diverso | Modifica istantanea del record testuale nella tabella della directory |
| **Spostamento** | Directory diverse, nomi uguali/diversi | Rimozione del puntatore dalla directory sorgente e inserimento nella directory destinazione |
| **Copia Directory** | Directory sorgente e directory destinazione | Navigazione a ritroso verso la root per impedire la paternità ciclica |

## Domande di Autovalutazione

1. Spiega la conseguenza logica sulle strutture dati del File System se venisse avviata la copia di una cartella all'interno di una sua stessa sottocartella senza effettuare controlli preventivi di navigazione a ritroso.
2. Un processo applicativo apre un file per scriverci dei log. Un secondo processo parallelo tenta di cancellare lo stesso file dal disco. Descrivi il ruolo dell'handle in questo scenario concorrente.

## Collegamenti

- Indice-sistemi
- [tipologie-file-system-fat-ext](tipologie-file-system-fat-ext.md)
