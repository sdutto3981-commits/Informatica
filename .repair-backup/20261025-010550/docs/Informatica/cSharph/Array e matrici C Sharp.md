# Array e matrici in C#

Un array contiene un numero fissato di elementi dello stesso tipo. Gli indici partono da zero; per un array di lunghezza `n`, gli indici validi vanno da `0` a `n - 1`.

```csharp
int[] numeri = { 4, 7, 2, 9 };
Console.WriteLine(numeri[0]);
numeri[1] = 10;

for (int i = 0; i < numeri.Length; i++)
    Console.WriteLine($"numeri[{i}] = {numeri[i]}");
```

`Length` restituisce il numero totale di elementi. Se si accede a un indice non valido, il programma genera un'eccezione `IndexOutOfRangeException`.

## Creazione e input

```csharp
Console.Write("Dimensione: ");
if (!int.TryParse(Console.ReadLine(), out int n) || n < 0)
{
    Console.WriteLine("Dimensione non valida");
    return;
}

int[] valori = new int[n];
for (int i = 0; i < valori.Length; i++)
{
    Console.Write($"Elemento {i}: ");
    if (!int.TryParse(Console.ReadLine(), out valori[i]))
    {
        Console.WriteLine("Valore non valido");
        return;
    }
}
```

## Copiare un array

L'assegnazione `b = a` copia il riferimento allo stesso array, non crea una seconda sequenza indipendente. Per copiare i valori puoi usare un ciclo o `Array.Copy`.

```csharp
int[] copia = new int[numeri.Length];
Array.Copy(numeri, copia, numeri.Length);
```

## Matrici

```csharp
int[,] matrice = new int[2, 3];
matrice[0, 1] = 5;

for (int r = 0; r < matrice.GetLength(0); r++)
    for (int c = 0; c < matrice.GetLength(1); c++)
        Console.WriteLine(matrice[r, c]);
```

`GetLength(0)` restituisce il numero di righe e `GetLength(1)` quello delle colonne in una matrice bidimensionale.

## Riferimento

[W3Schools — C# Arrays](https://www.w3schools.com/cs/cs_arrays.php)
