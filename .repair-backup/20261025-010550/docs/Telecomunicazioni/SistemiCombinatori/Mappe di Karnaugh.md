# Mappe di Karnaugh

Una mappa di Karnaugh è una rappresentazione grafica della tabella di verità che aiuta a minimizzare una funzione booleana.

## Procedura

1. Costruisci la tabella della verità della funzione.
2. Riporta gli 1 nelle celle corrispondenti ai mintermini (per la forma somma di prodotti). Se richiesto, si possono minimizzare gli 0 per ottenere una forma prodotto di somme.
3. Raggruppa celle adiacenti in gruppi di dimensione potenza di 2: 1, 2, 4, 8, ...
4. I gruppi possono avvolgersi ai bordi della mappa; celle agli angoli possono essere adiacenti secondo l'ordinamento Gray.
5. Usa gruppi più grandi quando possibile e copri tutti gli 1 necessari. I gruppi possono sovrapporsi se semplifica il risultato.
6. Per ogni gruppo conserva solo le variabili che non cambiano; elimina quelle che cambiano valore.

## Regole importanti

- Le righe e le colonne seguono l'ordine Gray, per esempio `00, 01, 11, 10`, non il normale ordine binario.
- Ogni gruppo deve contenere un numero di celle pari a una potenza di due.
- È possibile usare condizioni indifferenti (`X` o don't care) solo se il problema le fornisce e se aiutano la semplificazione.
- Una variabile costante a 1 compare diretta nel termine; una variabile costante a 0 compare negata.

## Esempio breve

Se `F(A,B) = 1` per le combinazioni `01` e `11`, la variabile `B` è sempre 1 e `A` cambia. Quindi la funzione minimizzata è `F = B`.

Verifica la soluzione confrontando la tabella di verità della funzione iniziale con quella semplificata.
