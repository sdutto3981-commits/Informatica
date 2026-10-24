# Gestione degli errori e validazione dell'input in C

C lascia al programmatore molte responsabilità: non controlla automaticamente i limiti degli array e può produrre comportamento indefinito in caso di accessi non validi o uso scorretto della memoria.

## Controllare le funzioni

Verifica il valore restituito da `scanf`, `fopen`, `malloc`, `fgets` e da ogni funzione la cui documentazione indica possibili errori.

```c
int eta;
printf("Età: ");
if (scanf("%d", &eta) != 1) {
    fprintf(stderr, "Input non valido\n");
    return 1;
}
```

`scanf` può lasciare caratteri non letti nell'input quando una conversione fallisce. Per input più robusto si usa spesso `fgets` per leggere una riga, poi si converte con `strtol` o funzioni analoghe controllando dove termina la conversione e se ci sono errori.

## Errori comuni

- Usare una variabile non inizializzata.
- Scrivere fuori dai limiti di un array o buffer.
- Dereferenziare `NULL` o un puntatore non valido.
- Dimenticare `free`, causando una perdita di memoria.
- Liberare due volte la stessa allocazione.
- Usare una stringa senza terminatore nullo.
- Ignorare gli errori di lettura/scrittura dei file.

## Compilare con avvisi

```bash
gcc -std=c11 -Wall -Wextra -Wpedantic -g main.c -o main
```

Gli avvisi e il debugger non rilevano ogni errore, ma sono strumenti importanti. Per analisi più approfondite si possono usare sanitizzatori e strumenti di analisi statica quando disponibili.

## Riferimento

[W3Schools — C Errors](https://www.w3schools.com/c/c_errors.php)
