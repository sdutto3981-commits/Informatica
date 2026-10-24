# Array in C#

Un array conserva un numero definito di elementi dello stesso tipo. Gli indici partono da `0`; se l'array ha `Length == n`, gli indici validi sono da `0` a `n - 1`.

## Dichiarazione e inizializzazione

```csharp
int[] numeri = new int[5];
int[] voti = { 7, 8, 6, 9 };
```

Per dimensioni determinate a runtime:

```csharp
Console.Write("Quanti elementi? ");
if (!int.TryParse(Console.ReadLine(), out int dimensione) || dimensione < 1)
{
    Console.WriteLine("Inserire un intero positivo.");
    return;
}

int[] valori = new int[dimensione];
for (int i = 0; i < valori.Length; i++)
{
    Console.Write($"valori[{i}] = ");
    while (!int.TryParse(Console.ReadLine(), out valori[i]))
        Console.Write("Valore non valido; riprova: ");
}
```

## Scansione e modifica

```csharp
for (int i = 0; i < valori.Length; i++)
    Console.WriteLine($"valori[{i}] = {valori[i]}");
```

Assegnare `valori[i] = nuovoValore;` sostituisce il contenuto di quella posizione.

## Copiare un array

L'assegnazione `int[] b = a;` copia il riferimento, quindi `a` e `b` indicano lo stesso array. Per ottenere una copia indipendente:

```csharp
int[] copia = (int[])valori.Clone();
// In alternativa: int[] copia = valori.ToArray(); con using System.Linq;
```

Oppure, per capire il processo, si può copiare elemento per elemento:

```csharp
int[] copiaManuale = new int[valori.Length];
for (int i = 0; i < valori.Length; i++)
    copiaManuale[i] = valori[i];
```

## Errori comuni

- Usare `Length` invece di `Length`.
- Accedere a `array[array.Length]`: è fuori dai limiti.
- Confondere la copia del riferimento con la copia degli elementi.
- Usare un indice senza verificare che rientri nell'intervallo valido.

Per array multidimensionali consulta [Matrici](Matrici.md); per algoritmi consulta [Ricerca e ordinamento](../AlgoritmiFondamentali/Ricerca%20e%20ordinamento.md).
