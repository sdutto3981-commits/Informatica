# Array e matrici in C#

Un array contiene un numero fisso di elementi dello stesso tipo. Gli indici iniziano da zero e l'ultimo indice valido è `Length - 1`.

## Array monodimensionale

```csharp
int[] voti = { 7, 8, 6, 9 };
Console.WriteLine(voti[0]);       // 7
Console.WriteLine(voti.Length);  // 4

for (int i = 0; i < voti.Length; i++)
    Console.WriteLine($"voti[{i}] = {voti[i]}");
```

Lunghezza fissa non significa contenuto immutabile: gli elementi possono essere aggiornati.

## Ricerca del massimo

```csharp
int[] valori = { 4, 7, 2, 9 };
int massimo = valori[0];
for (int i = 1; i < valori.Length; i++)
    if (valori[i] > massimo)
        massimo = valori[i];
Console.WriteLine(massimo); // 9
```

Prima di leggere `valori[0]`, verifica che l'array non sia vuoto.

## Matrici bidimensionali

Una matrice rettangolare può essere dichiarata con `[,]`.

```csharp
int[,] matrice = {
    { 1, 2, 3 },
    { 4, 5, 6 }
};

int righe = matrice.GetLength(0);
int colonne = matrice.GetLength(1);
for (int r = 0; r < righe; r++)
{
    for (int c = 0; c < colonne; c++)
        Console.Write(matrice[r, c] + " ");
    Console.WriteLine();
}
```

- `GetLength(0)` restituisce il numero di righe.
- `GetLength(1)` restituisce il numero di colonne.
- Ogni coppia di indici deve essere dentro i limiti.

## Copia e assegnazione

```csharp
int[] originale = { 1, 2, 3 };
int[] copia = new int[originale.Length];
for (int i = 0; i < originale.Length; i++)
    copia[i] = originale[i];
```

L'istruzione `int[] b = a;` non duplica i valori: copia il riferimento all'array, quindi `a` e `b` indicano lo stesso oggetto.

## Errori frequenti

- confondere indice e numero di elementi;
- utilizzare `<= Length` anziché `< Length`;
- non inizializzare una variabile di indice;
- assumere che assegnare un array a un altro crei una copia indipendente.

Vedi anche [la pagina sugli array](../ArrayMatrici/Array.md), [le matrici](../ArrayMatrici/Matrici.md) e [ricerca e ordinamento](Ricerca%20e%20ordinamento%20C%20Sharp.md).
