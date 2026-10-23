---
date: 2025-11-11
time: 11:55
---
# Flip Flop jk

Secondo la tabella di verita guardiamo di nuovo solo lo stato attivo mentre per tutti gli altri abbiamo memoria


| j   | k   | CK                     | Q(i)    |         |
| --- | --- | ---------------------- | ------- | ------- |
| 0   | 0   | $\rightarrow \uparrow$ | Q(i-1)  | memoria |
| 0   | 1   | $\rightarrow \uparrow$ | 0       | reset   |
| 1   | 0   | $\rightarrow \uparrow$ | 1       | set     |
| 1   | 1   | $\rightarrow \uparrow$ | -Q(i-1) | toggle  |


-Q(i-1) sarebbe memoria negata ovvero l'inversione di quello che avevamo precedentemente inserito
## Riferimenti
1. 