---
date: 2026-02-01
time: 15:34
---

# Tipi registri 8086

- Registro dato
- Registro segmento
- Registro puntatore
- Registri di stato
- Registro MDR
- Registro MAR
- Registro IR

## Registro Dato

I registri sono:
- **AX (Accumulator Register)**
- **BX (Base Register)**
- **CX (Count Register)**
- **DX (Data Register)**

Sono utilizzati per memorizzare operandi e risultato delle operazioni.  Possono essere utilizzare come registri da 16 bit oppure come coppie di registri da 8 bit

## Organizzazione memoria

La memoria è organizzata in segmenti, ognuno di dimensione pari a 64Kbyte che possono essere di 4 tipologie: **di codice**, **di dato**, **di stack o extra**

*Risorsa non inclusa: Pasted image 20260201155440.png*

### Registro Segmento

I registri sono:
- **CS (Code Segment)**
- **DS (Data Segment)**
- **ES (Extra Segment)**
- **SS (Stack Segment)**

Vengono utilizzati per costruire gli Indirizzi fisici con i quali fare accesso in memoria. Contengono i puntatore all'inizio dei segmenti di codice, di dato, extra e di stack rispettivamente.

## Registri Puntatore

Contengono degli indirizzi relativi (offset)

I principali sono:
- **PC (Program Counter) o IP:** contiene l'indirizzo relativo (offset) della prossima istruzione da eseguire rispetto all'inizio del Code Segment (CS)
- **SP (Stack Pointer):** contiene l'indirizzo relativo della cella corrente dello stack rispetto all'inizio del Segmento di Stack (SS)
- **SI, DI (Data Index):** contengono l'indirizzo relativo del prossimo dato da prelevare rispetto al per i Data Segment (DS)

*Risorsa non inclusa: Pasted image 20260201155535.png*

## Altri Registri

- **IR (Istruction Register):** all'interno viene memorizzato il codice binario dell'istruzione che deve essere eseguita dalla CPU
- **MDR (Memory Data Register):** all'interno vengono memorizzati i dati letti dal bus dati o che devono essere inviati al bus dati
- **MAR (Memory Address Register):** All'interno viene memorizzato l'ultimo indirizzo di memoria a cui la CPU ha fatto riferimento. Si tratta dell'unico registro a 20 bit

## Riferimenti

1.
