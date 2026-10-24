# Metodi e proprietà in C#

**Metodi** e **proprietà** sono membri di un tipo, ma svolgono ruoli diversi.

## Metodi

Un metodo rappresenta un'operazione e normalmente si richiama con parentesi tonde. Può accettare parametri e restituire un valore.

```csharp
static int Raddoppia(int valore)
{
    return valore * 2;
}

int risultato = Raddoppia(7);
```

## Proprietà

Una proprietà espone un dato attraverso gli accessor `get` e/o `set`. Non è semplicemente “un'azione”: rappresenta una caratteristica leggibile e/o modificabile dell'oggetto.

```csharp
public string Nome { get; set; }
public int AnnoNascita { get; private set; }
```

Una proprietà può essere automatica oppure contenere una logica di validazione. Si accede normalmente senza parentesi: `studente.Nome`.

## Metodo o proprietà?

Usa una proprietà per esporre uno stato o un valore calcolato senza effetti collaterali inattesi. Usa un metodo per un'azione, per elaborazioni con argomenti o quando l'operazione può avere effetti collaterali. Per il quadro completo consulta [campi, proprietà e metodi](../OOP/Campi%20proprietà%20e%20metodi.md).
