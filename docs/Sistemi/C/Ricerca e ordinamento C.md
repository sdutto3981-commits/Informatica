# Ricerca e ordinamento in C

## Ricerca lineare

Esamina gli elementi uno per volta; funziona anche quando i dati non sono ordinati.

```c
#include <stddef.h>

int ricerca_lineare(const int valori[], size_t n, int x) {
    for (size_t i = 0; i < n; i++) {
        if (valori[i] == x) return (int)i;
    }
    return -1;
}
```

Questa funzione usa `-1` per indicare che il valore non è stato trovato. Se `n` può essere maggiore del massimo `int`, usa un tipo di ritorno che rappresenti in modo sicuro sia un indice valido sia il caso assente, per esempio `ptrdiff_t`.

## Ricerca dicotomica

Richiede una sequenza ordinata. Ad ogni iterazione dimezza l'intervallo candidato.

```c
#include <stddef.h>

ptrdiff_t ricerca_binaria(const int valori[], size_t n, int x) {
    size_t sinistra = 0, destra = n;
    while (sinistra < destra) {
        size_t centro = sinistra + (destra - sinistra) / 2;
        if (valori[centro] == x) return (ptrdiff_t)centro;
        if (valori[centro] < x) sinistra = centro + 1;
        else destra = centro;
    }
    return -1;
}
```

In un file completo occorre includere `<stddef.h>` per `ptrdiff_t`. La complessità è `O(log n)`; la ricerca lineare è `O(n)` nel caso peggiore.

## Ordinamento

Per esercitarsi si possono implementare bubble sort, selection sort o insertion sort e confrontare il numero di confronti e scambi. In C standard, `qsort()` ordina un array usando una funzione di confronto; occorre però definire correttamente il comparatore.

## Riferimento

[W3Schools — C Searching and Sorting](https://www.w3schools.com/c/c_dsa.php)
