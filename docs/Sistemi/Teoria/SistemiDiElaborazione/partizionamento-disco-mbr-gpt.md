---
tags: [studio, materia/sistemi, stato/approfondimento]
data_creazione: 2026-10-25
argomento: Partizionamento del disco, MBR e GPT
---
# Partizionamento del disco: MBR e GPT

Il **partizionamento** divide lo spazio indirizzabile di un dispositivo in aree logiche chiamate partizioni. Ogni partizione può contenere un file system, dati di avvio o altri contenuti richiesti dal sistema operativo. Il partizionamento è distinto dalla formattazione: prima si definisce la struttura delle partizioni, poi si crea un file system all'interno della partizione quando necessario.

## MBR — Master Boot Record

Il **MBR** è lo schema di partizionamento classico associato storicamente all'avvio BIOS. Le informazioni di partizionamento sono conservate nel primo settore logico tradizionale, insieme al codice di avvio secondo la struttura MBR.

Caratteristiche principali:

- la tabella tradizionale ha quattro voci di partizione;
- per superare il limite delle quattro voci si può utilizzare una partizione estesa contenente unità logiche;
- con settori logici da 512 byte e l'indirizzamento a 32 bit delle voci MBR, il limite classico è circa 2 TiB (2^32 × 512 byte);
- la struttura primaria è concentrata in un punto del disco e non offre la ridondanza della tabella GPT.

Il limite di circa 2 TiB è riferito alla combinazione tradizionale di MBR e settori logici da 512 byte; non va presentato come una legge indipendente da ogni dettaglio del formato.

## GPT — GUID Partition Table

**GPT** fa parte dello standard UEFI ed è lo schema generalmente raccomandato per i dischi moderni. Utilizza indirizzi LBA e identificatori GUID per descrivere il tipo e l'identità delle partizioni.

Una struttura GPT tipica include:

1. **LBA 0 — Protective MBR:** una voce MBR protettiva segnala ai vecchi strumenti che il disco contiene una struttura non-MBR. È una protezione di compatibilità, non un blocco che impedisce ogni possibile sovrascrittura.
2. **LBA 1 — Header GPT primario:** include firma, versione, dimensione dell'header, CRC, posizione della copia di backup, intervallo LBA utilizzabile e informazioni sulla tabella delle partizioni.
3. **Array delle voci:** descrive le partizioni. Una voce standard GPT da 128 byte include GUID del tipo, GUID univoco, LBA iniziale e finale, attributi e nome in UTF-16LE. Sistemi e strumenti possono supportare dimensioni differenti delle voci.
4. **Area dati:** intervallo utilizzabile assegnato alle partizioni.
5. **Tabella e header di backup:** si trovano tipicamente alla fine del disco e permettono agli strumenti di rilevare o riparare alcune forme di corruzione.

Gli header e gli array GPT utilizzano CRC per rilevare corruzioni dei metadati. La presenza della copia di backup non garantisce però un ripristino automatico in ogni sistema: in caso di danni servono strumenti compatibili e, se i dati sono importanti, una copia di sicurezza esterna.

## Confronto

| Caratteristica | MBR tradizionale | GPT |
|---|---|---|
| Uso tipico | Sistemi legacy BIOS | Sistemi moderni UEFI; supportato anche in altri contesti |
| Numero di partizioni | Quattro voci primarie; possibile partizione estesa | Molte partizioni; il limite pratico dipende da OS e strumenti |
| Capacità con settore logico da 512 B | Limite classico circa 2 TiB | Superiore a 2 TiB e molto più ampio |
| Identificatori | Tipi di partizione a codice numerico | GUID per tipo e identità |
| Ridondanza della tabella | Limitata | Header/array primario e copia di backup |
| Controllo di integrità | Limitato | CRC di header e voci |

GPT è in genere preferibile per un nuovo sistema, ma la scelta dipende da firmware, sistema operativo e requisiti di avvio. BIOS non è semplicemente “un ambiente usato fino a un determinato anno”: sistemi e schede madri legacy possono ancora usare BIOS, mentre UEFI è lo standard moderno.

## Esempio di ragionamento

Un disco da 4 TB con settore logico da 512 byte non può essere sfruttato integralmente con lo schema MBR tradizionale. GPT supera questo limite e consente di creare più partizioni senza ricorrere alla partizione estesa.

## Precauzioni

- Identifica con precisione il disco prima di modificare la tabella delle partizioni.
- Effettua un backup verificato prima di ridimensionare, ricreare o convertire partizioni.
- Non confondere tabella delle partizioni, partizione, volume e file system.
- Una conversione MBR↔GPT può richiedere modifiche alle partizioni e alla configurazione di avvio; non è una semplice rinomina del formato.

- [UEFI Forum — Specifications](https://uefi.org/specifications)
- [Microsoft Learn — Disks and partitions](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions)
