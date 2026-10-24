# Algoritmi di ricerca

La ricerca serve a stabilire se un valore è presente in una sequenza e, quando richiesto, a restituire una o più posizioni.

## Ricerca lineare

Funziona su vettori sia ordinati sia non ordinati. Esamina gli elementi uno alla volta fino a trovare il valore o terminare il vettore.

```csharp
static int RicercaLineare(int[] valori, int cercato)
{
    for (int i = 0; i < valori.Length; i++)
        if (valori[i] == cercato)
            return i;
    return -1;
}
```

La funzione restituisce l'indice della prima occorrenza oppure `-1` se il valore non è presente. Il tempo di esecuzione nel caso peggiore cresce linearmente con il numero di elementi: `O(n)`.

## Cercare tutte le occorrenze

```csharp
static List<int> CercaTutte(int[] valori, int cercato)
{
    List<int> posizioni = new List<int>();
    for (int i = 0; i < valori.Length; i++)
        if (valori[i] == cercato)
            posizioni.Add(i);
    return posizioni;
}
```

Aggiungere `using System.Collections.Generic;` per utilizzare `List<int>`. Una lista vuota significa che non sono state trovate occorrenze.

## Ricerca dicotomica (binaria)

Richiede che il vettore sia **ordinato**. A ogni iterazione confronta il valore centrale e scarta metà dell'intervallo.

```csharp
static int RicercaBinaria(int[] valori, int cercato)
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

Costo nel caso peggiore: `O(log n)`. Se ci sono duplicati, la funzione restituisce una delle occorrenze; per ottenere la prima o tutte, occorre adattare l'algoritmo.

## Scelta del metodo

| Situazione | Metodo |
|---|---|
| Vettore non ordinato | ricerca lineare |
| Vettore piccolo o ricerca singola senza ordinamento | spesso lineare è più semplice |
| Vettore ordinato e molte ricerche | può convenire la ricerca binaria |
| Servono tutte le posizioni | scansione completa |

La ricerca binaria non può essere applicata correttamente a un vettore non ordinato senza prima ordinare i dati.
