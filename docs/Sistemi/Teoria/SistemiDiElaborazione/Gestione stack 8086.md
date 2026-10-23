---
date: 2026-02-01
time: 17:22
---
# Gestione stack 8086

Nel segmento Stack vengono salvate le variabili locali e i parametri passati da un
sottoprogramma.

I registri segmento e puntatore che gestiscono l’indirizzamento in memoria sono
rispettivamente SS e SP

A differenza dei segmenti precedenti nello stack il programma non può andare a scrivere direttamente ma può scrivere soltanto seguendo la regola LIFO (Last In First Out) cioè impilando i dati uno sopra l'altro 

Il segmento stack viene gestito in maniera differente rispetto agli alti segmenti:
- ha dimensione fissa 1024bytes
- Lo Stack Pointer SP anziché puntare alla cella iniziale punta all'ultima in fondo contenente il valore specifico EOS End Of Stack
## Operazioni di PUSH e POP

Le due istruzioni usate per gestire lo stack sono le istruzioni:
- **PUSH**: consente di salvare informazioni nello stack
- **POP**: consente di prelevare dallo stack l'ultima informazione in memoria

Ad Ogni PUSH: SP viene decrementato di una quantità pari alle dimensione dell'informazione salvata se si continua ad inserire informazioni SP viene decrementata fino a diventare 0 e si ottiene l'errore di **stack overflow**

Ad Ogni POP: SP viene incrementato si una quantità pari alle dimensioni dell'informazioni  se si continua a prendere informazioni sino a che SP raggiunge la sua dimensione massima e restituisce l'errore di **stack underflow**

![[Pasted image 20260201173155.png]]

# Esempio

***Si consideri un segmento stack che inizia all’indirizzo di memoria 10010h,
inizialmente vuoto, di dimensione fissa 20 bytes.
Considerando ogni valore su 2 byte, un programma Assembler esegue le operazioni
mostrate nel segmento codice scritto a fianco.***

***Determinare:***
1) ***Il contenuto del registro SS e SP, prima dell’esecuzione delle operazioni sullo stack***
2) ***Il contenuto finale dello stack***
3) ***Il valore del registro SP e l’indirizzo di memoria dove si trova il top dello stack, al termine delle operazioni eseguite al punto precedente; controllando se non viene eseguito nessun underflow/overflow***

PUSH 12
POP AX
PUSH 4
PUSH 15
POP AX
PUSH 16

Certamente. Ecco la soluzione dettagliata, formattata in **Markdown** per una chiara leggibilità.

---

# Soluzione Passo Passo

### Premessa Fondamentale

Nell'architettura x86 (8086), lo stack funziona secondo il principio **LIFO** (Last In, First Out) e **cresce verso il basso** (dagli indirizzi di memoria alti verso quelli bassi).

- **PUSH:** Diminuisce lo Stack Pointer (`SP = SP - 2`), poi scrive il dato.
    
- **POP:** Legge il dato, poi aumenta lo Stack Pointer (`SP = SP + 2`).
    

---

### 1. Calcolo dei registri SS e SP iniziali

**Registro SS (Stack Segment)**

L'indirizzo fisico di partenza del segmento è $10010h$. Poiché l'indirizzo fisico è dato da $SS \times 16 + Offset$ (e l'offset iniziale della base è 0):

$$SS = \frac{10010h}{10h} = \mathbf{1001h}$$

**Registro SP (Stack Pointer)**

Lo stack è vuoto e ha una dimensione di **20 byte**. Poiché lo stack cresce all'indietro, il puntatore parte dalla fine dello spazio allocato.

- Dimensione in decimale: $20$
    
- Dimensione in esadecimale: $14h$
    
- Quindi, inizialmente: **SP = 0014h**
    

> **Risposta 1:**
> 
> - **SS = 1001h**
>     
> - **SP = 0014h**
>     

---

### 2. Esecuzione Passo Passo (Traccia dello Stack)

Analizziamo come cambiano il registro `SP` e il contenuto della memoria istruzione per istruzione.

_Nota: Gli offset sono indicati in decimale per chiarezza, il valore tra parentesi `[]` indica il contenuto a quell'indirizzo._

|**Istruzione**|**Operazione su SP**|**Nuovo Valore SP (Dec / Hex)**|**Azione in Memoria**|**Contenuto Stack (Offset: Valore)**|
|---|---|---|---|---|
|**Inizio**|(Vuoto)|20 / `0014h`|Nessuna|`[Vuoto]`|
|**PUSH 12**|SP - 2|18 / `0012h`|Scrive 12 a offset 18|`[18: 12]`|
|**POP AX**|SP + 2|20 / `0014h`|Legge 12 in AX|`[Vuoto]`|
|**PUSH 4**|SP - 2|18 / `0012h`|Scrive 4 a offset 18|`[18: 4]`|
|**PUSH 15**|SP - 2|16 / `0010h`|Scrive 15 a offset 16|`[16: 15]`, `[18: 4]`|
|**POP AX**|SP + 2|18 / `0012h`|Legge 15 in AX|`[18: 4]`|
|**PUSH 16**|SP - 2|16 / `0010h`|Scrive 16 a offset 16|`[16: 16]`, `[18: 4]`|

> **Risposta 2 (Contenuto Finale):**
> 
> Lo stack contiene due valori:
> 
> 1. All'offset **16 (0010h)** c'è il valore **16** (Questo è il Top dello Stack).
>     
> 2. All'offset **18 (0012h)** c'è il valore **4**.
>     

---

### 3. Valori finali e Controllo Errori

**Valore finale di SP**

Come si vede dall'ultimo passaggio della tabella:

$$SP = 16_{10} = \mathbf{0010h}$$

**Indirizzo Fisico del Top dello Stack**

L'indirizzo fisico si calcola combinando il segmento (SS) e l'offset corrente (SP):

$$Indirizzo = (SS \times 10h) + SP$$

$$Indirizzo = (1001h \times 10h) + 0010h$$

$$Indirizzo = 10010h + 0010h = \mathbf{10020h}$$

**Controllo Overflow / Underflow**

- **Limite Minimo (Full):** SP = 0
    
- **Limite Massimo (Empty):** SP = 20
    

Durante l'esecuzione, lo SP ha oscillato tra **16** e **20**.

- Non è mai sceso sotto 0 (Overflow).
    
- Non è mai salito sopra 20 _durante un POP_ (Underflow).
    

> **Risposta 3:**
> 
> - **SP Finale:** `0010h`
>     
> - **Indirizzo Fisico Top:** `10020h`
>     
> - **Overflow/Underflow:** Nessuno.
>

## Riferimenti
1. 