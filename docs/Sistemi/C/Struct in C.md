# Strutture (`struct`) in C

Una `struct` aggrega campi di tipi differenti in un unico tipo composto.

```c
#include <stdio.h>

struct Persona {
    char nome[30];
    int eta;
    float altezza;
};

int main(void)
{
    struct Persona p = {"Ada", 20, 1.68f};
    printf("%s, %d anni, %.2f m\\n", p.nome, p.eta, p.altezza);
    return 0;
}
```

Il punto e virgola dopo la graffa che chiude la definizione della `struct` è obbligatorio. I membri si accedono con `.` quando si dispone di un oggetto e con `->` quando si dispone di un puntatore alla struttura.

## Array di strutture

```c
struct Persona persone[5];
persone[0].eta = 18;
```

La dichiarazione riserva spazio per cinque strutture. Prima di usare i campi, inizializzarli in modo appropriato. Per leggere stringhe da input, preferire funzioni che limitano il numero di caratteri letti.
