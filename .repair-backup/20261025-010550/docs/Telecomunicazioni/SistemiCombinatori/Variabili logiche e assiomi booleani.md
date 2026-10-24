# Variabili logiche e assiomi booleani

Una variabile logica può assumere due valori convenzionali: `0` e `1`. Un circuito combinatorio produce le uscite in funzione delle sole entrate presenti; la relazione può essere rappresentata con una funzione logica e una tabella di verità.

## Operazioni fondamentali

| A | B | AND `A·B` | OR `A+B` | XOR `A⊕B` |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

La negazione NOT inverte il valore: `NOT 0 = 1` e `NOT 1 = 0`.

## Proprietà da ricordare

- AND (`·`) è 1 solo quando tutti gli ingressi sono 1.
- OR (`+`) è 1 quando almeno un ingresso è 1.
- XOR è 1 quando gli ingressi sono differenti.
- NOT è l'operazione di complementazione.

L'algebra booleana usa simboli simili a quelli dell'algebra ordinaria ma con regole specifiche. Le leggi di De Morgan e le proprietà di assorbimento permettono di semplificare le espressioni; vedere [proprietà e teoremi dell'algebra di Boole](Proprietà%20e%20teoremi%20dell'algebra%20di%20Boole.md).
