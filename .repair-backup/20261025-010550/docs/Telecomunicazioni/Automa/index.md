# Automi a stati finiti

Un automa a stati finiti modella un sistema con un numero limitato di stati. Lo stato successivo dipende dallo stato corrente e dall'ingresso ricevuto.

## Elementi

- **Stati:** condizioni significative in cui può trovarsi il sistema.
- **Stato iniziale:** stato da cui parte il comportamento.
- **Ingressi:** eventi o segnali osservati.
- **Transizioni:** regole che determinano il cambiamento di stato.
- **Uscite:** azioni o valori prodotti dal sistema.

## Moore e Mealy

- **Automa di Moore:** l'uscita dipende soltanto dallo stato corrente.
- **Automa di Mealy:** l'uscita dipende dallo stato corrente e dall'ingresso.

## Metodo di progetto

1. Scrivi la descrizione del problema.
2. Individua ingressi, uscite e stati necessari, evitando stati ridondanti.
3. Disegna il diagramma delle transizioni.
4. Costruisci la tabella: stato corrente, ingresso, stato successivo e uscita.
5. Verifica tutte le transizioni possibili e i casi limite.
6. Se richiesto, codifica gli stati e ricava le funzioni logiche dei circuiti associati.

Un cancello automatico potrebbe avere stati `Chiuso`, `Apertura`, `Aperto` e `Chiusura`. Finecorsa, sensore di sicurezza e timer determinano le transizioni; il comportamento preciso va definito dalle specifiche.
