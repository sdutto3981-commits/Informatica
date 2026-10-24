# Ricerca e ordinamento

Un algoritmo di ricerca individua uno o più elementi che rispettano una condizione. La strategia dipende dal fatto che i dati siano ordinati e che un valore possa comparire più volte.

## Ricerca lineare

Scorre gli elementi uno alla volta. Funziona anche con dati non ordinati.

```csharp
static int RicercaLineare(int[] v, int x)
{
    for (int i = 0; i < v.Length; i++)
        if (v[i] == x) return i;
    return -1;
}
```

Restituisce il primo indice trovato oppure `-1` se il valore non è presente. Nel caso peggiore esegue un numero di confronti proporzionale a `n`, cioè `O(n)`.

## Ricerca dicotomica (binaria)

Richiede un array ordinato. A ogni passaggio restringe l'intervallo alla metà che può contenere il valore.

```csharp
static int RicercaBinaria(int[] v, int x)
{
    int sinistra = 0;
    int destra = v.Length - 1;

    while (sinistra <= destra)
    {
        int medio = sinistra + (destra - sinistra) / 2;
        if (v[medio] == x) return medio;
        if (v[medio] < x) sinistra = medio + 1;
        else destra = medio - 1;
    }
    return -1;
}
```

La complessità è `O(log n)` nel caso tipico/peggiore per la ricerca binaria. Non applicarla a dati non ordinati. Se i duplicati sono possibili, questa versione restituisce un'occorrenza, non necessariamente la prima.

## Trovare tutte le occorrenze

Per trovare tutte le posizioni in un array non ordinato, continua la scansione anche dopo una corrispondenza:

```csharp
for (int i = 0; i < v.Length; i++)
    if (v[i] == x)
        Console.WriteLine($"Trovato all'indice {i}");
```

## Ordinamento

L'ordinamento mette gli elementi in ordine crescente o decrescente. Gli algoritmi affrontati in classe possono includere:

- **Bubble sort:** confronta elementi adiacenti e scambia quelli fuori ordine; semplice ma `O(n²)` nel caso medio/peggiore.
- **Selection sort:** seleziona a ogni passaggio il minimo della parte non ordinata; `O(n²)` confronti.
- **Insertion sort:** inserisce ogni elemento nella posizione giusta della parte ordinata; `O(n²)` nel caso medio/peggiore, ma efficiente su piccoli array quasi ordinati.

Verifica con array vuoti, un solo elemento, valori già ordinati, ordine inverso e duplicati. Per un algoritmo di ordinamento non modificare l'array originale se il compito richiede di conservarlo: fai una copia esplicita.
