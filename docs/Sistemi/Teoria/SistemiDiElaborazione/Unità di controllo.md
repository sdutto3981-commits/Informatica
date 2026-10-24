---
date: 2025-11-17
time: 09:44
---

# Unità di controllo

### Unità di controllo

L'unita di controllo accede alla memoria e prende le operazioni che deve eseguire e ed esegue e le interpreta per fare delle azioni.

All'interno della CU ci sono dei registri utilizzati per memorizzare diverse operazioni ogni operazione eseguita viene sempre determinata dal clock i registri possono essere di due tipi principali:
- Generali
- Specifici
I registri hanno un nome per i registri generali sono lettere mentre per quelli speciali hanno un nome completo esso è l'elemento piu veloce per memorizzare le informazioni essi possono essere anche  numerate.

I registri generali sono ad uso generico essi vengono utilizzati per memorizzare qualsiasi tipo di dato la dimensione varia a seconda del modello a livelli generale hanno una funzionalità  generica :

>Per esempio l'accumulatore viene indicato con la lettera A

Mentre per i registri specifici hanno dei nomi speciali:
- Program Counter è un registro che mi permette di andare a registrare l'operazione successiva
- Status Register specifica alla CU se l'operazione è andata a buon fine tramite dei flag deriva dalla ALU e in base ai valori la CU determina come procedere d'ora in poi.
- Stack Pointer serve per determinare i puntatori agli stack
- Instructione Register contiene i comandi che sono da eseguire all' interno ce il codice del operazione
- Memory Adress Register contiene l'indirizzo della cella di memoria principale dove sono contenuti i dati e dove si trovano.
- Memory Data Register contiene il tipo i dati e istruzioni dalla memoria verso i registri

#### MDR

Memory Data Register è un registro di frontiera che ci permette di creare un collegamento tra CPU  e mondo esterno e si passa sempre per lui per il salvataggio di dati

#### MAR

Il MAR è un registro che punta solo verso un informazione ovvero la cella di memoria che devo andare a considerare

#### IR

Vanno a contenere il codice operativo dell'istruzione che devo andare ad eseguire in quel momento esso preleva un ciclo di comandi

#### PC

Il program counter contiene l'indirizzo di memoria dove si trova l'istruzione successiva con ogni colpo di clock vado a prendere l'operazioni successiva cosi da permettere alla CU di organizzare l'istruzione successiva

>Esempio nel PC troviamo questo valore 00100h questo ci indica che viene rappresentato in esadecimale sono 20 bit perchè ogni numero in esadecimale vale 4 bit di conseguenza ho 20 bit
>quindi posso avere $2^{20}$ dividiamo per 8 è abbiamo i bytes e poi diviso mille arrivo a 131KB

Quindi con un singolo indirizzo posso andare a capire quanto è grande la memoria quindi in base ai valori di registro posso calcolarlo

#### PSW

Il Proces Status World esso viene valorizzato dalla ALU che contiene una serie di flag e con esso capisce cosa dovrà effettuare per indicare il risultato del operazione svolta dalla ALU la differenza dalla SR che indica un flag generico formato da 0 e 1 la PSW utilizza una serie di flag che in base al loro valore la CU capisce come risolvere e come procedere dopo l'errore

- Zero contiene 1 quando il risultato dell'ultima operazione ' uguale a 0  e tre cintiene 0
- PARITY quando il risultato è pari. Viene usato principalmente negli algoritmi di comunicazione per  la gestione del rilevamento degli errori di comunicazione
- SING contiene true quando il risultato dell'ultima operazione aritmetico logica è negativa  copiando nel flag il bit più significativo del risultato che riflette

1. [Registri](Registri.md)
