# Condizioni e cicli in C#

Le strutture di controllo modificano l'ordine in cui vengono eseguite le istruzioni. La sequenza esegue le istruzioni nell'ordine scritto; la selezione sceglie un ramo; l'iterazione ripete un blocco.

## Selezione: `if`, `else if`, `else`

```csharp
int voto = 7;
if (voto >= 6)
{
    Console.WriteLine("Sufficiente");
}
else
{
    Console.WriteLine("Insufficiente");
}
```

Le condizioni devono essere booleane. In una catena `if / else if`, viene eseguito il primo ramo la cui condizione è vera.

## Selezione multipla: `switch`

```csharp
switch (scelta)
{
    case 1:
        Console.WriteLine("Nuovo");
        break;
    case 2:
        Console.WriteLine("Apri");
        break;
    default:
        Console.WriteLine("Scelta non valida");
        break;
}
```

`break` conclude il ramo. Le forme più recenti di `switch` dipendono dalla versione di C# del progetto.

## Ciclo `for`

Si usa quando il numero di iterazioni è noto o è gestito da un contatore.

```csharp
for (int i = 0; i < 5; i++)
    Console.WriteLine(i); // 0, 1, 2, 3, 4
```

## Cicli `while` e `do-while`

`while` verifica la condizione prima del corpo; `do-while` esegue il corpo almeno una volta.

```csharp
int numero = -1;
while (numero < 0)
{
    Console.Write("Inserisci un numero non negativo: ");
    if (!int.TryParse(Console.ReadLine(), out numero))
        numero = -1;
}
```

## `foreach`, `break` e `continue`

```csharp
int[] valori = { 3, 8, 2 };
foreach (int valore in valori)
    Console.WriteLine(valore);
```

- `break` esce dal ciclo più interno.
- `continue` salta alla successiva iterazione.
- Evita cicli senza una condizione di uscita raggiungibile.

## Errori frequenti

- confondere `=` (assegnazione) con `==` (confronto);
- usare `i <= array.Length` e arrivare a un indice non valido;
- dimenticare di aggiornare il contatore di un `while`;
- usare `&&` quando serve `||`, o viceversa.

Per ogni algoritmo prova almeno un caso normale, uno limite e uno non valido.
