# File, puntatori e memoria dinamica in C

## Apertura e chiusura di un file

Il tipo `FILE *` rappresenta il flusso gestito dalla libreria standard. `fopen` restituisce `NULL` se l'apertura fallisce.

```c
#include <stdio.h>

int main(void)
{
    FILE *file = fopen("dati.txt", "r");
    char riga[256];

    if (file == NULL) {
        perror("Impossibile aprire dati.txt");
        return 1;
    }

    while (fgets(riga, sizeof riga, file) != NULL) {
        fputs(riga, stdout);
    }

    if (ferror(file)) {
        fprintf(stderr, "Errore durante la lettura.\n");
        fclose(file);
        return 1;
    }

    if (fclose(file) != 0) {
        perror("Errore di chiusura");
        return 1;
    }
    return 0;
}
```

Modalità comuni: `"r"` lettura, `"w"` scrittura con troncamento/creazione, `"a"` aggiunta in fondo. Le modalità con `+` consentono lettura e scrittura. I file devono essere chiusi con `fclose`.

## Puntatori

Un puntatore memorizza un indirizzo. `&variabile` ottiene l'indirizzo e `*puntatore` accede all'oggetto puntato.

```c
int n = 5;
int *p = &n;
*p = 8; /* ora n vale 8 */
```

Un puntatore deve essere inizializzato prima di dereferenziarlo e non deve puntare a un oggetto che non esiste più. `NULL` indica che non punta a un oggetto valido.

## Memoria dinamica

`malloc` alloca un blocco di memoria non inizializzato; `calloc` alloca e azzera i byte. In entrambi i casi controlla che il risultato non sia `NULL`. La memoria allocata va liberata con `free` una volta terminato l'uso.

```c
#include <stdlib.h>

size_t n = 10;
size_t i;
int *v = malloc(n * sizeof *v);
if (v == NULL) {
    /* gestire l'errore */
} else {
    for (i = 0; i < n; ++i) v[i] = 0;
    free(v);
    v = NULL;
}
```

Gli esempi sono impostati per restare compatibili con le regole di base del C classico: in C90 le dichiarazioni vanno collocate all'inizio del blocco. `size_t` è definito dalle intestazioni standard appropriate, per esempio `<stdlib.h>` o `<stddef.h>`. Segui lo standard indicato dal docente.

## Problemi da evitare

- perdita di memoria: blocco allocato mai liberato;
- use-after-free: usare memoria dopo `free`;
- double free: liberare due volte lo stesso blocco;
- buffer overflow: scrivere oltre i limiti di un array;
- leggere dati senza controllare i risultati delle funzioni.
