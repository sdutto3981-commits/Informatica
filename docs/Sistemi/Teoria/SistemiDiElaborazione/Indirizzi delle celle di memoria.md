---
date: 2026-02-01
time: 18:46
---

# Indirizzi delle celle di memoria

La memoria centrale è suddivisa in celle o locazioni che possono essere identificate tramite il loro indirizzo, cioè la posizione della cella di memoria ogni cella ha la stessa dimensione. Essa è poi organizzata in word.

Per esempio una parola potrebbe essere costituita da 4byte ciascuno con un indirizzo. La prima locazione ha indirizzo 0 e cosi via.

## Indirizzi assoluti e relativi

Per **indirizzo assoluto** si intende la posizione di una locazione di memoria a partire da quella di indirizzo 0

Per **Indirizzo relativo** si intende la posizione di una locazione di memoria rispetto a un altra . Per esprimere un indirizzo relativo occorrono due numeri: l'indirizzo della locazione di riferimento **base** e la distanza da essa **offset**

## Spazio di indirizzamento

la quantità di celle presenti nella memoria viene chiamata **Spazio di indirizzamento** e il suo valore dipende dalle caratteristiche della CPU dei BUS della scheda madre.

Il calcolo dello spazio di indirizzamento si ottiene a partire dal numero di fili conduttori del BUS degli indirizzi individuando tutte le possibili disposizioni con ala ripetizione di due elementi 0 e 1.

Quindi possiamo applicare la formula precedente $2^n$ mentre l'ultimo indirizzo di memoria sara $2^n-1$

## Decodifica degli indirizzi

Un circuito integrato chip di memoria contiene oltre alle singole celle dei circuiti di codifica il cui scopo è riconoscere l'indirizzo per poter accedere in lettura o scrittura alle celle di memoria.

Le locazioni sono disposte in una matrice quadrata o rettangolare ogni locazione occupa una disposizione identificata dal numero di riga e dal numero di colonna.

Per attivare la cella di memoria è  necessario un decodificatore un circuito logico il cui scopo e riconoscere l'indirizzo per potere accedere in lettura o scrittura.

Un decodificatore è un circuito logico con n ingressi e $2^n$ uscite esso prendendo l'indirizzo va a definire colonna e riga

## Riferimenti

1.
