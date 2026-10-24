# Introduzione al linguaggio C

C è un linguaggio compilato. Un programma sorgente viene tradotto in un file eseguibile attraverso le fasi di preelaborazione, compilazione, assemblaggio e collegamento (i dettagli dipendono dalla toolchain).

## Programma minimo

```c
#include <stdio.h>

int main(void)
{
    int a;
    int b;

    printf("Inserisci due interi: ");
    if (scanf("%d %d", &a, &b) != 2) {
        fprintf(stderr, "Input non valido.\n");
        return 1;
    }

    printf("Somma: %d\n", a + b);
    return 0;
}
```

- `#include <stdio.h>` rende disponibili le dichiarazioni di input/output standard.
- `main` è il punto d'ingresso del programma hosted standard.
- `scanf` riceve gli indirizzi delle variabili con `&`; occorre verificare quanti valori sono stati letti.
- `printf` riceve i valori da visualizzare. `%d` è il formato per un `int`.
- `return 0` segnala normalmente il completamento corretto.

## Compilare con GCC

```bash
gcc -std=c90 -Wall -Wextra -pedantic programma.c -o programma
./programma
```

Il comando usa C90 (ANSI C) per esercitarsi con uno standard classico. Usa le opzioni richieste dal docente. Gli avvisi del compilatore aiutano a individuare problemi: non ignorarli senza averne capito il motivo.

## Errori comuni

- dimenticare `;` alla fine di un'istruzione;
- dimenticare `&` in una chiamata a `scanf` per una variabile scalare;
- usare specificatori di formato non coerenti con il tipo;
- non controllare il risultato delle funzioni di input e apertura file;
- confondere `=` (assegnazione) con `==` (confronto).
