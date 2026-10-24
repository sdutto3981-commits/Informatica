# Memoria dinamica in C

La memoria dinamica viene richiesta durante l'esecuzione. `malloc`, `calloc`, `realloc` e `free` sono dichiarate in `stdlib.h`.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t n = 5;
    int *valori = malloc(n * sizeof *valori);
    if (valori == NULL) {
        fprintf(stderr, "Memoria insufficiente\n");
        return 1;
    }

    for (size_t i = 0; i < n; i++) valori[i] = (int)i * 2;
    for (size_t i = 0; i < n; i++) printf("%d\n", valori[i]);

    free(valori);
    valori = NULL;
    return 0;
}
```

## Funzioni

- `malloc(size)`: alloca la quantità di byte richiesta; il contenuto non è inizializzato.
- `calloc(n, size)`: alloca spazio per più elementi e inizializza i byte a zero.
- `realloc(ptr, size)`: ridimensiona un blocco, eventualmente spostandolo.
- `free(ptr)`: rilascia un blocco allocato dinamicamente.

## Uso corretto

- Controlla sempre se l'allocazione è riuscita.
- Usa `sizeof *puntatore` per legare la dimensione al tipo effettivo.
- Mantieni separati puntatore originale e risultato temporaneo di `realloc` per non perdere il riferimento in caso di fallimento.
- Libera ogni allocazione una sola volta quando non serve più.
- Non accedere ai dati dopo `free`; non liberare puntatori che non provengono da una funzione di allocazione compatibile.
- Verifica overflow nel calcolo di `n * sizeof *ptr` quando `n` deriva da input.

## Esempio di `realloc`

```c
int *temporaneo = realloc(valori, nuova_n * sizeof *valori);
if (temporaneo != NULL) {
    valori = temporaneo;
    n = nuova_n;
}
```

Nel caso di fallimento, il blocco originale resta valido e può essere liberato o riutilizzato. Quando `nuova_n` è zero, il comportamento storico/standard di `realloc` ha particolarità: gestisci esplicitamente il caso invece di affidarti a esso.

## Riferimento

[W3Schools — C Memory Management](https://www.w3schools.com/c/c_memory_management.php)
