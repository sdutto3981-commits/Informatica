# Ricerca e ordinamento

Gli algoritmi di ricerca trovano elementi; quelli di ordinamento dispongono gli elementi secondo una relazione (per esempio crescente). La scelta dipende da dimensione dei dati, ordine iniziale, memoria disponibile e numero di operazioni.

## Ordinamento per selezione

A ogni passaggio individua il minimo nella parte non ordinata e lo scambia con il primo elemento di quella parte.

```csharp
static void SelectionSort(int[] valori)
{
    for (int i = 0; i < valori.Length - 1; i++)
    {
        int indiceMinimo = i;
        for (int j = i + 1; j < valori.Length; j++)
            if (valori[j] < valori[indiceMinimo])
                indiceMinimo = j;

        if (indiceMinimo != i)
            (valori[i], valori[indiceMinimo]) = (valori[indiceMinimo], valori[i]);
    }
}
```

Il costo temporale è `O(n²)` sia in caso medio sia nel caso peggiore; l'algoritmo usa memoria aggiuntiva costante. In genere non è stabile.

## Ricerca lineare e binaria

- Lineare: funziona senza ordinamento, costo peggiore `O(n)`.
- Binaria: richiede ordinamento, costo peggiore `O(log n)`.

Consulta [Algoritmi di ricerca](Algoritmi%20ricerca.md) per le implementazioni complete.
