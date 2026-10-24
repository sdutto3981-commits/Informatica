# Metodi e sottoprogrammi in C#

Un metodo raggruppa istruzioni che svolgono un compito definito. Favorisce il riuso, la leggibilità, il test e la scomposizione top-down del problema.

## Struttura

```csharp
static tipoRitorno NomeMetodo(tipo parametro1, tipo parametro2)
{
    // istruzioni
    return valore;
}
```

Se il metodo non restituisce un valore si usa `void` e non si restituisce un risultato con `return` (è comunque possibile usare `return;` per terminare il metodo).

```csharp
static int Somma(int a, int b)
{
    return a + b;
}

static void Main()
{
    int risultato = Somma(3, 4);
    Console.WriteLine(risultato); // 7
}
```

- **Parametri formali:** quelli nella dichiarazione del metodo (`a`, `b`).
- **Argomenti attuali:** i valori o le variabili passati nella chiamata (`3`, `4`).
- **Tipo restituito:** deve corrispondere al valore restituito su ogni percorso che termina normalmente.
- **Overload:** più metodi possono avere lo stesso nome se la firma dei parametri è diversa.

## Passaggio dei parametri

In C#, i parametri vengono passati per valore per impostazione predefinita. Per i tipi valore viene copiata la variabile; per i tipi riferimento viene copiata la *referenza* all'oggetto. Quindi un metodo può modificare lo stato dell'oggetto referenziato, ma riassegnare il parametro non riassegna la variabile del chiamante.

```csharp
static void Incrementa(int x) { x++; }
int n = 5;
Incrementa(n);
// n è ancora 5
```

Con `ref` il metodo riceve un parametro per riferimento alla variabile del chiamante; la variabile deve essere inizializzata prima della chiamata. Con `out` il metodo deve assegnare un valore prima di terminare normalmente.

```csharp
static void Incrementa(ref int x) { x++; }
int n = 5;
Incrementa(ref n);
// n ora vale 6
```

Questa semantica è diversa dai puntatori del linguaggio C: in C# normalmente non si gestiscono indirizzi manualmente e un array non è semplicemente un puntatore.

## Variabili locali e ambito

Una variabile locale esiste nel blocco in cui è dichiarata ed è accessibile secondo le regole di scope. Un campo di classe può essere condiviso tra metodi della stessa istanza. Preferisci la variabile con l'ambito più piccolo sufficiente al compito.

## Progettazione top-down

1. Descrivi il risultato richiesto.
2. Dividi il problema in compiti più piccoli.
3. Definisci metodi con responsabilità chiare e nomi descrittivi.
4. Passa i dati necessari tramite parametri e restituisci i risultati.
5. Prova ogni metodo con input normali e casi limite.
