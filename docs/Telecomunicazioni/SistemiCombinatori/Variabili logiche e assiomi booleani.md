# Variabili logiche e assiomi booleani

Una **variabile logica** assume uno dei due valori convenzionali `0` e `1`. In un circuito, questi simboli rappresentano stati logici; le tensioni fisiche che corrispondono a LOW e HIGH dipendono dalla famiglia logica e dal componente.

Un **circuito combinatorio** produce le uscite in funzione delle sole entrate presenti: non conserva uno stato precedente. La funzione può essere rappresentata attraverso un'espressione booleana e una tabella di verità.

## Operazioni fondamentali

| A | B | AND `A·B` | OR `A+B` | XOR `A⊕B` | NAND `¬(A·B)` | NOR `¬(A+B)` |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

NOT è un'operazione a un ingresso: `¬0 = 1` e `¬1 = 0`.

## Significato operativo

- **AND** vale 1 soltanto se tutti gli ingressi valgono 1.
- **OR** vale 1 quando almeno un ingresso vale 1.
- **XOR** vale 1 quando i due ingressi sono differenti.
- **NAND** è la negazione del risultato AND; **NOR** è la negazione del risultato OR.
- **NOT** inverte il valore dell'ingresso.

In elettronica digitale, NAND e NOR sono dette porte universali perché è possibile realizzare le operazioni booleane fondamentali componendo soltanto porte di una delle due famiglie.

## Assiomi e proprietà di base

Per le variabili booleane `A` e `B` valgono, tra le altre, le seguenti identità:

- Identità: `A·1=A`, `A+0=A`.
- Dominazione: `A·0=0`, `A+1=1`.
- Idempotenza: `A·A=A`, `A+A=A`.
- Complemento: `A·¬A=0`, `A+¬A=1`.
- Commutativa: `A·B=B·A`, `A+B=B+A`.

Queste operazioni sono logiche: `+` indica OR e `·` indica AND, non necessariamente somma e moltiplicazione aritmetiche. Per esempio `1+1=1` in algebra booleana.

## Tabelle della verità e complessità

Con `n` ingressi binari esistono `2^n` combinazioni possibili. Per tre variabili `A`, `B`, `C` la tabella contiene otto righe. Elenca ogni combinazione una sola volta e calcola l'uscita applicando l'espressione logica.

Per confrontare due espressioni equivalenti, valuta entrambi i membri su tutte le combinazioni: se le uscite coincidono in ogni riga, le funzioni sono equivalenti. Questa verifica è semplice per poche variabili; per minimizzare funzioni si possono usare algebra booleana e mappe di Karnaugh.

## Collegamenti

- [Proprietà e teoremi dell'algebra di Boole](Proprietà%20e%20teoremi%20dell'algebra%20di%20Boole.md)
- [Mappe di Karnaugh](Mappe%20di%20Karnaugh.md)
- [Sommatori e multiplexer](Sommatori%20e%20multiplexer.md)
