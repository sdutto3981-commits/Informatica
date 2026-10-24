# Introduzione ai file system

Un file system definisce come il sistema operativo organizza, nomina, localizza e gestisce file e directory su un dispositivo o volume. Può mantenere metadati come dimensione, date, proprietario e permessi, secondo il formato e il sistema operativo.

## Operazioni tipiche

- creare, aprire, leggere e scrivere un file;
- rinominare, spostare ed eliminare file;
- creare ed esplorare directory;
- verificare permessi e proprietà;
- gestire lo spazio libero e le informazioni necessarie al recupero dopo errori, se supportato.

## File system e partizioni non sono la stessa cosa

Una **partizione** definisce una porzione del dispositivo descritta dalla tabella delle partizioni. Un **file system** organizza i file all'interno di un volume. Un disco può avere più partizioni, e non tutte devono necessariamente contenere un file system montabile.

## Esempi

- FAT32: ampia compatibilità, ma non supporta file singoli oltre 4 GiB.
- exFAT: spesso usato per memorie rimovibili e file grandi.
- NTFS: comune in Windows, con funzionalità avanzate e permessi.
- ext4: comune nelle distribuzioni Linux.

Le caratteristiche dipendono dall'implementazione e dal sistema operativo. Prima di partizionare o formattare un'unità, eseguire un backup e verificare con precisione il dispositivo selezionato: la formattazione può cancellare i dati.
