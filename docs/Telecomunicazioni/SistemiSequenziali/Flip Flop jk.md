# Flip-flop JK

Il flip-flop **JK** è una variante del flip-flop SR che elimina la combinazione proibita tipica della versione SR sincrona. Al fronte attivo del clock, gli ingressi `J` e `K` selezionano mantenimento, reset, set o commutazione.

## Tabella caratteristica

| J | K | Q(t+1) | Comportamento |
|---:|---:|---:|---|
| 0 | 0 | Q(t) | Mantiene lo stato |
| 0 | 1 | 0 | Reset |
| 1 | 0 | 1 | Set |
| 1 | 1 | ¬Q(t) | Commutazione (*toggle*) |

L'equazione caratteristica è:

\[
Q(t+1) = J\,\overline{Q(t)} + \overline{K}\,Q(t)
\]

Il simbolo `¬Q(t)` o `Q̅(t)` indica la negazione del valore precedente; non è una sottrazione.

## Aspetti temporali

La tabella vale all'istante di aggiornamento previsto dal componente. Devi distinguere lo stato precedente `Q(t)` dallo stato successivo `Q(t+1)`, e controllare se il fronte attivo è quello di salita o di discesa. I dispositivi reali hanno inoltre tempi di setup/hold e possono avere ingressi asincroni di preset e clear.
