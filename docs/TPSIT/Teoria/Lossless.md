---
date: 2025-10-10
time: 13:29
---

# Lossless

Algoritmo di compressione Lossless salva le sequenze continue e nel momento di de compressione l'approccio è assegnare meno bit per i byte più frequenti mentre quelli che si ripetono di meno avranno più bit possiamo ridurre quei pattern in modo da avere meno dati.

##### gif

Riduce i colori passando da RGB 3 cali a 256 valori a canale in totale $256^3$ nasce proprio per internet quindi per ogni pixel troviamo un puntatore per collegarlo ad un colore della web safe palette e poi viene utilizzata la compressione LZW  in questo caso si cerca un area che ha lo stesso colore e comprimerle.

La Web Safe Palette contiene 256 colori garantiti visualizzabili su ogni sito ogni schermo inoltre troviamo un puntatore che permette di decidere la trasparenza di un colore o pixel

##### interallacciare un immagine

Questo consente un miglioramento importante siccome quando andiamo a creare un sito viene visualizzato prima il testo e le immagine devono caricare dopo mentre invece dopo caricando l'immagine in modo interlacciato ci permette di far si che si carichino più velocemente  caricandole come delle strisce

Per esempio le gif animate sono sequenze di immagini chiamate frame pe

##### PNG

Algoritmo di compressione nato per non pagare  GIF è lossless supporta la trasparenza e anche l'interllaciamento ed anche più veloce di gif circa 1/64 di secondo

## Riferimenti

1.
