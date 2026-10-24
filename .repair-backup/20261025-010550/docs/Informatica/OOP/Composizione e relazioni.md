# Composizione e relazioni tra oggetti

La composizione costruisce un oggetto usando altri oggetti come parti del suo stato. È indicata quando una cosa “ha un” componente; l'ereditarietà è indicata quando un tipo “è un” altro tipo.

```csharp
public class Batteria
{
    public int CapacitaWh { get; }
    public Batteria(int capacitaWh) => CapacitaWh = capacitaWh;
}

public class ComputerPortatile
{
    public Batteria Batteria { get; }

    public ComputerPortatile(Batteria batteria)
    {
        Batteria = batteria ?? throw new ArgumentNullException(nameof(batteria));
    }
}
```

Un `ComputerPortatile` **ha una** `Batteria`: non è una batteria. L'oggetto componente può essere passato dall'esterno, rendendo più semplice sostituirlo o testarlo.

## Associazione, aggregazione e composizione

- **Associazione:** due oggetti collaborano o mantengono un riferimento reciproco/esterno.
- **Aggregazione:** relazione parte-tutto in cui la parte può esistere indipendentemente dal contenitore; il significato preciso dipende dal modello adottato.
- **Composizione:** relazione parte-tutto più forte, in cui il ciclo di vita della parte è concettualmente controllato dal tutto.

In C# questi termini non sono parole chiave del linguaggio: sono concetti di progettazione. Si rappresentano tramite riferimenti, proprietà, costruttori e responsabilità del codice.
