# Conversioni di tipo in C#

La conversione cambia il tipo di un valore oppure controlla se questa modifica è possibile. Alcune conversioni sono implicite; altre richiedono un cast o un metodo di conversione.

## Conversione implicita

Una conversione implicita è consentita quando il linguaggio può eseguirla senza perdita di informazioni nel normale modello del tipo.

```csharp
int intero = 10;
double numero = intero;
```

## Cast esplicito

```csharp
double valore = 9.8;
int intero = (int)valore; // 9: la parte frazionaria viene troncata
```

Un cast da numero in virgola mobile a intero non è un arrotondamento. Per arrotondare usa `Math.Round`, `Math.Floor` o `Math.Ceiling` a seconda della regola richiesta.

## Input da console

```csharp
Console.Write("Inserisci l'età: ");
string? testo = Console.ReadLine();

if (int.TryParse(testo, out int eta))
{
    Console.WriteLine($"Età inserita: {eta}");
}
else
{
    Console.WriteLine("Valore non valido.");
}
```

`int.Parse()` lancia un'eccezione quando la stringa non è un intero valido; `int.TryParse()` restituisce `false` senza lanciare quell'eccezione per un normale input non convertibile.

## Conversioni testuali

Usa `ToString()` per ottenere una rappresentazione testuale. Per formattare numeri e date in modo dipendente dalla lingua considera le impostazioni di cultura (`CultureInfo`), specialmente quando elabori file o dati scambiati tra sistemi.

## Riferimento

[W3Schools — C# Type Casting](https://www.w3schools.com/cs/cs_type_casting.php)
