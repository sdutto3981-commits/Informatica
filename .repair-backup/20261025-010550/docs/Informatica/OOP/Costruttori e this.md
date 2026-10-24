# Costruttori e `this`

Un **costruttore** inizializza un nuovo oggetto. Ha lo stesso nome della classe e non dichiara un tipo di ritorno. Può ricevere parametri e possono esistere più costruttori con firme diverse (overload).

```csharp
public class Prodotto
{
    public string Nome { get; }
    public decimal Prezzo { get; }

    public Prodotto(string nome, decimal prezzo)
    {
        if (string.IsNullOrWhiteSpace(nome))
            throw new ArgumentException("Il nome è obbligatorio.", nameof(nome));
        if (prezzo < 0)
            throw new ArgumentOutOfRangeException(nameof(prezzo));

        Nome = nome;
        Prezzo = prezzo;
    }
}
```

## `this`

`this` indica l'istanza corrente. È utile per rendere esplicito che si sta accedendo a un membro dell'oggetto e per chiamare un altro costruttore della stessa classe.

```csharp
public class Punto
{
    public int X { get; }
    public int Y { get; }

    public Punto() : this(0, 0) { }

    public Punto(int x, int y)
    {
        this.X = x;
        this.Y = y;
    }
}
```

`Punto()` delega all'altro costruttore, evitando di duplicare l'inizializzazione.

## Costruttore predefinito

Se non viene dichiarato alcun costruttore di istanza, il compilatore fornisce un costruttore senza parametri. Quando si dichiara un costruttore personalizzato, quel costruttore predefinito non viene aggiunto automaticamente.
