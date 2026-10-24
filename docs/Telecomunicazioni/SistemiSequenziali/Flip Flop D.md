# Flip-flop D

Il flip-flop D memorizza il valore dell'ingresso `D` al fronte attivo del clock. Tra un fronte attivo e il successivo l'uscita `Q` mantiene il valore memorizzato.

## Tabella caratteristica

Per un flip-flop attivato sul fronte di salita:

| Fronte del clock | D | Q successivo |
|---|---:|---:|
| Fronte di salita | 0 | 0 |
| Fronte di salita | 1 | 1 |
| Nessun fronte attivo | X | Q precedente |

`X` significa che in quella riga l'ingresso può avere qualunque valore: senza fronte attivo non viene campionato.

La relazione caratteristica si scrive `Q(t+1) = D` al fronte attivo. Se il dispositivo è attivato sul fronte di discesa, l'aggiornamento avviene al fronte opposto. Simbolo, pallino e triangolo del clock indicano la modalità secondo la convenzione grafica adottata.

## Differenza tra latch e flip-flop

Un latch sensibile al livello può seguire l'ingresso quando il segnale di abilitazione è attivo; un flip-flop edge-triggered campiona al fronte del clock. Non confondere il fronte di salita con quello di discesa.

## Applicazioni

- memorizzazione di un bit;
- registri composti da più flip-flop;
- sincronizzazione e pipeline digitali (con le cautele di progetto appropriate).
