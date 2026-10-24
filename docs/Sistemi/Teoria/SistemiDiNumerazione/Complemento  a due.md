---
date: 2025-10-01
time: 09:54
---

# Complemento  a due

Per convertire in complemento a 2, si seguono i seguenti passaggi:
1. Se il numero è positivo la rappresentazione è u uguale a quella del modulo e segno
2. Se il numero è negativo:
	1. Converto il numero senza segno in binario i restanti N-1 bit (questo è il modulo)
	2. Eseguo il complemento a 1 del modulo ovvero inverto tutte le cifre
	3. Sommo 1 al modulo
	4. Unisco l'MSB=1 al risultato ottenuto

$$
\begin{flalign*}
&Convetiamo \ a \ 8 \ bit \\
& \\
&-12_{(10)}->...._{(2)} &12|0\\
&&6|0 \\
&&3|1 \\
&&1|1 \\
&&0|/ \\
&-12_{(10)}->1100_{(2)}\\
& \\
&1. \ convertiamo\ a \ 7 \ bit  \\
&0001100 \\
& \\
&2. \ eseguiamo \ il \ complemento \ a \ 1 \\
&1110011 \\
& \\
&3. \ sommo \ 1 \\
&1110011 \ + \\
& \ \ \ \ \ \ \ \ \  \ \ \ 1 \ = \\
&---- \\
&1110100 \\
& \\
&4. \ siccome \ è \ negativo \ aggiungo \ 1 \ davanti \\
&11110100_{(2)}
\end{flalign*}
$$
