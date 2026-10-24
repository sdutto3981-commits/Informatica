# Strutture (`struct`) in C

Una `struct` consente di raggruppare campi di tipi differenti in un unico oggetto.

## Dichiarazione e uso

```c
#include <stdio.h>

struct Persona {
    char nome[30];
    int eta;
    float altezza;
};

int main(void)
{
    struct Persona p = {"Ada", 18, 1.68f};
    printf("%s: %d anni, %.2f m\n", p.nome, p.eta, p.altezza);
    return 0;
}
```

Attenzione al punto e virgola dopo la definizione di `struct`. I campi si accedono con l'operatore `.`; se si dispone di un puntatore alla struttura, si usa `->`.

## Array di strutture

```c
struct Persona persone[5];
persone[0].eta = 17;
```

L'array contiene cinque strutture, indicizzate da `0` a `4`. Prima di utilizzare un campo, assicurati che abbia ricevuto un valore valido. Le stringhe C sono array di `char` terminati da `\0`; la capacità dell'array deve comprendere anche il terminatore.

## `typedef` (opzionale)

```c
typedef struct {
    int codice;
    float prezzo;
} Prodotto;

Prodotto p;
```

`typedef` crea un alias di tipo, evitando di scrivere `struct` ad ogni dichiarazione.
