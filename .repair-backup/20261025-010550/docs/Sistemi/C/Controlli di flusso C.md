# Condizioni e cicli in C

## Selezione

```c
if (voto >= 6) {
    printf("Sufficiente\n");
} else {
    printf("Insufficiente\n");
}
```

`else if` consente più condizioni. `switch` confronta un'espressione intera o di tipo enumerato con casi costanti:

```c
switch (scelta) {
    case 1: printf("Avvio\n"); break;
    case 2: printf("Esci\n"); break;
    default: printf("Scelta non valida\n"); break;
}
```

In mancanza di `break` il controllo può proseguire nei casi seguenti (fall-through) quando consentito, cosa che va usata consapevolmente.

## Cicli

```c
for (int i = 0; i < 5; i++) printf("%d\n", i);

int i = 0;
while (i < 3) {
    i++;
}

do {
    printf("Eseguito una volta\n");
} while (0);
```

- `for`: inizializzazione, condizione e aggiornamento.
- `while`: verifica la condizione prima del corpo.
- `do...while`: il corpo viene eseguito almeno una volta.
- `break`: esce dal ciclo o dallo `switch` più interno.
- `continue`: passa alla successiva iterazione del ciclo.

## Errori frequenti

- Usare `=` in una condizione quando si voleva `==`.
- Scrivere una condizione che non cambia mai e creare un ciclo infinito.
- Accedere a un array tramite un indice negativo o maggiore/uguale alla lunghezza.

## Riferimento

[W3Schools — C Conditions](https://www.w3schools.com/c/c_conditions.php) · [C Loops](https://www.w3schools.com/c/c_loops.php)
