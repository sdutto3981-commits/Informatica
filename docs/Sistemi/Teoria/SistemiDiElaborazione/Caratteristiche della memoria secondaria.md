---

date: 2026-03-23
time: 09:10
---

# L14 — Gestione della Memoria Secondaria

## Indice

1. [[#1. Formattazione]]
2. [[#2. Blocco di BOOT]]
3. [[#3. Gestione dei Blocchi Difettosi]]
4. [[#4. Gestione dell'Area di Swap]]
5. [[#5. RAID — Redundant Array of Independent Disks]]
6. [[#6. Connessione dei Dispositivi di Memoria]]

---

> [!abstract] Obiettivi della lezione Il SO deve occuparsi di quattro compiti fondamentali relativi alla memoria secondaria:
>
> 1. **Inizializzare** i dispositivi tramite formattazione (fisica e logica)
> 2. **Creare il blocco di boot** per l'avvio del sistema
> 3. **Gestire i blocchi difettosi** del disco
> 4. **Gestire in modo efficiente l'area di swap**

## 1. Formattazione

### 1.1 Formattazione Fisica (o di basso livello)

Alla produzione, il disco magnetico **non è diviso in settori** e quindi non può essere letto o scritto dal controller. La formattazione fisica è l'operazione che:

- Suddivide il disco in **settori**
- Identifica ogni settore (header + area dati + coda)
- Aggiunge spazio per la **correzione degli errori (ECC)**

> [!info] Struttura di un settore (512 byte standard) Ogni settore è composto da:
>
> - **Intestazione (Header)** — contiene numero di settore/pagina e codice ECC
> - **Area dati** — tipicamente 512 byte (standard moderno: 4 KB)
> - **Coda (ECC)** — 40 × 10 bit = 50 byte per la correzione degli errori

> [!note] Come funziona l'ECC Il controller calcola il codice ECC a **run-time** durante ogni lettura. Se il valore calcolato **differisce** da quello memorizzato nel settore → si è verificato un errore su quel settore.

**Nel caso di NVM (es. SSD):** devono essere inizializzate le **pagine** e creata la tabella **FTL (Flash Translation Layer)**.

In entrambi i casi, la formattazione di basso livello inserisce per ogni blocco: **intestazione, dati, coda**.

> [!warning] La formattazione fisica è eseguita dal costruttore dell'unità come parte del processo produttivo.

---

### 1.2 Formattazione Logica (creazione del file system)

Per poter memorizzare file, il SO deve mantenere le proprie strutture dati sul disco:

1. Si **partiziona** il dispositivo in uno o più gruppi di cilindri/pagine → ogni gruppo è un **disco logico**
2. Si crea un **file system** su ogni partizione:
    - Strutture dati per descrivere lo spazio libero/occupato
    - Creazione di una **directory radice vuota**
    - Lista spazio occupato (**FAT**) e libero (**Free List – FL**)

> [!tip] Cluster Per migliorare le prestazioni, la maggior parte dei file system accorpa i blocchi in gruppi detti **cluster**:
>
> - L'I/O su disco avviene per **blocchi**
> - L'I/O via file system avviene per **cluster** (accesso sequenziale)
> - File e metadati vicini su HDD → meno movimenti della testina

```
Disco vergine → [formattazione fisica] → H | ECC | H | ECC | H | ...
              → [formattazione logica]  → H | FAT | H | FAT | H | FL | ...
```

---

## 2. Blocco di BOOT

### 2.1 Bootstrap

All'accensione (o riavvio), il computer esegue un programma iniziale molto semplice detto **bootstrap**, che:

- Inizializza il sistema
- Avvia il Sistema Operativo

### 2.2 Dove si trova il bootstrap?

|Posizione|Vantaggio|Svantaggio|
|---|---|---|
|**ROM**|Sempre disponibile|Difficile aggiornare il codice|
|**Disco (area di boot)**|Facilmente aggiornabile|Richiede lettura dal disco prima del SO|

**Approccio reale (misto):**

- Nella **ROM** → piccolo programma detto **bootstrap loader**
- Sul **disco** → programma di avvio completo nell'**area di boot**

> [!important] Nota bene Quando viene letta l'area di boot, il SO **non è ancora stato caricato**, non esistono driver né file system. L'accesso è quindi una lettura diretta di **settori fisici**, non una normale lettura di file.

### 2.3 Struttura del disco di boot

Un **disco di sistema** (o unità di avvio) contiene:

- Una **partizione di boot** → contiene il SO
- Un **boot block** (primo blocco logico del dispositivo)
- Altre partizioni → possono contenere altri SO, file system, o partizioni raw

**In Windows:** il boot block si chiama **MBR (Master Boot Record)**

```
Sequenza di avvio Windows:
1. Firmware esegue il bootstrap loader (ROM)
2. Lettura/esecuzione del codice nell'MBR
   └── MBR contiene: boot code + partition table (con flag che identifica la partizione di boot)
3. Caricamento del kernel dalla partizione di boot
```

> [!note] Al montaggio di ogni partizione Si verifica la **coerenza del file system** (correttezza dei metadati) e si aggiorna la **tabella di montaggio**.

---

## 3. Gestione dei Blocchi Difettosi

I dischi magnetici sono strutturalmente soggetti a malfunzionamenti perché composti da **parti mobili con basse tolleranze**.

### Tecnica: Accantonamento dei settori (Sector Sparing)

- Durante la formattazione fisica si mantiene un **gruppo di settori di riserva** non visibili al SO
- Il controller sostituisce logicamente un **settore difettoso** con uno dei settori di riserva inutilizzati

> [!note] NVM (SSD) Anche i dispositivi NVM possono contenere **pagine difettose**, sostituite logicamente tramite pagine accantonate o appartenenti alla riserva dell'**over-provisioning**.

---

## 4. Gestione dell'Area di Swap

### 4.1 Cos'è

L'**area di swap** è una porzione di disco usata dal gestore della memoria come **estensione della memoria principale** (memoria virtuale).

Essa viene utilizzata per caricare un programma in modo sequenziale e fa da estensione per la RAM

> [!tip] Oggi meno comune grazie all'aumento delle capacità delle memorie RAM.

### 4.2 Dove si trova

- Nel **file system normale** (meno efficiente)
- In una **partizione separata (raw)** → preferibile, perché adotta algoritmi ottimizzati per la velocità di accesso, non per l'occupazione di spazio

### 4.3 Strategie di allocazione a confronto

| Sistema          | Strategia                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| **4.3BSD**       | Alloca spazio appena parte il processo (text + data); per lo stack, alloca man mano che cresce                     |
| **Solaris 2**    | Alloca una pagina sullo stack solo quando si deve fare un **page-out**, non alla creazione della pagina virtuale   |
| **Windows 2000** | Alloca spazio sul file di swap per ogni pagina virtuale non corrispondente a nessun file nel file system (es. DLL) |

### 4.4 Gestione dell'area di swap in Linux

In Linux, lo swap è usato **solo per la memoria anonima**: dati che non corrispondono a file (stack, heap, dati non inizializzati).

- Linux permette **una o più aree di avvicendamento** (sia su file che su partizione raw), su unità diverse per distribuire il carico della paginazione
- Un'area di avvicendamento è formata da moduli da **4 KB** detti **slot delle pagine**

**Mappa di avvicendamento (swap map):** Ogni area dispone di un array di contatori interi, uno per slot:

| Valore contatore | Significato                                                                         |
| ---------------- | ----------------------------------------------------------------------------------- |
| **0**            | Pagina disponibile (slot libero)                                                    |
| **> 0**          | Slot occupato; il valore indica il numero di processi che condividono quella pagina |

```
Swap Area:
┌──────┬──────┬──────┬──────┬──────┐
│  P1  │      │  P2  │      │  P3  │   ← swap partition/file
└──────┴──────┴──────┴──────┴──────┘
   1      0      3      0      1        ← swap map
```

> Se il contatore vale **3** → la pagina fa parte dello spazio degli indirizzi virtuali di **3 processi distinti**.

---

## 5. RAID — Redundant Array of Independent Disks

### 5.1 Motivazione

Problema: la differenza di velocità tra applicazioni e dischi aumenta sempre di più, e le cache non sono sempre efficaci.

**Soluzione:** Suddividere il carico su più dischi che cooperano per offrire l'immagine di un **disco virtuale unitario** più efficiente.

### 5.2 Cos'è il RAID

> RAID implementa **affidabilità** del sistema memorizzando **informazione ridondante**.

L'idea è quella di combinare una serie di dischi a basso costo in modo da ottimizzare il sistema in termine di capacità affidabilità  e velocità rispetto a un disco di ultima generazione.

I dischi più economici sono gli
- IDE
- ATA
- SATA

Si raggruppano più unita fisiche reali in un unico disco logico esso viene chiamato ULU

- La ridondanza può essere gestita dal **controller** (RAID hardware) o dal **driver** (RAID software)
- Esistono diversi **livelli** (organizzazioni), a seconda del tipo di ridondanza
- I dati vengono partizionati in **stripes** di uguale lunghezza e distribuiti su più dischi quando l'elemento supera la lunghezza della stripe esso viene distribuito in parallelo sui vari dischi

### 5.3 Livelli RAID

#### RAID 0 — Striping (min. 2 dischi)

```
      RAID 0
  Disk 0 | Disk 1
  -------+-------
    A1   |   A2
    A3   |   A4
    A5   |   A6
    A7   |   A8
```

- I dati vengono suddivisi in blocchi (stripe) distribuiti sui dischi
- **Altissima performance** in lettura/scrittura
- **Nessuna ridondanza** → perdita di dati in caso di guasto

#### RAID 1 — Mirroring / Shadowing (min. 2 dischi)

```
      RAID 1
  Disk 0 | Disk 1
  -------+-------
    A1   |   A1
    A2   |   A2
    A3   |   A3
    A4   |   A4
```

- I dati vengono **duplicati** su coppie di dischi
- **Lettura raddoppiata**, scrittura uguale a disco singolo
- In caso di guasto → si usa immediatamente l'altro disco (no ricostruzione)
- **Svantaggio:** spreco di spazio (50% di efficienza) siccome duplichiamo le informazioni

#### RAID 3 — Bit/Byte Interleaved Parity (min. 3 dischi)

- Dati organizzati a livello di **bit o byte**
- Usa **XOR** come ECC; i byte di parità sono su un disco dedicato
- Prestazioni molto elevate in lettura/scrittura
- Ottima tolleranza ai guasti
- **Limite:** può evadere una sola richiesta per volta

#### RAID 4 — Block-Level Parity (min. 3 dischi)

- Dati suddivisi in **blocchi**; parità su disco dedicato
- Prestazioni molto elevate in **lettura**
- Ottima tolleranza ai guasti
- **Svantaggio:** il disco di parità è un **collo di bottiglia** in scrittura

#### RAID 5 — Block Interleaved Distributed Parity (min. 3 dischi)

```
      RAID 5 (4 dischi)
  D0  |  D1  |  D2  |  D3
 -----+-------+------+------
  A1  |  A2  |  A3  |  Ap
  B1  |  B2  |  Bp  |  B3
  C1  |  Cp  |  C2  |  C3
  Dp  |  D1  |  D2  |  D3
```

- Come RAID 4, ma i **blocchi di parità sono distribuiti** su tutti i dischi
- Elimina il collo di bottiglia del disco di parità che invece avveniva sul ride 4
- **Prestazioni migliorate in scrittura**
- Sistema complesso e costoso da realizzare

#### RAID 6 — Double Distributed Parity (min. 4 dischi)

- Come RAID 5, ma utilizza **due tipi di controllo d'errori** (p e q) quindi su ogni blocco ci sarà un doppio controllo rispetto al raid 5
- **Grande ridondanza e sicurezza** (tollera il guasto di 2 dischi)
- **Svantaggio:** ricostruzione dei dati molto lenta (doppio calcolo ECC)

### 5.4 Riepilogo RAID

|Livello|Min. Dischi|Ridondanza|Performance Lettura|Performance Scrittura|Uso tipico|
|---|---|---|---|---|---|
|**0**|2|❌|⭐⭐⭐|⭐⭐⭐|Gaming, editing|
|**1**|2|✅ (mirror)|⭐⭐|⭐|OS, database critici|
|**3**|3|✅ (parità)|⭐⭐⭐|⭐⭐⭐|Stream sequenziale|
|**4**|3|✅ (parità)|⭐⭐⭐|⭐|Letture casuali|
|**5**|3|✅ (parità distr.)|⭐⭐⭐|⭐⭐|Server generici|
|**6**|4|✅✅ (doppia parità)|⭐⭐⭐|⭐|Archivi critici|

---

## 6. Connessione dei Dispositivi di Memoria

I calcolatori accedono alla memoria secondaria in **tre modi**:

### 6.1 Dispositivo collegato alla macchina (Host-Attached)

- Accesso tramite **porte locali di I/O** collegate al bus
- Nei PC: interfaccia **SATA** (max 2 unità per bus)
- Per maggiore spazio: porte **USB, FireWire, Thunderbolt**
- **FC (Fiber Channel):** architettura seriale ad alta velocità
    - Gestisce spazio di 24 bit → base delle **SAN**

**Flusso I/O:**

```
SO → comando in porte I/O mappate in memoria
   → adattatore invia comando al controller del disco
   → controller gestisce l'hardware
   → trasferimento disco ↔ cache controller
   → trasferimento verso host tramite DMA
```

> [!info] DMA (Direct Memory Access) Meccanismo che permette alle periferiche di accedere **direttamente** alla memoria interna senza coinvolgere la CPU, per scambiare dati in lettura/scrittura ad alta velocità.

### 6.2 Dispositivo connesso alla rete (NAS)

**NAS (Network-Attached Storage):** sistema di memoria specializzato accessibile in modo remoto attraverso la rete.

- I client accedono tramite interfaccia **RPC**
- Protocolli supportati: **NFS** (UNIX) e **CIFS** (Windows)
- Le chiamate remote sono implementate tramite **TCP o UDP** su rete IP

```
NAS ──┐
      ├── LAN/WAN ──── client
NAS ──┘              ── client
                     ── client
```

### 6.3 Storage in Cloud

- Simile al NAS: accesso tramite rete
- Differenza: accesso al **data center remoto tramite Internet o WAN**
- NAS si presenta come un file system; il **cloud storage è basato su API**
- Esempi: **Dropbox, Amazon S3, Microsoft OneDrive, Apple iCloud, Google Drive**
- Si usano API a causa delle **lunghe latenze** e dei numerosi scenari di errore sulle WAN

### 6.4 SAN (Storage Area Network)

- **Reti private** con protocolli specifici per la memorizzazione tra server e unità di memoria secondaria
- **Flessibilità:** molti calcolatori e molti storage array connessi alla stessa SAN

```
storage array ─┐
storage array ─┤── SAN ──── server ──┐
tape library  ─┘         ── server ──┤── LAN/WAN ── client
                    data-processing  │              client
                    center ──────────┘              client
```

---

## Riepilogo Generale

```
Memoria Secondaria
├── Formattazione
│   ├── Fisica (basso livello): settori, ECC, intestazione/coda
│   └── Logica: file system, FAT, Free List, cluster
├── Blocco di Boot
│   ├── Bootstrap loader (ROM)
│   ├── Area di boot (disco) → MBR in Windows
│   └── Partizione di boot → contiene il kernel
├── Blocchi Difettosi → sector sparing (settori di riserva)
├── Area di Swap → estensione della RAM su disco
│   └── Linux: slot da 4KB, swap map con contatori
├── RAID → ridondanza + parallelismo
│   ├── RAID 0: striping (performance max, no ridondanza)
│   ├── RAID 1: mirroring (affidabilità max, spreco spazio)
│   ├── RAID 3/4: parità su disco dedicato
│   ├── RAID 5: parità distribuita (bilanciato)
│   └── RAID 6: doppia parità (sicurezza massima)
└── Connessione
    ├── Host-Attached (SATA, USB, FC)
    ├── NAS (RPC, NFS, CIFS)
    ├── Cloud (API, Internet/WAN)
    └── SAN (rete privata, enterprise storage)
```

---

_Riferimenti: Silberschatz, Galvin, Gagne — "Operating System Concepts", Cap. 11_
