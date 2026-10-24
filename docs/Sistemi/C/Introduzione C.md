# Introduzione a C e compilazione

C è un linguaggio compilato. Il compilatore controlla e traduce il codice sorgente; il linker collega il programma alle librerie necessarie.

```c
#include <stdio.h>

int main(void) {
    int a = 0;
    int b = 0;
    printf("Inserisci due interi: ");

    if (scanf("%d %d", &a, &b) != 2) {
        fprintf(stderr, "Input non valido.\n");
        return 1;
    }

    printf("Somma: %d\n", a + b);
    return 0;
}
```

`printf` formatta e scrive testo; `scanf` legge dati secondo il formato indicato. Per `scanf` bisogna normalmente passare l'indirizzo della variabile tramite `&`. Il valore restituito da `scanf` indica quante conversioni sono state completate: è importante controllarlo.

## Compilazione con GCC

```bash
gcc -std=c11 -Wall -Wextra -Wpedantic main.c -o main
```

- `-std=c11`: seleziona lo standard C11 per la compilazione.
- `-Wall -Wextra -Wpedantic`: abilita avvisi utili.
- `main.c`: sorgente.
- `-o main`: nome dell'eseguibile prodotto.

Un eseguibile non viene creato correttamente se il compilatore rileva errori che impediscono la generazione del programma.

## Struttura classica

- direttive di preprocessore, per esempio `#include`;
- dichiarazioni e prototipi;
- definizioni di funzioni;
- `main`, che restituisce un codice di uscita convenzionale (`0` per successo).

## Riferimento

[W3Schools — C Get Started](https://www.w3schools.com/c/c_getstarted.php)
