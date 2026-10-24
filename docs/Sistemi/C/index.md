# Linguaggio C

## Distinzione tra le note

- [Tipi e variabili in C](Tipi%20e%20variabili%20C.md): panoramica di dichiarazioni, operatori e conversioni.
- [Tipi di dati in C](Data%20types%20C.md): categorie dei tipi, intervalli dipendenti dall'implementazione e specificatori di formato.
- [File in C](File%20in%20C.md): apertura, lettura, scrittura e chiusura dei file.
- [Memoria dinamica in C](Memoria%20dinamica%20C.md): ownership, allocazione, `realloc` e `free`.


C è un linguaggio compilato e procedurale molto usato in sistemi, applicazioni a basso livello e programmi che richiedono controllo diretto della memoria. Il percorso segue i fondamenti proposti dal tutorial W3Schools e approfondisce gli argomenti utili per il laboratorio.

## Percorso di studio

1. [Introduzione e compilazione](Introduzione%20C.md)
2. [Tipi, variabili e operatori](Tipi%20e%20variabili%20C.md)
3. [Controlli di flusso](Controlli%20di%20flusso%20C.md)
4. [Funzioni](Funzioni%20C.md)
5. [Vettori e stringhe](Vettori%20e%20stringhe%20C.md)
6. [Puntatori](Puntatori%20C.md)
7. [Struct ed enum](Struct%20in%20C.md)
8. [File](File%20in%20C.md)
9. [Memoria dinamica](Memoria%20dinamica%20C.md)
10. [Gestione errori e input](Errori%20e%20input%20C.md)
11. [Macro, preprocessore e bitwise](Bitwise%20macro%20e%20preprocessore%20C.md)
12. [Ricerca e ordinamento](Ricerca%20e%20ordinamento%20C.md)
13. [Liste concatenate](Liste%20concatenate.md)

## Primo programma

```c
#include <stdio.h>

int main(void) {
    printf("Ciao, mondo!\n");
    return 0;
}
```

Compilazione con GCC:

```bash
gcc -std=c11 -Wall -Wextra -Wpedantic main.c -o main
./main
```

I comandi di esecuzione variano per sistema operativo; su Windows, ad esempio, l'eseguibile normalmente è `main.exe`.

## Regole importanti

- Controlla i valori restituiti dalle funzioni che possono fallire.
- Non leggere input senza limite in un buffer.
- In C non esiste un controllo automatico degli indici degli array.
- Ogni memoria allocata dinamicamente e non più necessaria va rilasciata correttamente.

## Fonte di approfondimento

[W3Schools — C Tutorial](https://www.w3schools.com/c/index.php)
