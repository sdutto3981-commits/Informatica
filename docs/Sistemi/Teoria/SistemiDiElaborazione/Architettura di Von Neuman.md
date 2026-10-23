---
date: 2025-11-05
time: 10:17
---
 # Architettura di Von Neuman

Il modello di Von Neuman descrive il comportamento di una macchina che il suo inventore chiamo stored-program computer esecutore sequenziale dotati di un programma memorizzato.

Lo stored Program indica le istruzioni che la CPU deve eseguire. Tali istruzioni sono collocate stored nella memoria del compute e l'insieme delle istruzioni rappresenta il programma program che deve essere eseguito. Nella memoria risiedono oltre alle istruzioni in linguaggio Assembly dei programmi in corso di esecuzione i dati sui quali tali programmi operano.

Questo sistema ad oggi è alla base del calcolatore moderno.

### Unità all'interno del modello
- Unità di ingresson per l'acquisizione dei dati e dei programmi e per il loro trsferimento in memoria
- Unità di memoria per l aregistrazione sia dei dati che delle istruzioni del programma
- Unità di controllo presiede a tutte le operazion interpreta le istruzioni
- Unità aritmetico logica dedicata alla esexuzione delle operazioni aritmetiche e logiche
- Unità di uscita il trasferimento delle informazioni rielaborate in ingresso

### Programma memorizato

- Il modello di Von Neuman si basa suk concetto di programma memorizzato:


### Ruolo dell' unità

Permette di interpretate i dati ricevuti in input e poi rielaborarli per rieseguire le varie operazioni memorizzate e poi rielaborarle mentre la memoria contiene il programma stesso

### L'elaborazione secondo il modello di Von Neumann
- Il programma ed i dati su cui esso oopera devono trovarsi in memoria
- Il programma viene prelevato dall'unità di ingresso e registrato in memoria 
- La lettura dei dari su cui opera è una delle operazione previste dal proframma pertanto la refistrazione in memoria dei dati avvienee nella fase successica 
- Le azioni elaborative descritte dal programma vengono eseguite dall'unitò di controllo con l'ausilio delle unità  fase di esecuzione

L'interconnessione è possibile grazie ai bus che collegano i vari componenti ne esistono diversi tipi:
- bus controllo
- bus indirizzi
- bus dati

### Modello

- Il processore o CPU è il cervello del sistema: legge le istruzioni dalla memoria fetch le interpreta decode e le esegue execute una alla volta;
- La memoria centrale Ram random access memory, Conserva dati e istruzioni codificati come sequenze finite di cifre binarie 0 e 1 
- Le interfacce di I/O collegamenti tra il sistema e il mondo esterno. Servono per connete al sistemi i dispositivi utili all'inserimento e di dati esterni
- Bus collegamenti tra i vari componenti

#### Esempio

- Dati due numeri a e b, calcolare il loro prodotto
- ($res=a*$b) i valori a e b decono essere lerri da tastiera e iil risultato viene stampo a video 
La ALU esegue sia l'addizione 

Quindi dovremo usare dei cicli e poi delle somme in input chiederemo a e b e come output avremo il risultato del operazione

- [[Registri]]
- [[Memoria centrale von Neuman]]
- [[Unità di controllo]]
- [[ALU]]
- [[BUS]]
- [[Clock]]

## Riferimenti
1. [[Architettura dei sistemi di elaborazione]]