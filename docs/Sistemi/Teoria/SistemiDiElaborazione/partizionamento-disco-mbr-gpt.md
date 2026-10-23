---
tags: [studio, materia/sistemi, stato/bozza]
data_creazione: 2026-05-24
argomento: Partizionamento del Disco, MBR e GPT
priorità: alta
collegamenti: [indice-sistemi]
---

# Partizionamento del Disco, MBR e GPT

## Concetti Chiave

- **Partizione**: porzione logica indipendente di un disco fisico.
- **MBR (Master Boot Record)**: standard classico di partizionamento legato all'ambiente BIOS.
- **GPT (GUID Partition Table)**: standard moderno di partizionamento legato all'ambiente UEFI.
- **LBA (Logical Block Addressing)**: metodo di indirizzamento dei blocchi del disco che sostituisce il vecchio sistema CHS.

## Spiegazione Approfondita

Il partizionamento consente di suddividere un disco fisicamente unitario in più entità logiche separate. Questa operazione risponde a diverse necessità ingegneristiche: separare i file del Sistema Operativo dai dati utente, permettere l'installazione di sistemi multi-boot, impiegare File System differenti sullo stesso supporto e isolare aree di backup o di ibernazione per i dispositivi portatili.

> **Definizione**: Una partizione di un disco è una parte di disco separata da un punto di vista logico, considerata dal sistema operativo come un'unità di memorizzazione indipendente.

Storicamente, l'organizzazione logica in ambiente BIOS (utilizzato fino al 2010 circa) si è basata sul **MBR (Master Boot Record)**, posizionato nel primo settore del disco. Il MBR presenta forti limitazioni strutturali: supporta al massimo 4 partizioni primarie e ha un limite massimo di indirizzamento della memoria pari a 2 TB. 

I sistemi moderni utilizzano l'architettura **GPT (GUID Partition Table)** basata su **LBA (Logical Block Addressing)**. GPT supera i vincoli di spazio del predecessore e introduce ridondanza per la tolleranza ai guasti. La sua struttura fisica sul disco prevede:
- **LBA 0 (Protective MBR)**: un blocco di retro-compatibilità in sola lettura che mostra ai vecchi software di partizionamento il disco come un'unica grande partizione occupata. Questo evita che applicativi obsoleti interpretino erroneamente il disco GPT come vuoto, azzerando il rischio di formattazioni accidentali.
- **LBA 1 (Header GPT Primario)**: contiene la firma del disco, la dimensione dei blocchi e la posizione della tabella.
- **LBA 2-33 (Tabella delle Partizioni)**: contiene i record delle partizioni. Ogni record usa 16 byte per il Type Partition GUID, 16 byte per l'Unique Partition GUID, 8 byte per l'LBA iniziale, 8 byte per l'LBA finale, più il nome testuale e gli attributi.
- **Data Partition**: l'area effettiva in cui risiedono i file.
- **Backup Partition Table**: una copia speculare di sicurezza dell'header e della tabella dei record posizionata negli ultimi settori del disco, utilizzata per il ripristino automatico in caso di corruzione dei dati primari.

## Schema Riassuntivo

| Aspetto | MBR (Master Boot Record) | GPT (GUID Partition Table) |
|---------|---------------------------|----------------------------|
| **Ambiente Nativo** | BIOS | UEFI |
| **Limite Dimensione** | Max 2 TB | Supera i 2 TB (fino a 9.4 Zettabyte) |
| **Numero Partizioni** | Max 4 primarie (o 3 primarie + 1 estesa) | Praticamente illimitate (es. 128 in ambiente Windows) |
| **Sicurezza** | Nessuna copia di backup (Single Point of Failure) | Backup Partition Table alla fine del disco rigido |
| **Indirizzamento** | Sistema CHS (Cylinder-Head-Sector) / LBA limitato | Logical Block Addressing (LBA) nativo a 64 bit |

## Domande di Autovalutazione

1. Spiega per quale motivo un software di partizionamento obsoleto non distrugge la tabella GPT di un disco moderno quando esegue la lettura dell'LBA 0.
2. Un utente possiede un hard disk da 4 TB e desidera configurare 6 partizioni distinte per scopi di sviluppo. Quale schema di partizionamento è obbligatorio scegliere e per quali ragioni tecniche?

## Collegamenti

- [[Indice-sistemi]]
- [[creazione-gestione-partizioni]]