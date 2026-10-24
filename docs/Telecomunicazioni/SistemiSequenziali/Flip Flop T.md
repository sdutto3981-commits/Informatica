# Flip-flop T

Il flip-flop T (toggle) mantiene lo stato se `T=0` e inverte lo stato se `T=1`, al fronte attivo del clock.

| T | Fronte attivo | Q(t+1) |
|---:|---|---|
| 0 | sì | Q(t) |
| 1 | sì | ¬Q(t) |
| X | nessun fronte attivo | mantiene Q(t) |

Equazione caratteristica: `Q(t+1) = T ⊕ Q(t)` al fronte attivo. Il flip-flop T è utile per costruire contatori, perché con `T=1` commuta a ogni fronte.
