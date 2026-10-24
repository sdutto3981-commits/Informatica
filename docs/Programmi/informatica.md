# Informatica e laboratorio — programma 3INF

## Obiettivi

Risolvere problemi tramite algoritmi e diagrammi a blocchi e implementarli in C#/.NET. Il percorso passa dalla programmazione strutturata alle interfacce grafiche a eventi, con modularità e gestione dei file.

## 1. Programmazione strutturata e sottoprogrammi (50 ore)

**Appunti:** [schemi di flusso](../Informatica/SchemiDiFlusso/index.md), [C#](../Informatica/cSharph/index.md), [algoritmi fondamentali](../Informatica/AlgoritmiFondamentali/index.md).

- Analisi del problema, dati in ingresso, risultato e casi limite.
- Algoritmi e diagrammi a blocchi: sequenza, selezione e iterazione.
- Variabili, costanti, tipi, operatori e conversioni.
- Progettazione top-down e scomposizione in sottoproblemi.
- Metodi C#: parametri, tipo restituito, chiamata e riuso.
- Passaggio per valore e uso di `ref`/`out` quando previsto.
- Classi .NET come `Math` e `String`/`string`.
- Test con casi normali, limiti e input non validi.

```csharp
static double Media(double a, double b)
{
    return (a + b) / 2.0;
}
```

## 2. Dati strutturati (25 ore)

**Appunti:** [array e matrici](../Informatica/ArrayMatrici/index.md), [ricerca e ordinamento](../Informatica/AlgoritmiFondamentali/Ricerca%20e%20ordinamento.md).

- Array monodimensionali e bidimensionali; indici da zero.
- Inizializzazione, scansione e aggiornamento degli elementi.
- Ricerca lineare e ricerca dicotomica su dati ordinati.
- Algoritmi di ordinamento affrontati in classe e confronto del costo.
- Record come modello di dati composti; in C# usare i tipi previsti dal progetto.
- Distinguere numero di elementi e indice: gli indici fuori intervallo generano errori.

## 3. Strumenti di sviluppo software (5 ore)

- Ciclo di vita: analisi, progettazione, implementazione, test, rilascio e manutenzione.
- Compilatore e debugger hanno funzioni differenti.
- Breakpoint, passo-passo, variabili locali, call stack e watch.
- Distinguere errori di compilazione, runtime ed errori logici.

## 4. Programmazione visuale e oggetti dinamici (60 ore)

- Form e controlli: proprietà, metodi ed eventi.
- Programmazione a eventi: rispondere a click, input e altre azioni dell'utente.
- Creazione dinamica di controlli a runtime e gestione del layout.
- Separazione tra stato/dati, regole di funzionamento e interfaccia.
- Campo Minato e Forza 4: griglia, turno, condizioni di vittoria e reset.

```csharp
private void btnIncrementa_Click(object sender, EventArgs e)
{
    contatore++;
    lblContatore.Text = contatore.ToString();
}
```

Il campo `contatore` deve essere dichiarato in un ambito accessibile al gestore, per esempio come campo della form.

## 5. File e interfacce grafiche avanzate (15 ore)

- `StreamReader`/`StreamWriter`, `using` e gestione degli errori.
- Form multiple, finestre modali e non modali e passaggio dei dati.
- Collezioni dinamiche come `List<T>`: inserimento, rimozione, ricerca e iterazione.
- Definire un formato per salvare e ricaricare lo stato dell'applicazione.

```csharp
using System;
using System.IO;

try
{
    using StreamReader reader = new StreamReader("dati.txt");
    string? riga;
    while ((riga = reader.ReadLine()) != null)
        Console.WriteLine(riga);
}
catch (IOException ex)
{
    Console.WriteLine($"Errore di lettura: {ex.Message}");
}
```

La sintassi nullable `string?` dipende dalla versione e dalla configurazione del progetto .NET.

## 6. Cittadinanza: robotica e intelligenza artificiale (4 ore)

- Robotica: sensori, attuatori, controllo e retroazione.
- Distinguere automazione, robotica e intelligenza artificiale.
- Valutare qualità dei dati, bias, privacy, sicurezza e responsabilità.
- Verificare le risposte degli strumenti IA: non sono automaticamente corrette.

## Autoverifica

- [ ] Trasformare un problema in algoritmo e diagramma a blocchi.
- [ ] Scrivere metodi C# e scomporre un problema.
- [ ] Gestire array, matrici, ricerca e ordinamento.
- [ ] Usare debugger e breakpoint.
- [ ] Gestire controlli ed eventi in una GUI.
- [ ] Separare logica e interfaccia in un piccolo gioco.
- [ ] Leggere/scrivere file e usare collezioni dinamiche.
