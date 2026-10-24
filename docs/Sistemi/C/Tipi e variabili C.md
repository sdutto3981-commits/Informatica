# Tipi, variabili e operatori in C

C è tipizzato staticamente. Il tipo determina interpretazione, memoria e operazioni consentite; la dimensione concreta di alcuni tipi dipende dall'implementazione, quindi `sizeof` permette di verificarla.

| Tipo | Uso generale |
|---|---|
| `char` | carattere o piccolo intero; il comportamento di `char` con segno dipende dall'implementazione |
| `short`, `int`, `long`, `long long` | interi con diverse ampiezze minime/garanzie |
| `unsigned` | versione senza segno di un tipo intero |
| `float`, `double`, `long double` | valori in virgola mobile |
| `_Bool` | tipo booleano standard C; con `stdbool.h` è disponibile il nome `bool` in C standard moderni |
| `void` | assenza di un valore o tipo generico del puntatore `void *` |

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int quantita = 12;
    double prezzo = 19.50;
    bool disponibile = true;

    printf("quantita = %d\n", quantita);
    printf("prezzo = %.2f\n", prezzo);
    printf("sizeof(int) = %zu byte\n", sizeof(int));
    printf("disponibile = %d\n", disponibile);
    return 0;
}
```

## Costanti e identificatori

`const` limita la modifica attraverso un identificatore qualificato; `#define` definisce una macro del preprocessore. Non sono esattamente lo stesso meccanismo.

## Operatori

- Aritmetici: `+ - * / %`; `%` si applica agli interi.
- Confronto: `== != < > <= >=`.
- Logici: `&& || !` con cortocircuito.
- Bitwise: `& | ^ ~ << >>` operano sui bit degli interi.
- Assegnazione: `=`, `+=`, `-=`, ecc.

La divisione tra interi tronca la parte frazionaria: `7 / 2` dà `3`. Non confondere `=` (assegnamento) con `==` (confronto).

## Formati di `printf`

Usa un formato compatibile con il tipo: `%d` per `int`, `%u` per `unsigned int`, `%ld` per `long`, `%f` per `double` in `printf`, `%c` per `char`, `%s` per stringa C e `%zu` per `size_t`.

## Riferimento

[W3Schools — C Data Types](https://www.w3schools.com/c/c_data_types.php) · [C Variables](https://www.w3schools.com/c/c_variables.php)
