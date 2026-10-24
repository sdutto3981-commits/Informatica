# Classi astratte

Una classe dichiarata `abstract` rappresenta una base incompleta che non può essere istanziata direttamente. Può contenere campi, proprietà, costruttori e metodi concreti, oltre a membri astratti che devono essere implementati dalle classi derivate concrete.

```csharp
public abstract class Figura
{
    public abstract double Area();

    public virtual string Descrizione() => "Figura geometrica";
}

public sealed class Rettangolo : Figura
{
    public double Base { get; }
    public double Altezza { get; }

    public Rettangolo(double @base, double altezza)
    {
        if (@base <= 0) throw new ArgumentOutOfRangeException(nameof(@base));
        if (altezza <= 0) throw new ArgumentOutOfRangeException(nameof(altezza));
        Base = @base;
        Altezza = altezza;
    }

    public override double Area() => Base * Altezza;
}
```

`Figura f = new Rettangolo(4, 3);` è valido; `new Figura()` non lo è. Il tipo della variabile può essere astratto, ma l'oggetto creato deve avere un tipo concreto.

## Quando usare una classe astratta

È adatta quando i tipi derivati condividono stato o implementazioni comuni, oltre a un contratto obbligatorio. Se occorre soltanto definire un contratto di capacità, spesso è preferibile un'interfaccia.
