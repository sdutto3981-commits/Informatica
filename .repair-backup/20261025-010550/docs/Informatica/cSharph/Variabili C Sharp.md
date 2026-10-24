# Variabili in C#

Una variabile è un nome associato a un dato di un tipo definito. In C# il tipo determina quali valori si possono rappresentare e quali operazioni sono disponibili.

```csharp
int eta = 17;
double temperatura = 21.5;
char iniziale = 'S';
bool attivo = true;
string nome = "Stefano";
```

## Dichiarazione e assegnazione

```csharp
int punteggio;    // dichiarazione
punteggio = 0;    // assegnazione
punteggio += 5;   // aggiornamento
```

Le variabili locali devono essere assegnate in modo definitivo prima di essere lette. I campi di una classe ricevono invece i valori predefiniti del tipo se non inizializzati esplicitamente.

## `var` e `const`

```csharp
var messaggio = "Ciao"; // tipo dedotto come string
const double PiGreco = 3.141592653589793;
```

`var` non rende la variabile dinamica: il compilatore deduce un tipo statico dall'inizializzatore. `const` dichiara una costante a tempo di compilazione e richiede un valore assegnabile costante.

## Ambito (scope)

Una variabile locale esiste nel blocco in cui è dichiarata; un campo appartiene a un'istanza o al tipo se è `static`. Evita di riutilizzare lo stesso nome in ambiti sovrapposti quando riduce la chiarezza.

## Riferimento

[W3Schools — C# Variables](https://www.w3schools.com/cs/cs_variables.php)
