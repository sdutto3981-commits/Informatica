# Form multiple e finestre modali in C#

Un'applicazione Windows Forms può contenere più finestre. Una finestra può servire per mostrare dettagli, configurazioni o chiedere conferma.

## Modale e non modale

- `ShowDialog()` apre la finestra in modalità **modale**: l'utente deve chiuderla prima di tornare alla finestra chiamante. È adatta a dialoghi e configurazioni.
- `Show()` apre una finestra **non modale**: consente di tornare alla finestra principale senza chiuderla.

## Esempio di dialogo modale

```csharp
using (FormDettagli dialogo = new FormDettagli())
{
    DialogResult esito = dialogo.ShowDialog(this);
    if (esito == DialogResult.OK)
        lblRisultato.Text = dialogo.ValoreInserito;
}
```

Nella form `FormDettagli` si può esporre una proprietà che restituisce il valore validato:

```csharp
public string ValoreInserito
{
    get { return txtValore.Text.Trim(); }
}
```

Il pulsante di conferma può impostare `DialogResult = DialogResult.OK`; il pulsante Annulla può usare `DialogResult.Cancel`.

## Passare dati tra form

Passa al costruttore i dati che la seconda finestra deve visualizzare oppure usa proprietà esplicite. Evita di accedere direttamente a controlli privati di un'altra form.

## Buone pratiche

- Definisci cosa accade su OK, Annulla e chiusura della finestra.
- Valida i campi prima di restituire i dati.
- Chiudi o elimina le form quando non servono più.
- Mantieni la logica dei dati separata dai dettagli grafici.
