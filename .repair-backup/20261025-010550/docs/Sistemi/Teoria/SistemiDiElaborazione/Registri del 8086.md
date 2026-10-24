---
date: 2026-02-01
time: 15:05
---

# Registri del 8086

*Risorsa non inclusa: Pasted image 20260201150748.png*

1. **Data Register (Registri Dati)**

Sono registri a 16 bit ma  possono essere accessibili anche come due registri separati a 8 bit.

- **AX (AH,AL) - Accumulatore:** usato per le operazioni aritmetiche e logiche per I/O
- **BX (BH, BL) - Base:** Usato per indirizzare la memoria
- **CX (CH, CL) - Counter:** Usato come contatore nei loop e nelle operazioni sulle stringhe.
- **DX (DH,HL) - Data:** Usato per le operazioni di moltiplicazione e divisione per I/O

2. **Pointers (Puntatori)**

Sono i registri utilizzati per gestire la memoria e lo stack:

- **SP (Stack Pointer):** Punta alla cima dello stack (la memoria temporanea)
- **BP (Base Pointer:** Usato per accedere ai dati all'interno dello stack
- **SI (Source Index):** Indice sorgente per le operazioni sulle stringhe o array
- **DI (Destination Index):** Indice di destinazione per le operazioni sulle stringhe o array
- **IP (Instruction Pointer):** Contiene l'indirizzo della prossima istruzione da eseguire

3. **Segment Register (Registri di Segmento)**

 L'8086 divide la memoria in segmenti logici:

- **CS (Code Segment):** Contiene il codice del programma (le istruzioni)
- **SS (Stack Segment):** Contiene lo stack
- **DS (Data Segment):** Contiene i dati e le variabili globaliao
- **ES (Extra Segment):** Segmento aggiuntivo per dati extra

4. **Instruction Queue (Coda Istruzioni)**

Rappresenta la coda di pre-fetch.

- L'8086 è stato uno dei primi processori a implementare questa funzione. Mentre la CPU esegue un istruzione l'unità di interfaccia bus (BIU) preleva in anticipo le istruzioni successive dalla memoria e le mette in questa coda lunga 6byte
- Questo velocizza l'esecuzione concetto di **pipeline**

5. **ALU e PSW**

- **Arithmetic Logic Unit (ALU):** circuito che esegue effettivamente i calcoli logici
- **PSW (Program Status Word) o Flags:** Il registro dei flag. Ogni bit segnalo lo stato dell'ultima operazione della **ALU**

6. **Control Logic (Logica di Controllo)**

Decodifica le istruzioni prelevate dalla coda e invia segnali elettrici a tutti gli altri componenti per eseguire l'operazione richiesta

7. **Interfaccia Esterna**

- **Adress/Data (20pin):** L'8086 ha un bus di indirizzi a 20bit che permette di indirizzare 1MB di memoria $2^{20}$
- **Control (16pin):** Segnali per controllare la memoria e le periferiche lettura scrittura interrupt

## Riferimenti

1.
