# Metodi e proprietà in C#

Un metodo esegue un'operazione; una proprietà espone un valore attraverso gli accessori `get` e/o `set`. Non è corretto definire una proprietà semplicemente come un'azione senza parentesi.

```csharp
class Prodotto
{
    public string Nome { get; set; } = "Senza nome";
    public decimal Prezzo { get; private set; }

    public Prodotto(string nome, decimal prezzo)
    {
        Nome = nome;
        Prezzo = prezzo;
    }

    public decimal PrezzoConIva(decimal aliquota)
    {
        return Prezzo * (1 + aliquota / 100m);
    }
}
```

`Nome` è una proprietà auto-implementata. `Prezzo` può essere letto dall'esterno ma modificato soltanto dall'interno della classe. `PrezzoConIva` è un metodo perché rappresenta un calcolo e può ricevere un parametro.

## Proprietà calcolate

```csharp
public decimal PrezzoConSconto => Prezzo * 0.9m;
```

Una proprietà calcolata può derivare il valore da altri dati senza memorizzarlo separatamente.

## Distinzione tra campi, proprietà e metodi

- Campo: conserva direttamente un dato.
- Proprietà: controlla o espone l'accesso a un dato.
- Metodo: esegue un comportamento.

Le proprietà sono spesso preferibili ai campi pubblici perché consentono di cambiare l'implementazione interna senza cambiare l'interfaccia di uso.

## Riferimento

[W3Schools — C# Properties](https://www.w3schools.com/cs/cs_properties.php)
