# Flip-flop JK

Il flip-flop JK è simile al tipo SR ma evita la combinazione proibita tipica dell'SR: quando `J=K=1`, l'uscita commuta (toggle) al fronte attivo del clock.

| J | K | Q(t+1) | Funzione |
|---:|---:|---|---|
| 0 | 0 | Q(t) | memoria |
| 0 | 1 | 0 | reset |
| 1 | 0 | 1 | set |
| 1 | 1 | ¬Q(t) | commutazione |

La tabella descrive il comportamento al fronte attivo. Tra due fronti attivi l'uscita mantiene lo stato. Il simbolo `¬Q(t)` significa il complemento dello stato precedente.

Equazione caratteristica: `Q(t+1) = J·¬Q(t) + ¬K·Q(t)` al fronte attivo.
