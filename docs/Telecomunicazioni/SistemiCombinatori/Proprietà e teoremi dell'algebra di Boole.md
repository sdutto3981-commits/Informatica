# Proprietà e teoremi dell'algebra di Boole

L'algebra booleana descrive funzioni con valori logici `0` e `1`. Nelle espressioni digitali, `+` indica OR, `·` indica AND e `¬A` indica NOT. La precedenza convenzionale è NOT, poi AND, poi OR; usa parentesi quando l'ordine può essere ambiguo.

## Leggi fondamentali

| Proprietà | OR | AND |
|---|---|---|
| Identità | `A + 0 = A` | `A · 1 = A` |
| Dominazione | `A + 1 = 1` | `A · 0 = 0` |
| Idempotenza | `A + A = A` | `A · A = A` |
| Complemento | `A + ¬A = 1` | `A · ¬A = 0` |
| Commutativa | `A + B = B + A` | `A · B = B · A` |
| Associativa | `(A+B)+C = A+(B+C)` | `(AB)C = A(BC)` |
| Distributiva | `A(B+C) = AB+AC` | `A+BC = (A+B)(A+C)` |

## Assorbimento

Le leggi di assorbimento eliminano termini già inclusi in un altro termine:

- `A + A·B = A`
- `A·(A+B) = A`
- `A + ¬A·B = A+B`
- `A·(¬A+B) = A·B`

Ad esempio, `A + A·B` vale 1 quando A vale 1; quando A vale 0 anche `A·B` vale 0. Perciò il secondo termine non cambia il risultato e `A + A·B = A`.

## De Morgan

\[
\overline{A+B}=\overline A\cdot\overline B
\]

\[
\overline{A\cdot B}=\overline A+\overline B
\]

La negazione di una OR diventa AND delle negazioni; la negazione di una AND diventa OR delle negazioni. Per più variabili, il principio si estende all'intera espressione, invertendo AND/OR e negando ogni termine.

## Dualità

Scambiando `+` con `·` e `0` con `1` in un'identità valida, si ottiene la sua identità duale. Per esempio, il duale di `A+0=A` è `A·1=A`. Questa regola è utile per ricordare e verificare famiglie di proprietà.

## Esempi di semplificazione

### Esempio 1 — assorbimento

`F = A + A·B = A`

### Esempio 2 — raccoglimento

`F = A·B + A·C = A·(B+C)`

### Esempio 3 — De Morgan

`F = ¬(A+B) = ¬A·¬B`

### Esempio 4 — distributiva

`F = A + B·C = (A+B)·(A+C)`

Una forma è migliore di un'altra secondo lo scopo: meno letterali può significare un circuito più semplice, ma la realizzazione fisica dipende anche da porte disponibili, ritardi e vincoli di progetto.

## Verifica con tabella della verità

Per provare un'identità costruisci una tabella con tutti gli ingressi e calcola entrambi i membri. Con due variabili ci sono `2² = 4` righe; con tre variabili `2³ = 8`. Se le colonne coincidono in ogni riga, le espressioni descrivono la stessa funzione.

Per minimizzare sistematicamente funzioni a poche variabili puoi usare le [mappe di Karnaugh](Mappe%20di%20Karnaugh.md). Dopo la minimizzazione, verifica la funzione ottenuta con la tabella originale.
