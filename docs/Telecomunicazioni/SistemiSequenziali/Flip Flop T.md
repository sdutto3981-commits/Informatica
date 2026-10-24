# Flip-flop T

Il flip-flop **T** (*toggle*) è un circuito sequenziale sincrono che aggiorna l'uscita al fronte attivo del clock. L'ingresso `T` decide se mantenere il dato o commutarlo.

## Tabella caratteristica

| T | Q(t) | Q(t+1) | Comportamento |
|---:|---:|---:|---|
| 0 | 0 | 0 | Mantiene |
| 0 | 1 | 1 | Mantiene |
| 1 | 0 | 1 | Commutazione (*toggle*) |
| 1 | 1 | 0 | Commutazione (*toggle*) |

Forma compatta al fronte attivo:

\[
Q(t+1) = T \oplus Q(t)
\]

Dove `⊕` indica XOR. Se `T = 0`, XOR restituisce lo stato corrente; se `T = 1`, l'uscita viene invertita.

## Relazione con il contatore

Con `T = 1` costante, l'uscita commuta a ogni fronte attivo e quindi divide per due la frequenza del clock ideale. Collegando più stadi si possono costruire contatori, tenendo conto dei ritardi e del tipo di trigger.

Un flip-flop edge-triggered non è trasparente per tutta la durata del livello di clock: si aggiorna sul fronte specificato dal simbolo (salita o discesa).
