---
tags: [studio, materia/sistemi, stato/approfondimento]
data_creazione: 2026-10-25
argomento: Tipologie di file system FAT ed Ext
---
# Tipologie di file system: FAT, ext e journaling

Un **file system** definisce come file e directory sono rappresentati, nominati, localizzati e protetti su un volume. Le implementazioni differiscono per compatibilità, limiti di dimensione, gestione dei metadati, permessi, resilienza agli arresti improvvisi e strumenti di manutenzione.

## FAT: File Allocation Table

La famiglia **FAT** usa una tabella di allocazione che descrive come sono collegati i cluster assegnati ai file. I cluster sono gruppi di settori gestiti come unità di allocazione del file system; la loro dimensione dipende dalla formattazione del volume.

- **FAT12** è stata usata principalmente su supporti piccoli e storici.
- **FAT16** usa una tabella con voci a 16 bit ed è stata impiegata su volumi di dimensioni limitate rispetto ai sistemi moderni.
- **FAT32** aumenta il numero di cluster indirizzabili rispetto a FAT16, ma mantiene limiti noti, tra cui la dimensione massima teorica di un singolo file di 4 GiB meno 1 byte.
- **exFAT** è stata progettata per memorie flash e supporti rimovibili di capacità maggiori, riducendo alcuni limiti di FAT32.

Una rappresentazione didattica di un volume FAT comprende area di avvio/parametri, copie della FAT secondo il formato, directory e area dati. I dettagli esatti variano tra FAT12, FAT16, FAT32 ed exFAT. Le voci di directory memorizzano il nome e attributi; la catena di cluster permette di trovare i blocchi successivi del file. Se la tabella viene danneggiata, un percorso può interrompersi oppure collegare cluster errati.

FAT non offre nativamente lo stesso modello di permessi Unix e ACL avanzate tipiche di file system moderni. È comunque utile quando si cerca ampia compatibilità fra sistemi e dispositivi.

## File system ext in Linux

La famiglia **ext** è usata su Linux:

- **ext2:** non dispone del journaling tipico delle versioni successive; un arresto improvviso può richiedere controlli più lunghi;
- **ext3:** aggiunge il journaling a una base compatibile con ext2;
- **ext4:** introduce miglioramenti di capacità, prestazioni e affidabilità, tra cui extents, allocazione ritardata e altre ottimizzazioni.

### Inode e directory

In ext, l'**inode** conserva metadati come tipo del file, permessi, proprietario, dimensione e timestamp, oltre alle informazioni necessarie a localizzare i dati. Il nome del file è conservato nella directory, che associa un nome a un numero di inode. Perciò il nome non è normalmente un campo dell'inode stesso.

Gli inode non sono “il file” in senso esclusivamente testuale: sono strutture del file system che descrivono un oggetto e i suoi metadati. Più nomi (*hard link*) possono riferirsi allo stesso inode, nei limiti del file system e dei permessi.

### Puntatori classici ed extents

Nei file system ext2/ext3 è comune descrivere l'organizzazione dei dati tramite puntatori diretti e indiretti (semplice, doppio e triplo) negli inode. Questa è una descrizione classica utile per comprendere la crescita dei file.

**Non va generalizzata all'implementazione tipica di ext4:** ext4 utilizza normalmente una struttura a **extents**, che descrive intervalli contigui di blocchi logici e fisici. Un extent può ridurre il numero di metadati necessari per grandi file contigui. La struttura esatta dipende dalle funzionalità del file system e dalle opzioni con cui è stato creato.

## Journaling: che cosa protegge

Il journaling registra in un giornale determinate modifiche ai metadati (e, in base alla modalità, parte o tutti i dati) in modo che il file system possa recuperare più rapidamente uno stato strutturalmente coerente dopo un arresto anomalo.

Non significa che ogni contenuto del file venga sempre copiato integralmente nel journal prima di essere scritto. Per ext3/ext4 esistono modalità diverse, tra cui `ordered`, `writeback` e `journal`; le garanzie e le prestazioni non sono uguali. Il journal migliora il recupero della **coerenza strutturale**, ma non sostituisce backup e non garantisce il ripristino di ogni scrittura applicativa immediatamente precedente al crash.

## Confronto sintetico

| Aspetto | FAT32/exFAT | ext2 | ext3 | ext4 |
|---|---|---|---|---|
| Contesto tipico | Rimovibili e compatibilità | Linux, uso specifico | Linux | Linux moderno |
| Organizzazione | FAT e cluster | Inode e blocchi | Inode e blocchi | Inode ed extents in uso tipico |
| Journaling | No journaling classico FAT | No | Sì | Sì |
| Permessi Unix | Non nativi come in ext | Sì | Sì | Sì |
| Caso d'uso | Scambio dati e supporti | Ambienti compatibili | Sistemi legacy | Sistemi Linux generali |

Il confronto non sostituisce le specifiche del sistema operativo e della versione: opzioni di mount, strumenti e funzionalità possono cambiare il comportamento effettivo.

## Scelta e manutenzione

1. Verifica il sistema operativo e i dispositivi che devono accedere al volume.
2. Controlla i limiti di dimensione per file e volume.
3. Valuta permessi, journaling, prestazioni, compatibilità e strumenti di recupero.
4. Prima di riformattare o riparare un volume, crea un backup e identifica con certezza il dispositivo.

- [Kernel.org — ext4 overview](https://docs.kernel.org/filesystems/ext4/)
- [Microsoft — exFAT specification](https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification)
- [The Linux man-pages project](https://man7.org/linux/man-pages/)
