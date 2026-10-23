---
date: 2025-11-17
time: 09:45
---
# BUS

### Collegamento tra le unita 

Esistono un sacco si unità esse sono collegate tramite i bus che sono capaci di trasmettere un segnale elettrico possono essere interni ed esterni interni se collega ALU e unita di controllo ed esterni se è un bus di sistema.

#### BUS di sistema 

Partendo dalla cpu che deve colloquiare con le altre unita essa ha dei piedini dove ogni bus può indicarmi ogni singolo valore 

Per esempio ho un registro da 8 bit la comunicazione avviene quindi in modo parallelo e ci permette di far viaggiare l'informazione sulla linea in modo parallelo .

Quindi se abbiamo un BUS di sistema possiamo divederli in tre gruppi principali:
- BUS dati doveA viaggiano in parallelo in modo bidirezionale
- BUS degli indirizzi è un BUS specifico che va ad identificare una sequenza di istruzioni 
- BUS controllo controlla determinati processi su di esso viaggia il clock l'input output il tipo di scrittura ecc..

Quindi i BUS di sistema riassumendo collega due unità di sistema una trasmette e l'altra riceve il trasferimento dei dati  avviene o sotto il controllo della CPU.

Se ho un bus degli indirizzi a 8 linee posso andare a gestire al massimo 256 linee di memoria quindi la mia capacita di eseguire salvataggi in memoria dipende anche molto dai bus essa determina la quantità di operazioni da svolgere in parallelo

Il bus dati è bidirezionale siccome dobbiamo scrivere e dobbiamo leggere mentre il BUS degli indirizzi determinano la trasmissione il contenuto del registro indirizzi di memoria.

BUS dei comandi è bidirezionale può quindi inviare e ricevere comandi verso una direzione e verso l'altra può inviare dei comandi verso il processore e possiamo anche inviarli ad atre unità 

BUS dati permette il trasferimento nelle quattro direzioni:
- Celle di memoria -> CPU caricamento 
- CPU -> cella di memoria scrittura quando il processo richiede di scrivere un dato specifico quindi acquisiamo il dato può essere interno o esterno
- CPU -> porta di uscita quindi l'output questa operazione è bidirezionale a seconda del operazione che dobbiamo effettuare

Maggiore il bus dati maggiore il parallelismo delle operazioni tra i vari dati per trasferire un informazione con un BUS dati a 8 bit e trasferire un informazione ci servono 8 colpi di clock 





## Riferimenti
1. 