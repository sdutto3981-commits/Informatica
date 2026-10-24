# Array in C#

Un array contiene un numero determinato di elementi tutti dello stesso tipo. Gli indici partono da `0`; per un array di lunghezza `n`, l'ultimo indice valido è `n - 1`.

## Dichiarazione e inizializzazione

```csharp
int[] numeri = new int[5];          // cinque interi, inizializzati al valore predefinito
int[] voti = { 7, 8, 6, 9 };
```

La dimensione di un array esistente non cambia. `Length` restituisce il numero di elementi.

## Caricamento e visualizzazione

```csharp
int[] v = new int[3];
for (int i = 0; i < v.Length; i++)
{
    Console.Write($"Inserisci v[{i}]: ");
    if (!int.TryParse(Console.ReadLine(), out v[i]))
    {
        Console.WriteLine("Valore non valido.");
        return;
    }
}

for (int i = 0; i < v.Length; i++)
    Console.WriteLine($"v[{i}] = {v[i]}");
```

`TryParse` evita un'eccezione in caso di input non numerico. Per esercizi che richiedono `Convert.ToInt32`, ricordati che l'input non valido può produrre un errore.

## Lettura e modifica

```csharp
int x = v[0];
v[0] = 42;
```

Assegnare a una posizione già occupata sostituisce il valore esistente.

## Copiare un array

L'assegnazione `int[] b = a;` copia il riferimento all'array, non crea una seconda copia indipendente.

```csharp
int[] copia = new int[v.Length];
for (int i = 0; i < v.Length; i++)
    copia[i] = v[i];
```

Oppure, quando consentito dal percorso, si può usare `Array.Copy(v, copia, v.Length)`.

## Errori frequenti

- usare `i <= v.Length` al posto di `i < v.Length`;
- confondere indice e numero di elementi;
- dimenticare di inizializzare una variabile di indice;
- credere che l'assegnazione di un array crei automaticamente una copia;
- usare un array di lunghezza zero senza gestirne il caso.

Per matrici consulta [Matrici](Matrici.md) e per la ricerca [Ricerca e ordinamento](../AlgoritmiFondamentali/Ricerca%20e%20ordinamento.md).
