# Proprietà e teoremi dell'algebra di Boole

Le variabili booleane assumono i valori 0 e 1. Usiamo `+` per OR, `·` per AND e `¬A` per NOT.

## Leggi fondamentali

| Proprietà | OR | AND |
|---|---|---|
| Identità | `A + 0 = A` | `A · 1 = A` |
| Dominazione | `A + 1 = 1` | `A · 0 = 0` |
| Idempotenza | `A + A = A` | `A · A = A` |
| Complemento | `A + ¬A = 1` | `A · ¬A = 0` |
| Commutativa | `A + B = B + A` | `AB = BA` |
| Associativa | `(A+B)+C=A+(B+C)` | `(AB)C=A(BC)` |
| Distributiva | `A(B+C)=AB+AC` | `A+BC=(A+B)(A+C)` |

## Assorbimento

`A + AB = A` e `A(A+B) = A`.

## Teoremi di De Morgan

`¬(A+B) = ¬A · ¬B`

`¬(A·B) = ¬A + ¬B`

La negazione di una OR diventa AND delle negazioni; la negazione di una AND diventa OR delle negazioni.

## Semplificazione

`F = A + AB = A(1+B) = A`.

Per verificare un'identità, costruisci la tabella della verità dei due membri e controlla tutte le combinazioni. Le mappe di Karnaugh permettono la minimizzazione sistematica di funzioni con un numero ridotto di variabili.
