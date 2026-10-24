---
date: 2025-10-01
time: 10:40
---

# Conversione decimale-binario di numeri non interi

- La parte intera si converte con il metodi divisivo secessive
- Per la parte alla destra della virgola
	- Si moltiplica la parte decimale per 2
	- Si annota la parte intera del risultato come cifra utile
	- Si ripetono i 2 passaggi precedenti finche la parte di destra non diventa 0

$$
\begin{align*}
&0.375*2=0.75\\
&0.75*2=1.5 \\
&0.5*2=1.0
\end{align*}
$$

Poi possiamo usare la codifica 754 per convertirlo in un numero binario a 32 bit

## Riferimenti

1.
