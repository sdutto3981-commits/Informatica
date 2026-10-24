---
date: 2026-10-25
---
# Flip-flop D

Il **flip-flop D** (*Data* o *Delay*) memorizza il valore dell'ingresso `D` quando arriva il fronte attivo del clock. È un circuito sequenziale: l'uscita dipende dal valore campionato al fronte attivo e rimane memorizzata tra due fronti, salvo l'eventuale intervento di ingressi asincroni di preset o clear.

## Tabella caratteristica

Questa tabella descrive un dispositivo attivato sul fronte di salita (`↑`):

| Evento | D | Q dopo l'evento | Significato |
|---|---:|---:|---|
| Fronte di salita | 0 | 0 | Memorizza 0 |
| Fronte di salita | 1 | 1 | Memorizza 1 |
| Nessun fronte attivo | X | Q(t) | Mantiene il valore precedente |

`X` significa “indifferente” nella riga: quando non arriva il fronte attivo, il valore di `D` non viene campionato. Se il simbolo del componente indica il fronte di discesa (`↓`), il campionamento avviene in corrispondenza di quel fronte invece che della salita.

## Equazione caratteristica

Al fronte attivo:

\[
Q(t+1)=D
\]

`Q(t)` è il valore prima del fronte e `Q(t+1)` quello dopo l'aggiornamento. L'uscita complementare viene indicata `Q̅`, quando è presente.

## Temporizzazione e vincoli reali

La tabella logica presuppone che `D` sia stabile per i tempi richiesti dal componente:

- **setup time:** intervallo minimo per cui `D` deve essere stabile prima del fronte attivo;
- **hold time:** intervallo minimo per cui `D` deve restare stabile dopo il fronte;
- **clock-to-Q delay:** ritardo fra il fronte attivo e l'aggiornamento visibile di `Q`.

Se questi vincoli vengono violati, il circuito può entrare in metastabilità o produrre un comportamento non garantito. Questi aspetti temporali sono importanti nei circuiti reali, anche se la tabella di verità ideale non li mostra.

## Flip-flop D e latch D

Un **latch D** è sensibile al livello dell'ingresso di abilitazione: mentre è abilitato, può seguire `D`. Un **flip-flop D edge-triggered** campiona invece `D` soltanto al fronte attivo. Non sono dispositivi equivalenti.

## Esempio d'uso

Collegando l'uscita `Q` di un flip-flop D all'ingresso `D` del flip-flop successivo, i dati possono essere trasferiti fra stadi sincronizzati dal medesimo clock. Questa struttura è alla base di registri, pipeline e altri circuiti sequenziali.

Per distinguere il D da altri dispositivi consulta [flip-flop T](Flip%20Flop%20T.md), [flip-flop JK](Flip%20Flop%20jk.md) e [flip-flop SR](Flip%20Flop%20sr.md).
