# File di testo in C#: StreamReader e StreamWriter

I file consentono di conservare dati anche dopo la chiusura del programma. `StreamReader` legge testo e `StreamWriter` scrive testo.

## Lettura riga per riga

```csharp
using System;
using System.IO;

string percorso = "dati.txt";
try
{
    using (StreamReader reader = new StreamReader(percorso))
    {
        string riga;
        while ((riga = reader.ReadLine()) != null)
            Console.WriteLine(riga);
    }
}
catch (IOException ex)
{
    Console.WriteLine("Errore di lettura: " + ex.Message);
}
```

`ReadLine()` restituisce `null` quando non ci sono altre righe. `using` assicura che il file venga chiuso anche quando si verifica un errore.

## Scrittura

```csharp
try
{
    using (StreamWriter writer = new StreamWriter("risultati.txt", false))
    {
        writer.WriteLine("Prima riga");
        writer.WriteLine("Seconda riga");
    }
}
catch (IOException ex)
{
    Console.WriteLine("Errore di scrittura: " + ex.Message);
}
```

Il secondo parametro `false` sovrascrive il file; `true` richiede l'accodamento al contenuto esistente. Usare la sovrascrittura con attenzione.

## Percorsi e dati

- Un percorso relativo è interpretato rispetto alla directory di lavoro del processo.
- Gestisci file mancanti, permessi insufficienti e disco non disponibile.
- Se il formato è strutturato, definisci separatori e regole di conversione e valida i dati letti.
- Evita di presumere che il file contenga sempre righe valide.

In applicazioni Windows Forms la lettura/scrittura non dovrebbe bloccare a lungo l'interfaccia; per esercizi brevi e file piccoli è sufficiente mostrare la corretta gestione delle risorse e degli errori.
