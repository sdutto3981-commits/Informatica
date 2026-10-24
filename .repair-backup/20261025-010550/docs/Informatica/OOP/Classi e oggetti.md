# Classi e oggetti

Una **classe** è una definizione di un tipo: descrive i dati e le operazioni disponibili. Un **oggetto** è un'istanza di quel tipo. L'operatore `new` crea un'istanza e richiama un costruttore.

```csharp
public class Studente
{
    public string Nome { get; set; }
    public int Anno { get; set; }

    public Studente(string nome, int anno)
    {
        Nome = nome;
        Anno = anno;
    }

    public string Descrizione()
    {
        return $"{Nome}, anno {Anno}";
    }
}

Studente s1 = new Studente("Ada", 3);
Studente s2 = new Studente("Alan", 4);
Console.WriteLine(s1.Descrizione());
```

` s1` e `s2` fanno riferimento a oggetti distinti: modificare lo stato di uno non modifica automaticamente l'altro.

## Tipo riferimento

In C#, una variabile di tipo classe contiene un riferimento all'oggetto, non una copia automatica di tutti i suoi campi. Assegnare `Studente s3 = s1;` copia il riferimento: `s1` e `s3` indicano lo stesso oggetto. Questo comportamento è diverso da quello dei tipi valore come `int` e, in generale, `struct`.

## Convenzioni

- Nomi di classi e metodi in `PascalCase`, per esempio `GestioneOrdini`.
- Variabili locali e parametri in `camelCase`, per esempio `nomeStudente`.
- Una classe pubblica di norma è collocata in un file con lo stesso nome.
- Evita classi che contengono dati non correlati o troppi compiti diversi.

Prosegui con [campi, proprietà e metodi](Campi%20proprietà%20e%20metodi.md).
