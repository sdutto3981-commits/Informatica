# Introduzione al linguaggio C

C è un linguaggio compilato, procedurale e con gestione esplicita di memoria e indirizzi. Un programma tipico include le librerie necessarie, definisce `main` e restituisce un codice d'uscita.

```c
#include <stdio.h>

int main(void)
{
    int a, b;
    printf("Inserisci due interi: ");

    if (scanf("%d %d", &a, &b) != 2) {
        fprintf(stderr, "Input non valido.\\n");
        return 1;
    }

    printf("Somma: %d\\n", a + b);
    return 0;
}
```

`scanf` riceve gli indirizzi delle variabili da riempire, quindi si usa `&a` e `&b`. `printf` riceve invece i valori da visualizzare. Ogni istruzione C termina normalmente con `;`.

## Compilazione con GCC

```bash
gcc -std=c11 -Wall -Wextra -Wpedantic main.c -o main
./main
```

La prima riga compila il sorgente e crea l'eseguibile `main`; la seconda lo avvia su Linux/macOS. In caso di errori, leggere il primo messaggio utile del compilatore e correggere una cosa alla volta.
