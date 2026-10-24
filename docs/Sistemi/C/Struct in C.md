# `struct` in C

Una `struct` raggruppa campi di tipi differenti sotto un unico tipo composto.

```c
#include <stdio.h>

struct Persona {
    char nome[30];
    int eta;
    double altezza;
};

int main(void) {
    struct Persona p = {"Ada", 20, 1.70};
    printf("%s, %d anni\n", p.nome, p.eta);
    return 0;
}
```

Il punto e virgola dopo la parentesi graffa che conclude la definizione del tipo è obbligatorio. I membri si accedono con `.`; con un puntatore a struct si usa `->`.

```c
struct Persona persone[5];
struct Persona *ptr = &persone[0];
ptr->eta = 21;
```

## `typedef`

`typedef` crea un alias per un tipo:

```c
typedef struct {
    int x;
    int y;
} Punto;

Punto origine = {0, 0};
```

Un array di struct contiene una struttura completa in ciascuna posizione. In una struct che contiene puntatori, la copia della struct copia i puntatori, non necessariamente i dati a cui puntano.

## `enum`

Un tipo enumerato rappresenta un insieme di costanti nominate:

```c
enum Stato { SPENTO, ACCESO, ERRORE };
enum Stato stato = ACCESO;
```

I valori sono interi; se il programma dipende dalla rappresentazione numerica, definisci e documenta i valori intenzionalmente.

## Riferimento

[W3Schools — C Structures](https://www.w3schools.com/c/c_structs.php) · [C Enums](https://www.w3schools.com/c/c_enums.php)
