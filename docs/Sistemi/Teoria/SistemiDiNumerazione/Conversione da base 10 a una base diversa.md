# Conversione dalla base 10 a una base diversa

Per convertire un numero intero positivo dalla base 10 alla base `b`, si divide ripetutamente per `b` e si registrano i resti. Il risultato nella nuova base si ottiene leggendo i resti **dal basso verso l'alto**, cioè dall'ultimo resto al primo.

## Esempio: convertire `294₁₀` in base 5

| Divisione | Quoziente | Resto |
|---|---:|---:|
| 294 ÷ 5 | 58 | 4 |
| 58 ÷ 5 | 11 | 3 |
| 11 ÷ 5 | 2 | 1 |
| 2 ÷ 5 | 0 | 2 |

I resti sono stati ottenuti nell'ordine `4, 3, 1, 2`; letti al contrario danno:

\[
294_{10} = 2134_5
\]

## Verifica inversa

\[
2134_5 = 2\cdot 5^3 + 1\cdot 5^2 + 3\cdot 5^1 + 4\cdot 5^0
\]

\[
= 250 + 25 + 15 + 4 = 294_{10}
\]

## Note

- La conversione tramite divisioni successive vale direttamente per interi non negativi.
- Per la parte frazionaria si usa il metodo delle moltiplicazioni successive della frazione per la base.
- Se la base supera 10, per le cifre maggiori di 9 si usano simboli aggiuntivi, spesso `A`, `B`, … nelle basi esadecimali.
