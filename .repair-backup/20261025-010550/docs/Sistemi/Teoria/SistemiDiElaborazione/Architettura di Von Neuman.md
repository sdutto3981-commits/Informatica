# Architettura di Von Neumannn

Il modello di Von Neumannn descrive un calcolatore a programma memorizzato (*stored-program computer*): **istruzioni e dati risiedono nella stessa memoria principale** e la CPU preleva ed esegue le istruzioni secondo il flusso di controllo del programma.

## Componenti principali

- **CPU:** esegue le istruzioni; comprende unità di controllo, ALU e registri.
- **Memoria principale:** conserva istruzioni e dati necessari all'esecuzione; la RAM è volatile.
- **Input/output (I/O):** permette lo scambio di dati con periferiche e ambiente esterno.
- **Bus/interconnessioni:** trasportano informazioni tra CPU, memoria e I/O.

## Ciclo di istruzione

1. **Fetch:** l'unità di controllo preleva dalla memoria l'istruzione individuata dal program counter.
2. **Decode:** interpreta l'istruzione e determina le operazioni e gli operandi necessari.
3. **Execute:** l'unità funzionale esegue l'operazione; il risultato può essere scritto in un registro o in memoria.
4. **Aggiornamento:** il flusso prosegue con l'istruzione successiva, salvo salti, chiamate, interruzioni o altri eventi.

Questo è un modello concettuale; le CPU moderne usano pipeline, cache, esecuzione fuori ordine e altre ottimizzazioni, pur mantenendo un modello architetturale compatibile.

## Bus

- **Bus dati:** trasporta dati e istruzioni.
- **Bus indirizzi:** identifica le posizioni di memoria o i registri I/O da accedere.
- **Bus di controllo:** trasporta segnali di controllo e temporizzazione.

L'ampiezza del bus indirizzi contribuisce allo spazio di indirizzamento; l'ampiezza del bus dati indica quanti bit si possono trasferire in parallelo per una singola operazione del bus. Non confondere larghezza del bus, frequenza e throughput effettivo.

## Esempio concettuale

Per calcolare `a * b`, il programma acquisisce i valori, li memorizza, la CPU esegue l'operazione prevista dall'istruzione e il risultato viene presentato in output. L'ALU non esegue soltanto addizioni: può svolgere operazioni aritmetiche e logiche compatibili con l'architettura.
