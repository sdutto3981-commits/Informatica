---
date: 2026-02-01
time: 16:40
---
# Ciclo Macchina

Quando si avvia un qualsiasi programma, esso viene eseguito istruzione per istruzione dal processore.

L'esecuzione di ciascuna istruzione di compone di 3 fas:
- **Fetch:** la singola istruzione da eseguire viene letta dalla memoria e portata all'interno della CPU questo spetta alla BIU
- **Decode:** l'istruzione viene decodificata. Questo compito spetta alla CU
- **Execute:** l'istruzione viene eseguita e ne scrive il risultato in memoria questo compito spetta alla EU

E poi si continua il ciclo con il caricamento dell'istruzione successiva rieseguendo il ciclo F-D-E  e così via fino al termine del programma.

## Fase di fetch

1. La Cu imposta il registro CS e PC per calcolare il valore del MAR
2. Il contenuto di MAR viene calcolato dalla BIu e caricato sul Address Bus
3. Contemporaneamente viene abilitato un segnale di Read sul bus di controllo 
4. La memoria decodifica l'indirizzo dell'istruzione da caricare e la trasferisce sul Data Bus
5. L'istruzione viene portata dal Data Bus su MDR
6. L'istruzione viene copiata da MDR a IR
7. Il registro PC viene incrementato di una quantità pari alle dimensione dell'istruzione caricata

## Fase di decide

1. La CU decodifica l'istruzione verificando quali registri e sono coinvolti e operazioni devono essere eseguite e se la ALU dovrà lavorare
2. La CU legge un eventuale dato aggiuntivo della memoria centrale eseguendo un secondo ciclo di fetch e provvedendo ad incrementare ulteriormente il registro PC

## Fase di execute

1. Carica i dati necessari sui registri di ingresso della ALU 
2. La CU genera i segnali di controllo verso la ALU  per eseguire l'istruzione
3. Preleva il risultato dal registro di output della ALU e lo carica nel registro di destinazione o eventualmente nel MDR se il risultato deve essere salvato in memoria
4. Se il risultato deve essere salvato in memoria esegue un ultimo ciclo di scrittura in memoria.
5. Terminata l'istruzione in corso la CU riprende il cilco caricando la prossima istruzione fino al termine del programa.

## Riferimenti
1. 