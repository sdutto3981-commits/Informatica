# Interfacce in C#

Un'interfaccia definisce un contratto: stabilisce quali membri deve esporre un tipo che la implementa. Si dichiara con `interface`; una classe può implementarne più di una.

```csharp
public interface IStampabile
{
    string GeneraTesto();
}

public class Fattura : IStampabile
{
    public int Numero { get; }
    public Fattura(int numero) => Numero = numero;

    public string GeneraTesto() => $"Fattura n. {Numero}";
}

static void Stampa(IStampabile elemento)
{
    Console.WriteLine(elemento.GeneraTesto());
}
```

`Stampa` dipende dal contratto `IStampabile`, non dalla classe concreta `Fattura`. Questo rende il codice riutilizzabile con qualunque altro tipo che rispetti lo stesso contratto.

## Interfaccia o classe astratta?

- Classe astratta: può condividere stato e implementazione; una classe eredita al massimo da una classe base.
- Interfaccia: descrive una capacità/contratto; una classe può implementare più interfacce.

Le versioni moderne di C# consentono anche implementazioni predefinite in alcune interfacce; per gli esercizi introduttivi, considera prima il modello essenziale con firme da implementare.
