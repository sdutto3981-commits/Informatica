---
date: 2025-11-24
time: 09:03
---

# Apertura di un programma

Quando noi iniziamo il nuovo programma il program counter si resetta quindi l'istruzione viene prelevata dalla memoria e viene interpretata ed eseguita
- Fecht esecuzione della singola istruzione memoria to cpu
- Decode istruzione interpretata
- Execute esecuzione del istruzione

Poi il program counter viene incrementato per passare all'istruzione successiva nello stesso colpo di clock

Il program counter contiene l'indirizzo di memoria dov'è memorizzata l'istruzione da eseguire l'accumulatore è il registro tramite il quale viene memorizzato il risultato della ALU e in base ad esso invia un flag mentre il PSW

## Fecht

Il bus di controllo andra a eseguire quindi un operazione di READ per l'indirizzo di memoria dell'istruzione quindi poi essa viene trasferita e viene trasferita nel registro MDR e copy copiato nel instruczione registrer e il program counter si incrementa e punta alla nota successiva

## Execute

Carica i dati di controllo esegue le operazioni verso la ALU quindi ottenuto il risultato viene poi gestito dalla CPU per l'istruzione successiva questo è possibile grazie al program counter che aumentando punta verso l'istruzione successiva.

Una volta completata l'operazione il registro accumulatore avra il risultato dell'operazione della ALU e come capiamo a cosa serva andiamo a vedere l'istruzione successiva

```

```
