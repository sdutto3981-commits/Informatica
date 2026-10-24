# Protocolli e modello ISO/OSI

Il modello ISO/OSI suddivide le funzioni di comunicazione in sette livelli. È un modello di riferimento: protocolli reali possono organizzare diversamente alcune funzioni.

| Livello | Nome | Funzione tipica | Esempio/concetto |
|---:|---|---|---|
| 7 | Applicazione | servizi usati dalle applicazioni | HTTP, DNS |
| 6 | Presentazione | formato, codifica, compressione, cifratura concettuale | rappresentazione dei dati |
| 5 | Sessione | gestione delle sessioni | dialogo e sincronizzazione |
| 4 | Trasporto | comunicazione end-to-end, porte, affidabilità ove prevista | TCP, UDP |
| 3 | Rete | indirizzamento logico e instradamento | IP |
| 2 | Collegamento dati | trama, accesso al mezzo, rilevazione errori sul collegamento | Ethernet, Wi-Fi MAC |
| 1 | Fisico | trasmissione di bit e caratteristiche elettriche/radio | cavo, segnale radio |

## Incapsulamento

Quando i dati scendono nello stack, ciascun livello può aggiungere informazioni di controllo (header ed eventualmente trailer). In ricezione, le informazioni vengono analizzate e rimosse livello per livello.

## Livello 2: trama ed errori

Il livello di collegamento organizza i bit in **frame/trame**, gestisce l'accesso al mezzo e può rilevare errori tramite FCS/CRC. La rilevazione segnala un possibile errore; non significa automaticamente che il destinatario possa correggerlo. Affidabilità e ritrasmissioni dipendono dal protocollo specifico.

Il controllo di flusso evita che il mittente invii dati più velocemente di quanto il ricevitore riesca a gestire. Il controllo degli errori può utilizzare numeri di sequenza, acknowledgement e ritrasmissioni quando previsti.

## Compressione, codifica e cifratura

- **Compressione lossless:** i dati originali sono ricostruibili esattamente (es. ZIP).
- **Compressione lossy:** elimina informazioni per ridurre la dimensione (es. JPEG, MP3).
- **Codifica:** rappresenta informazioni in un formato convenuto e non implica segretezza.
- **Cifratura:** trasforma i dati usando un algoritmo e una chiave per impedire la lettura a chi non è autorizzato.

## Wireshark e Burp Suite

Wireshark permette di catturare e analizzare pacchetti su una rete a cui si è autorizzati ad accedere. Burp Suite è utilizzato per osservare e testare il traffico HTTP/S di applicazioni web nel contesto di un laboratorio autorizzato. Non intercettare traffico altrui né testare sistemi senza permesso.
