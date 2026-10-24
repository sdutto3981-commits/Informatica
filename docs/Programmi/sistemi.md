# Sistemi telematici e laboratorio — programma 3INF

## Obiettivi

Comprendere l'architettura del calcolatore, memorie e file system; assemblare PC, installare sistemi operativi fisici o virtuali, utilizzare la shell Linux e programmare in ANSI C, soprattutto per la gestione dei file.

## 1. Sistema calcolatore (28 ore)

**Appunti:** [sistemi di elaborazione](../Sistemi/Teoria/SistemiDiElaborazione/index.md), [componenti del computer](../Sistemi/Teoria/ComponentiComputer/index.md).

- Modello di Von Neumann: CPU, memoria, input/output e bus.
- CPU: unità di controllo, ALU, registri e ciclo fetch-decode-execute.
- Microprocessore e microcontrollore; ISA e microarchitettura.
- Pipeline: sovrapposizione delle fasi di istruzioni, stalli e conflitti introduttivi.
- Bus dati, indirizzi e controllo.
- Gerarchia della memoria: registri, cache e RAM.

## 2. Memorie di massa e file system (20 ore)

- HDD magnetici e SSD: funzionamento, prestazioni, latenza e differenze.
- Capacità, tempo di accesso e throughput.
- RAID: striping, mirroring e parità. RAID non equivale a backup.
- Partizioni, MBR/GPT, avvio del sistema e volumi.
- FAT/exFAT, NTFS ed ext: directory, metadati, permessi e organizzazione dei dati.
- Operazioni di creazione, apertura, lettura, scrittura, rinomina ed eliminazione dei file.

Prima di modificare partizioni o file system, eseguire un backup e verificare con attenzione il dispositivo selezionato.

## 3. Sistemi operativi e memoria centrale (18 ore)

**Integrazioni:** [kernel e interrupt](../Sistemi/Teoria/SistemiDiElaborazione/Kernel%20e%20interrupt.md), [paginazione e segmentazione](../Sistemi/Teoria/SistemiDiElaborazione/Paginazione%20e%20segmentazione.md).

- Sistema operativo come intermediario tra hardware, applicazioni e utenti.
- Kernel, processi e servizi; modalità utente e kernel.
- Interrupt e gestione degli eventi.
- Modello a strati (incluso il modello “Onion Skin” se usato dal docente).
- Memoria virtuale, indirizzi logici e fisici.
- Segmentazione e paginazione: organizzazione dello spazio, tabelle e protezione.

## 4. Assemblaggio e macchine virtuali (12 ore)

**Appunti:** [componenti PC](../Sistemi/Teoria/ComponentiComputer/index.md), [macchine virtuali](../Sistemi/VirtualMachine/index.md).

- Compatibilità tra scheda madre, socket, CPU, RAM, alimentatore, case e dissipatore.
- Montaggio sicuro, connettori di alimentazione e front panel; attenzione alle scariche elettrostatiche.
- BIOS/UEFI e controllo del riconoscimento dei componenti.
- Host, guest, hypervisor, disco e rete virtuale.
- Snapshot come ripristino rapido, non come unico backup.

## 5. Linux e shell (15 ore)

**Appunti:** [Linux](../Sistemi/Linux/index.md), [comandi Linux](../Sistemi/Linux/Comandi%20Linux.md), [permessi](../Sistemi/Linux/Permessi%20in%20Linux.md), [utenti](../Sistemi/Linux/Utenti.md).

| Comando | Funzione |
|---|---|
| `pwd`, `ls -la`, `cd` | mostra, elenca e cambia directory |
| `mkdir`, `rmdir` | crea/elimina una directory vuota |
| `cp`, `mv`, `rm` | copia, sposta/rinomina, elimina (attenzione) |
| `cat`, `less`, `tail` | visualizza contenuto dei file |
| `grep`, `find` | ricerca testo e file |
| `chmod`, `chown` | modifica permessi e proprietario |
| `whoami`, `id` | mostra identità e gruppi |
| `man` | apre il manuale |

Approfondire percorsi assoluti/relativi, utenti e gruppi, permessi `rwx`, pipeline (`|`), redirezioni (`>`, `>>`, `<`), codici di uscita e uso prudente di `sudo`.

## 6. ANSI C (40 ore)

**Appunti:** [C](../Sistemi/C/index.md), [file, puntatori e memoria dinamica](../Sistemi/C/File%20e%20memoria%20dinamica.md), [liste concatenate](../Sistemi/C/Liste%20concatenate.md).

- Compilazione e collegamento; tipi, costanti, operatori e formati di `printf`/`scanf`.
- Selezione, iterazione, funzioni e prototipi.
- Vettori, stringhe terminate da `\0`, matrici e `struct`.
- Puntatori, indirizzi e dereferenziazione.
- File con `FILE *`, `fopen`, `fclose`, `fprintf`, `fscanf`, `fgets` e gestione errori.
- Memoria dinamica con `malloc`/`calloc` e rilascio con `free`.
- Liste collegate introduttive: nodi, collegamenti, inserimento e attraversamento.

## Autoverifica

- [ ] Descrivere ciclo macchina, ALU, registri e bus.
- [ ] Confrontare RAM, cache, HDD e SSD.
- [ ] Spiegare MBR/GPT e lo scopo di un file system.
- [ ] Distinguere kernel, interrupt e memoria virtuale.
- [ ] Descrivere assemblaggio PC e configurazione VM.
- [ ] Gestire file e permessi da shell.
- [ ] Usare funzioni, stringhe, `struct` e puntatori in C.
- [ ] Leggere file, gestire memoria dinamica e spiegare liste concatenate.
