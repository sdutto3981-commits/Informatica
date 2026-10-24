# Creazione dinamica dei controlli in Windows Forms

È possibile creare controlli durante l'esecuzione, configurarne proprietà e aggiungerli alla raccolta `Controls` di una form o di un contenitore.

```csharp
private void AggiungiPulsante()
{
    Button pulsante = new Button
    {
        Text = "Nuovo",
        Width = 100,
        Height = 35,
        Left = 20,
        Top = 20
    };

    pulsante.Click += (sender, e) =>
    {
        MessageBox.Show("Pulsante creato a runtime");
    };

    flowLayoutPanel1.Controls.Add(pulsante);
}
```

L'esempio presume che `flowLayoutPanel1` esista già nella form. Un `FlowLayoutPanel` dispone i controlli in sequenza; in altri layout, proprietà come `Location` o `Dock` possono essere rilevanti.

## Rimozione e gestione della vita del controllo

Per rimuovere un controllo usa la raccolta `Controls` del contenitore che lo ospita. Quando crei controlli dinamicamente, assicurati di non aggiungerne duplicati a ogni evento involontariamente e di liberare le risorse quando il contesto lo richiede.

## Separare logica e interfaccia

Il gestore evento dovrebbe aggiornare lo stato o chiamare un metodo di dominio; evita di mettere tutta la logica del gioco in una singola lambda. Per giochi come Campo Minato o Forza 4, mantieni separati griglia, turno, regole di vittoria e rendering.

## Riferimento

[Microsoft — Windows Forms Controls](https://learn.microsoft.com/dotnet/desktop/winforms/controls/)
