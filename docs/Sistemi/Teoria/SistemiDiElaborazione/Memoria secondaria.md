# Memoria di Massa (Memoria Secondaria)

## Indice

- [Memorie di Massa e I/O](#wiki-memorie-di-massa-e-dispositivi-di-i-o)
- [File System](#wiki-file-system-e-memoria-di-massa)
- [Dischi Magnetici (HDD)](#wiki-struttura-dei-dischi-magnetici)
- [SSD e NVM](#wiki-dischi-a-stato-solido-ssd)
- [Algoritmi di Scheduling](#wiki-scheduling-del-disco)
- [Scheduling NVM](#wiki-scheduling-su-nvm)
- [Errori e Correzione](#wiki-rilevamento-e-correzione-di-errori)

---

## Memorie di Massa e Dispositivi di I/O {#wiki-memorie-di-massa-e-dispositivi-di-i-o}

I dispositivi collegati ad un calcolatore possono avere **caratteristiche altamente variabili** e rappresentano, nel loro insieme, la componente più **lenta, voluminosa e variegata** dell'elaboratore.

Il sistema operativo deve:

- Offrire alle applicazioni **interfacce semplici e uniformi** per l'accesso ai dispositivi
- Garantire l'**ottimizzazione dell'I/O**, che costituisce il collo di bottiglia delle prestazioni

---

## File System e Memoria di Massa {#wiki-file-system-e-memoria-di-massa}

### Struttura logica del File System

Dal punto di vista logico il file system si compone di **tre parti**:

1. **L'interfaccia al programmatore** → File system logico
2. **Le strutture dati interne e gli algoritmi di allocazione** → Modulo di organizzazione dei file + File System di Base
3. **Il livello più basso** legato alla memorizzazione su memoria secondaria → Controllo dell'I/O → Device

```
Programmi applicativi
        ↓
File system logico
        ↓
Modulo di organizzazione dei file
        ↓
File System di Base
        ↓
Controllo dell'I/O
        ↓
Device (HDD/SSD)
```

### Tipologie principali

|Tipo|Descrizione|
|---|---|
|**HDD**|Dischi magnetici – meccanici, economici, lenti|
|**SSD**|Dischi a stato solido – elettronici, veloci, costosi|

---

## Struttura dei Dischi Magnetici {#wiki-struttura-dei-dischi-magnetici}

### Composizione fisica

I dischi magnetici sono composti da:

- **Piatti** (platters): superfici circolari con diametro 1,8–5,25" ricoperte di materiale magnetico
- **Tracce** (tracks): corone circolari concentriche sulla superficie
- **Settori** (sectors): suddivisioni delle tracce
- **Cilindri** (cylinders): insieme delle tracce equidistanti dal centro su tutti i piatti
- **Spindle (asse)**: asse di rotazione dei piatti
- **Attuatore** + **braccio** + **testina** (read-write head): meccanismo di posizionamento

!!! info "Geometria del disco Cilindri + Tracce + Settori = **Geometria del disco**"

### Organizzazione della superficie

- Le tracce sono numerate **a partire da zero** dal bordo verso l'interno
- I settori contengono uno o più **blocchi** (normalmente 512 byte → standard attuale 4 KB)
- Il SO organizza il disco in **cluster** (più blocchi) per motivi di efficienza (2 KB–32 KB)
- Un file occupa sempre **almeno un cluster**

### Struttura logica (indirizzamento)

Dal punto di vista dell'indirizzamento, il disco è un **vettore monodimensionale di blocchi logici**:

- Si parte dalla traccia 0 del cilindro più esterno
- Si procede lungo la traccia → verso i cilindri più interni

### Modalità di rotazione

|Modalità|Descrizione|Utilizzo|
|---|---|---|
|**CAV** (Constant Angular Velocity)|Velocità di rotazione costante; densità bit decresce verso l'esterno|Dischi magnetici|
|**CLV** (Constant Linear Velocity)|Densità bit per traccia uniforme; velocità aumenta verso l'interno|CD, DVD|

### Lettura e Scrittura

La memorizzazione avviene tramite **testina** (bobina conduttiva):

- **Scrittura**: corrente nella bobina → campo magnetico → orientamento particelle ossido di ferro (0/1)
- **Lettura**: campo magnetico sul disco muove le particelle → induce corrente nella bobina

!!! warning "Head crash Le testine \"planano\" sulla superficie a ~10⁻⁴ mm. Il crollo della testina causa impatto fisico → necessità di sostituzione dell'unità."

Le fasi di accesso sono:

1. Posizionamento della testina sulla traccia di interesse
2. Attesa del passaggio del settore di interesse
3. Lettura o scrittura del dato → **accesso random**

---

## Tempo di Accesso al Disco

$$T_{accesso} = T_{seek} + T_{latency} + T_{transfer}$$

|Componente|Descrizione|Note|
|---|---|---|
|**Seek time**|Tempo per spostare la testina sulla traccia|Fattore più critico (movimento meccanico)|
|**Latency time**|Tempo per portare il settore sotto la testina|Dipende da RPM (~5.000–10.000 giri/min)|
|**Transfer time**|Tempo effettivo di lettura del settore|Lettura vera e propria|

### Latenza media in base agli RPM

|RPM|Latenza media|
|---|---|
|15.000|2 ms|
|10.000|3 ms|
|7.200|4,16 ms|
|5.400|5,55 ms|
|4.800|6,25 ms|

> **Latenza media = ½ giro** → formula: `60 / RPM / 2`

### Performance degli hard disk

- Velocità di trasferimento teorica: **6 Gb/sec**
- Velocità di trasferimento effettiva: **1 Gb/sec**
- Seek time: **3–12 ms** (9 ms in media per PC)

**Tempo medio di accesso** = seek time medio + latenza media

- Disco veloce: 3 ms + 2 ms = **5 ms**
- Disco lento: 9 ms + 5,55 ms = **14,55 ms**

**Tempo medio di I/O** = tempo medio accesso + (dati / velocità trasf.) + overhead

!!! example "Esempio calcolo I/O Blocco 4 KB, disco 7200 RPM, seek 5 ms, transfer 1 Gb/s, overhead 0,1 ms:"

    - Transfer = 4 KB / 1 Gb/s = 0,031 ms
    - I/O totale = 5 + 4,16 + 0,1 + 0,031 ≅ **9,3 ms**

### Formula Tempo di Lettura File

$$T_{lettura} = N_{blocchi} \times \left[ (N_{cilindri} \times T_{spostamento}) + T_{latenza} + T_{trasferimento/blocco} \right]$$

---

## Dischi a Stato Solido (SSD) {#wiki-dischi-a-stato-solido-ssd}

### Caratteristiche generali

Gli SSD utilizzano **tecnologia elettronica** (non meccanica) per memorizzare i dati:

- Nessuna parte in movimento
- Circuiti elettronici integrati per memorizzazione permanente
- Interfacce compatibili con HDD (SATA, SATA Express, M.2)
- Velocità di accesso **< 1 ms**, throughput ~200 MB/s

### SSD vs HDD

|Caratteristica|HDD|SSD|
|---|---|---|
|Parti meccaniche|Sì|No|
|Seek time|3–12 ms|~0,1 ms|
|Rumore|Sì|No|
|Resistenza urti|Bassa|Alta|
|Costo/GB|Basso|~4× HDD|
|Durata celle|Illimitata|Limitata (cicli write)|

### Tecnologia NAND Flash

Le memorie flash sono **EEPROM** basate su **Floating Gate MOSFET**:

- Ogni transistor = una "cella di memoria" (1 bit o più)

|Tipo|Bit/cella|Capacità|Affidabilità|
|---|---|---|---|
|**SLC**|1|Bassa|Alta|
|**MLC**|2|Media|Media|
|**TLC**|3|Alta|Bassa|

### Problematiche NAND

!!! warning "Impossibile sovrascrivere direttamente"

    - Scrittura a granularità di **pagina** (analogo del settore)
    - Cancellazione solo per **blocchi** interi (più pagine)
    - Le celle si **deteriorano** ad ogni ciclo di cancellazione

**FTL (Flash Translation Layer)**: tabella mantenuta dal controller per tracciare i blocchi logici validi.

**Garbage Collection**: processo per liberare spazio

1. Copiare le pagine valide in un altro blocco
2. Cancellare il blocco da liberare
3. Riscrivere nuovi dati

**Overprovisioning**: 7–20% di pagine riservate per la garbage collection e il wear leveling.

**DWPD (Drive Writes Per Day)**: metrica di durata

> Es.: SSD da 1 TB classe 5DWPD → si possono scrivere **5 TB/giorno** per tutta la garanzia

### NAND 3D

Le memorie NAND 3D impilano **strati multipli** di celle verticalmente:

- Maggiore capacità a parità di dimensioni
- Connessioni più corte → migliori performance
- Costi per byte ridotti rispetto a NAND 2D

Il **controller flash** gestisce: wear leveling + correzione errori.

---

## Connessione dei Dispositivi di Memoria

L'unità disco è connessa al calcolatore tramite **bus di I/O**:

|Bus|Note|
|---|---|
|IDE-ATA|Legacy|
|**SATA** (Serial ATA)|Standard attuale per HDD/SSD|
|USB|Plug and play, rimovibili|
|SCSI / SAS|Ambienti server|
|FC (Fiber Channel)|Alta velocità, enterprise|
|**NVMe**|SSD ad alte prestazioni via PCIe|

!!! info "NVMe I bus standard (SATA) possono essere troppo lenti per gli SSD ad alte prestazioni → collegamento diretto al **bus PCI** tramite tecnologia **NVMe (NVM express)**"

**Controllori**: unità di elaborazione sul bus

- **Adattatori**: lato calcolatore
- **Controllori dei dischi**: incorporati nell'unità a disco

---

## Scheduling del Disco {#wiki-scheduling-del-disco}

### Obiettivi

Il SO deve garantire per i dischi magnetici:

- **Tempi di accesso** contenuti
- **Ampiezza di banda elevata**

> **Ampiezza di banda** = bytes trasferiti / tempo dalla prima richiesta al completamento dell'ultimo trasferimento

Il SO può intervenire solo sul **seek time** (minimizzandolo).

`Seek time ∝ distanza di spostamento fra le tracce`

### Coda di test (esempio)

```
Coda richieste cilindri: 98, 183, 37, 122, 14, 124, 65, 67
Posizione iniziale testina: cilindro 53
Range dischi: 0–199
```

---

### Algoritmo FCFS (First Come First Served)

- Serve le richieste **nell'ordine di arrivo**
- **Intrinsecamente equo**
- Produce grandi oscillazioni → inefficiente

> **Movimento totale**: 640 cilindri (nell'esempio)

---

### Algoritmo SSTF (Shortest Seek Time First)

- Serve la richiesta con **minimo spostamento** dalla posizione attuale
- Più efficiente di FCFS
- Può causare **starvation** delle tracce periferiche
- Non è la scelta ottima globale

> **Movimento totale**: 236 cilindri (nell'esempio)

---

### Algoritmo SCAN (dell'Ascensore)

- Il braccio si muove da un **estremo all'altro** del disco
- Serve le richieste in sequenza, poi **inverte direzione**
- Richieste all'estremo opposto hanno i **tempi di attesa più lunghi**

> **Movimento totale**: 236 cilindri (nell'esempio)

---

### Algoritmo C-SCAN (Circular SCAN)

- Come SCAN ma al raggiungimento dell'ultimo cilindro **ritorna all'inizio senza servire richieste**
- I cilindri sono trattati come una **lista circolare**
- Garantisce **tempo di attesa più uniforme** rispetto a SCAN

> **Movimento totale**: 383 cilindri (nell'esempio)

---

### Algoritmo C-LOOK

- Miglioramento di C-SCAN
- Il braccio si sposta solo fino alla **richiesta più estrema** (non fino alla fine del disco)
- Poi inverte direzione immediatamente

> **Movimento totale**: tipicamente inferiore a C-SCAN

---

### Confronto algoritmi

|Algoritmo|Pro|Contro|
|---|---|---|
|**FCFS**|Equo|Inefficiente, grandi oscillazioni|
|**SSTF**|Semplice, efficiente|Starvation, tracce periferiche svantaggiate|
|**SCAN**|Buon compromesso|Attese lunghe agli estremi|
|**C-SCAN**|Attese uniformi|Movimento extra (ritorno)|
|**C-LOOK**|Attese uniformi, efficiente|Leggermente complesso|

!!! tip "Algoritmo consigliato"

    - **SSTF**: comune, semplice, abbastanza efficiente
    - **SCAN / C-SCAN**: migliori per sistemi con elevato carico I/O (evitano starvation)
    - **SSTF / LOOK** (e varianti circolari): scelte ragionevoli come algoritmi default

---

## Scheduling su NVM {#wiki-scheduling-su-nvm}

### Differenze rispetto agli HDD

Nei dispositivi NVM **non esistono parti mobili**, quindi:

- Si utilizza solitamente una politica **FCFS**
- Gli algoritmi tradizionali di scheduling **non hanno più senso**
- Tempo di accesso molto più veloce: **0,05–0,5 ms**

### Write Amplification

$$WA = \frac{\text{dati scritti sulla memoria flash}}{\text{dati inviati dal S.O.}}$$

Quando si riscrive una pagina:

1. Bisogna **cancellare l'intero blocco** che la contiene
2. Le pagine valide nel blocco vanno **copiate altrove**
3. Solo allora si può scrivere il nuovo dato

→ Necessità di **garbage collector** per mantenere le performance

### Istruzione TRIM

!!! info "TRIM Permette al SO di **notificare al controller SSD** quali pagine non sono più utilizzate dal filesystem. Senza TRIM, il controller non sa quali blocchi eliminare e le performance calano nel tempo."

---

## Rilevamento e Correzione di Errori {#wiki-rilevamento-e-correzione-di-errori}

### Tecniche di rilevamento

|Tecnica|Descrizione|
|---|---|
|**Bit di parità**|Forma semplice di checksum; rileva errori singoli|
|**Checksum**|Aritmetica modulare su parole a lunghezza fissa|
|**CRC** (Cyclic Redundancy Check)|Funzione hash per rilevare errori su più bit; comune nelle reti|
|**ECC** (Error Correction Code)|Rileva **e corregge** alcuni errori|

### Tipologie di errori ECC

- **Errori soft**: correggibili
- **Errori hard**: rilevati ma **non correggibili**

> ECC è utilizzato a livello di **settore/pagina** nei dispositivi di storage.

---

## 📌 Note e Riferimenti

!!! note "Primo hard disk commerciale **1956** – IBM 305 RAMAC: occupava una stanza 9×15m, includeva 50 dischi da 24\", capacità 5 milioni caratteri, tempo di accesso ~600 ms."

### Tag

#sistemi-operativi #memoria #storage #HDD #SSD #NAND #scheduling #filesystem

---

_Data di aggiornamento gestita dalla cronologia Git._
