# Numeri reali con segno e virgola mobile

I numeri reali nei calcolatori sono spesso rappresentati in virgola mobile. Una rappresentazione IEEE 754 comprende tre campi: **segno**, **esponente** e **frazione** (spesso chiamata mantissa negli appunti introduttivi).

Per un valore normalizzato, la forma concettuale in base 2 è:

\[
(-1)^s \times 1.frazione_2 \times 2^{E}
\]

L'esponente memorizzato è biasato. Il bit di segno vale 0 per il segno positivo e 1 per il segno negativo. La parte iniziale `1` dei numeri normalizzati è implicita.

## Formati comuni

| Formato | Segno | Esponente | Frazione |
|---|---:|---:|---:|
| binary32 (`float`) | 1 bit | 8 bit | 23 bit |
| binary64 (`double`) | 1 bit | 11 bit | 52 bit |

I numeri non sono tutti rappresentabili esattamente: ad esempio molte frazioni decimali hanno espansione binaria periodica. Per questo, confrontare numeri in virgola mobile con uguaglianza esatta può essere inappropriato; nei problemi numerici si usa una tolleranza adatta al contesto.

Gli esponenti riservati permettono di rappresentare zero, valori subnormali, infinito e NaN. Non confondere precisione, intervallo rappresentabile e numero di cifre decimali stampate: sono concetti distinti.
