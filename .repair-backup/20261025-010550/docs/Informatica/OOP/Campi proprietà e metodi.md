# Campi, proprietà e metodi

## Campi

Un campo memorizza lo stato interno dell'oggetto. Di norma i campi che rappresentano lo stato sono `private` per impedirne la modifica diretta dall'esterno.

```csharp
private int saldoInCentesimi;
```

## Proprietà

Una proprietà espone un valore attraverso `get` e, se consentito, `set`. Può validare il valore o calcolarlo a partire da altri dati.

```csharp
public string Nome { get; private set; }

public int Eta
{
    get => eta;
    set
    {
        if (value < 0)
            throw new ArgumentOutOfRangeException(nameof(value));
        eta = value;
    }
}
private int eta;
```

In una proprietà automatica come `public string Nome { get; set; }`, il compilatore genera un campo di supporto. Non è obbligatorio creare un campo esplicito se non serve una logica particolare.

## Metodi

Un metodo definisce un'operazione eseguibile. Può ricevere parametri e restituire un risultato, oppure essere `void` se non restituisce alcun valore.

```csharp
public decimal ApplicaSconto(decimal prezzo, decimal percentuale)
{
    if (prezzo < 0 || percentuale < 0 || percentuale > 100)
        throw new ArgumentOutOfRangeException();

    return prezzo * (1 - percentuale / 100m);
}
```

Il suffisso `m` indica un letterale `decimal` ed è utile nei calcoli monetari introduttivi. Per valori reali di produzione si devono definire anche regole di arrotondamento.

## Distinzione

- Campo: conserva dati.
- Proprietà: offre accesso controllato a un dato.
- Metodo: esegue un comportamento.

Prosegui con [costruttori e `this`](Costruttori%20e%20this.md).
