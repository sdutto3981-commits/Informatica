# Telecomunicazioni — programma 3INF

## Obiettivi

Comprendere e progettare semplici circuiti logici combinatori e sequenziali, modellare sistemi tramite automi e comprendere la trasmissione e i protocolli digitali.

## 1. Circuiti combinatori

**Appunti:** [Algebra logica](../Telecomunicazioni/AlgebraLogica/index.md), [sistemi combinatori](../Telecomunicazioni/SistemiCombinatori/index.md), [mappe di Karnaugh](../Telecomunicazioni/SistemiCombinatori/Mappe%20di%20Karnaugh.md), [circuiti tipici](../Telecomunicazioni/SistemiCombinatori/Sommatori%20e%20multiplexer.md).

Da saper fare:

- interpretare le variabili binarie e le tabelle di verità;
- usare AND, OR, NOT e le leggi dell'algebra di Boole;
- applicare i teoremi di De Morgan;
- semplificare funzioni con mappe di Karnaugh;
- comprendere il principio di sommatori e multiplexer;
- simulare e verificare un circuito in LabVIEW.

## 2. Circuiti sequenziali

**Appunti:** [sistemi sequenziali](../Telecomunicazioni/SistemiSequenziali/index.md), [automi](../Telecomunicazioni/Automa/index.md).

- Differenza tra circuito combinatorio e sequenziale; stato e memoria.
- Latch e flip-flop SR, D, T e JK; tabelle caratteristiche.
- Clock, fronte attivo e temporizzazione.
- Automi di Moore e Mealy, tabella di transizione e diagramma degli stati.
- Sintesi introduttiva di contatori e automi come quello di un cancello.
- Verifica tramite LabVIEW e Tinkercad.

## 3. Trasmissione dati

**Appunti:** [seriale asincrona e `millis()`](../Telecomunicazioni/Trasmissione%20seriale%20e%20Arduino.md).

- Trasmissione seriale e parallela: differenze, vantaggi e limiti.
- Trama asincrona: bit di start, bit dati, parità opzionale, bit di stop e baud rate.
- UART/USART e configurazione coerente di mittente e ricevitore.
- Multitasking cooperativo non bloccante tramite `millis()` su Arduino.

## 4. Protocolli di comunicazione digitale

**Appunti:** [ISO/OSI, livello 2 e strumenti](../Telecomunicazioni/Protocolli%20e%20modello%20ISO-OSI.md).

- Modello ISO/OSI: sette livelli, funzioni e incapsulamento.
- Livello 2: trame, indirizzamento locale, rilevazione errori e controllo di flusso.
- Differenza tra rilevazione e correzione degli errori; checksum e CRC a livello introduttivo.
- Compressione senza perdita (ZIP) e con perdita (JPEG, MP3).
- Differenza tra codifica e cifratura.
- Analisi del traffico con Wireshark e uso di Burp Suite in laboratorio.
- Esercitazioni Olicyber e strumenti di sicurezza soltanto su sistemi autorizzati.

## 5. Cittadinanza e Costituzione: IVA e fatturazione elettronica

- IVA: imposta indiretta sui consumi; distinguere imponibile, aliquota, imposta e totale.
- Formula semplificata: `IVA = imponibile × aliquota / 100`; `totale = imponibile + IVA`, salvo altre voci.
- Fattura elettronica: documento strutturato trasmesso tramite Sistema di Interscambio (SdI).
- Lo SdI svolge controlli formali e gestisce l'inoltro e gli esiti; non certifica da solo la correttezza commerciale della fattura.

Per aliquote e adempimenti reali, consultare le fonti istituzionali aggiornate e il materiale indicato dal docente.

## Autoverifica

- [ ] Minimizzare una funzione booleana con Karnaugh.
- [ ] Spiegare una tabella caratteristica di un flip-flop.
- [ ] Disegnare un automa Moore o Mealy.
- [ ] Spiegare una trama seriale asincrona.
- [ ] Scrivere un ciclo Arduino non bloccante con `millis()`.
- [ ] Descrivere il modello ISO/OSI e il ruolo del livello 2.
- [ ] Distinguere compressione, codifica e cifratura.
