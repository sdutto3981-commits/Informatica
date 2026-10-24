# Ereditarietà

L'ereditarietà consente a una classe derivata di specializzare una classe base. In C# si usa `:`. Il rapporto deve esprimere una relazione coerente “è un”, non essere scelto soltanto per riutilizzare del codice.

```csharp
public class Animale
{
    public string Nome { get; }

    public Animale(string nome) => Nome = nome;

    public virtual string Verso() => "Suono generico";
}

public class Cane : Animale
{
    public Cane(string nome) : base(nome) { }

    public override string Verso() => "Bau";
}
```

- `:` indica la classe base o le interfacce implementate.
- `base(nome)` chiama il costruttore della classe base.
- `virtual` permette alle classi derivate di ridefinire un metodo.
- `override` fornisce la nuova implementazione.

C# supporta l'ereditarietà da una sola classe base, ma una classe può implementare più interfacce. Tutte le classi derivano, direttamente o indirettamente, da `object`.

## Attenzione

Una classe derivata eredita i membri accessibili, non i costruttori privati della base. I membri `private` della base non diventano direttamente accessibili nella derivata. Preferisci la composizione quando un oggetto “possiede/usa” un altro oggetto invece di “essere” quel tipo.
