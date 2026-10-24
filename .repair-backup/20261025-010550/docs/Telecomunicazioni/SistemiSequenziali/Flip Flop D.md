# Flip-flop D

Il flip-flop D memorizza il valore dell'ingresso `D` al fronte attivo del clock. Tra due fronti attivi, l'uscita `Q` mantiene lo stato memorizzato (salvo eventuali ingressi asincroni di set/reset, se presenti nel componente).

Per un flip-flop attivato sul fronte di salita:

| Fronte di clock | D | Q dopo il fronte |
|---|---:|---:|
| salita `↑` | 0 | 0 |
| salita `↑` | 1 | 1 |
| nessun fronte attivo | X | mantiene il valore precedente |

`X` indica “non importa” in quella riga perché il valore di `D` non viene campionato senza un fronte attivo. Un cerchio sul simbolo del clock indica normalmente un ingresso attivo basso/una negazione, ma va interpretato secondo il simbolo elettrico completo.

## Equazione caratteristica

Al fronte attivo, `Q(t+1) = D`. La funzione del D è rendere semplice il trasferimento di un bit all'uscita e il suo mantenimento fino al successivo fronte attivo.

Un latch D è diverso: è sensibile a un livello di abilitazione, non soltanto al fronte del clock.
