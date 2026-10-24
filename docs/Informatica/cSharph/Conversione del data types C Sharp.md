---
date: 2025-10-16
time: 08:27
---

# Conversione del data types C Sharp

La conversione dei tipi di dati può avvenire in modo :

- **Implicito** ovvero quando la conversione avviene in modo automatico ed è il passaggio da un data type minore a uno maggiore: `char->int->long->float->double`
- **Esplicito** ovvero quando la conversione avviene in modo manuale ed è il passaggio da un data type maggiore a uno minore: `double->float->long->int->char`

## Conversione implicita

Conversione implicita avviene in modo automatico quando passiamo da tu type minore a uno maggiore
```csharp
int myInt = 9;
double myDouble = myInt;       // Automatic casting: int to double

Console.WriteLine(myInt);      // Outputs 9
Console.WriteLine(myDouble);   // Outputs 9
```

## Conversione esplicita

Conversione esplicita dev'avvenire manualmente piazzando il parametro del type di fronte al valore
```csharp
double myDouble = 9.78;
int myInt = (int) myDouble;    // Manual casting: double to int

Console.WriteLine(myDouble);   // Outputs 9.78
Console.WriteLine(myInt);      // Outputs 9
```

## Funzione di conversione

é anche possibile convertire tipi di dato esplicitamente usando una funzione interna nei seguenti metodi `Convet.ToBoolean`,`Convet.ToDouble`, `Convet.ToString`,`Convert.ToInt32(int)`, `Convet.ToInt64(long)`

Esempio:
```csharp
int myInt = 10;
double myDouble = 5.25;
bool myBool = true;

Console.WriteLine(Convert.ToString(myInt));    // convert int to string
Console.WriteLine(Convert.ToDouble(myInt));    // convert int to double
Console.WriteLine(Convert.ToInt32(myDouble));  // convert double to int
Console.WriteLine(Convert.ToString(myBool));   // convert bool to string
```
