---
date: 2025-10-28
time: 09:57
---
# Sottoprogramma C Sharp

Sono dei programmi di istruzioni finite che servono per delle azioni ripetute che poi possono essere richiamate più volte nel codice esso svolge un compito specifico.

Che vengono inserite nello stack che contiene i sotto programmi 

Quando parliamo di funzione si intende un particole tipo di sottoprogramma la cui caratteristica principale è quella  di calcolare e fornire un risultato in uscita il risultato calcolato dalla funzione viene quindi ritornato al programma chiamante negli altri casi è una procedura.

La funzione è un sottoprogramma che restituisce un valore oppure restituisce nessun valore.

##### intestazione della funzione o firma

```
tipo di dato nome funzione(parametri)
{
	return
}
```

- Tipo di dato = se restituisce oppure void se non restituisce nome
- Nome funzione = nome che viene richiamato 
- Parametri = quello su cui andrà a lavorare la funzione
- return  = restituisce una variabile dello stesso tipo di dato con cui e stata dichiarata la funzione se void non lo scrivo

![[Variabili locali e globali C Sharp]]

##### richiamare una funzione

Per richiamare una funzione ci basta richiamare il suo nome inserendo i parametri e se ci da un return possiamo assegnarla ad una variabile in modo tale che il return della funzione sia uguale alla variabile

##### parametri

I parametri specificati nella dichiarazione di una funzione sono **parametri formali** mentre quelli inseriti quando richiamiamo una funzione vengono detti **parametri attuali** e inizia il meccanismo per qui i formali vengono sostituite con gli attuali

Viene considerata la regola del NOT ovvero il numero di parametri formali dev'essere uguale al numero di parametri attuali il tipo che dev'essere uguale 

Passaggio di parametri:
1. **Per valore**
Quando un parametro viene passato **per valore**, il **valore della variabile originale viene copiato** in una nuova variabile (il **parametro formale** della funzione).

- `a` ha il valore `5` nel `main`.
    
- Quando chiami `incrementa(a)`, viene **copiato** il valore 5 in una nuova cella (il parametro `x`).
    
- Dentro la funzione modifichi `x`, **non** `a`.
    
- Quando la funzione finisce, la variabile `x` viene **deallocata**, e le modifiche **non si riflettono su `a`**.

 2. **Per referenza (per indirizzo)**

In questo caso, invece di passare il valore, **si passa l’indirizzo di memoria** della variabile.  
La funzione riceve un **puntatore** e può modificare **direttamente** la variabile originale.
Quando passo i parametri per referenza le modiche fatte sui parametri formali valgono anche dopo

- `a` ha il valore `5` nel `main`.
    
- `&a` è l’indirizzo di `a` (es. 0x7ffe...).
    
- Dentro la funzione `incrementa`, il parametro `x` contiene quell’indirizzo.
    
- Quando scrivi `*x = *x + 1`, vai in quella posizione di memoria e **modifichi il valore originale**.
    
- Al termine, `a` nel `main` è cambiato (ora vale 6).

Se vogliamo andare a caricare come parametro un vettore non serve passarlo per referenza anche se sarebbe logico farlo siccome un array e già un puntatore quindi passandolo per referenza creeremmo un puntatore che punta ad un altro puntatore che punta all' area di memoria 

## Riferimenti
1. [[00 Top Down]]