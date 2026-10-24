# Enumerazioni (`enum`) in C#

Un'enumerazione definisce un insieme di costanti nominate e rende più leggibili gli stati possibili di un dato.

```csharp
enum StatoPartita
{
    InCorso,
    Vittoria,
    Sconfitta
}

StatoPartita stato = StatoPartita.InCorso;

if (stato == StatoPartita.Vittoria)
    Console.WriteLine("Partita conclusa");
```

Per impostazione predefinita, i membri ricevono valori interi a partire da zero, ma si possono assegnare valori espliciti quando serve. Il tipo sottostante predefinito è `int`.

## `switch` con enum

```csharp
switch (stato)
{
    case StatoPartita.InCorso:
        Console.WriteLine("Continua");
        break;
    case StatoPartita.Vittoria:
        Console.WriteLine("Hai vinto");
        break;
    case StatoPartita.Sconfitta:
        Console.WriteLine("Hai perso");
        break;
    default:
        Console.WriteLine("Stato non gestito");
        break;
}
```

Le enumerazioni evitano di usare numeri arbitrari o stringhe magiche per rappresentare stati. Se i valori vengono salvati o inviati in rete, stabilisci un formato stabile invece di dipendere inconsapevolmente dall'ordine dei membri.

## Riferimento

[W3Schools — C# Enums](https://www.w3schools.com/cs/cs_enums.php)
