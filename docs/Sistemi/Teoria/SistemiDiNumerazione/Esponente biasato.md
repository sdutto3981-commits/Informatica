# Esponente biasato

Nelle rappresentazioni in virgola mobile come IEEE 754, l'esponente viene memorizzato spesso come **esponente biasato** (*biased exponent*). Si somma una costante detta *bias* all'esponente reale, così il campo memorizzato è non negativo per gli esponenti che devono essere rappresentati.

## Formula

\[
E_{memorizzato} = E_{reale} + bias
\]

\[
E_{reale} = E_{memorizzato} - bias
\]

Per il formato IEEE 754 binary32 (singola precisione) il campo esponente ha 8 bit e il bias è 127. Per binary64 (doppia precisione) il campo ha 11 bit e il bias è 1023.

## Esempio binary32

Se l'esponente reale è `+3`, il valore memorizzato è `3 + 127 = 130`, cioè `10000010₂`.

Se il campo contiene 130, l'esponente reale è `130 - 127 = +3`.

## Eccezioni importanti

In IEEE 754, gli esponenti tutti zero e tutti uno sono riservati a casi speciali: zero/subnormali nel primo caso e infinito/NaN nel secondo. Quindi il semplice calcolo del bias non basta a classificare ogni sequenza di bit. La codifica esatta va sempre letta insieme al formato e ai suoi campi segno, esponente e frazione.
