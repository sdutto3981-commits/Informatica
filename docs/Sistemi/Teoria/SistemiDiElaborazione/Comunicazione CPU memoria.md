---
date: 2026-02-01
time: 19:39
---

# Comunicazione CPU memoria

La comunicazione tra CPU e memoria avviene nel modo seguente:
- La CPU assumendo il ruolo di master invia ordini di scrittura e lettura a memorie o periferiche
- La memoria assume il ruolo di slave si comporta da sorgente quando invia i dati sul data bus o dal destinatario quando si predispone a riceverli
- Il bus dati trasporta le informazioni scambiate
- Il bus degli indirizzi individua l'unità  sorgente/destinazione
- Per distinguere se l'istruzione è di lettura o di scrittura viene attivato uno dei segnali di Read e Write
- Per distinguere se l'indirizzo che viene posto sull'adress bus si riferisca a una memoria o a una periferica viene attivato uno dei segnali MREQ o IOREQ

## Ciclo di lettura e scrittura

Un generico ciclo di lettura dalla memoria è svolto nel modo seguente
- L'indirizzo della locazione di memoria è posto sull'adress bus all'inizio del primo ciclo di clock
- Il segnale MREQ diventa attivo basso quando il bus indizzi è stabile il chip di memoria viene abilitato
- La linea di RD diventa attiva per indicare che i dati letti dalla memoria sono posti sul bus dati ili segnale WR rimane inattivo

## Ciclo di scrittura

Un generico ciclo di scrittura in memoria è svolto nel modo seguent.
- L'indirizzo della locazione di memoria è posto sull'adress bus all'inizio del primo ciclo di clock
- Il segnale MREQ diventa attivo basso quando il bus di indirizzi è stabile il chip di memoria viene abilitato
- La linea di WR diventa attiva bassa quando i dati sul data bus sono stabili il segnale RD rimane inattivo per tuto il tempo dell'operazione di scrittura
-
