# Sommatori e multiplexer

Questi sono esempi classici di circuiti combinatori: l'uscita dipende esclusivamente dagli ingressi presenti in quell'istante.

## Half adder (semisommatore)

Somma due bit `A` e `B` e produce somma `S` e riporto `C`.

| A | B | S | C |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Le funzioni sono `S = A XOR B` e `C = A AND B`.

## Full adder (sommatore completo)

Somma `A`, `B` e il riporto in ingresso `Cin`; restituisce `S` e `Cout`.

- `S = A XOR B XOR Cin`
- `Cout = (A AND B) OR (Cin AND (A XOR B))`

Un full adder può essere costruito combinando due half adder e una porta OR per i riporti.

## Multiplexer 2:1

Un multiplexer seleziona uno tra due ingressi dati `D0` e `D1` tramite il bit di selezione `S`.

| S | Uscita Y |
|---:|---|
| 0 | `D0` |
| 1 | `D1` |

La funzione booleana è `Y = (NOT S AND D0) OR (S AND D1)`. Con più bit di selezione si possono selezionare più ingressi: con `n` selettori si possono indirizzare fino a `2^n` ingressi.

## Metodo per simulare

1. Definisci ingressi e uscite.
2. Crea la tabella della verità.
3. Ricava le espressioni booleane.
4. Disegna il circuito con porte logiche.
5. Simula tutti i casi e confronta le uscite con la tabella.
