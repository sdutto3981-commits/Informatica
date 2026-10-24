# Metodi e sottoprogrammi in C#

Un metodo è un blocco di codice nominato che svolge un compito preciso. Può ricevere parametri, restituire un valore e venire richiamato da più punti del programma. Scomporre il problema in metodi riduce duplicazioni e rende il codice più facile da verificare.

## Dichiarazione

```csharp
static int Somma(int a, int b)
{
    return a + b;
}

static void StampaTitolo()
{
    Console.WriteLine("Risultato");
}
```

- `static`: il metodo appartiene al tipo, non a una singola istanza.
- `int`: tipo del valore restituito; `void` significa che non viene restituito un valore.
- `Somma`: identificatore del metodo.
- `int a, int b`: parametri formali.
- `return`: termina il metodo e restituisce il risultato, quando richiesto.

Chiamata: `int risultato = Somma(3, 4);`. I valori `3` e `4` sono argomenti (parametri attuali).

## Passaggio dei parametri

In C# i parametri sono passati **per valore** per impostazione predefinita. Per un tipo valore viene copiato il valore; per un tipo riferimento viene copiato il riferimento all'oggetto. In questo secondo caso, il metodo può modificare l'oggetto raggiunto dal riferimento, ma riassegnare il parametro non riassegna la variabile del chiamante.

Per richiedere esplicitamente un passaggio per riferimento si possono usare `ref`, `out` o `in`, rispettandone le regole:

```csharp
static void Incrementa(ref int valore)
{
    valore++;
}

int n = 5;
Incrementa(ref n); // n vale 6
```

`ref` non significa che si debba usare un puntatore C: è una regola del linguaggio C#. `out` richiede che il metodo assegni il parametro prima di terminare; `in` consente un parametro passato per riferimento in sola lettura secondo le regole del linguaggio.

## Ambito delle variabili

Una variabile locale vive nel blocco in cui è dichiarata. Un campo appartiene a un oggetto o al tipo (`static`). Evita di usare campi globali per dati che possono essere passati come parametri: dipendenze esplicite sono più facili da testare.

## Overload

È possibile dichiarare metodi con lo stesso nome e parametri diversi:

```csharp
static int Somma(int a, int b) => a + b;
static double Somma(double a, double b) => a + b;
```

Il solo tipo restituito non basta a distinguere due overload.

Per classi, proprietà, costruttori e principi OOP consulta [Programmazione orientata agli oggetti](../OOP/index.md).
