---
date: 2026-03-16
time: 09:21
---
# Cache

## Indice

1. [[#Capitolo 1 — Il Problema del Gap CPU/Memoria]]
2. [[#Capitolo 2 — La Gerarchia di Memoria]]
3. [[#Capitolo 3 — La Memoria Cache: Cos'è e Perché Esiste]]
4. [[#Capitolo 4 — Come Funziona la Cache: Hit, Miss, e Gestione]]
5. [[#Capitolo 5 — Operazioni di Scrittura: Write-Through e Write-Back]]
6. [[#Capitolo 6 — I Principi di Località]]
7. [[#Capitolo 7 — Organizzazione Fisica della Cache: Blocchi, Linee e Indirizzi]]
8. [[#Capitolo 8 — Le Tre Tipologie di Cache]]
9. [[#Capitolo 9 — Cache a Mappatura Diretta (Direct Mapped)]]
10. [[#Capitolo 10 — Cache Completamente Associativa (Fully Associative)]]
11. [[#Capitolo 11 — Cache a K-Vie (Set Associative)]]
12. [[#Capitolo 12 — Livelli di Cache: L1, L2, L3]]
13. [[#Capitolo 13 — Cache Unica vs Cache Distinte]]
14. [[#Capitolo 14 — La Gerarchia Multilivello Completa]]
15. [[#Riepilogo e Schemi Riassuntivi]]

---

# Capitolo 1 — Il Problema del Gap CPU/Memoria

## 1.1 Il Divario Storico

Per capire perché esiste la cache, devi prima capire il **problema fondamentale** che essa risolve.

Dagli anni '80 ad oggi, la velocità dei processori (CPU) è cresciuta in modo **esponenziale**: raddoppiava circa ogni 18 mesi (Legge di Moore). Le memorie DRAM invece crescevano in velocità molto più lentamente — circa il 7% all'anno contro il 60% annuo dei processori.

Il risultato è un grafico a forbice:

```
Prestazioni
(scala log)
100.000 |                              ●  CPU (≈30.000x)
 10.000 |                     ●●●●●●●
  1.000 |              ●●●●●●
    100 |       ●●●●●●
     10 |  ●●●●                    ◆  RAM (≈9x)
      1 |◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
        +----+----+----+----+----+----
       1980 1985 1990 1995 2000 2005 2010
```

Dal 1980 al 2010:

- La CPU è diventata circa **30.000 volte più veloce**
- La DRAM è diventata circa **9 volte più veloce**

Il divario è di **tre ordini di grandezza**. Questo significa che una CPU moderna può eseguire migliaia di operazioni nel tempo in cui la RAM risponde a una singola richiesta.

## 1.2 La Conseguenza Pratica

Prima dell'introduzione della cache, il processore **passava circa il 90% del tempo ad aspettare i dati dalla memoria**, non ad elaborarli. Era come avere un chirurgo velocissimo che passava la quasi totalità del suo tempo ad aspettare che qualcuno gli portasse gli strumenti dal magazzino.

Questo problema si chiama **Memory Wall** (muro della memoria) e rappresenta il collo di bottiglia principale delle architetture moderne.

> **Concetto chiave**: Il problema non è che la RAM sia "lenta" in assoluto. Il problema è che è lenta _rispetto alla CPU_. E questo gap non è stato colmato tecnologicamente — anzi, tende ad allargarsi. La cache è la soluzione _architettonica_ a un problema _tecnologico_.

## 1.3 Perché Non Costruire una RAM più Veloce?

Questa è la domanda ovvia. La risposta sta nei trade-off fisici fondamentali:

|Tipo di Memoria|Velocità|Costo per bit|Capacità|
|---|---|---|---|
|**SRAM** (Static RAM)|✅ Molto alta (1-10 ns)|❌ Molto alto|❌ Piccola|
|**DRAM** (Dynamic RAM)|❌ Bassa (50-100 ns)|✅ Basso|✅ Grande|

La **SRAM** usa 4-6 transistor per bit. È velocissima ma occupa molto spazio sul chip ed è costosa. La **DRAM** usa 1 transistor + 1 condensatore per bit. È densa ed economica ma lenta (il condensatore si scarica e va rinfrescato periodicamente — da qui il nome "Dynamic").

Non si può avere tutto: un banco di SRAM grande come una DRAM costerebbe centinaia di volte di più e occuperebbe un'area di silicio enormemente maggiore. La soluzione è usare _entrambe_ in modo intelligente: una gerarchia.

---

# Capitolo 2 — La Gerarchia di Memoria

## 2.1 L'Idea Fondamentale

La soluzione al problema del Memory Wall non è costruire una singola memoria perfetta, ma organizzare **più memorie diverse in una gerarchia**, in modo che:

- Le memorie **piccole e veloci** stiano vicino alla CPU
- Le memorie **grandi e lente** stiano lontano dalla CPU
- Il programmatore e la CPU abbiano l'_illusione_ di avere una memoria grande e veloce allo stesso tempo

## 2.2 La Piramide della Memoria

Ogni livello della gerarchia è caratterizzato da:

```
        ╔══════════════════╗
        ║  Registri CPU    ║  < 1 ns  | ~centinaia di byte  | costo massimo
        ╠══════════════════╣
        ║  Cache L1        ║  1-3 ns  | 8–64 KB             |
        ╠══════════════════╣
        ║  Cache L2        ║  3-10 ns | 128 KB – 1 MB       |
        ╠══════════════════╣
        ║  Cache L3        ║  10-30 ns| 2–32 MB             |
        ╠══════════════════╣
        ║  RAM (DRAM)      ║  50-100 ns| 4–64 GB            |
        ╠══════════════════╣
        ║  SSD             ║  20-100 µs| ~1 TB              |
        ╠══════════════════╣
        ║  Hard Disk (HDD) ║  5-10 ms | ~4+ TB              |
        ╠══════════════════╣
        ║  Nastri magnetici║  secondi | centinaia di TB     | costo minimo
        ╚══════════════════╝
        ↑ velocità/costo              capacità ↓
```

**Regola fondamentale**: Salendo nella piramide (verso la CPU), la memoria diventa più veloce, più piccola e più costosa. Scendendo, diventa più lenta, più grande e meno costosa.

## 2.3 Come Funziona la Gerarchia

La gerarchia funziona perché i programmi non accedono alla memoria in modo casuale. Al contrario, seguono dei **pattern prevedibili** (che vedremo nel Capitolo 6 — i Principi di Località). Grazie a questi pattern, si riesce a mantenere nei livelli veloci esattamente i dati che la CPU utilizzerà a breve.

Quando la CPU richiede un dato, la ricerca parte sempre dal livello più alto (cache L1) e scende fino a trovarlo:

```
CPU richiede dato X
        ↓
[L1] X è qui? → SÌ → consegna alla CPU (≈2 ns)
        ↓ NO
[L2] X è qui? → SÌ → copia in L1 → consegna (≈5 ns)
        ↓ NO
[L3] X è qui? → SÌ → copia in L2, L1 → consegna (≈20 ns)
        ↓ NO
[RAM] X è qui? → SÌ → copia in L3, L2, L1 → consegna (≈80 ns)
        ↓ NO
[Disco] → carica in RAM, poi risale la gerarchia (ms)
```

---

# Capitolo 3 — La Memoria Cache: Cos'è e Perché Esiste

## 3.1 Definizione Precisa

> La **memoria cache** è un dispositivo di memoria ad alta velocità posizionato tra il processore e la memoria principale (RAM), che contiene una **copia** di un sottoinsieme delle locazioni di memoria centrale, scelto in base alla probabilità di essere acceduto a breve.

Elementi chiave di questa definizione:

1. È una **copia** — i dati originali restano in RAM
2. È un **sottoinsieme** — la cache è molto più piccola della RAM
3. La scelta di cosa copiare è guidata dalla **probabilità di utilizzo futuro**

## 3.2 Il Ruolo della Cache nel Sistema

```
        ┌─────────────┐
        │     CPU     │  ← elabora istruzioni alla massima velocità
        │  (registri) │
        └──────┬──────┘
               │ bus privato ad alta velocità
        ┌──────┴──────┐
        │    CACHE    │  ← SRAM, veloce, piccola, costosa
        │  (L1/L2/L3) │
        └──────┬──────┘
               │ bus di sistema
        ┌──────┴──────┐
        │     RAM     │  ← DRAM, lenta, grande, economica
        │  (DRAM)     │
        └──────┬──────┘
               │ bus I/O
        ┌──────┴──────┐
        │  Hard Drive │  ← modulo I/O, molto lento, enorme
        └─────────────┘
```

La cache è gestita direttamente dal processore attraverso un **bus di indirizzi e un bus dati "privati"** — non visibili al programmatore. Dal punto di vista del software, esiste solo la RAM. La cache è trasparente.

## 3.3 Come è Organizzata Internamente la Cache

La cache memorizza **coppie (Indirizzo, Valore)**:

- **Indirizzo** (Address): corrisponde all'indirizzo della locazione nella memoria centrale
- **Valore** (Value): la parola di dati (word) memorizzata a quell'indirizzo

Esempio di contenuto di una cache:

|Indirizzo (Address)|Valore (Value)|
|---|---|
|`0x00001000`|`0xABCD`|
|`0x00001004`|`0x1234`|
|`0x00002020`|`0x89AB`|
|...|...|

La cache è quindi come un **dizionario**: dato un indirizzo (chiave), restituisce il valore. Il trucco sta nel come si organizza questo dizionario per renderlo veloce.

## 3.4 Il Meccanismo Base di Lettura (Semplificato)

```
1. La CPU vuole leggere l'indirizzo 0x0000A000
2. La cache controlla se ha una voce per quell'indirizzo
   ├─ SE SÌ (Cache Hit):
   │    → Restituisce il valore direttamente alla CPU
   │    → Tempo: ~2-5 ns
   └─ SE NO (Cache Miss):
        → Va a leggere dalla RAM (100+ ns)
        → Copia il dato in cache (per usi futuri)
        → Restituisce il valore alla CPU
```

---

# Capitolo 4 — Come Funziona la Cache: Hit, Miss, e Gestione

## 4.1 Cache Hit — Il Caso Fortunato

Un **Cache Hit** si verifica quando il dato richiesto dalla CPU è già presente in cache.

**Meccanismo dettagliato:**

1. La CPU emette un'istruzione `LDR R0, [0x0000A000]` (carica in R0 il dato all'indirizzo `0x0000A000`)
2. Il **cache controller** (un circuito hardware dedicato) intercetta la richiesta
3. Il controller cerca l'indirizzo `0x0000A000` nelle proprie voci
4. L'indirizzo viene trovato → il controller legge il valore associato
5. Il valore viene consegnato alla CPU **senza mai coinvolgere la RAM o il bus di sistema**

Questo è il caso ottimale: la CPU non si accorge nemmeno che c'è una gerarchia sottostante.

## 4.2 Cache Miss — Il Caso Sfortunato

Un **Cache Miss** si verifica quando il dato NON è in cache.

**Meccanismo dettagliato:**

1. La CPU emette `LDR R0, [0x0000A000]`
2. Il cache controller cerca `0x0000A000` in cache
3. L'indirizzo NON viene trovato → **Cache Miss**
4. Il cache controller accede alla RAM tramite il bus di sistema
5. Legge il dato all'indirizzo `0x0000A000` dalla RAM
6. **Inserisce una nuova voce in cache**: `(0x0000A000, valore_letto)`
7. Consegna il valore alla CPU

Durante i passi 4-6, la CPU è in attesa (**stall**). Questo è il costo del cache miss.

## 4.3 Hit Rate — La Metrica di Efficacia

La metrica fondamentale per valutare l'efficienza di una cache è l'**Hit Rate** (rapporto di successo):

$$\text{Hit Rate} = \frac{N_{\text{cache hit}}}{N_{\text{accessi totali alla memoria}}}$$

Un hit rate del 95% significa che il 95% delle volte il dato è già in cache. Un hit rate del 99% è eccellente. Il **Miss Rate** è semplicemente `1 - Hit Rate`.

**Perché l'hit rate è cruciale?**

Considera un sistema con:

- Tempo di accesso alla cache: 2 ns
- Tempo di accesso alla RAM: 100 ns
- Hit Rate: 95%

Tempo medio di accesso = `0.95 × 2 ns + 0.05 × 100 ns = 1.9 + 5 = 6.9 ns`

Con hit rate 99%: `0.99 × 2 + 0.01 × 100 = 1.98 + 1 = 2.98 ns`

La differenza tra 95% e 99% di hit rate dimezza il tempo medio di accesso. Piccole variazioni nell'hit rate hanno impatto enorme sulle prestazioni.

---

# Capitolo 5 — Operazioni di Scrittura: Write-Through e Write-Back

## 5.1 Il Problema della Scrittura

La lettura dalla cache è semplice: si cerca il dato, lo si trova o no. La **scrittura** è più complessa perché introduce un problema di **coerenza** (coherency): se modifico un dato in cache, quando lo aggiorno anche in RAM?

Se la cache contiene una copia di un dato della RAM, e io modifico la copia in cache, RAM e cache diventano **inconsistenti** (hanno valori diversi). Questo è un problema: se un altro componente del sistema (ad esempio, un dispositivo I/O o un altro processore) legge il dato dalla RAM, otterrà un valore obsoleto.

Esistono due politiche principali per gestire questo problema.

## 5.2 Write-Through (Scrittura Immediata)

> In Write-Through, **ogni scrittura nella cache viene propagata immediatamente anche nella RAM**.

**Meccanismo:**

```
CPU esegue STR R0, [0x0000A000]  (scrivi il valore di R0 in RAM[0x0000A000])
        ↓
Cache aggiorna la voce (0x0000A000, nuovo_valore)
        ↓ CONTEMPORANEAMENTE
RAM aggiorna la locazione 0x0000A000 con nuovo_valore
```

**Vantaggi:**

- Semplicità: RAM e cache sono sempre sincronizzate
- Nessun problema di coerenza: la RAM è sempre aggiornata
- In caso di crash del sistema, i dati in RAM sono sempre validi

**Svantaggi:**

- Ogni scrittura genera un accesso alla RAM → alto traffico sul bus
- Se la CPU scrive ripetutamente la stessa variabile (es. un contatore in un loop), ogni scrittura genera un accesso inutile alla RAM

## 5.3 Write-Back (Scrittura Differita)

> In Write-Back, la scrittura avviene **solo in cache**. La RAM viene aggiornata solo quando il blocco viene **rimosso dalla cache** per fare spazio a nuovi dati.

**Meccanismo:**

```
CPU esegue STR R0, [0x0000A000]
        ↓
Cache aggiorna la voce (0x0000A000, nuovo_valore)
Cache marca la voce come DIRTY (sporca) ← il dato in cache ≠ dato in RAM
        ↓
... tempo passa, la CPU continua a lavorare ...
        ↓
Quando il blocco deve essere rimosso dalla cache:
  → Se DIRTY: scrivi in RAM il valore aggiornato (Write-Back)
  → Se non DIRTY: elimina semplicemente il blocco (già consistente con RAM)
```

## 5.4 Il Dirty Bit

Il **Dirty Bit** è un singolo bit associato ad ogni blocco della cache che indica:

- `0` (pulito): il dato in cache è identico a quello in RAM
- `1` (sporco): il dato in cache è stato modificato e la RAM è obsoleta

Senza dirty bit, ogni volta che un blocco viene rimosso bisognerebbe riscriverlo in RAM "per sicurezza", anche se non è cambiato. Il dirty bit evita questo spreco.

## 5.5 Conseguenza del Write-Back: i Due Accessi

Considera questo scenario in una cache write-back:

1. La CPU richiede il dato all'indirizzo `B` (Cache Miss)
2. La cache è piena: bisogna rimuovere un blocco
3. Il blocco da rimuovere, quello con indirizzo `A`, è **DIRTY** (è stato modificato)

In questo caso, il cache miss genera **due accessi alla RAM**:

1. Scrivi il blocco `A` sporco nella RAM (write-back del vecchio dato)
2. Leggi il blocco `B` dalla RAM (caricamento del nuovo dato)

Questo è il costo nascosto del write-back: un singolo cache miss può generare due accessi alla memoria invece di uno.

## 5.6 Confronto Write-Through vs Write-Back

|Caratteristica|Write-Through|Write-Back|
|---|---|---|
|Coerenza cache/RAM|Sempre garantita|Garantita solo dopo write-back|
|Traffico sul bus|Alto (ogni write va in RAM)|Basso (solo alla rimozione)|
|Complessità|Bassa|Alta (dirty bit, gestione eviction)|
|Prestazioni in scrittura|Peggiori|Migliori|
|Utilizzo pratico|Cache L1 semplici|Cache L2/L3 moderne|

---

# Capitolo 6 — I Principi di Località

## 6.1 Perché la Cache Funziona?

La cache funziona perché i programmi reali non accedono alla memoria in modo casuale. Se accedessero casualmente, la cache non servirebbe a nulla (l'hit rate sarebbe uguale alla frazione di RAM coperta dalla cache, tipicamente < 1%).

Invece i programmi reali seguono due **principi di località** che rendono la cache estremamente efficace.

## 6.2 Principio di Località Temporale

> **Se una locazione di memoria viene acceduta al tempo t, è molto probabile che venga acceduta di nuovo in un intervallo di tempo breve.**

**Intuizione**: I programmi eseguono cicli. Ogni istruzione di un ciclo viene eseguita migliaia di volte. Le variabili di controllo di un ciclo vengono lette e scritte ad ogni iterazione.

**Esempio concreto:**

```c
int sum = 0;
for (int i = 0; i < 1000000; i++) {
    sum = sum + V[i];
}
```

In questo codice:

- La variabile `sum` viene letta e scritta **1.000.000 di volte**
- La variabile `i` viene letta e scritta **1.000.000 di volte**
- Entrambe vengono accedute in ogni iterazione → altissima località temporale

Dopo il primo accesso, `sum` e `i` vengono caricate in cache. Tutti i successivi 999.999 accessi trovano il dato già in cache → **hit rate vicino al 100% per queste variabili**.

## 6.3 Principio di Località Spaziale

> **Se una locazione di memoria viene acceduta al tempo t, è molto probabile che vengano accedute locazioni con indirizzi vicini in un intervallo di tempo breve.**

**Intuizione**: I programmi eseguono istruzioni sequenzialmente. Gli array sono allocati in memoria contigua. Le strutture dati sono contigue.

**Esempio concreto:**

```c
for (int i = 0; i < 1000000; i++) {
    sum = sum + V[i];   // V[0], V[1], V[2], V[3], ... acceduti in ordine
}
```

Il vettore `V` è allocato in memoria in modo contiguo. Se si accede a `V[0]`, quasi certamente si accederà presto a `V[1]`, `V[2]`, ecc.

**Come la cache sfrutta la località spaziale**: Quando si verifica un cache miss su `V[0]`, la cache **non carica solo `V[0]`**. Carica un intero **blocco** di word consecutive: `V[0], V[1], V[2], ..., V[k]`. Così i prossimi k accessi al vettore risulteranno tutti in cache hit.

## 6.4 Analisi dell'Esempio: il Loop

Riprendiamo il loop e analizziamo ogni accesso:

```c
int sum = 0;                      // sum allocata a indirizzo, es. 0x1000
for (int i = 0; i < n; i++) {    // i allocata a indirizzo es. 0x1004
    sum = sum + V[i];             // V[0] a 0x2000, V[1] a 0x2004, ...
}
```

**Prima iterazione (i=0):**

- Accesso a `sum` (0x1000): MISS → carico in cache
- Accesso a `i` (0x1004): MISS → carico in cache (stesso blocco di `sum` probabilmente)
- Accesso a `V[0]` (0x2000): MISS → carico blocco: V[0]...V[k] in cache

**Seconda iterazione (i=1):**

- Accesso a `sum` (0x1000): **HIT** (località temporale)
- Accesso a `i` (0x1004): **HIT** (località temporale)
- Accesso a `V[1]` (0x2004): **HIT** (località spaziale — era nel blocco caricato)

**Iterazioni successive:**

- `sum` e `i`: **sempre HIT** (locality temporale)
- `V[i]`: **HIT** finché `i` è nell'intervallo del blocco caricato (locality spaziale)

Il risultato è un hit rate elevatissimo, nonostante la cache sia piccola rispetto all'array.

## 6.5 Implicazioni Pratiche

I principi di località spiegano perché:

1. La cache funziona bene con **codice con cicli** (locality temporale)
2. La cache funziona bene con **accessi sequenziali** agli array (locality spaziale)
3. La cache funziona **male** con accessi casuali a strutture dati grandi (es. hashtable molto grandi, accessi random a array enormi)

> **Nota per il programmatore**: Scrivere codice "cache-friendly" significa massimizzare la locality. Ad esempio, nella moltiplicazione di matrici, l'ordine dei cicli influenza drasticamente le prestazioni a causa di come vengono sfruttati (o meno) i principi di locality.

---

# Capitolo 7 — Organizzazione Fisica della Cache: Blocchi, Linee e Indirizzi

## 7.1 Perché si Trasferiscono Blocchi e non Singole Word

Abbiamo visto che la cache sfrutta la **locality spaziale** caricando non solo il dato richiesto ma anche i suoi "vicini". Questo trasferimento di dati contigui si chiama **block transfer** (trasferimento a blocchi).

In una cache reale, l'unità minima di trasferimento tra RAM e cache non è una singola word, ma un **blocco** (o **linea di cache**, cache line). Tipicamente una cache line è di **64 byte** nelle CPU moderne.

> **Attenzione**: Non si può caricare in cache metà di un blocco. Se serve anche solo 1 byte di un blocco, si carica l'intero blocco da 64 byte. Allo stesso modo, se si deve rimpiazzare un blocco, si rimpiazza l'intera linea.

## 7.2 Struttura di una Linea di Cache

Ogni **entry** (riga) della cache non contiene solo il dato. Contiene:

```
┌──────────┬──────────┬──────────────────────────────────────┐
│  Valid   │   TAG    │              DATA                    │
│  (1 bit) │ (n bit)  │      (dimensione di 1 blocco)        │
└──────────┴──────────┴──────────────────────────────────────┘
```

- **Valid bit**: indica se la linea contiene dati validi (1 = valida, 0 = vuota/non inizializzata)
- **TAG**: identifica quale blocco della RAM è memorizzato in questa linea (lo vedremo in dettaglio)
- **DATA**: il contenuto effettivo del blocco (es. 64 byte)
- In cache write-back c'è anche il **Dirty bit** (1 bit per linea)

## 7.3 Come si Interpreta un Indirizzo di Memoria

Per capire le diverse tipologie di cache, dobbiamo capire come viene **decodificato** un indirizzo di memoria.

**Scenario di riferimento** (useremo questo esempio nei prossimi capitoli):

- Architettura a **10 bit di indirizzo** (1 KB di RAM → 256 word da 4 byte)
- Cache con **8 linee** (8 word da 4 byte) — cache da 32 byte
- Ogni word è di **4 byte**

Un indirizzo a 10 bit viene suddiviso in parti:

```
Indirizzo a 10 bit:
| bit 9 | bit 8 | bit 7 | bit 6 | bit 5 | bit 4 | bit 3 | bit 2 | bit 1 | bit 0 |
```

Le parti dipendono dalla tipologia di cache:

- **Byte offset**: identifica il byte all'interno della word (se word = 4 byte → 2 bit)
- **Word/Block offset**: identifica la word all'interno della linea (se linea = 4 word → 2 bit)
- **Index**: identifica la riga della cache (se cache ha 8 righe → 3 bit)
- **TAG**: i bit rimanenti, identificano quale dei tanti blocchi RAM possono stare nella stessa riga

## 7.4 Locazioni e Bit di Indirizzo — Calcoli Base

**Quante locazioni può indirizzare un indirizzo di n bit?** $$N_{\text{locazioni}} = 2^n$$

**Quanti bit servono per indirizzare N locazioni?** $$n = \log_2(N)$$

**Esempio pratico:**

- Memoria da 1 KB = 1024 byte
- Ogni locazione = 1 byte → servono $\log_2(1024) = 10$ bit di indirizzo
- Ogni locazione = 4 byte (1 word) → la memoria ha 256 word → servono $\log_2(256) = 8$ bit per indirizzare le word

**Note utili:**

- $2^{10} = 1024 \approx 1K$
- $2^{20} \approx 1M$
- $2^{30} \approx 1G$

---

# Capitolo 8 — Le Tre Tipologie di Cache

## 8.1 Il Problema del Mapping

Abbiamo una cache con N linee e una RAM con M blocchi, dove M >> N (molto più blocchi in RAM che linee in cache). Dobbiamo decidere: **quando un blocco della RAM viene caricato in cache, in quale linea va messo?**

Questa decisione si chiama **politica di mapping** e le soluzioni principali sono tre:

|Tipologia|Dove può andare un blocco?|Analogia|
|---|---|---|
|**Mappatura Diretta**|In una e una sola linea predeterminata|Parcheggio con posto assegnato fisso|
|**Completamente Associativa**|In qualsiasi linea libera|Parcheggio libero|
|**K-Vie (Set Associativa)**|In una delle K linee di un set predeterminato|Parcheggio multipiano con piano assegnato|

## 8.2 L'Analogia del Parcheggio (da comprendere bene)

Immagina:

- **RAM** = parcheggio grande con 20 piazzole (celle di memoria)
- **Cache** = parcheggio piccolo con 4 piazzole (linee di cache), più vicino alla destinazione
- **Dato** = automobile (da "parcheggiare" in cache per un accesso rapido)

Le tipologie di cache corrispondono a tre diversi regolamenti del parcheggio piccolo:

**Mappatura Diretta** = Ogni automobile può parcheggiare _solo_ nella piazzola con lo stesso colore della piazzola da cui viene nel parcheggio grande. Se la piazzola del suo colore è occupata, deve spostare l'auto che c'è.

**Completamente Associativa** = Ogni automobile può parcheggiare in qualsiasi piazzola libera. Se il parcheggio è pieno, devi scegliere quale auto spostare (politica di rimpiazzo).

**K-Vie** = Ibrido. Ogni automobile deve parcheggiare in una piazzola del suo "settore" (colore), ma ogni settore ha K piazzole (K piani). Puoi scegliere tra K posizioni disponibili.

---

# Capitolo 9 — Cache a Mappatura Diretta (Direct Mapped)

## 9.1 Principio Fondamentale

In una cache a mappatura diretta con N linee, ogni blocco della RAM può essere memorizzato in **una e una sola linea** della cache. Quale linea? Si usa la funzione:

$$\text{linea_cache} = \text{numero_blocco_RAM} \mod N$$

In pratica, si divide la RAM in gruppi di N blocchi e ogni gruppo usa le stesse N linee della cache (con "avvolgimento" — wrap-around).

## 9.2 Struttura dell'Indirizzo

Prendiamo il nostro esempio: cache con 8 linee, word da 4 byte, indirizzo a 10 bit.

```
|  9  8  7  6  5  |  4  3  2  |  1  0  |
|   TAG (5 bit)   | INDEX(3b) | BYTE(2)|

- BYTE (2 bit): offset del byte all'interno della word (word = 4 byte → 2 bit)
- INDEX (3 bit): numero della linea in cache (8 linee → 3 bit)
- TAG (5 bit): i bit rimanenti, identificano "quale gruppo" di blocchi
```

**Come si legge l'indirizzo:**

- I bit 1-0 (BYTE) dicono _dove nel word_ cercare il dato
- I bit 4-2 (INDEX) dicono _quale riga della cache_ controllare
- I bit 9-5 (TAG) dicono _quale dei tanti blocchi_ che mappano su quella riga è quello richiesto

## 9.3 Esempio Numerico Dettagliato

**Scenario**: CPU richiede il dato all'indirizzo `0000001100` (in binario).

Decodifica dell'indirizzo:

```
|  0  0  0  0  0  |  0  1  1  |  0  0  |
|   TAG = 00000   | INDEX= 011| BYTE=00|
```

**Operazione del cache controller:**

1. Estrae INDEX = `011` (decimale: 3) → va alla riga 3 della cache
2. Legge il TAG memorizzato nella riga 3
3. Confronta il TAG letto con il TAG dell'indirizzo (`00000`):
    - Se **uguali** → **Cache Hit** → restituisce il dato al byte 00 del word in riga 3
    - Se **diversi** → **Cache Miss** → carica il blocco della RAM con indirizzo `00000_011_00` in riga 3

**Cosa succede al Cache Miss:**

- Il vecchio dato nella riga 3 viene rimpiazzato (eventualmente con write-back se dirty)
- Il nuovo blocco viene caricato dalla RAM
- Il TAG della riga 3 viene aggiornato a `00000`
- Il dato viene consegnato alla CPU

## 9.4 Problema della Mappatura Diretta: Thrashing

Il grande difetto della mappatura diretta è che **blocchi di RAM con lo stesso INDEX competono per la stessa riga**, anche se le altre righe sono vuote.

**Esempio di Thrashing:**

Supponiamo che la CPU acceda ripetutamente a questi quattro indirizzi:

```
1: 0000001000  → TAG=00000, INDEX=010
2: 0010001000  → TAG=00100, INDEX=010
3: 0100101000  → TAG=01001, INDEX=010  (errore: 0100_101_00 → tag=01001, idx=010)
4: 1001001000  → TAG=10010, INDEX=010
```

Tutti e quattro mappano sull'INDEX `010` (stessa riga!). Ogni accesso trova la riga occupata dal blocco precedente → **ogni accesso è un Cache Miss**. Le altre 7 righe restano vuote. Hit rate = 0%, nonostante la cache non sia piena!

Questo fenomeno si chiama **thrashing** (oscillazione) ed è il principale limite della mappatura diretta.

## 9.5 Pro e Contro della Mappatura Diretta

**Pro:**

- Hardware semplice e veloce: dato un indirizzo, si conosce subito quale riga controllare (una sola)
- Costo hardware basso
- Latenza di accesso minima (si controlla solo 1 TAG)

**Contro:**

- Thrashing: blocchi con lo stesso INDEX si sovrascrivono a vicenda
- Hit rate potenzialmente basso per certi pattern di accesso
- Non sfrutta a pieno la capacità della cache

---

# Capitolo 10 — Cache Completamente Associativa (Fully Associative)

## 10.1 Principio Fondamentale

Nella cache completamente associativa **non esiste la nozione di INDEX**: un blocco della RAM può essere memorizzato in **qualsiasi linea** della cache. Questo elimina completamente il problema del thrashing.

## 10.2 Struttura dell'Indirizzo

Con la stessa architettura di prima (10 bit, word da 4 byte):

```
|  9  8  7  6  5  4  3  2  |  1  0  |
|        TAG (8 bit)        | BYTE(2)|

- BYTE (2 bit): offset del byte nel word
- TAG (8 bit): identifica univocamente il blocco di RAM
```

Non c'è l'INDEX perché non si sa in quale riga il blocco potrebbe trovarsi. Il TAG deve quindi essere abbastanza grande da identificare univocamente un blocco (8 bit → 256 possibili blocchi, che corrisponde al numero di word nella nostra RAM da 1KB).

## 10.3 Il Problema della Ricerca: la CAM

Senza INDEX, per trovare il dato devo **cercare il TAG in tutte le righe** della cache. Se la cache ha 8 righe, devo fare 8 confronti. Se ha 256 righe, 256 confronti.

Fare questi confronti **uno alla volta** sarebbe lentissimo. La soluzione è la **CAM (Content Addressable Memory)** — Memoria Indirizzabile per Contenuto.

> La CAM è un tipo speciale di memoria che, dato un valore di ricerca, confronta **in parallelo** il valore con tutte le voci memorizzate, e indica quali voci corrispondono. Il confronto avviene in hardware, in un singolo ciclo di clock.

**Schema di funzionamento della CAM:**

```
Valore cercato: TAG = 00000011

Cache (CAM):
  Riga 0: TAG = 01000100  →  0  (non corrisponde)
  Riga 1: TAG = 11000100  →  0
  Riga 2: TAG = 11111100  →  0
  Riga 3: TAG = 00000011  →  1  ← MATCH! (Cache Hit)
  Riga 4: TAG = 00001011  →  0
  Riga 5: TAG = 00000010  →  0
  ...
```

Tutti i confronti avvengono **contemporaneamente** (in parallelo) in hardware → la ricerca è O(1) in tempo.

## 10.4 Politiche di Rimpiazzo

Quando la cache è piena e arriva un nuovo blocco, dobbiamo scegliere quale linea rimpiazzare. Tre politiche principali:

### FIFO (First In, First Out)

Rimpiazza il blocco che è stato caricato per primo (il più vecchio).

- Semplice da implementare (basta un timestamp o un counter)
- Non necessariamente ottimale: un blocco "vecchio" potrebbe essere molto usato

### LRU (Least Recently Used) ⭐ — Il più usato nella pratica

Rimpiazza il blocco che **non viene acceduto da più tempo**.

- Basato sulla locality temporale: se non lo uso da tanto, probabilmente non mi servirà presto
- Più costoso da implementare (richiede di tracciare l'ordine degli accessi)
- Offre generalmente il miglior hit rate
- **È l'algoritmo più utilizzato nelle cache reali**

### RANDOM

Rimpiazza un blocco scelto casualmente.

- Semplicissimo da implementare
- Sorprendentemente buono in pratica (evita i pattern peggiori del FIFO)
- Usato in alcune cache semplici

## 10.5 Funzionamento Completo

```
CPU richiede dato all'indirizzo: 0000001100
                                 ←TAG=00000011→ ←BYTE=00→

1. CAM confronta TAG=00000011 con tutti i TAG in cache
   ├─ TROVATO (Hit): 
   │   → la riga con quel TAG restituisce il dato
   │   → aggiorna l'ordine LRU (questa riga è la "più recente")
   └─ NON TROVATO (Miss):
       → accedi alla RAM, carica il blocco
       → scegli una riga da rimpiazzare (es. LRU → la riga meno recente)
       → se quella riga è DIRTY → write-back prima del rimpiazzo
       → inserisci il nuovo blocco + TAG nella riga scelta
       → restituisci il dato alla CPU
```

## 10.6 Pro e Contro

**Pro:**

- Massima flessibilità: usa sempre tutte le linee disponibili
- Nessun thrashing
- Migliore hit rate potenziale
- Si adatta a qualsiasi pattern di accesso

**Contro:**

- Richiede una CAM → hardware complesso e costoso (area su chip)
- TAG più grandi (nessun INDEX)
- La complessità della CAM ne limita l'uso a cache piccole
- Più costosa da realizzare

---

# Capitolo 11 — Cache a K-Vie (Set Associative)

## 11.1 L'Idea: il Compromesso Ottimale

La cache a K-vie nasce per combinare i vantaggi della mappatura diretta (semplicità, hardware economico) e della cache completamente associativa (flessibilità, alto hit rate), limitando gli svantaggi di entrambe.

**L'idea chiave**: divido le linee della cache in **gruppi** (chiamati **set**). Ogni set contiene **K linee** (K = numero di vie). Un blocco della RAM può essere memorizzato in **qualsiasi delle K linee del suo set predeterminato**.

- Se K=1 → è la mappatura diretta (ogni set ha 1 sola linea)
- Se K=N (numero totale linee) → è la completamente associativa (un solo set con tutte le linee)
- Valori pratici: K = 2, 4, 8, 16

## 11.2 Struttura dell'Indirizzo

Con 8 linee totali divise in 4 set da 2 (cache a 2-vie):

```
|  9  8  7  6  5  4  |  3  2  |  1  0  |
|     TAG (6 bit)     |IDX(2b) | BYTE(2)|

- BYTE (2 bit): offset nel word
- INDEX (2 bit): identifica il SET (4 set → 2 bit)
- TAG (6 bit): identifica il blocco all'interno del set
```

Rispetto alla mappatura diretta:

- INDEX è più piccolo (identifica il set, non la singola riga)
- TAG è più grande (deve distinguere tra più blocchi che mappano sullo stesso set)

## 11.3 Funzionamento Dettagliato

**Esempio: Cache a 2-vie, indirizzo** `0000001100`

Decodifica:

```
|  0  0  0  0  0  0  |  1  1  |  0  0  |
|     TAG = 000000    | IDX=11 | BYTE=00|
```

**Operazione:**

1. INDEX = `11` → vai al **Set 3** della cache
2. Il Set 3 contiene **2 linee** (2 vie)
3. Controlla il TAG di entrambe le linee:
    - Via 0 del Set 3: TAG = `000000`? Se sì → **Hit** sulla via 0
    - Via 1 del Set 3: TAG = `000000`? Se sì → **Hit** sulla via 1
4. Se nessuna via ha il TAG cercato → **Miss**
    - Accedi alla RAM
    - Scegli quale delle 2 vie del Set 3 rimpiazzare (es. LRU tra le 2 vie)
    - Carica il nuovo blocco nella via scelta

La ricerca del TAG avviene in **parallelo** sulle K vie del set (hardware più semplice della CAM completa, poiché si confrontano solo K TAG invece di tutti gli N).

## 11.4 Cache a 2-vie con 4 Word Lines

Esempio più realistico: cache a 2-vie con linee da 4 word, indirizzo a 10 bit.

```
|  9  8  7  6  5  4  |  3  2  |  1  0  |
|     TAG (6 bit)     | IDX(2b)| WORD(2)|

- WORD (2 bit): identifica quale delle 4 word nella linea
- INDEX (2 bit): identifica il SET
- TAG (6 bit): identifica il blocco
```

Quando avviene un cache miss:

1. Si identifica il SET tramite INDEX
2. Si sceglie una via da rimpiazzare (LRU tra le K vie)
3. Si carica **l'intera linea** (4 word consecutive) dalla RAM
4. → Sfruttamento della **locality spaziale**: si caricano 4 word con un solo accesso alla RAM

## 11.5 Pro e Contro

**Pro:**

- Compromesso ottimale tra costo hardware e hit rate
- Riduce drasticamente il thrashing rispetto alla mappatura diretta
- Meno hardware rispetto alla completamente associativa (solo K confronti per set)
- Utilizzata in praticamente tutte le CPU moderne

**Contro:**

- Più complessa della mappatura diretta
- Aumento del TAG aumenta l'overhead di memoria
- K grandi avvicinano alla completamente associativa (più costosa)

## 11.6 Confronto tra le Tre Tipologie

|Caratteristica|Mappatura Diretta|K-Vie|Completamente Associativa|
|---|---|---|---|
|**Flessibilità**|Bassa (1 sola riga)|Media (K righe per set)|Massima (qualsiasi riga)|
|**Thrashing**|Frequente|Ridotto|Assente|
|**Hit Rate**|Basso|Alto|Massimo|
|**Hardware**|Semplice|Moderato|Complesso (CAM)|
|**Costo**|Basso|Medio|Alto|
|**TAG size**|Piccolo|Medio|Grande|
|**Uso pratico**|Rare, cache semplici|L1, L2, L3 moderne|TLB, piccole cache|

---

# Capitolo 12 — Livelli di Cache: L1, L2, L3

## 12.1 Perché Più Livelli?

Aumentare la dimensione della cache L1 la renderebbe più lenta (fisica: memoria più grande → percorsi più lunghi → più cicli). Ridurla la renderebbe troppo piccola per avere un buon hit rate. La soluzione è usare **più livelli**, ognuno ottimizzato per velocità o capacità.

## 12.2 Cache L1 — Il Primo Livello

- **Posizione**: integrata direttamente nel chip del processore, a pochissimi mm dai core
- **Dimensione**: 8 KB – 64 KB (piccola per restare veloce)
- **Velocità**: 1-4 cicli di clock (≈1-3 ns con CPU a 3 GHz)
- **Organizzazione tipica**: K-vie (spesso 4-vie o 8-vie)
- **Struttura**: spesso divisa in **L1 istruzioni** (L1-I) e **L1 dati** (L1-D) → cache separate
- **Condivisione**: **privata per ogni core** — ogni core ha la propria L1

## 12.3 Cache L2 — Il Secondo Livello

- **Posizione**: a seconda dell'architettura, può essere on-chip (nello stesso die del processore) o esterna
- **Dimensione**: 128 KB – 1 MB (più grande di L1, ma più lenta)
- **Velocità**: 5-15 cicli di clock (≈5-10 ns)
- **Organizzazione tipica**: K-vie (spesso 8-vie o 16-vie)
- **Struttura**: unificata (istruzioni + dati insieme)
- **Condivisione**: tipicamente **privata per ogni core**, come L1

## 12.4 Cache L3 — Il Terzo Livello

- **Posizione**: on-chip, esterna ai singoli core ma nello stesso package del processore
- **Dimensione**: 2 MB – 64 MB (molto più grande)
- **Velocità**: 20-50 cicli di clock (≈10-30 ns)
- **Organizzazione tipica**: K-vie (16-vie o più)
- **Condivisione**: **condivisa tra tutti i core** del processore
- **Ruolo**: agisce come buffer per ridurre gli accessi alla RAM (molto più lenta)

## 12.5 Schema con Più Core

```
Core 0                          Core 1
┌─────────────────┐             ┌─────────────────┐
│  Registri       │             │  Registri       │
│  L1-I  L1-D     │             │  L1-I  L1-D     │
│    L2           │             │    L2           │
└────────┬────────┘             └────────┬────────┘
         │                               │
         └──────────────┬────────────────┘
                ┌───────┴───────┐
                │  L3 (shared)  │
                └───────┬───────┘
                        │
                ┌───────┴───────┐
                │  RAM (DRAM)   │
                └───────────────┘
```

La L3 condivisa permette ai core di **comunicare** tramite la cache: se Core 0 ha un dato in L3, Core 1 può accedervi senza andare in RAM.

---

# Capitolo 13 — Cache Unica vs Cache Distinte

## 13.1 Il Problema: Istruzioni e Dati Insieme?

Ogni programma genera due tipi di accessi alla memoria:

1. **Fetch delle istruzioni**: la CPU legge le istruzioni da eseguire (lettura sequenziale, molto regolare)
2. **Accesso ai dati**: la CPU legge/scrive i dati su cui operano le istruzioni (pattern più vario)

La domanda è: una singola cache gestisce entrambi, o si usano cache separate?

## 13.2 Cache Unica (Unified Cache)

```
         CPU (Fetch istruzioni + Accesso dati)
                        ↕
              ┌─────────────────┐
              │  Cache Unica    │ ← contiene sia istruzioni che dati
              └─────────────────┘
                        ↕
                       RAM
```

**Vantaggi:**

- **Flessibilità**: lo spazio della cache si adatta automaticamente. Se il programma è data-intensive, la cache si riempie di dati; se è code-intensive, di istruzioni
- **Semplicità**: un solo sistema da gestire
- **Potenzialmente più alto hit rate** per la flessibilità

**Svantaggi:**

- Un solo accesso per ciclo di clock: fetch istruzione o accesso dato, non entrambi simultaneamente
- Le istruzioni e i dati "competono" per lo spazio

## 13.3 Cache Distinte (Split Cache / Harvard Cache)

```
      Cache Istruzioni (I-Cache)    CPU    Cache Dati (D-Cache)
             ↕                       │            ↕
             RAM ─────────────────────────────── RAM
```

**Vantaggi:**

- **Due accessi simultanei** per ciclo: fetch istruzione dalla I-Cache + accesso dato dalla D-Cache allo stesso ciclo → raddoppia la banda
- Design semplificato: la I-Cache può essere ottimizzata per letture sequenziali, la D-Cache per read/write random
- Maggiore parallelismo nel pipeline della CPU

**Svantaggi:**

- Meno flessibile: se il programma ha molti dati, la D-Cache si riempie ma la I-Cache è vuota (spazio sprecato)
- Due sistemi da progettare

## 13.4 Uso Pratico

Nella pratica moderna:

- La **L1** è quasi sempre **divisa** (I-Cache + D-Cache separate): il guadagno di parallelismo nel pipeline è fondamentale
- La **L2 e L3** sono generalmente **unificate** (dati + istruzioni insieme): la flessibilità conta di più a quel livello

---

# Capitolo 14 — La Gerarchia Multilivello Completa

## 14.1 Il Quadro Generale

La gerarchia di memoria è il sistema che permette di avere, _apparentemente_, una memoria grande, veloce ed economica combinando tecnologie diverse.

Il principio fondamentale è:

> **I livelli superiori memorizzano il sottoinsieme di dati che il processore utilizzerà nell'immediato futuro.** La scelta è guidata dai principi di locality. Lo scopo è evitare gli accessi ai livelli inferiori, più costosi in tempo.

## 14.2 Come si Muovono i Dati

Quando la CPU accede a un dato, la gerarchia funziona così:

```
STEP 1: CPU richiede dato X

STEP 2: Cerca in L1
        → HIT: consegna alla CPU in ≈2 ns. FINE.
        → MISS: vai a STEP 3

STEP 3: Cerca in L2
        → HIT: copia il blocco in L1, consegna alla CPU in ≈5 ns. FINE.
        → MISS: vai a STEP 4

STEP 4: Cerca in L3
        → HIT: copia il blocco in L2 e L1, consegna in ≈20 ns. FINE.
        → MISS: vai a STEP 5

STEP 5: Cerca in RAM
        → HIT: copia il blocco in L3, L2, L1, consegna in ≈80 ns. FINE.
        → MISS: vai a STEP 6

STEP 6: Cerca su Disco (SSD/HDD)
        → Carica in RAM, poi risale la gerarchia (millisecondi)
```

Ogni livello **copia** verso l'alto, non sposta. Il dato originale rimane sempre nel livello più basso in cui è presente.

## 14.3 La Gestione delle Eviction (Rimpiazzi)

Quando un livello è pieno e arriva un nuovo dato:

1. Si sceglie una linea da rimpiazzare (LRU o altra politica)
2. Se la linea è dirty (write-back), si propaga il dato al livello inferiore
3. Si carica il nuovo dato

Questo processo si chiama **eviction** e può propagarsi a cascata verso il basso.

## 14.4 Numeri Reali a Confronto

|Livello|Latenza|Dimensione tipica (2024)|Hit Rate tipico|
|---|---|---|---|
|Registri CPU|< 1 ns|~1 KB (decine di registri)|—|
|Cache L1|1-4 ns|32 KB – 128 KB per core|90–95%|
|Cache L2|5-12 ns|256 KB – 2 MB per core|95–99%|
|Cache L3|15-40 ns|4 MB – 64 MB (condivisa)|99–99.9%|
|RAM DRAM|50-100 ns|8 – 128 GB|—|
|SSD NVMe|50-100 µs|500 GB – 4 TB|—|
|HDD|5-10 ms|2 – 20 TB|—|

---

# Riepilogo e Schemi Riassuntivi

## R.1 — Mappa Concettuale

```
PROBLEMA: CPU molto più veloce della RAM
        ↓
SOLUZIONE: Gerarchia di Memoria con CACHE
        ↓
CACHE FUNZIONA grazie a:
    ├── Locality Temporale → stessi dati riacceduti spesso
    └── Locality Spaziale → dati vicini acceduti insieme

MECCANISMI CACHE:
    ├── Cache Hit  → dato trovato, accesso rapido
    ├── Cache Miss → dato non trovato, accesso a RAM
    └── Hit Rate = Hit / (Hit + Miss) → misura l'efficacia

POLITICHE DI SCRITTURA:
    ├── Write-Through → scrivi in cache E RAM subito
    └── Write-Back → scrivi solo in cache, RAM dopo (dirty bit)

TIPOLOGIE DI MAPPING:
    ├── Diretta → 1 riga fissa per blocco (semplice ma thrashing)
    ├── Completamente Associativa → qualsiasi riga (ottimale ma costosa, usa CAM)
    └── K-Vie → K righe per set (compromesso, usata ovunque)

LIVELLI:
    ├── L1 (privata per core, velocissima, piccola, split I/D)
    ├── L2 (privata per core, rapida, media)
    └── L3 (condivisa tra core, lenta rispetto a L2, grande)
```

## R.2 — Tabella Riassuntiva delle Tipologie di Cache

||Mappatura Diretta|Completamente Associativa|K-Vie (es. 2-vie)|
|---|---|---|---|
|Struttura indirizzo|TAG + INDEX + BYTE|TAG + BYTE|TAG + INDEX + BYTE|
|INDEX|Identifica 1 riga|Nessuno|Identifica il SET|
|TAG|Più piccolo|Più grande|Medio|
|Ricerca|1 confronto|N confronti in parallelo (CAM)|K confronti in parallelo|
|Thrashing|Sì, frequente|No|Ridotto|
|Politica rimpiazzo|Deterministica (no scelta)|LRU / FIFO / Random|LRU / FIFO / Random per set|
|Costo hardware|Basso|Alto|Medio|
|Hit rate|Più basso|Potenzialmente massimo|Alto|
|Utilizzo|Cache semplici|TLB, cache piccole|L1, L2, L3 moderne|

## R.3 — Formula per Decomporre un Indirizzo (Cache K-Vie)

Dati:

- Dimensione memoria: $M$ byte → $\log_2 M$ bit di indirizzo
- Dimensione cache: $C$ byte
- Numero di vie: $K$
- Dimensione di una linea: $L$ byte

Allora:

- **Bit BYTE** (offset nel byte): $\log_2 L$ bit
- **Numero di set**: $S = C / (K \times L)$
- **Bit INDEX** (seleziona il set): $\log_2 S$ bit
- **Bit TAG**: bit rimanenti = $\log_2 M - \log_2 L - \log_2 S$

**Caso speciale — Mappatura Diretta:** K=1 → $S = C/L$, indistinguibile dalla formula sopra

**Caso speciale — Completamente Associativa:** S=1 (un solo set) → INDEX = 0 bit, tutti i bit rimanenti sono TAG

## R.4 — Concetti da Saper Spiegare all'Esame

1. **Perché esiste la cache?** → Gap CPU/DRAM (Memory Wall)
2. **Come funziona un cache hit?** → Controller trova il TAG, restituisce dato senza accedere alla RAM
3. **Come funziona un cache miss?** → Controller non trova il TAG, accede a RAM, aggiorna cache
4. **Cos'è l'hit rate e perché è importante?** → Frazione di accessi risolti in cache; piccole variazioni hanno grande impatto sul tempo medio
5. **Differenza Write-Through vs Write-Back?** → Quando si propaga la scrittura alla RAM
6. **Cos'è il dirty bit?** → Indica che il dato in cache è stato modificato e RAM è obsoleta
7. **Cos'è la locality temporale?** → Dato usato ora → probabilmente riusato presto
8. **Cos'è la locality spaziale?** → Dato usato → i dati vicini probabilmente usati presto
9. **Perché si trasferiscono blocchi e non word singole?** → Sfruttare la locality spaziale
10. **Differenza tra le 3 tipologie?** → Dove può andare un blocco (1 riga / K righe / qualsiasi riga)
11. **Cos'è il thrashing nella mappatura diretta?** → Blocchi con stesso INDEX si sovrascrivono ciclicamente
12. **Cos'è la CAM?** → Memoria associativa per ricerca parallela dei TAG
13. **Cos'è LRU?** → Politica di rimpiazzo che elimina il blocco meno recentemente usato
14. **Differenza L1/L2/L3?** → Velocità, dimensione, posizione, condivisione tra core
15. **Cache unica vs distinte?** → Trade-off tra flessibilità e parallelismo di accesso

---

## Riferimenti
1. 