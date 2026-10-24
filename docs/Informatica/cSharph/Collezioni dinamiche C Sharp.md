# Collezioni dinamiche in C#

Un array ha lunghezza fissa. Una collezione dinamica consente di aggiungere e rimuovere elementi durante l'esecuzione. Nel programma introduttivo è particolarmente utile `List<T>`.

## Creare e utilizzare una lista

```csharp
using System.Collections.Generic;

List<string> nomi = new List<string>();
nomi.Add("Ada");
nomi.Add("Alan");
nomi.Add("Grace");

foreach (string nome in nomi)
    Console.WriteLine(nome);

nomi.Remove("Alan");
Console.WriteLine(nomi.Count);
```

`T` rappresenta il tipo degli elementi: `List<int>` conserva interi, `List<string>` conserva stringhe. `Count` restituisce il numero di elementi attualmente presenti.

## Operazioni utili

- `Add(elemento)`: aggiunge in fondo.
- `Remove(elemento)`: rimuove una corrispondenza, se presente.
- `RemoveAt(indice)`: rimuove l'elemento in una posizione valida.
- `Contains(elemento)`: controlla la presenza.
- `Clear()`: rimuove tutti gli elementi.
- `Count`: numero di elementi.

## Lista e array a confronto

| Array | `List<T>` |
|---|---|
| Lunghezza fissa | Dimensione che cresce o diminuisce |
| Accesso per indice | Accesso per indice e metodi di modifica |
| Utile quando la dimensione è nota | Utile quando gli elementi variano |

Quando si rimuovono elementi durante un ciclo `for`, gli indici successivi possono spostarsi: procedi con attenzione oppure usa una strategia che non salti elementi.
