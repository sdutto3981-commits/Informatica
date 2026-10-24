# Variabili logiche e assiomi booleani

In elettronica digitale, una variabile logica assume uno tra due valori convenzionali: `0` e `1`. Questi valori rappresentano stati logici; il livello di tensione fisico associato dipende dalla tecnologia del circuito.

Un **circuito combinatorio** produce uscite determinate dalla combinazione degli ingressi presenti in quell'istante. Il suo comportamento può essere descritto con una tabella della verità e con una funzione booleana. Un circuito sequenziale, invece, conserva uno stato e dipende anche dalla storia/condizione memorizzata.

## Operazioni fondamentali

| A | B | AND `A·B` | OR `A+B` | NOT A `¬A` |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

- **AND (prodotto logico):** vale `1` solo quando entrambi gli ingressi sono `1`.
- **OR (somma logica):** vale `1` quando almeno un ingresso è `1`.
- **NOT (complementazione):** inverte il valore logico.

Queste operazioni seguono le definizioni dell'algebra di Boole, non le usuali regole dell'aritmetica decimale. Per esempio, `1 + 1 = 1` nella OR logica.

## Ordine di valutazione

Le parentesi chiariscono l'ordine. Nelle espressioni miste conviene indicare esplicitamente il raggruppamento, ad esempio `F = (A AND B) OR C`.

Per le proprietà, l'assorbimento e i teoremi di De Morgan consulta [Proprietà e teoremi dell'algebra di Boole](Proprietà%20e%20teoremi%20dell'algebra%20di%20Boole.md). Per gli esercizi di minimizzazione consulta [Mappe di Karnaugh](Mappe%20di%20Karnaugh.md).
