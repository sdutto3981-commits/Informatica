---
date: 2026-02-01
time: 16:59
---
# Gestione memoria 8086

## Segmenti

La memoria dell'8086 è organizzata in segmenti aree di memoria ognuna della dimensione massima di 64 Kbyte Tutti i segmenti cominciano ad indirizzi multipli di 16 

## Caratteristiche segmenti

- Ogni programma eseguito dall'8086 è suddiviso nella memori ain segmenti CODICE, DATI o extra e STACK
- Ogni programma può contenere più segmenti di codice o di dato ma uno solo di stack
- Ogni segmento ha una dimensione variabile ma massima di 64 Kbytes e inizia sempre a una cella di posizione multipla di 16 
- Il numero di segmenti massimo non è fisso ma dipenderà dalla dimensione dei segmenti stessi

## Segmento codice

All'interno del segmento codice sono contenute tutte le istruzioni del programma in formato binario. ogni istruzione ha una sua dimensione variabile tra 1 e 6 bytes.

I registri segmento e puntatore che gestiscono l'indirizzamento in memoria sono rispettivamente CS e PC o IP
![[Pasted image 20260201171856.png]]

## Segmento dati 

All'interno del segmento dati sono contenuti le variabili globali del programma. I registri segmento e puntatore che gestiscono l'indirizzamento in memoria sono rispettivamente DS e DI o SI

![[Pasted image 20260201170750.png]]

## Segmento Stack

Nel segmento Stack vengono salvate le variabili locali e i parametri passati da un sottoprogramma.

I registri segmento e puntatore che gestiscono l'indirizzamento in memoria sono rispettivamente SS e SP

![[Pasted image 20260201170909.png]]

## Spazio di Indirizzamento

Lo spazio di indirizzamento è lo spazio di memoria messo a disposizione dal calcolatore per poter immagazzinare i programmi in esecuzione che dipernde dal numero N di bit a disposizione per ogni indirizzo di memoria. Nel 8086 avendo 20 bit a disposizione il suo spazio di indirizzamento e pari a 1 MB

***N bit -> $2^N$ indirizzi di  memoria possibili***

## Calcolo indirizzi

Ogni volta che l'8086 deve generare un indirizzo assoluto su 20 bit esso esegue un operazione di somma tra il contenuto di un registro segmento detto **INDIRIZZO RELATIVO** ed il contenuto di un registro puntatore detto **OFFSET**.

La somma avviene dopo aver moltiplicato per 16 shift di 4 posizioni in avanti il contenuto del registro segmento.
![[Pasted image 20260201171402.png]]

# Esempi

***Si consideri un programma scritto in linguaggio Assembler e in esecuzione, caricato all'interno della memoria centrale. Sono stati creati tre segmenti in memoria tra cui il segmento Codice cha ha inizio all'indirizzo 14B10h.***
***Sapendo che si deve eseguire l'istruzione che ha offset rispetto all'inizio del segmento codice pari a 1234h, determinare:***

***- Il contenuto del registro CS***
***- Il contenuto del registro PC***
***- Il valore dell'Indirizzo assoluto a cui si sa facendo riferimento in base al contenuto dei registri***


**Soluzione**
1.  CS: 14B10h
2. PC: 1234h
3. Indirizzo Assoluto: 14B10h + 01234h = 15D44h
## Riferimenti
1. 