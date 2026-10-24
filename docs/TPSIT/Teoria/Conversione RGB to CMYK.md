---
date: 2025-10-02
time: 11:14
---

# Conversione RGB to CMYK

1. Normalizzare la scala tra 0 e 1
R'=R/255 G'=G/255 B'=B/255
2. Calcolare il nero
K = 1-MAX(R',G',B')
3. Calcolare il CIANO, MAGENTA, GIALLO
SE K=1 C=M=Y=0
ALTRIMENTI

C=1-R'-K/1-K
M=1-G'-K/1-K
Y=1-B'-K/1-K
4. Trasformo C M Y in percentuale ($*100$)

$C=C*100$
$M=M*100$
$Y=Y*100$
