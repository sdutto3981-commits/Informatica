# Funzioni in C

Una funzione raggruppa istruzioni per svolgere un compito. Il prototipo dichiara la firma, la definizione contiene il corpo e la chiamata avvia l'esecuzione.

```c
#include <stdio.h>

int somma(int a, int b); /* prototipo */

int main(void) {
    printf("%d\n", somma(3, 4));
    return 0;
}

int somma(int a, int b) {
    return a + b;
}
```

`int` è il tipo restituito. Una funzione senza valore restituito usa `void`. La forma `int main(void)` dichiara esplicitamente che `main` non riceve argomenti.

## Parametri e passaggio di dati

C passa gli argomenti **per valore**: la funzione riceve una copia. Per modificare un dato del chiamante si passa normalmente un puntatore alla variabile.

```c
void incrementa(int *n) {
    if (n != NULL) (*n)++;
}
```

Chiamata: `incrementa(&valore);`. L'asterisco nel parametro indica un puntatore; `&valore` calcola l'indirizzo della variabile.

## Scope e durata

Le variabili locali sono disponibili nel blocco in cui sono dichiarate e normalmente hanno durata limitata all'attivazione della funzione. Una variabile `static` locale conserva il valore tra chiamate; va usata quando questo stato persistente è voluto.

## Ricorsione

Una funzione ricorsiva deve prevedere un caso base per terminare. Una ricorsione profonda può esaurire lo stack; cicli iterativi possono essere più adatti in base al problema.

## Riferimento

[W3Schools — C Functions](https://www.w3schools.com/c/c_functions.php)
