# Stringhe, `Math` e numeri casuali in C#

## Stringhe

`string` è un tipo riferimento immutabile: operazioni di modifica producono normalmente nuove stringhe.

```csharp
string nome = "Ada";
string saluto = $"Ciao, {nome}!";
string pulito = "  testo  ".Trim();
Console.WriteLine(pulito.ToUpperInvariant());
```

Metodi comuni: `Trim`, `ToUpper`, `ToLower`, `Contains`, `StartsWith`, `EndsWith`, `Replace`, `Substring` e `Split`. Per confronti indipendenti dalla lingua o regole precise, valuta gli overload con `StringComparison` o le API di cultura appropriate.

## `Math`

```csharp
double valore = 3.7;
Console.WriteLine(Math.Round(valore));
Console.WriteLine(Math.Floor(valore));
Console.WriteLine(Math.Ceiling(valore));
Console.WriteLine(Math.Sqrt(16));
```

`Round` arrotonda secondo le regole previste dall'overload; `Floor` va verso il basso e `Ceiling` verso l'alto. Per i valori in virgola mobile, tieni conto della precisione finita.

## Numeri pseudo-casuali

```csharp
Random casuale = new Random();
int numero = casuale.Next(1, 21); // 1..20, limite superiore escluso
```

`Next(min, max)` include il limite inferiore ed esclude quello superiore. Per un gioco semplice, `Random` è adeguato; non va usato per generare segreti crittografici.

## Riferimento

[W3Schools — C# Strings](https://www.w3schools.com/cs/cs_strings.php) · [C# Math](https://www.w3schools.com/cs/cs_math.php)
