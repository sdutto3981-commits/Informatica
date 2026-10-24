# Liste concatenate in C

Una lista concatenata è una struttura dinamica formata da nodi. Ogni nodo contiene un dato e un puntatore al nodo successivo; il puntatore iniziale identifica la testa della lista.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Nodo {
    int valore;
    struct Nodo *successivo;
} Nodo;

void stampa(const Nodo *testa) {
    for (const Nodo *p = testa; p != NULL; p = p->successivo)
        printf("%d -> ", p->valore);
    puts("NULL");
}

void libera(Nodo *testa) {
    while (testa != NULL) {
        Nodo *successivo = testa->successivo;
        free(testa);
        testa = successivo;
    }
}
```

## Inserimento in testa

```c
Nodo *inserisci_testa(Nodo *testa, int valore) {
    Nodo *nuovo = malloc(sizeof *nuovo);
    if (nuovo == NULL) return testa; /* in un progetto reale segnala anche l'errore */

    nuovo->valore = valore;
    nuovo->successivo = testa;
    return nuovo;
}
```

Il chiamante deve aggiornare la testa: `testa = inserisci_testa(testa, 42);`. L'allocazione può fallire; nei programmi più completi è preferibile restituire anche un indicatore di errore separato.

## Complessità introduttiva

- Inserimento in testa: `O(1)`.
- Ricerca di un valore: `O(n)`.
- Accesso all'elemento in posizione arbitraria: `O(n)` perché si attraversano i nodi.

Rispetto a un array, la lista permette inserimenti/rimozioni locali comodi se si possiede il puntatore al nodo precedente, ma richiede memoria aggiuntiva e non offre accesso casuale efficiente.

## Regole di gestione memoria

Ogni nodo allocato deve essere raggiungibile finché serve e liberato esattamente una volta. Non leggere un nodo dopo `free` e non usare il suo campo `successivo` dopo averlo liberato.

## Riferimento

[W3Schools — C Linked Lists](https://www.w3schools.com/c/c_linked_lists.php)
