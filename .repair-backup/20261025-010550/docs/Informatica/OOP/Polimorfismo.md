# Polimorfismo

Il polimorfismo consente di invocare un'operazione attraverso un tipo base e lasciare che l'implementazione dell'oggetto concreto determini il comportamento. Per il polimorfismo dinamico in C# si usano tipicamente `virtual` e `override`, oppure interfacce.

```csharp
Animale[] animali =
{
    new Cane("Fido"),
    new Animale("Creatura")
};

foreach (Animale animale in animali)
    Console.WriteLine($"{animale.Nome}: {animale.Verso()}");
```

La chiamata a `Verso()` seleziona la versione del metodo corrispondente al tipo reale dell'istanza.

## Overload e override non sono sinonimi

- **Overload (sovraccarico):** stesso nome di metodo, parametri diversi; la scelta avviene in compilazione.
- **Override (ridefinizione):** una classe derivata sostituisce l'implementazione di un membro virtuale/astratto; la scelta avviene in base al tipo reale dell'oggetto a runtime.
- **Hiding (`new`):** nasconde un membro con lo stesso nome, ma non equivale al dispatch virtuale.

Non è possibile fare `override` di un normale metodo non virtuale.
