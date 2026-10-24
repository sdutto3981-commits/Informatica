# C# e .NET

C# è un linguaggio tipizzato usato su .NET. Il compilatore controlla la sintassi e i tipi, quindi il programma può essere eseguito nell'ambiente di runtime .NET.

## Percorso consigliato

1. [Introduzione a C#](Cos'%C3%A8%20C%20Sharp.md) e [sintassi](Sintassi%20C%20Sharp.md)
2. [Variabili](Variabili%20C%20Sharp.md), [tipi di dati](Data%20Types%20C%20Sharp.md), [conversioni](Conversione%20del%20data%20types%20C%20Sharp.md) e [operatori](Operatori%20C%20Sharp.md)
3. [Controlli di flusso](Controlli%20di%20flusso%20C%20Sharp.md)
4. [Metodi e proprietà](Metodi%20e%20propriet%C3%A0%20C%20Sharp.md)
5. [Array e matrici](Array%20e%20matrici%20C%20Sharp.md), [ricerca e ordinamento](Ricerca%20e%20ordinamento%20C%20Sharp.md)
6. [Classi e oggetti](Classi%20e%20oggetti%20C%20Sharp.md)
7. [Costruttori e incapsulamento](Costruttori%20incapsulamento%20e%20propriet%C3%A0%20C%20Sharp.md)
8. [Ereditarietà, polimorfismo e interfacce](Ereditariet%C3%A0%20polimorfismo%20interfacce%20C%20Sharp.md)
9. [Stringhe, Math e Random](Stringhe%20Math%20e%20Random%20C%20Sharp.md) · [enum](Enum%20C%20Sharp.md)
10. [Eccezioni](Eccezioni%20C%20Sharp.md), [file di testo](File%20di%20testo%20C%20Sharp.md) e [collezioni](Collezioni%20dinamiche%20C%20Sharp.md)
11. [Programmazione visuale con Windows Forms](Programmazione%20visuale%20Windows%20Forms.md)

## Programma minimo

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Ciao, mondo!");
    }
}
```

Le versioni moderne di C# permettono anche programmi con istruzioni top-level, ma la forma con `Program` e `Main` è utile per comprendere la struttura tradizionale.

## Concetti da distinguere

- Classe: definizione di un tipo.
- Oggetto: istanza concreta di una classe.
- Metodo: operazione eseguibile.
- Proprietà: membro che espone un valore con accessori `get` e/o `set`.
- Campo: dato memorizzato nell'oggetto o nella classe.
- Costruttore: inizializza un nuovo oggetto.

## Fonte di approfondimento

[W3Schools — C# Tutorial](https://www.w3schools.com/cs/index.php)
