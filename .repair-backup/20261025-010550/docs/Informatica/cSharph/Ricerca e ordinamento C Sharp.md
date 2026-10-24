# Ricerca e ordinamento in C#

## Ricerca lineare

Esamina gli elementi uno alla volta e termina quando trova il valore o finisce l'array. Funziona anche su dati non ordinati.

```csharp
static int RicercaLineare(int[] valori, int cercato)
{
    for (int i = 0; i < valori.Length; i++)
        if (valori[i] == cercato) return i;
    return -1;
}
```

`-1` indica che il valore non è stato trovato. La ricerca lineare richiede nel caso peggiore un numero di confronti proporzionale alla lunghezza, cioè `O(n)`.

## Ricerca dicotomica

Funziona solo su una sequenza ordinata in modo compatibile con il confronto. A ogni passo restringe l'intervallo a metà.

```csharp
static int RicercaBinaria(int[] valori, int cercato)
{
    int sinistra = 0;
    int destra = valori.Length - 1;

    while (sinistra <= destra)
    {
        int centro = sinistra + (destra - sinistra) / 2;
        if (valori[centro] == cercato) return centro;
        if (valori[centro] < cercato) sinistra = centro + 1;
        else destra = centro - 1;
    }
    return -1;
}
```

La complessità è `O(log n)` nel caso peggiore, ma prima di usarla l'array deve essere ordinato.

## Ordinamento

I metodi didattici come bubble sort, selection sort e insertion sort permettono di comprendere confronti e scambi. Per codice reale con array di tipi standard, valuta `Array.Sort()`.

```csharp
int[] valori = { 8, 3, 6, 1 };
Array.Sort(valori);
```

## Riferimento

[W3Schools — C# Arrays](https://www.w3schools.com/cs/cs_arrays.php)
