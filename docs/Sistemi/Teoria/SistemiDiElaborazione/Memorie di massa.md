---
date: 2026-03-02
time: 09:12
---
# Memorie di massa

Le **memorie di massa** conservano dati e programmi anche quando il calcolatore è spento. Hanno capacità elevate rispetto alla memoria principale e un costo per bit generalmente inferiore, ma latenze e modalità di accesso differenti dalla RAM. Il sistema operativo espone un'interfaccia logica comune attraverso driver, sottosistemi di I/O e file system.

## Memoria secondaria e file system

Dal punto di vista logico, il file system organizza i dati in file e directory, tiene traccia dei metadati e associa i contenuti a blocchi o estensioni del dispositivo. La separazione fra interfaccia del file system e driver permette alle applicazioni di accedere ai file senza conoscere la geometria fisica del dispositivo.

È utile distinguere:

- **supporto/dispositivo:** HDD, SSD, memoria flash USB o altro dispositivo persistente;
- **partizione/volume:** area logica gestita dal sistema operativo;
- **file system:** regole per nomi, directory, metadati, permessi e allocazione;
- **file:** oggetto logico identificato da nome e percorso, associato ai dati memorizzati.

Una partizione non è un file system e un file system non descrive necessariamente un intero disco fisico. Un disco può contenere più partizioni e un sistema operativo può usare anche volumi composti da più dispositivi.

## HDD: dischi magnetici

Un **Hard Disk Drive (HDD)** conserva i dati tramite magnetizzazione su piatti rotanti. Un HDD tradizionale comprende piatti, mandrino, testine di lettura/scrittura, braccio attuatore, elettronica di controllo e firmware. Le superfici sono organizzate fisicamente in tracce e settori; le tracce alla stessa posizione radiale sui diversi piatti vengono tradizionalmente descritte come un cilindro.

Il sistema operativo moderno indirizza normalmente i blocchi usando **LBA (Logical Block Addressing)**, cioè numeri logici di blocco, senza occuparsi direttamente di tracce e cilindri fisici. La geometria CHS (Cylinder-Head-Sector) è soprattutto un modello storico e non descrive fedelmente il modo in cui i dischi attuali rimappano i settori.

### Tempo di accesso

Per una lettura casuale su HDD, il tempo di accesso comprende soprattutto:

- **seek time:** movimento della testina sulla traccia richiesta;
- **latenza rotazionale:** attesa che il settore ruoti sotto la testina;
- **trasferimento:** tempo necessario a trasferire i dati;
- overhead del controller, firmware, interfaccia e sistema operativo.

Con velocità di rotazione `RPM`, la latenza di una rotazione completa è `60 / RPM` secondi; assumendo che il settore richiesto sia distribuito uniformemente, la latenza rotazionale media è approssimativamente metà rotazione:

\[
L_{media} \approx \frac{30}{RPM}\;s
\]

Ad esempio, a 7200 RPM la latenza rotazionale media ideale è circa 4,17 ms. È una stima: il tempo totale include anche seek e trasferimento e varia in base al carico.

Gli HDD sono particolarmente penalizzati da molte operazioni casuali perché la testina deve riposizionarsi. Letture sequenziali possono invece trasferire molti dati dopo un solo posizionamento iniziale.

## SSD e memoria flash

Un **Solid State Drive (SSD)** non ha parti meccaniche mobili. I dati sono memorizzati in celle NAND flash organizzate in pagine e blocchi. In generale, le pagine sono unità di lettura/programmazione mentre i blocchi sono unità di cancellazione; i dettagli dipendono dal tipo di memoria.

L'SSD include un controller che traduce gli indirizzi logici in posizioni fisiche, gestisce correzione degli errori, allocazione, recupero degli spazi e distribuzione delle scritture. La **Flash Translation Layer (FTL)** nasconde al sistema operativo la disposizione fisica delle celle.

Concetti importanti:

- **wear leveling:** distribuisce le scritture per evitare di consumare sempre le stesse celle;
- **garbage collection:** ricompone pagine ancora valide e recupera blocchi;
- **write amplification:** quantità di scritture interne rispetto ai dati richiesti dall'host;
- **TRIM/discard:** consente al sistema operativo di segnalare blocchi logici non più in uso, permettendo al dispositivo di gestirli più efficacemente;
- **ECC:** codici di correzione che aiutano a rilevare/correggere errori nelle celle.

La memoria NAND ha un numero finito di cicli di programmazione/cancellazione. Il controller e le tecniche di gestione contribuiscono alla durata, ma la resistenza effettiva dipende dalla tecnologia, dalla capacità, dal carico e dal modello del dispositivo.

## Interfacce e dispositivi

Le interfacce comuni includono SATA e PCIe/NVMe per unità interne; USB per dischi esterni e supporti rimovibili. **SATA** è un'interfaccia, mentre **NVMe** è un protocollo progettato per sfruttare unità a stato solido attraverso PCIe. Non confondere interfaccia fisica, protocollo e tecnologia di memorizzazione.

Esistono inoltre:

- **NAS:** dispositivo di archiviazione raggiunto tramite rete, spesso con accesso a file;
- **SAN:** rete/storage che espone risorse di memorizzazione a livello di blocco;
- **cloud storage:** servizio di memorizzazione fornito tramite rete, la cui durabilità dipende dall'architettura e dal contratto del provider;
- **supporti ottici e rimovibili:** utili per distribuzione, trasferimento o archiviazione, con caratteristiche e limiti propri.

RAID può migliorare disponibilità o prestazioni secondo il livello, ma **non sostituisce un backup**: cancellazioni accidentali, ransomware e guasti logici possono propagarsi anche su un array ridondato.

## Capacità, settori e unità

La capacità si esprime spesso in byte e multipli decimali (kB, MB, GB, TB) oppure binari (KiB, MiB, GiB, TiB). I produttori di unità usano normalmente multipli decimali, mentre alcuni sistemi operativi mostrano unità binarie con etichette non uniformi.

Non esiste una dimensione di settore universale valida per tutti i dispositivi. I settori logici da 512 byte sono comuni nei dispositivi legacy e il formato **Advanced Format** usa spesso settori fisici da 4096 byte, con presentazione logica che può essere 512e o 4Kn. L'unità logica vista dal sistema operativo non deve essere confusa con il settore fisico.

## File system e argomenti correlati

Per approfondire l'organizzazione e la gestione dei file consulta:

- [Filesystem manager](Filesystem%20manager.md): attributi, operazioni, mount/unmount e ruolo del sistema operativo;
- [Memoria secondaria](Memoria%20secondaria.md): struttura, prestazioni e tecnologie dei dispositivi;
- [Caratteristiche della memoria secondaria](Caratteristiche%20della%20memoria%20secondaria.md): formattazione, boot, swap e RAID;
- [Partizionamento MBR e GPT](partizionamento-disco-mbr-gpt.md);
- [Tipologie FAT ed Ext](tipologie-file-system-fat-ext.md);
- [Gestione delle partizioni](creazione-gestione-partizioni.md).

## Riepilogo

| Aspetto | HDD | SSD NAND |
|---|---|---|
| Principio | Magnetico, meccanico | Cella flash, nessuna parte mobile |
| Accesso casuale | Più lento per seek e rotazione | Generalmente molto più rapido |
| Latenza | Millisecondi tipici | In genere molto più bassa |
| Rumore/vibrazioni | Possibili | Nessuna parte meccanica mobile |
| Gestione specifica | Posizionamento testina, rotazione | Wear leveling, garbage collection, ECC, TRIM |
| Considerazioni | Capacità/costo convenienti in molti casi | Prestazioni e resistenza dipendono da modello e carico |

- [NVM Express](https://nvmexpress.org/)
- [Seagate — HDD basics](https://www.seagate.com/)
- [W3Schools — File handling in C](https://www.w3schools.com/c/c_files.php)
