# Numeri interi con segno

Un numero intero con segno deve rappresentare sia valori positivi sia negativi. La rappresentazione dipende dal numero di bit disponibile e dalla convenzione adottata.

## Modulo e segno

Con `n` bit, il bit più significativo rappresenta convenzionalmente il segno e i restanti `n−1` bit il modulo. Con 8 bit, `+5` è `00000101` e `−5` è `10000101`. Esiste una rappresentazione per `+0` e una per `−0`; questo e altre proprietà rendono la convenzione meno pratica.

## Complemento a due

La rappresentazione più comune per gli interi con segno a livello hardware è il complemento a due. Per ottenere il negativo di un valore positivo:

1. scrivi il modulo in binario sulla larghezza richiesta;
2. inverti tutti i bit;
3. aggiungi 1.

Su `n` bit l'intervallo è:

\[
-2^{n-1} \leq x \leq 2^{n-1}-1
\]

Con 8 bit: `−128 … +127`. Ad esempio `+5 = 00000101`, quindi `−5 = 11111011`.

## Overflow

La somma su una larghezza fissa può oltrepassare l'intervallo rappresentabile. In complemento a due, per esempio, `127 + 1` su 8 bit produce il pattern `10000000`, interpretato come −128: il risultato è in overflow. In esercizi e sistemi reali occorre distinguere il valore matematico dal pattern di bit memorizzato.
