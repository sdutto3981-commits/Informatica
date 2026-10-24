# Operatori in C#

Gli operatori combinano valori ed espressioni. I tipi degli operandi influiscono sul risultato.

## Aritmetici

| Operatore | Significato | Esempio |
|---|---|---|
| `+` | somma; concatenazione tra stringhe in contesti validi | `a + b` |
| `-` | sottrazione | `a - b` |
| `*` | moltiplicazione | `a * b` |
| `/` | divisione | `5 / 2` vale `2` se entrambi sono `int` |
| `%` | resto della divisione intera | `7 % 3` vale `1` |
| `++`, `--` | incremento/decremento di uno | `i++` |

## Assegnazione composta

`x += 3` equivale in molti casi a `x = x + 3`; analogamente `-=`, `*=`, `/=`, `%=`.

## Confronto

`==`, `!=`, `<`, `>`, `<=`, `>=` producono un `bool`. Per oggetti, `==` può dipendere dal tipo e dall'eventuale overload; non assumere che confronti sempre i contenuti.

## Logici

| Operatore | Significato | Esempio |
|---|---|---|
| `&&` | AND logico con cortocircuito | `x > 0 && y > 0` |
| `||` | OR logico con cortocircuito | `x == 0 || y == 0` |
| `!` | negazione logica | `!(x > 0)` |

`&&` non è `&` e `||` non è `|`: le versioni singole possono avere significati differenti, in particolare su interi e booleani.

## Pre/post incremento

`i++` restituisce il valore precedente all'incremento quando è usato in un'espressione; `++i` restituisce quello successivo. In istruzioni semplici come `i++;` entrambi incrementano `i` di uno. Per codice chiaro, evita di combinarli con altre modifiche nella stessa espressione.

Usa parentesi quando l'ordine delle operazioni non è evidente e ripassa le regole di precedenza prima di semplificare condizioni complesse.
