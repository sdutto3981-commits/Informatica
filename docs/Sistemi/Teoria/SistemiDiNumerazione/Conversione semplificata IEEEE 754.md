---
date: 2025-10-01
time: 09:55
---

# Conversione semplificata IEEEE 754

Per convertire un numero reale viene utilizzata la notazione scientifica normalizzata.
Un numero reale in notazione scientifica normalizzata si esprime sempre come:
$$
\begin{flalign*}
&+-+--------+---------+ \\
& \ \ \ \ |S| \ \ \ \ \ \ | Esp. | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ |       Mantissa        | \\
&+-+--------+---------+ \\

\end{flalign*}
$$
$$
\begin{flalign*}
&X=0,M*10^E \\
&75 -> 0,75*10^2
\end{flalign*}
$$

La mantissa  e esponente possiamo rappresentare un numero a 32 bit come il primo 1bit (0 Positivo 1 Negativo) dedicato al segno gli altri 8 bit corrispondono al esponente e gli altri 23 bit corrispondo alla mantissa

$$
\begin{align*}
&Convesione \ a \ 32 \ bit \ in \ formato \ IEEEE \ 754 \\
& \\
&73000_{(10)}\\
&0,73*10^5 \\
&M=73 \ \ \ \  E=5 \\
&& 73|1 \\
&&36|0 \\
&&18|0 \\
&&9|1 \\
&&4|0 \\
&&2|0 \\
&&1|1 \\
&&0|0 \\
&00000010100000000000000001001001
\end{align*}
$$

$$
\begin{align*}
&\text{Convesione  a  32  bit  in  formato IEEEE 754} \\
& \\
&-0,0010\\
&0,10*10^{-2} \\
&M=10 \ E=-2 \\
&&10\;|\:0 \\
&&5\;|\;1 \\
&&2\;|\;0\\
&&1\;|\;1\\
&&0\;|\;-\\
&M=10_{(10)}=1010_{(2)} \\
&E=2_{(10)}=10_{2} \;\rightarrow \; 00000010_{(10)} \; \text{su 8 bit} \\
& \\
& \text{Complemento a uno del esponente}\\
&11111101 \; + \; \\
& \quad\quad\quad\;  1 \; = \\
&---- \\
&11111110 \\
& \\
&-0,0010_{(10)}=11111111000000000000000000001010_{(2)}
\end{align*}
$$

# Conversione standard IEEE 754

$$
\begin{align*}
&\text{Su 8 bit il primo è il segno quindi possiamo usare solo 7 bit} \\
&7bit\rightarrow2^7-1\rightarrow^{+}_{-}127 \\
&-127 \\
&\;\;| \\
&-0 \\
&\;\;| \\
&-\;-126 \\
&\text{Sono possibili 255 valori da 0-254}\\
&126+127=253+0=254\text{ valori}
\end{align*}
$$

$$
\begin{align*}
&\text{Conversione in IEEE 754 di -20,25}_{(10)} \\
&20|0 &0.25*2=0.5\\
&10|0 &0.5*2=1\\
&5|1 \\
&2|0 \\
&1|1 \\
&0|- \\
&Segno\rightarrow 1 \;\text{Perchè il segno è negativo} \\
&-10100,10 \rightarrow -1,010010 *10^4 \\
&Esponente \rightarrow 4+127=131 \; \text{Perchè andando a sottrare 127} \\ &\text{se l'esponente è positivo sarebbe 131-127=4} \\
&\text{se fosse negativo -4 127-4=123 e al contrario 123-127=-4} \\
&1100000110100100000000000000000
\end{align*}
$$
