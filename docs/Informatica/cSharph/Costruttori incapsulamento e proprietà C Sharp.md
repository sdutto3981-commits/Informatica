# Costruttori, incapsulamento e proprietà C#

## Costruttore

Un costruttore ha lo stesso nome della classe e non dichiara un tipo restituito. Inizializza i dati necessari a creare un oggetto coerente.

```csharp
class Conto
{
    public string Intestatario { get; }
    public decimal Saldo { get; private set; }

    public Conto(string intestatario, decimal saldoIniziale)
    {
        if (saldoIniziale < 0) throw new ArgumentOutOfRangeException(nameof(saldoIniziale));
        Intestatario = intestatario;
        Saldo = saldoIniziale;
    }

    public void Versa(decimal importo)
    {
        if (importo <= 0) throw new ArgumentOutOfRangeException(nameof(importo));
        Saldo += importo;
    }
}
```

## Incapsulamento

L'incapsulamento protegge lo stato interno e fa passare le modifiche attraverso regole controllate. Nell'esempio, il saldo non può essere assegnato liberamente da codice esterno; si modifica tramite `Versa`, che verifica l'importo.

## Modificatori di accesso

- `public`: accessibile da contesti esterni consentiti.
- `private`: visibile soltanto all'interno del tipo che lo dichiara.
- `protected`: accessibile nel tipo e nei tipi derivati.
- `internal`: accessibile all'interno dello stesso assembly.
- `protected internal` e `private protected`: combinazioni con regole di accesso più specifiche.

## Proprietà auto-implementate

```csharp
public string Nome { get; set; }
public DateTime DataCreazione { get; } = DateTime.Now;
public string Codice { get; init; } = "";
```

`init` consente l'assegnazione in fase di inizializzazione dell'oggetto nelle versioni che supportano questa funzionalità. Versione del linguaggio e progetto scolastico possono influire sulla sintassi disponibile.

## Riferimento

[W3Schools — C# Constructors](https://www.w3schools.com/cs/cs_constructors.php) · [C# Access Modifiers](https://www.w3schools.com/cs/cs_access_modifiers.php)
