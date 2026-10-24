# Esercizio OOP: gestione di una piccola biblioteca

## Requisiti

Realizzare un modello minimale che rappresenti libri e una biblioteca. La biblioteca deve poter aggiungere libri, cercarli per codice e stamparne l'elenco. L'esercizio usa classi, proprietà, costruttori, incapsulamento e collezioni.

## Implementazione di base

```csharp
using System;
using System.Collections.Generic;

public class Libro
{
    public string Codice { get; }
    public string Titolo { get; }
    public string Autore { get; }
    public bool InPrestito { get; private set; }

    public Libro(string codice, string titolo, string autore)
    {
        if (string.IsNullOrWhiteSpace(codice))
            throw new ArgumentException("Il codice è obbligatorio.", nameof(codice));
        if (string.IsNullOrWhiteSpace(titolo))
            throw new ArgumentException("Il titolo è obbligatorio.", nameof(titolo));
        if (string.IsNullOrWhiteSpace(autore))
            throw new ArgumentException("L'autore è obbligatorio.", nameof(autore));

        Codice = codice;
        Titolo = titolo;
        Autore = autore;
    }

    public bool PrendiInPrestito()
    {
        if (InPrestito) return false;
        InPrestito = true;
        return true;
    }

    public bool Restituisci()
    {
        if (!InPrestito) return false;
        InPrestito = false;
        return true;
    }

    public override string ToString() => $"{Codice}: {Titolo} — {Autore}";
}

public class Biblioteca
{
    private readonly List<Libro> libri = new List<Libro>();

    public void Aggiungi(Libro libro)
    {
        if (libro is null) throw new ArgumentNullException(nameof(libro));
        if (Cerca(libro.Codice) is not null)
            throw new InvalidOperationException("Codice già presente.");
        libri.Add(libro);
    }

    public Libro? Cerca(string codice)
    {
        return libri.Find(l => string.Equals(
            l.Codice, codice, StringComparison.OrdinalIgnoreCase));
    }

    public void StampaCatalogo()
    {
        foreach (Libro libro in libri)
            Console.WriteLine($"{libro} {(libro.InPrestito ? "(in prestito)" : "(disponibile)")}");
    }
}
```

## Cosa osservare

- I dati identificativi sono in sola lettura dall'esterno.
- `InPrestito` si modifica solo tramite metodi che controllano lo stato.
- `Biblioteca` contiene una `List<Libro>`: è composizione/associazione, non ereditarietà.
- La ricerca restituisce `null` se non trova il codice. Il tipo `Libro?` richiede il contesto nullable previsto dal progetto; nei progetti più vecchi, adeguare l'annotazione alla versione C# utilizzata.

- Un'applicazione reale richiederebbe persistenza su file/database, utenti, scadenze e test automatici: qui lo scopo è didattico.

## Estensioni

1. Implementa una classe base astratta `ElementoCatalogo`.
2. Aggiungi un'interfaccia `IPrestabile`.
3. Scrivi test per codice duplicato, libro già in prestito e restituzione senza prestito.
4. Salva e ricarica il catalogo da un file, gestendo gli errori.
