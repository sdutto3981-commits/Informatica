# Creazione dinamica di controlli in Windows Forms

Un controllo può essere creato dal designer oppure durante l'esecuzione. La creazione dinamica è utile per griglie, liste di pulsanti, tabelloni e giochi come Campo Minato o Forza 4.

## Esempio: aggiungere pulsanti a runtime

```csharp
private void CreaPulsanti(int quanti)
{
    for (int i = 0; i < quanti; i++)
    {
        Button pulsante = new Button();
        pulsante.Name = "btn" + i;
        pulsante.Text = i.ToString();
        pulsante.Width = 50;
        pulsante.Height = 35;
        pulsante.Left = 10 + i * 55;
        pulsante.Top = 20;
        pulsante.Tag = i;
        pulsante.Click += PulsanteDinamico_Click;
        Controls.Add(pulsante);
    }
}

private void PulsanteDinamico_Click(object sender, EventArgs e)
{
    Button pulsante = sender as Button;
    if (pulsante != null)
        MessageBox.Show("Indice: " + pulsante.Tag);
}
```

`Controls.Add()` aggiunge il controllo al contenitore corrente. Se la form è già complessa, considera un `Panel`, un `FlowLayoutPanel` o un `TableLayoutPanel` per evitare di calcolare manualmente tutte le coordinate.

## Griglia di gioco

Per una griglia di righe e colonne si può usare un ciclo annidato e conservare i controlli in un array bidimensionale:

```csharp
Button[,] celle = new Button[righe, colonne];
```

Ogni gestore evento deve sapere quale cella è stata premuta. Si può usare una chiusura che cattura indici locali o la proprietà `Tag`, purché il dato venga gestito con un tipo coerente.

## Pulizia e gestione

- Rimuovi i controlli dal contenitore quando non servono più.
- Non registrare ripetutamente lo stesso gestore evento a ogni aggiornamento.
- Conserva lo stato del gioco in strutture dati distinte dalla grafica.
- Controlla larghezza, altezza e comportamento con ridimensionamento della finestra.
