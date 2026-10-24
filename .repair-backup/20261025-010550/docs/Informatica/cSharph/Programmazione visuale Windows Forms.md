# Programmazione visuale con Windows Forms

Windows Forms è una tecnologia .NET per creare applicazioni desktop a finestre. Una form contiene controlli come `Button`, `Label`, `TextBox`, `CheckBox` e `ListBox`.

## Proprietà, metodi ed eventi

- Proprietà: caratteristiche del controllo, per esempio `Text`, `Enabled`, `Visible` e `BackColor`.
- Metodi: operazioni, per esempio `Show()`, `Hide()` o `Focus()`.
- Eventi: notifiche a cui si collegano gestori, per esempio `Click`, `TextChanged` e `FormClosing`.

```csharp
private int contatore = 0;

private void btnIncrementa_Click(object sender, EventArgs e)
{
    contatore++;
    lblContatore.Text = contatore.ToString();
}
```

Il gestore evento viene associato tramite il designer oppure nel codice. Il campo `contatore` deve appartenere alla form (o a un componente di stato) affinché il valore persista tra eventi.

## Principi di progettazione

- Mantieni breve il codice nei gestori evento e delega i calcoli a metodi separati.
- Valida l'input dell'utente prima di usarlo.
- Non bloccare il thread dell'interfaccia con operazioni lunghe.
- Usa contenitori come `Panel`, `TableLayoutPanel` e `FlowLayoutPanel` quando aiutano la disposizione dei controlli.

Le API disponibili dipendono dal tipo di progetto, dal framework .NET e dal sistema operativo usato in laboratorio.

## Riferimento

[W3Schools — C# Classes](https://www.w3schools.com/cs/cs_classes.php) · [Microsoft — Windows Forms](https://learn.microsoft.com/dotnet/desktop/winforms/)
