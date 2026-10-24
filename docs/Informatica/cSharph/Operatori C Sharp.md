# Operatori C#

## Aritmetici

| Operatore | Significato |
|---|---|
| `+`, `-` | addizione e sottrazione |
| `*`, `/` | moltiplicazione e divisione |
| `%` | resto della divisione intera o operazione di resto numerico |
| `++`, `--` | incremento e decremento |

Se entrambi gli operandi di `/` sono interi, il risultato è intero e la parte decimale viene scartata: `7 / 2` produce `3`; `7.0 / 2` produce `3.5`.

## Assegnazione

`=`, `+=`, `-=`, `*=`, `/=`, `%=` assegnano un valore o aggiornano una variabile. `x += 3` equivale a `x = x + 3` per gli usi ordinari.

## Confronto e logica

| Operatori | Significato |
|---|---|
| `==`, `!=` | uguaglianza e disuguaglianza |
| `<`, `>`, `<=`, `>=` | confronti relazionali |
| `&&`, `||`, `!` | AND, OR e NOT logici |

`&&` e `||` usano la valutazione con cortocircuito: il secondo operando può non essere valutato se il risultato è già determinato.

## Altri operatori frequenti

- `condition ? valore1 : valore2`: operatore condizionale.
- `??`: restituisce il lato destro se quello sinistro è `null`.
- `?.`: accesso condizionale quando il riferimento può essere `null`.
- `is`: verifica il tipo o un pattern.
- `as`: tenta una conversione compatibile verso un tipo riferimento o nullable.

## Precedenza

La precedenza stabilisce l'ordine delle operazioni. Quando espressioni complesse diventano difficili da leggere, aggiungi parentesi per rendere esplicita l'intenzione.

## Riferimento

[W3Schools — C# Operators](https://www.w3schools.com/cs/cs_operators.php)
