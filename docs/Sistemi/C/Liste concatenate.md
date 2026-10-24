# Liste concatenate in C

Una lista semplicemente concatenata è composta da nodi. Ogni nodo contiene un dato e un puntatore al nodo successivo; l'ultimo nodo punta a `NULL`.

## Definizione di un nodo

```c
#include <stdlib.h>
#include <stdio.h>

typedef struct Nodo {
    int valore;
    struct Nodo *next;
} Nodo;
```

## Inserimento in testa

```c
Nodo *inserisci_testa(Nodo *testa, int valore)
{
    Nodo *nuovo = malloc(sizeof *nuovo);
    if (nuovo == NULL) return testa; /* il chiamante dovrebbe distinguere l'errore */

    nuovo->valore = valore;
    nuovo->next = testa;
    return nuovo;
}
```

La funzione restituisce la nuova testa: dopo l'inserimento va assegnata, per esempio `testa = inserisci_testa(testa, 42);`. In un programma robusto è meglio segnalare separatamente l'errore di allocazione.

## Attraversamento e deallocazione

```c
void stampa_lista(const Nodo *testa)
{
    const Nodo *corrente = testa;
    while (corrente != NULL) {
        printf("%d\n", corrente->valore);
        corrente = corrente->next;
    }
}

void libera_lista(Nodo *testa)
{
    while (testa != NULL) {
        Nodo *successivo = testa->next;
        free(testa);
        testa = successivo;
    }
}
```

Prima si salva il puntatore al nodo successivo e poi si libera quello corrente. Non accedere più a un nodo dopo averlo liberato.

## Complessità indicativa

- Inserimento in testa: `O(1)`.
- Ricerca di un valore: `O(n)`.
- Accesso al n-esimo elemento: `O(n)` perché si percorrono i nodi.

Le liste non hanno accesso casuale efficiente come gli array, ma possono crescere senza richiedere un blocco contiguo di memoria.
