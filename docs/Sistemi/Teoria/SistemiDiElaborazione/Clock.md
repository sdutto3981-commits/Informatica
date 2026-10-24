# Clock del calcolatore

Il **clock** è un segnale periodico usato da molte parti sincronizzate del calcolatore per coordinare i cambiamenti di stato. Il periodo è la durata di un ciclo, mentre la frequenza indica quanti cicli avvengono in un secondo.

## Frequenza e periodo

Le grandezze sono legate da:

\[
f = \frac{1}{T} \qquad T = \frac{1}{f}
\]

- `f` è la frequenza, misurata in hertz (Hz).
- `T` è il periodo, misurato in secondi.
- `1 GHz = 10^9 Hz`.

**Esempio:** un clock da 2,5 GHz ha un periodo nominale di `1 / (2,5 × 10^9) = 0,4 ns`.

## Cosa non significa la frequenza

Una CPU a frequenza più alta non è sempre più veloce di una CPU diversa: contano anche istruzioni eseguite per ciclo (IPC), numero di core, cache, architettura, memoria, limiti termici e tipo di carico. I processori moderni possono variare dinamicamente la frequenza.

## Clock e circuiti sequenziali

Nei circuiti sincroni, flip-flop e registri aggiornano lo stato in corrispondenza del fronte attivo (salita o discesa, secondo il componente). I segnali devono rispettare i tempi di setup e hold rispetto al fronte di clock; violazioni possono causare metastabilità o risultati imprevedibili.
