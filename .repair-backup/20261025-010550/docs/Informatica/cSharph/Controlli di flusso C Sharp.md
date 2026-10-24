# Controlli di flusso in C#

I costrutti di controllo scelgono quali istruzioni eseguire e quante volte ripeterle.

## Selezione

```csharp
if (voto >= 6)
{
    Console.WriteLine("Sufficiente");
}
else
{
    Console.WriteLine("Insufficiente");
}
```

`else if` gestisce condizioni successive; `switch` è utile per confrontare un valore con più casi.

```csharp
switch (giorno)
{
    case 1:
        Console.WriteLine("Lunedì");
        break;
    case 2:
        Console.WriteLine("Martedì");
        break;
    default:
        Console.WriteLine("Altro giorno");
        break;
}
```

## Iterazione

```csharp
for (int i = 0; i < 5; i++)
    Console.WriteLine(i);

int tentativi = 0;
while (tentativi < 3)
    tentativi++;

do
{
    Console.WriteLine("Eseguito almeno una volta");
} while (false);
```

- `for`: spesso adatto a contatori e scansioni.
- `while`: controlla la condizione prima di ogni iterazione.
- `do...while`: esegue il corpo almeno una volta.
- `foreach`: attraversa gli elementi di una collezione.
- `break`: interrompe il ciclo; `continue`: passa all'iterazione successiva.

Controlla sempre che la condizione possa diventare falsa e che gli indici restino nei limiti.

## Riferimento

[W3Schools — C# Conditions](https://www.w3schools.com/cs/cs_conditions.php) · [C# Loops](https://www.w3schools.com/cs/cs_loops.php)
