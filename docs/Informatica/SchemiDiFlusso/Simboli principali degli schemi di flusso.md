# Simboli principali degli schemi di flusso

Tutti gli schemi di flusso iniziano con **Start** e finiscono con **End** generalmente ovali con testo all'interno.

```mermaid
flowchart LR
    id1([START])
    id2([END])
    id1-->id2
```

Uno spazio per eseguire le **operazione di assegnazione e di dichiarazione delle variabili** Forma generalmente rettangolare.

```mermaid
flowchart LR
    id1[Azione]
```

Abbiamo blocchi di **Input e di Output** che servono per avere dei valori inseriti dall'utente e per dare dell'testo o dei risultati in output forma generalmente di parallelogramma.

```mermaid
flowchart LR
    id1[/IF/]
```

Poi abbiamo le  **Condizioni** che servono per eseguire una scelta tra un operazione usando gli operatori forma generalmente di rombo con in entrata una freccia  e in uscita due frecce una per il vero e una per il falsa.

```mermaid
flowchart LR
    id1{IF condition}
```

Poi un Programma che richiama dei **sottoprogrammi** forma rettangolare con dei bordi laterale oppure rombi con bordi su tutto il contorno per le condizioni

```mermaid
flowchart LR
    id1[[Sottoprogramma]]
```

Inoltre troviamo per collegare le varie forme geometriche delle **linee di flusso**:

```mermaid
flowchart LR
    id1([START])
    id2([END])
    id3[Azione]
    id1 --> id3
    id3 --> id2
```
