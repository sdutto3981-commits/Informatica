---
date: 2025-09-17
time: 10:17
---

# Conversione tra esatta e approssimata

$$
\begin{flalign*}
&\frac{512Mb}{X} = \frac{1024Mb}{1Gb} -> \\
&X=\frac{512Mb*1Gb}{1024Mb}-> \\
&X=\frac{512Gb}{1024}-> \\
&X=\frac{1Gb}{2}-> \\
&X=0.5Gb
\end{flalign*}
$$

L'unita di misura in Mb scompare perché si semplifica nella frazione

$$
\begin{flalign*}
&1024Gb=XTiB -> \\
&1Tb=1000Gb / 1TiB = 1024GiB  -> \\
&1024Gb = 1024000000000 Byte -> \\
&\frac{1024000000000}{1024^4}=0.931322 \\
\end{flalign*}
$$

La conversine di questi numeri ci porta o a passare tra multipli e sottomultipli oppure tra un tipo ed un altro eseguiamo queste operazioni rispettivamente come:

- Multipli o in base 1000 o in base 1024  divido per questi numeri
- Sottomultipli o in base 100 o in base 1024 moltiplico per questi numeri
- Per passare da una conversione ad un altra devo retrocedere sino ai byte e poi dividere  per 1000 o 1024 per passare agli eventuali multipli posso esprimere la divisione sotto stante come una potenza
