# Classi e oggetti C#

> **Approfondimento OOP:** per incapsulamento, costruttori, ereditarietà, polimorfismo, interfacce e composizione, prosegui con [Programmazione orientata agli oggetti](../OOP/index.md).


Una **classe** definisce un tipo che raggruppa dati e comportamenti. Un **oggetto** è un'istanza concreta di una classe. Le classi consentono di modellare entità e separare responsabilità.

```csharp
class Rettangolo
{
    public double Larghezza { get; }
    public double Altezza { get; }

    public Rettangolo(double larghezza, double altezza)
    {
        Larghezza = larghezza;
        Altezza = altezza;
    }

    public double Area() => Larghezza * Altezza;
}

class Program
{
    static void Main()
    {
        Rettangolo r = new Rettangolo(4, 3);
        Console.WriteLine(r.Area()); // 12
    }
}
```

`new` costruisce un oggetto. `Larghezza` e `Altezza` sono proprietà; `Area()` è un metodo. Le proprietà con solo `get` vengono inizializzate nel costruttore e poi non possono essere assegnate normalmente dall'esterno.

## Campi, proprietà e metodi

- Campi: dati conservati direttamente nell'oggetto.
- Proprietà: accesso controllato a un valore (`get`, `set`, `init`).
- Metodi: comportamenti o operazioni.
- Membri `static`: appartengono al tipo e non a una specifica istanza.

## Riferimenti e null

Una variabile di tipo riferimento può riferirsi a un oggetto oppure, quando consentito, essere `null`. Con nullable reference types abilitati, `string?` indica che il valore può essere null; il compilatore segnala possibili accessi non sicuri ma non elimina ogni errore a runtime.

## Responsabilità della classe

Ogni classe dovrebbe avere uno scopo chiaro. Evita classi che gestiscono contemporaneamente interfaccia, file, logica di dominio e rete senza una separazione adeguata.

## Riferimento

[W3Schools — C# Classes and Objects](https://www.w3schools.com/cs/cs_classes.php)
