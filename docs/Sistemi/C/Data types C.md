# Tipi di dati in C

Il tipo di un oggetto C determina le operazioni valide, l'interpretazione del valore e, insieme all'implementazione, la quantità di memoria utilizzata. Le dimensioni esatte di molti tipi dipendono dall'implementazione: non assumere che `int` sia sempre di 32 bit o `long` sempre di 64 bit.

## Tipi fondamentali

| Categoria | Tipi comuni | Osservazioni |
|---|---|---|
| Interi | `char`, `short`, `int`, `long`, `long long` | Le varianti `signed` e `unsigned` hanno intervalli differenti. |
| Reali | `float`, `double`, `long double` | Precisione e rappresentazione dipendono dall'implementazione. |
| Logico | `_Bool` (e `bool` con `<stdbool.h>` negli standard che lo prevedono) | Il valore memorizzato è 0 o 1. |
| Assenza di valore | `void` | Indica, ad esempio, una funzione senza valore restituito. |

`char` è un tipo intero destinato a rappresentare un'unità di carattere; non è garantito che abbia segno. Per gli intervalli si possono consultare `limits.h` e `float.h`.

## Dichiarazione e inizializzazione

```c
int conteggio = 0;
unsigned int tentativi = 3;
double media = 7.5;
char iniziale = 'A';
_Bool valido = 1;
```

Le costanti carattere usano apici singoli (`'A'`); le stringhe sono sequenze di caratteri terminate da `\0`, di solito conservate in array di `char`.

## Formati di input/output

| Tipo / uso | `printf` / `scanf` più comuni |
|---|---|
| `int` | `%d` |
| `unsigned int` | `%u` |
| `long` | `%ld` |
| `long long` | `%lld` |
| `double` con `printf` | `%f` |
| `double` con `scanf` | `%lf` |
| `char` | `%c` |
| stringa in un array di `char` | `%s` (con limite di larghezza in input) |

Il formato deve corrispondere al tipo dell'argomento: una specifica errata può produrre comportamento indefinito. `scanf` restituisce il numero di assegnazioni riuscite; controllalo prima di usare i valori letti.

Per la dichiarazione delle variabili, gli operatori e la conversione tra tipi consulta [Tipi e variabili in C](Tipi%20e%20variabili%20C.md) e [Gestione dell'input](Errori%20e%20input%20C.md).
