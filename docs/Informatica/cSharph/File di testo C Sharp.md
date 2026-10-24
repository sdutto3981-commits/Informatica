# Gestione dei file di testo in C#

Le classi `StreamReader` e `StreamWriter` consentono di leggere e scrivere testo. I file devono essere chiusi correttamente; `using` garantisce il rilascio della risorsa anche se si verifica un'eccezione.

## Scrittura

```csharp
using System.IO;

using (StreamWriter writer = new StreamWriter("dati.txt"))
{
    writer.WriteLine("Prima riga");
    writer.WriteLine("Seconda riga");
}
```

Il costruttore predefinito di `StreamWriter` sovrascrive il file se esiste. Per aggiungere testo puoi usare il parametro `append: true`.

## Lettura riga per riga

```csharp
using System;
using System.IO;

try
{
    using StreamReader reader = new StreamReader("dati.txt");
    string? riga;
    while ((riga = reader.ReadLine()) != null)
        Console.WriteLine(riga);
}
catch (IOException ex)
{
    Console.WriteLine($"Errore di I/O: {ex.Message}");
}
```

La sintassi `string?` richiede l'uso della funzionalità nullable supportata dal progetto. In progetti scolastici con configurazione diversa, la dichiarazione può essere `string riga;` ma il controllo del valore di fine file va comunque mantenuto in modo coerente con il contesto.

## Percorsi e sicurezza

Usa `Path.Combine()` per comporre percorsi ed evita di fidarti direttamente di nomi file inseriti dall'utente. Gestisci file mancanti, permessi insufficienti, errori di encoding e formati inattesi.

## Riferimento

[W3Schools — C# Files](https://www.w3schools.com/cs/cs_files.php)
