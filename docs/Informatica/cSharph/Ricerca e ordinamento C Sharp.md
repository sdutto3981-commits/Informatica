# Ricerca e ordinamento in C#

La ricerca individua uno o più elementi che soddisfano un criterio. L'ordinamento dispone gli elementi secondo una regola, per esempio dal più piccolo al più grande.

## Ricerca lineare

Funziona anche su un array non ordinato. Nel caso peggiore controlla tutti gli `n` elementi: costo temporale `O(n)`.

```csharp
static int RicercaLineare(int[] valori, int cercato)
{
    for (int i = 0; i < valori.Length; i++)
        if (valori[i] == cercato)
            return i;
    return -1; // valore non trovato
}
```

## Ricerca dicotomica

Richiede un array ordinato. A ogni passo dimezza l'intervallo di ricerca, ottenendo costo `O(log n)` nel caso tipico.

```csharp
static int RicercaDicotomica(int[] valori, int cercato)
{
    int sinistra = 0;
    int destra = valori.Length - 1;
    while (sinistra <= destra)
    {
        int medio = sinistra + (destra - sinistra) / 2;
        if (valori[medio] == cercato) return medio;
        if (valori[medio] < cercato) sinistra = medio + 1;
        else destra = medio - 1;
    }
    return -1;
}
```

## Ordinamento per selezione

In ogni iterazione si cerca il minimo della parte non ancora ordinata e lo si porta nella posizione corretta.

```csharp
static void SelectionSort(int[] a)
{
    for (int i = 0; i < a.Length - 1; i++)
    {
        int indiceMin = i;
        for (int j = i + 1; j < a.Length; j++)
            if (a[j] < a[indiceMin]) indiceMin = j;

        int temp = a[i];
        a[i] = a[indiceMin];
        a[indiceMin] = temp;
    }
}
```

Questo algoritmo è semplice ma ha costo `O(n²)`; per grandi quantità di dati si usano algoritmi più efficienti.

## Come verificare

- Array vuoto e array con un solo elemento.
- Elemento presente in prima/ultima posizione.
- Elemento assente.
- Valori ripetuti e valori già ordinati.
- Per la ricerca dicotomica, verifica che l'array sia ordinato prima della chiamata.
