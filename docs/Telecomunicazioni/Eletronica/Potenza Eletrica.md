# Potenza eletrica

La potenza eletrica indica quanta energia viene trasferita o trasformata nell'unita di tempo.

!!!note Il simpolo è **P** e l'unità di misura è il watt (W)

La formula principale per il calcolo della potenza è:

$$
\boxed{P=V*I}
$$

Se partiamo da questa formual de andiamo ad applicare la legge di ohm in caso non si conoscano V o I possiamo andare a sostituirli con le loro formule precedentemente viste:

$$
\text{Se} \ V=R*I \\
\text{E noi per calcolare la potenza dobbiamo andare a trovare V la formula diventa} \\
P = V*I \ -> P = (R*I)*I \ -> P=R*I^2 \\
\text{Mentre se per calcolare la potenza dobbiamo andare a calcolare la I la formula diventa} \\
P = V*I \ -> P=V*(\frac{V}{R}) \ -> P = \frac{V^2}{R}
$$

### Esempio

Un resistore da 20Ω è attraversato da 2 A. Calcola la potenza dissipata.

!!!tip Come visto prima rispetto alla formula normale della potenza ci manca la V ma possiamo andarla a calcolare tramite l'utilizzo delle leggi di ohm applicate alla potenza

$$
P=R*I^2 \\
P=20*"^2=20*4=80W
$$

## Generatore e resistori

In un circuito in corrente contunita costituito da un generatore ideale e resistore, la potenza eerogata dal generatore è uguale alla somma delle potenze dissipiate dai resistori:

$$
\boxed{P_{\text{generata}}=\sum P_{\text{dissipata}}}
$$

Questo è un modo per verificare i risultati dei calcoli.

### Esempio

Se un generatore eroga 36W e due resistori dissipano rispettivamente 10W e 26W il bilancio torna perchè:

$$
36=10+26
$$
Se il bilancio non torna controlla le corrente le tensioni e l'unita di misura
