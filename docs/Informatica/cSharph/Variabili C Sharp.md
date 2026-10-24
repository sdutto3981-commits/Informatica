# Variabili in C#

Una variabile è un nome associato a un valore di un determinato tipo. La dichiarazione tipica è `tipo nome = valore;`.

```csharp
int eta = 17;
string nome = "Ada";
bool iscritta = true;
eta = eta + 1;
```

- `int`: intero.
- `double`: numero in virgola mobile.
- `decimal`: adatto a molti calcoli monetari.
- `char`: singolo carattere.
- `bool`: vero/falso.
- `string`: testo.

La stringa usa virgolette doppie; un `char` usa apici singoli. Il tipo del valore assegnato deve essere compatibile con quello della variabile.

## Dichiarazione e assegnazione

```csharp
int punteggio;       // dichiarazione
punteggio = 0;       // assegnazione
punteggio = 10;      // nuova assegnazione
```

Le variabili locali devono essere assegnate prima di essere lette. Per gli ambiti e la durata delle variabili consulta [sottoprogrammi](Sottoprogramma%20C%20Sharp.md) e [programmazione a oggetti](../OOP/index.md).
