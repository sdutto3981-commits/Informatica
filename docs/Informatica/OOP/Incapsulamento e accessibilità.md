# Incapsulamento e modificatori di accesso

L'incapsulamento protegge lo stato di un oggetto e permette di imporre regole per mantenerlo valido. In genere i campi sono `private`; l'esterno interagisce con proprietà e metodi pubblici.

```csharp
public class ContoBancario
{
    public string Intestatario { get; }
    public decimal Saldo { get; private set; }

    public ContoBancario(string intestatario, decimal saldoIniziale = 0m)
    {
        if (string.IsNullOrWhiteSpace(intestatario))
            throw new ArgumentException("Intestatario obbligatorio.", nameof(intestatario));
        if (saldoIniziale < 0)
            throw new ArgumentOutOfRangeException(nameof(saldoIniziale));

        Intestatario = intestatario;
        Saldo = saldoIniziale;
    }

    public void Versa(decimal importo)
    {
        if (importo <= 0)
            throw new ArgumentOutOfRangeException(nameof(importo));
        Saldo += importo;
    }

    public bool Preleva(decimal importo)
    {
        if (importo <= 0 || importo > Saldo)
            return false;
        Saldo -= importo;
        return true;
    }
}
```

Il chiamante non può assegnare direttamente `Saldo`; deve usare le operazioni che controllano l'input.

## Modificatori principali

| Modificatore | Accessibilità, in sintesi |
|---|---|
| `public` | accessibile da tutti i contesti autorizzati dal tipo |
| `private` | accessibile all'interno del tipo che lo dichiara |
| `protected` | accessibile nel tipo e nei tipi derivati |
| `internal` | accessibile nello stesso assembly |
| `protected internal` | stesso assembly oppure tipi derivati |
| `private protected` | stesso assembly e contesto derivato |

La disponibilità e le sfumature dipendono dal contesto (membri, tipi annidati, assembly). In caso di dubbio, preferire l'accessibilità più restrittiva che soddisfa i requisiti.
