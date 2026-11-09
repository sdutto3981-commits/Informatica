# Modelli dei casi d'uso

Servono per rappresentare gli aspetti funzionali 

**Esempio** 
Gestione di un ambulatorio  medico in cui i pazienti devon accedere a un sistema per prenotare una visita medica  se si trova u posot libero si prenota il  sitema deve dire se un orario è prenotato o meno inoltre il sistema dovra dire il costo.

```mermaid
usecase-beta
direction LR
actor Customer("Utente")

prenota("Prenota visita")
cercaPosto("Cerca posto")
pagaVisita("Paga visita")
aggiornaPrenotazione("Aggiorna prenotazione")

Customer --> prenota
Customer --> cercaPosto
Customer --> pagaVisita
prenota --> cercaPosto
prenota --> aggiornaPrenotazione
```



```mermaid
usecase-beta
direction LR

actor Customer("Utente")
actor System("Sistema")

richiestaCampo("Richiesta campo")
pagaCampo("Paga campo")
ricercaDisponibilita("Ricerca disponibilita")
aggiornaStato("Aggiorna stato")
ricevuta("ricevuta")

Customer --> richiestaCampo
richiestaCampo  --> ricercaDisponibilita
System --> richiestaCampo
Customer --> pagaCampo
pagaCampo --> aggiornaStato
pagaCampo --> ricevuta
```
