# Introduzione a C#

C# (si legge *C sharp*) è un linguaggio di programmazione general-purpose, tipizzato e multiparadigma, frequentemente utilizzato insieme alla piattaforma .NET.

## Compilazione ed esecuzione

In un progetto .NET moderno, il compilatore traduce il codice sorgente in un assembly intermedio che il runtime .NET esegue e compila ulteriormente quando necessario. Il flusso concreto dipende dagli strumenti e dal tipo di progetto utilizzato.

## Programma minimo

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Ciao, mondo!");
    }
}
```

- `using System;` rende accessibili i nomi del namespace `System` senza doverli qualificare ogni volta.
- `class Program` dichiara una classe.
- `Main` è il punto di ingresso nella forma tradizionale.
- `Console.WriteLine()` scrive testo seguito da una nuova riga.
- `;` termina un'istruzione, mentre `{}` delimitano blocchi.

Le istruzioni top-level sono ammesse nelle versioni moderne del linguaggio, quindi alcuni esempi brevi non richiedono una classe esplicita.

## Convenzioni

I nomi di classi e metodi pubblici seguono comunemente `PascalCase`; variabili locali e parametri `camelCase`. Le convenzioni migliorano la leggibilità ma non sono tutte vincoli imposti dal compilatore.

## Riferimento

[W3Schools — C# Introduction](https://www.w3schools.com/cs/cs_intro.php)
