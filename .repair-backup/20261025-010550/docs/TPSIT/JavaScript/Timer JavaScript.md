# Timer JavaScript: `setTimeout` e `setInterval`

I timer pianificano una callback dopo un intervallo minimo indicativo. Il browser può ritardarne l'esecuzione in base al carico, alla scheda inattiva e alle regole del sistema; non sono timer real-time.

## `setTimeout`

```javascript
const timeoutId = setTimeout(() => {
  console.log("Eseguito dopo circa un secondo");
}, 1000);

// Per annullare prima dell'esecuzione:
// clearTimeout(timeoutId);
```

## `setInterval`

```javascript
let secondi = 0;
const intervalId = setInterval(() => {
  secondi++;
  console.log(secondi);
  if (secondi >= 5) clearInterval(intervalId);
}, 1000);
```

`setInterval()` richiede di essere fermato con `clearInterval()` quando non serve più, per esempio quando termina un gioco o viene smontata una vista.

## Contatore visuale e limiti

Un timer grafico non dovrebbe presupporre che ogni callback arrivi esattamente ogni 1000 ms. Per misurare tempo trascorso con più precisione, confronta `performance.now()` o un riferimento temporale invece di sommare soltanto un secondo per callback.

```javascript
const inizio = performance.now();
setTimeout(() => {
  const trascorso = (performance.now() - inizio) / 1000;
  console.log(`Secondi trascorsi: ${trascorso.toFixed(2)}`);
}, 1000);
```

## Riferimento

[W3Schools — JavaScript Timing Events](https://www.w3schools.com/js/js_timing.asp)
