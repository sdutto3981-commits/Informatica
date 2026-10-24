# Array in C#

Un array (`array`) contiene un numero fissato di elementi dello stesso tipo. Gli indici partono da zero: per un array di lunghezza `n` gli indici validi sono `0` … `n - 1`.

```csharp
int[] temperature = { 18, 20, 22, 21 };
Console.WriteLine(temperature[0]);       // 18
Console.WriteLine(temperature.Length);   // 4
```

## Dichiarazione e caricamento

```csharp
int dimensione = 3;
int[] valori = new int[dimensione];

for (int i = 0; i < valori.Length; i++)
{
    Console.Write($"valori[{i}] = ");
    valori[i] = Convert.ToInt32(Console.ReadLine());
}
```

Prima di usare un indice, verifica che sia compreso tra `0` e `Length - 1`. `Length` è il nome corretto della proprietà, non `Lenght`.

## Copia degli array

L'assegnazione `secondo = primo` copia il riferimento all'array, non i suoi elementi. Se serve una copia indipendente si può usare `Array.Copy` o `Clone`:

```csharp
int[] originale = { 2, 4, 6 };
int[] copia = (int[])originale.Clone();
copia[0] = 99;
// originale[0] resta 2.
```

Per scansioni, minimi/massimi, ricerca e ordinamento consulta [Array e matrici](index.md) e [Algoritmi fondamentali](../AlgoritmiFondamentali/index.md).
