---
date: 2025-10-06
time: 09:05
---
# Virgola Mobile

Nella rappresentazione in virgola mobile la posizione della virgola varia dinamicamente
#### Formato floating point standard IEEE 754

Mantissa: 23 bit prima cifra significati alla sinistra hidden bit 
Esponente: 8 bit polarizzati 127

$$
\begin{align*}
&|S|---E----|----------M----------| \\
&1bit \ \ \ \ \ \ \ \ \ \ \ 8bit \ \ \ \ \ \  \ \ \ \ \ \ \ \ \  \ \ \  \ \ \  \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ 23bit\\ 
&N=(-1)^S*2^{(E-127)}*1.M\\ 
\end{align*}
$$
La mantissa normalizzata con un primo bit che corrisponderà al hidden bit 

$$
\begin{align*}
&160.75=01000011001000001100000000000000\\ 
&0.75*2=1.5 &160|0\\&0.5*2=1&80|0\\&&40|0\\&&20|0\\&&10|0\\&&5|1\\&&2|0\\&&1|1\\
&
\end{align*}
$$


## Riferimenti
1. 
