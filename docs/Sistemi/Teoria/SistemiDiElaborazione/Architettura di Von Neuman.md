# Architettura di Von Neumann

L'architettura di Von Neumann descrive un calcolatore a programma memorizzato (*stored-program computer*): istruzioni del programma e dati risiedono nella stessa memoria principale e vengono trasferiti tra memoria, processore e periferiche.

## Componenti essenziali

- **CPU:** comprende unità di controllo, ALU e registri. Preleva le istruzioni, le decodifica e coordina l'esecuzione.
- **Memoria principale:** conserva istruzioni e dati in uso. È normalmente volatile quando realizzata come RAM.
- **Input/output:** consente la comunicazione con dispositivi esterni e controller.
- **Bus:** collegano i componenti e trasportano dati, indirizzi e segnali di controllo.

### Registri rilevanti

- **Program Counter (PC):** contiene l'indirizzo dell'istruzione da prelevare o del prossimo indirizzo previsto dal flusso di esecuzione.
- **Instruction Register (IR):** conserva l'istruzione in corso di decodifica/esecuzione nei modelli didattici.
- **MAR (Memory Address Register):** rappresenta l'indirizzo della locazione coinvolta nell'accesso alla memoria.
- **MDR/MBR (Memory Data Register/Buffer):** contiene il dato trasferito da o verso la memoria nel modello semplificato.
- **Registri generali e registri di stato:** conservano operandi, risultati temporanei e informazioni come flag di condizione.

I nomi e la presenza di questi registri variano tra le architetture concrete; sono un modello per capire i trasferimenti interni alla CPU.

### Unità di controllo e ALU

L'unità di controllo interpreta il codice operativo e coordina i segnali necessari a registri, ALU, memoria e I/O. L'ALU (*Arithmetic Logic Unit*) esegue operazioni aritmetiche e logiche, per esempio addizioni, confronti, AND/OR e spostamenti, secondo l'insieme di istruzioni supportato.

## Ciclo di istruzione

Il modello didattico distingue tre fasi:

1. **Fetch:** l'unità di controllo preleva l'istruzione dalla memoria, usando il Program Counter per individuarla.
2. **Decode:** l'istruzione viene interpretata e si determinano gli operandi e l'operazione da svolgere.
3. **Execute:** la CPU esegue l'operazione, può accedere alla memoria o alle periferiche e aggiorna registri e stato.

Il ciclo può includere ulteriori fasi (accesso alla memoria, write-back, gestione delle interruzioni) secondo l'architettura concreta.

## Bus di sistema

- Il **bus dati** trasferisce dati e istruzioni.
- Il **bus indirizzi** seleziona una posizione di memoria o una periferica indirizzabile.
- Il **bus di controllo** trasporta segnali come lettura/scrittura e sincronizzazione.

La larghezza dei bus e il protocollo di comunicazione influenzano le prestazioni e la quantità di dati trasferibili.

## Trasferimenti di memoria: esempio concettuale

Per leggere un dato in memoria, la CPU o il controller imposta l'indirizzo da raggiungere e avvia l'operazione di lettura; il dato viene trasferito al processore e può essere caricato in un registro. Per scrivere, si forniscono sia l'indirizzo sia il dato da memorizzare, con i segnali di controllo corrispondenti. I moderni sistemi usano cache, buffer, controller di memoria e protocolli molto più complessi di questo schema, ma la distinzione tra indirizzo, dato e controllo resta fondamentale.

Per sommare due numeri inseriti da tastiera, il programma acquisisce i valori tramite il sistema di I/O; essi vengono conservati in memoria o caricati in registri. La CPU preleva le istruzioni che descrivono l'operazione, la ALU esegue la somma e il risultato viene conservato in un registro o in memoria prima di essere mostrato tramite il dispositivo di uscita. Il dettaglio dipende dal codice macchina e dall'architettura.

## Limite e varianti

Il fatto che dati e istruzioni condividano un percorso verso la memoria è associato al *collo di bottiglia di Von Neumann*: la CPU può essere limitata dal trasferimento tra processore e memoria. Cache, gerarchie di memoria, prefetching, bus più veloci e accessi organizzati a blocchi cercano di ridurre il problema. La velocità non dipende soltanto dal clock del processore: anche la latenza della memoria, la banda disponibile e il comportamento del programma sono determinanti.

L'architettura **Harvard** distingue invece memoria o percorsi per istruzioni e dati. In molti processori general purpose si trovano soluzioni ibride: memoria principale condivisa, ma cache L1 separate per codice e dati. Questa scelta può consentire accessi simultanei senza richiedere due memorie principali completamente indipendenti.

## Vantaggi e limiti del modello

**Vantaggi:** un unico spazio di memoria semplifica il modello di programmazione; lo stesso hardware può trattare dati e istruzioni memorizzati; la memoria può essere allocata in modo flessibile tra codice e dati.

**Limiti:** il trasferimento condiviso tra CPU e memoria può diventare un collo di bottiglia; istruzioni e dati devono essere interpretati secondo il loro contesto; protezione, memoria virtuale, cache e concorrenza richiedono ulteriori meccanismi non rappresentati dal modello essenziale.

Approfondimenti: [Registri](Registri.md), [memoria centrale](Memoria%20centrale.md), [unità di controllo](Unità%20di%20controllo.md), [ALU](ALU.md) e [BUS](BUS.md).
