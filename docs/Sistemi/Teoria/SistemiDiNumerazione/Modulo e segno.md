---
date: 2025-10-01
time: 09:54
---

# Modulo e segno

Per convertire il numero in modulo e segno
1. Converto il valore de numero binario su N-1 bit
2. Aggiungo con MSB
	- 0 se il numero è positivo
	- 1 se il numero è negativo
3. se devo convertire da binario a decimale tolgo MSB

$$
\begin{flalign*}
&nBit=8bit \\
&+12_{10}->1100_{2}->00001100 \\
&-12_{(10)}->1100_{(2)}->10001100\\
\end{flalign*}
$$
1 bit è riservato al segno quindi possiamo usare al massimo 7bit quanti valori possiamo rappresentare con 7bit $2^7-1 =127$  pero avendo il segno possiamo avere sia positivo che negativo quindi $+127 <-0 |0->-127$ pero vengono rappresentati due quindi il range è dato da questa formula $Da->2^n-1(positivi) A->2^{-n}(negativi)$ in questo caso da+127 a -128 siccome togliendo lo zero nei numeri negativi possiamo rappresentare un numero in più
