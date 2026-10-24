# Vettori e stringhe in C

## Array

Un array contiene elementi dello stesso tipo in posizioni contigue. C non controlla automaticamente che gli indici siano nei limiti.

```c
int valori[] = {4, 7, 2, 9};
size_t n = sizeof valori / sizeof valori[0];

for (size_t i = 0; i < n; i++) {
    printf("%d\n", valori[i]);
}
```

La formula con `sizeof` funziona qui perché `valori` è ancora un array. Quando un array viene passato a una funzione, il parametro viene trattato come puntatore e la lunghezza va passata separatamente.

## Stringhe C

Una stringa C è un array di `char` terminato dal carattere nullo `\0`.

```c
char nome[] = "Ada";
printf("%s\n", nome);
```

`sizeof nome` include il terminatore; `strlen(nome)` dalla libreria `string.h` conta i caratteri prima di `\0`.

## Input sicuro di una riga

```c
char nome[50];
if (fgets(nome, sizeof nome, stdin) != NULL) {
    /* La riga è stata letta; può includere il carattere newline. */
}
```

Non usare `gets`: è stata rimossa dallo standard perché non permette di limitare la quantità di dati letti. Le funzioni di input devono ricevere dimensioni corrette e gli input devono essere controllati.

## Funzioni utili di `string.h`

- `strlen`: lunghezza senza `\0`.
- `strcmp`: confronto lessicografico, restituisce un valore minore, uguale o maggiore di zero.
- `strcpy`: copia una stringa, ma la destinazione deve avere spazio sufficiente.
- `strncpy`: non garantisce sempre il terminatore nullo se la sorgente è troppo lunga; serve controllo esplicito.

## Riferimento

[W3Schools — C Strings](https://www.w3schools.com/c/c_strings.php) · [C Arrays](https://www.w3schools.com/c/c_arrays.php)
