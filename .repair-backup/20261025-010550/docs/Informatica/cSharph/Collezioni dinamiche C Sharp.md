# Collezioni dinamiche in C#

Un array ha lunghezza fissa; una collezione dinamica consente di aggiungere e rimuovere elementi. `List<T>` memorizza una sequenza tipizzata e ridimensionabile.

```csharp
using System.Collections.Generic;

List<string> nomi = new List<string>();
nomi.Add("Ada");
nomi.Add("Luca");
nomi.Remove("Ada");

foreach (string nome in nomi)
    Console.WriteLine(nome);
```

## Metodi e proprietà utili

- `Add`: aggiunge un elemento.
- `Remove`: rimuove la prima occorrenza corrispondente e restituisce un booleano.
- `Contains`: verifica se è presente un elemento.
- `Count`: numero corrente di elementi.
- `Clear`: rimuove tutti gli elementi.
- `Sort`: ordina secondo il comparatore predefinito quando il tipo lo supporta.

## Altre strutture

- `Dictionary<TKey, TValue>`: associa chiavi univoche a valori.
- `Queue<T>`: coda FIFO (primo inserito, primo estratto).
- `Stack<T>`: pila LIFO (ultimo inserito, primo estratto).
- `HashSet<T>`: insieme senza duplicati secondo le regole di uguaglianza.

Scegli la struttura in base alle operazioni che devi eseguire e alle caratteristiche dei dati.

## Riferimento

[W3Schools — C# Arrays](https://www.w3schools.com/cs/cs_arrays.php) · [Microsoft — Collections](https://learn.microsoft.com/dotnet/standard/collections/)
