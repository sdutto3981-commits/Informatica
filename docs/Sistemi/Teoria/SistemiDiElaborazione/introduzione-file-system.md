---
tags: [studio, materia/sistemi, stato/bozza]
data_creazione: 2026-05-24
argomento: Introduzione al File System e Protezione dei File
priorità: alta
collegamenti: [indice-sistemi]
---

# Introduzione al File System e Protezione dei File

## Concetti Chiave

- **Memoria Secondaria**: supporto di memorizzazione permanente, non volatile e ad alta capacità.
- **File System**: modulo del Sistema Operativo incaricato di organizzare e gestire i dati sui dispositivi di memoria di massa.
- **ACL (Access Control List)**: lista di controllo degli accessi associata a ogni file per verificarne i permessi.

## Spiegazione Approfondita

I programmi e i dati richiedono di essere preservati in modo persistente. Questo compito è affidato alla **memoria secondaria**, che offre non-volatilità e ampie capacità ma sconta latenze elevate a causa dei limiti fisici del supporto (come i movimenti meccanici nei dischi HDD o i cicli di lettura/scrittura nelle memorie Flash rispetto alla velocità elettronica della CPU).

> **Definizione**: Il File System è l'insieme dei file, delle strutture dati, delle directory e dei meccanismi software del sistema operativo che gestiscono la memorizzazione permanente dei dati, mascherando l'organizzazione fisica dei settori sul disco e offrendo una visione logica unitaria.

Il File System assolve la necessità di memorizzare enormi quantità di informazioni, permettere l'accesso contemporaneo ai dati da parte di più processi e attivare le misure di protezione. La sicurezza logica è implementata mediante le **ACL (Access Control List)**, tabelle consultate dal kernel prima di autorizzare operazioni di lettura, scrittura, esecuzione, accodamento o cancellazione.

Nei sistemi POSIX/Linux-like viene impiegata una versione sintetica della ACL basata su tre categorie di utenti:
- **Proprietario (Owner)**: l'utente che ha creato il file.
- **Gruppo (Group)**: insieme di utenti che condividono diritti d'accesso simili per motivi di collaborazione o di ruolo.
- **Universo (Others/World)**: la totalità degli altri utenti registrati nel sistema calcolatore.

Ciascuna categoria dispone di un campo da 3 bit per mappare i diritti di Lettura (r), Scrittura (w) ed Esecuzione (x), richiedendo solo 9 bit totali per definire la stringa di protezione fondamentale del file.

## Schema Riassuntivo

| Categoria Utente | Bit di Controllo | Significato Operativo |
|------------------|------------------|-----------------------|
| **Proprietario** | `r w x` | Permessi di accesso ed esecuzione esclusivi del creatore del file |
| **Gruppo** | `r w x` | Permessi assegnati a un team ristretto per la condivisione protetta |
| **Universo** | `r w x` | Permessi di base o nulli validi per qualsiasi altro utente del sistema |

## Domande di Autovalutazione

1. Perché il controllo degli accessi tramite ACL è una funzione critica che deve essere gestita ed eseguita esclusivamente in modalità protetta (kernel mode) dal Sistema Operativo?
2. Se un file possiede una stringa di permessi pari a `rwxr-x---`, quali operazioni sono consentite ai membri del gruppo proprietario e quali agli utenti appartenenti all'universo?

## Collegamenti

- [[Indice-sistemi]]
- [[struttura-attributi-operazioni-file]]
- [[tipologie-file-system-fat-ext]]