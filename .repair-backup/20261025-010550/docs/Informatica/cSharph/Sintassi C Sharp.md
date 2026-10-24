# Sintassi di C#

C# distingue maiuscole e minuscole: `nome`, `Nome` e `NOME` sono identificatori differenti.

```csharp
using System;

class Program
{
    static void Main()
    {
        int contatore = 0;
        contatore++;
        Console.WriteLine($"Valore: {contatore}");
    }
}
```

## Regole essenziali

- Termina le istruzioni con `;`.
- Delimita blocchi con `{` e `}`.
- I commenti su una riga iniziano con `//`; quelli su più righe con `/* ... */`.
- Gli identificatori non possono iniziare con una cifra e non devono coincidere con parole riservate, salvo l'uso del prefisso `@` in casi specifici.
- Usa parentesi per rendere chiara l'ordine delle operazioni quando la precedenza può creare dubbi.
- Le stringhe sono tra doppi apici (`"testo"`), mentre un `char` usa apici singoli (`'A'`).

## Interpolazione di stringhe

```csharp
string nome = "Ada";
int eta = 20;
Console.WriteLine($"{nome} ha {eta} anni.");
```

L'interpolazione inserisce espressioni tra `{}` dentro una stringa preceduta da `$`.

## Commenti e documentazione

```csharp
// Commento breve
/* Commento su più righe */
/// <summary>Calcola la somma di due interi.</summary>
static int Somma(int a, int b) => a + b;
```

I commenti XML `///` possono essere usati per generare documentazione dei membri.

## Riferimento

[W3Schools — C# Syntax](https://www.w3schools.com/cs/cs_syntax.php)
