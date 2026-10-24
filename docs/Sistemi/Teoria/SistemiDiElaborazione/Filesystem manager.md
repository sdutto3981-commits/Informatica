---
date: 2026-10-25
tags: [studio, materia/sistemi, file-system]
---
# Filesystem manager

Il **file system manager** è la parte del sistema operativo che coordina l'accesso ai file e alle directory sui volumi. Offre alle applicazioni operazioni logiche come creare, aprire, leggere, scrivere, rinominare e cancellare file, nascondendo la maggior parte dei dettagli del dispositivo fisico e del layout dei blocchi.

Il file system manager non coincide con una singola struttura su disco: collabora con il codice che gestisce i file system, i driver del dispositivo, la cache/buffer del kernel e i meccanismi di autorizzazione.

## Indice

- [Attributi e metadati dei file](#attributi-e-metadati-dei-file)
- [Funzioni del file system manager](#funzioni-del-file-system-manager)
- [Operazioni sui volumi: formattazione, mount e unmount](#operazioni-sui-volumi-formattazione-mount-e-unmount)
- [Creazione e descrittori dei file](#creazione-e-descrittori-dei-file)
- [Lettura, scrittura e chiusura](#lettura-scrittura-e-chiusura)
- [Cancellazione e recupero dello spazio](#cancellazione-e-recupero-dello-spazio)
- [Strutture interne e allocazione](#strutture-interne-e-allocazione)
- [NTFS, inode ed ext](#ntfs-inode-ed-ext)
- [Riepilogo](#riepilogo)

## Attributi e metadati dei file

Oltre ai contenuti, il file system conserva metadati che consentono al sistema operativo di identificare, localizzare e proteggere un oggetto. Gli attributi effettivamente disponibili cambiano secondo il file system e il sistema operativo.

Gli attributi comuni possono includere:

- **nome e percorso:** il nome è normalmente un elemento della directory; il percorso identifica la posizione logica nel namespace;
- **tipo:** file regolare, directory, collegamento simbolico o altro oggetto, secondo il sistema;
- **dimensione logica:** lunghezza del contenuto in byte; può differire dallo spazio fisico occupato;
- **posizione dei dati:** intervalli, blocchi o altre strutture che consentono di localizzare i dati sul volume;
- **proprietario e gruppo:** identità cui sono associati alcuni diritti, quando il file system supporta il concetto;
- **permessi e attributi di sicurezza:** regole che controllano lettura, scrittura, esecuzione o accesso;
- **timestamp:** tempi di creazione, modifica dei dati, modifica dei metadati e/o ultimo accesso. I nomi e la semantica dei timestamp variano tra file system;
- **stato e attributi specifici:** sola lettura, nascosto, compressione, cifratura, integrità, collegamenti e altri campi proprietari.

Non tutte le implementazioni memorizzano questi campi nello stesso modo e non tutti i timestamp hanno una semantica identica. Per esempio, il nome di una directory non è necessariamente contenuto nell'inode di un file ext: la directory associa un nome all'identificatore dell'oggetto.

## Funzioni del file system manager

Le responsabilità principali comprendono:

1. presentare una struttura gerarchica di file e directory;
2. tradurre percorsi e nomi nei relativi oggetti e metadati;
3. allocare e liberare lo spazio quando il contenuto viene creato, esteso o eliminato;
4. coordinare lettura e scrittura con driver, cache e dispositivo;
5. gestire permessi, proprietà, condivisione e controlli di accesso;
6. fornire operazioni coerenti per aprire, leggere, scrivere, spostare, rinominare e cancellare oggetti;
7. gestire il mount/unmount di volumi e l'interpretazione delle strutture del file system;
8. supportare consistenza e recupero in caso di arresti imprevisti, secondo le capacità del file system;
9. coordinare accessi concorrenti e blocchi quando necessario;
10. notificare errori di I/O, spazio insufficiente, permessi negati e altre condizioni eccezionali.

Il backup non è una funzione garantita dal solo file system manager. Può essere realizzato da altri servizi, applicazioni o strumenti amministrativi; una copia di backup deve essere gestita e verificata esplicitamente.

## Operazioni sui volumi: formattazione, mount e unmount

### Inizializzazione o creazione di un file system

Su un volume nuovo o destinato a essere riutilizzato, la creazione del file system scrive strutture quali superblock o boot sector, tabelle/indici, mappe dello spazio libero, directory radice e altre informazioni previste dall'implementazione. I nomi e la posizione dei metadati dipendono dal file system.

L'inizializzazione può registrare identificativo del volume, parametri organizzativi, numero e dimensione dei blocchi e strutture che consentono di individuare lo spazio allocato e quello libero. La directory radice viene creata secondo il formato, pronta a contenere altre directory e file.

**La formattazione di alto livello non è la stessa cosa della formattazione fisica del supporto.** Nei sistemi moderni i settori fisici e le aree difettose sono spesso gestiti dal firmware del dispositivo. La creazione del file system organizza invece il volume in modo che il sistema operativo possa salvarvi i dati.

### Mount

Il **mount** collega un file system a un punto del namespace del sistema operativo, rendendo raggiungibili i suoi file tramite un percorso. In Linux il comando è tipicamente `mount`; la directory scelta è chiamata *mount point*. In altri sistemi il volume può essere associato a una lettera di unità o a un altro identificatore visibile all'utente.

Durante il mount il sistema controlla che il formato sia riconosciuto, legge i metadati essenziali e applica le opzioni di accesso. Se il volume risulta incoerente, il sistema può limitarne l'accesso, montarlo in sola lettura oppure richiedere una verifica o una riparazione. Il controllo non sempre esamina subito ogni singolo contenuto: eseguire una scansione completa può richiedere tempo.

### Unmount

L'**unmount** rimuove il file system dal punto di accesso e chiede al sistema di completare le operazioni pendenti e sincronizzare le modifiche necessarie. Il volume non va scollegato mentre è in uso: farlo può causare perdita di dati o incoerenza, soprattutto se sono presenti scritture in cache.

Lo smontaggio può essere richiesto manualmente o effettuato durante la chiusura del sistema. In Linux si usa normalmente `umount` (senza la lettera `n` finale). Se un file è aperto o un processo usa il mount point, il sistema può rifiutare l'operazione o segnalare che il file system è occupato.

## Creazione e descrittori dei file

Quando un programma chiede di creare o aprire un file, il sistema controlla percorso, permessi e modalità richieste. In un file system Unix-like, directory e inode (o strutture equivalenti) permettono di collegare il nome al contenuto e ai metadati. Il programma riceve un descrittore o un handle che utilizzerà nelle successive operazioni.

Il descrittore di file restituito da una chiamata di sistema non è necessariamente il record fisico conservato sul disco. È un riferimento gestito dal sistema operativo alla risorsa aperta, con stato quale posizione corrente di lettura/scrittura e flag di apertura.

Al momento della creazione, il sistema memorizza i metadati e alloca o riserva le strutture necessarie. **Lo spazio per il contenuto può essere allocato in maniera differita**, secondo il file system e le modalità di scrittura; la creazione di un file vuoto non implica sempre che sia già stato assegnato un grande intervallo di blocchi dati.

Le operazioni comuni comprendono:

- creazione di un file vuoto;
- apertura di un file esistente in lettura, scrittura o modalità combinata;
- lettura di una parte dei contenuti a partire dalla posizione corrente;
- scrittura o aggiunta di dati e aggiornamento della dimensione;
- spostamento della posizione di lettura/scrittura (*seek*), quando supportato;
- chiusura dell'handle e rilascio delle risorse del processo.

## Lettura, scrittura e chiusura

In lettura, il sistema recupera i dati dai blocchi/extent pertinenti, eventualmente tramite cache e buffer, e li mette a disposizione del processo. In scrittura, i dati possono essere prima inseriti in buffer di memoria e poi inviati al dispositivo. Di conseguenza, il ritorno di una chiamata di scrittura non implica sempre che tutti i dati siano già persistiti fisicamente sul supporto: la garanzia dipende dall'API e dalle richieste di sincronizzazione.

Durante la scrittura possono essere aggiornati dimensione del file, timestamp, mappe di allocazione, directory e altre strutture di metadati. Le implementazioni con journaling o altri meccanismi di consistenza adottano procedure specifiche per coordinare questi aggiornamenti.

Il concetto di **EOF (End Of File)** indica che non restano altri dati da leggere da quel flusso. In molte API, EOF è rilevato quando un tentativo di lettura non riesce a produrre altri dati; non è corretto presumere che ogni file contenga un carattere fisico speciale EOF inserito dopo l'ultimo byte. In C, ad esempio, `feof()` segnala un indicatore impostato dopo un tentativo di lettura che raggiunge la fine del file.

La chiusura del file rilascia il descrittore o handle e può completare il flush dei buffer. Per applicazioni che richiedono durabilità specifica esistono API di sincronizzazione, ma il loro significato dipende dal sistema operativo e dal dispositivo.

## Cancellazione e recupero dello spazio

L'eliminazione di un file normalmente rimuove il collegamento del nome dalla directory e aggiorna i metadati o i riferimenti necessari. I blocchi precedentemente occupati possono essere marcati come liberi, resi riutilizzabili o recuperati da un processo di garbage collection: non è garantito che ogni byte venga immediatamente azzerato.

Su file system con collegamenti multipli, la rimozione di un nome non elimina necessariamente il contenuto se altri nomi o processi mantengono riferimenti aperti. Su sistemi Unix-like, un file cancellato può continuare a occupare spazio fino a quando l'ultimo handle aperto viene chiuso.

La cancellazione logica non è una procedura sicura di cancellazione dei dati. Su SSD, wear leveling e rimappatura delle celle rendono inoltre difficile garantire la sovrascrittura fisica tramite una semplice scrittura sullo stesso indirizzo logico. Per la cancellazione sicura occorre considerare le funzionalità supportate dal dispositivo, la cifratura e le procedure specifiche del sistema.

## Strutture interne e allocazione

Il file system gestisce unità di allocazione come blocchi o cluster e struttura i metadati in base al formato. È importante distinguere:

- **settore:** unità di indirizzamento logico/fisico del dispositivo secondo il formato;
- **blocco del file system:** unità logica con cui un file system organizza e trasferisce dati;
- **cluster:** gruppo di settori usato come unità di allocazione in file system come FAT;
- **extent:** intervallo di blocchi contigui rappresentato come singola estensione, usato da file system moderni;
- **inode o record equivalente:** struttura dei metadati che descrive un oggetto del file system.

Nei file system basati su inode, un inode può memorizzare riferimenti diretti/indiretti (come in una descrizione classica di ext2/ext3) o extents, secondo l'implementazione. In FAT la tabella di allocazione descrive la catena dei cluster. Altri file system, ad esempio NTFS, utilizzano record e attributi della Master File Table (MFT), senza seguire necessariamente lo stesso modello degli inode Unix.

Le strutture sono progettate per rendere efficienti operazioni su file grandi e piccoli, directory, spazio libero, permessi e recupero. Le scelte interne influiscono su frammentazione, prestazioni, limiti di dimensione e robustezza; non esiste un solo layout valido per tutti i file system.

## NTFS, inode ed ext

In **NTFS**, la Master File Table (MFT) contiene record che descrivono i file e le directory. I record contengono attributi, che possono includere nome, dati, sicurezza e altri metadati. Alcuni contenuti piccoli possono essere residenti nel record stesso; i contenuti più grandi sono descritti tramite strutture che indicano dove si trovano i dati.

Nei file system **ext** di Linux, l'inode descrive l'oggetto e la directory memorizza il collegamento fra il nome e l'inode. Ext2/ext3 sono spesso illustrati con puntatori diretti e indiretti; ext4 usa normalmente extents per descrivere intervalli di blocchi. Ext3 ha introdotto il journaling nella famiglia ext: il journal contribuisce alla coerenza e al recupero dei metadati, ma non rappresenta un backup e le garanzie sui dati dipendono dalla modalità.

## Riepilogo

Il file system manager fornisce un'interfaccia ai file e alle directory, mentre le strutture interne determinano come i dati e i metadati sono organizzati sul volume. Le operazioni di creazione, lettura, scrittura, chiusura, cancellazione e mount/unmount richiedono aggiornamenti coordinati e controlli di accesso. Per comprendere un caso reale occorre distinguere le responsabilità del sistema operativo dai dettagli specifici di FAT, NTFS, ext e degli altri file system.

- [Linux man-pages — mount(8)](https://man7.org/linux/man-pages/man8/mount.8.html)
- [Linux man-pages — umount(8)](https://man7.org/linux/man-pages/man8/umount.8.html)
- [Linux kernel documentation — ext4](https://docs.kernel.org/filesystems/ext4/)
