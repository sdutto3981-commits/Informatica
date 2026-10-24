# Programmazione visuale con Windows Forms

Windows Forms è un framework .NET per creare applicazioni desktop con finestre e controlli. Una `Form` rappresenta una finestra; i controlli includono `Button`, `Label`, `TextBox`, `CheckBox`, `ComboBox` e altri componenti.

## Proprietà, metodi ed eventi

- **Proprietà:** descrivono lo stato o l'aspetto, per esempio `Text`, `Name`, `Enabled`, `Visible`, `Width`.
- **Metodi:** eseguono operazioni, per esempio `Show()` o `Focus()`.
- **Eventi:** notificano azioni, per esempio `Click`, `TextChanged`, `FormClosing`.

Il programma resta in attesa di eventi e richiama il gestore associato quando l'evento si verifica.

## Esempio: pulsante e contatore

Supponendo che la form contenga `btnIncrementa` e `lblContatore`:

```csharp
public partial class Form1 : Form
{
    private int contatore = 0;

    public Form1()
    {
        InitializeComponent();
        lblContatore.Text = contatore.ToString();
    }

    private void btnIncrementa_Click(object sender, EventArgs e)
    {
        contatore++;
        lblContatore.Text = contatore.ToString();
    }
}
```

Il gestore deve essere collegato all'evento `Click`, tramite il designer o il codice. `sender` indica il controllo che ha generato l'evento; `EventArgs` contiene informazioni sull'evento, quando previste.

## Organizzare il codice

Mantieni distinti lo stato dell'applicazione, le regole e la presentazione. Sposta in metodi separati la logica riutilizzabile: evita di concentrare tutto in un singolo gestore click.

## Attenzioni

- Non confondere il nome del controllo (`Name`) con il testo mostrato (`Text`).
- Valida l'input prima di convertirlo.
- Aggiorna l'interfaccia dopo aver aggiornato lo stato dell'applicazione.
- Per operazioni lente, non bloccare il thread dell'interfaccia: la finestra potrebbe non rispondere.
