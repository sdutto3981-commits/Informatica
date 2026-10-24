# Membri e classi `static`

Un membro di istanza appartiene a una specifica istanza; un membro `static` appartiene al tipo e viene condiviso dalle sue istanze. Un membro statico non può accedere direttamente a un membro di istanza perché non dispone di un oggetto corrente (`this`).

```csharp
public class Conversioni
{
    public static double CelsiusAFahrenheit(double celsius)
    {
        return celsius * 9 / 5 + 32;
    }
}

Console.WriteLine(Conversioni.CelsiusAFahrenheit(20));
```

Si chiama il metodo tramite il nome del tipo, senza creare un oggetto.

## Campo statico

```csharp
public class Sessione
{
    public static int NumeroCreate { get; private set; }

    public Sessione()
    {
        NumeroCreate++;
    }
}
```

Il contatore è condiviso tra le istanze. In applicazioni concorrenti, un aggiornamento condiviso può richiedere sincronizzazione.

## Quando usare `static`

Usalo quando l'operazione non dipende dallo stato di una singola istanza oppure quando un valore è veramente condiviso. Evita di trasformare ogni dato in statico: stato globale condiviso rende il codice più difficile da testare e comprendere.
