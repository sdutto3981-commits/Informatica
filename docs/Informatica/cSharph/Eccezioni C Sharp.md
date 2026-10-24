# Eccezioni in C#

Un'eccezione segnala una condizione anomala durante l'esecuzione. Si usano `try`, `catch` e `finally` per gestire errori recuperabili e assicurare eventuali operazioni finali.

```csharp
try
{
    Console.Write("Dividendo: ");
    if (!double.TryParse(Console.ReadLine(), out double a))
        throw new FormatException("Il dividendo non è numerico.");

    Console.Write("Divisore: ");
    if (!double.TryParse(Console.ReadLine(), out double b))
        throw new FormatException("Il divisore non è numerico.");

    if (b == 0) throw new DivideByZeroException("Il divisore è zero.");
    Console.WriteLine(a / b);
}
catch (FormatException ex)
{
    Console.WriteLine($"Input non valido: {ex.Message}");
}
catch (DivideByZeroException ex)
{
    Console.WriteLine(ex.Message);
}
```

## Buone pratiche

- Preferisci `TryParse` quando un input non numerico è un caso previsto.
- Intercetta eccezioni specifiche che puoi gestire; evitare `catch (Exception)` indiscriminati nasconde problemi.
- Non usare le eccezioni per il normale flusso di controllo se esiste una soluzione più semplice.
- Non ignorare un'eccezione silenziosamente.
- `finally` è utile per operazioni finali; per oggetti che implementano `IDisposable`, preferisci spesso `using`.

## Riferimento

[W3Schools — C# Exceptions](https://www.w3schools.com/cs/cs_exceptions.php)
