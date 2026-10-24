# File in C

La libreria `stdio.h` fornisce `FILE` e funzioni per lavorare con file. `fopen()` apre un file e restituisce un puntatore a `FILE`, oppure `NULL` se l'apertura fallisce.

## Lettura di testo

```c
#include <stdio.h>

int main(void) {
    FILE *file = fopen("dati.txt", "r");
    if (file == NULL) {
        perror("dati.txt");
        return 1;
    }

    char riga[256];
    while (fgets(riga, sizeof riga, file) != NULL) {
        fputs(riga, stdout);
    }

    if (ferror(file)) {
        perror("Errore di lettura");
        fclose(file);
        return 1;
    }

    if (fclose(file) != 0) {
        perror("Errore chiusura");
        return 1;
    }
    return 0;
}
```

## Modalità comuni

- `"r"`: lettura, file esistente.
- `"w"`: scrittura, crea o tronca il file.
- `"a"`: aggiunta in fondo.
- `"r+"`, `"w+"`, `"a+"`: lettura e scrittura, con semantica specifica della modalità.
- Aggiungere `b` può essere usato per modalità binaria, ad esempio `"rb"`.

## Funzioni comuni

`fprintf`, `fscanf`, `fputs`, `fgets`, `fgetc`, `fputc`, `fread`, `fwrite`, `fseek`, `ftell`, `rewind`, `feof`, `ferror` e `fclose`.

Non usare `feof()` come condizione principale prima della lettura: il flag di fine file si attiva dopo che un tentativo di lettura raggiunge EOF. Controlla il valore restituito dalla funzione di lettura.

## Riferimento

[W3Schools — C Files](https://www.w3schools.com/c/c_files.php)
