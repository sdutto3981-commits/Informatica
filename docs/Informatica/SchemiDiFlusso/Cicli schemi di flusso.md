# Cicli schemi di flusso

Possiamo ritrovare diversi tipi di cicli per esempio come detto negli schemi fondamentali troviamo quelli di **Iterazione** ovvero che fanno usi di cicli:
- Precondizionale: La condizione potrebbe non essere mai eseguita
- Post condizionale: La condizione almeno una volta viene eseguita
- Ciclo For: Lo usiamo solo quando sappiamo il numero esatto di volte che il ciclo deve ripetersi


## Ciclo Pre-condizionale
```mermaid
flowchart TD
    A([Arrivo del flusso]) --> B{Condizione Vera?}
    B -- Sì --> C[Esegui Istruzioni]
    C --> B
    B -- No --> D([Prosegui col programma])
```

## Ciclo Post-condizionale
```mermaid
flowchart TD
    A([Arrivo del flusso]) --> B[Esegui Istruzioni]
    B --> C{Condizione Vera?}
    C -- Sì --> B
    C -- No --> D([Prosegui col programma])
```

## Ciclo for
```mermaid
flowchart TD
    A([Arrivo del flusso]) --> B{{Per i = 1 fino a N}}
    B -- "Esegui" --> C[Istruzioni del ciclo]
    C -- "Ritorno (incrementa i)" --> B
    B -- "Fine ciclo" --> D([Prosegui col programma])
```