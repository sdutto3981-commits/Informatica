# Timer in JavaScript: setTimeout e setInterval

JavaScript mette a disposizione funzioni per pianificare l'esecuzione di codice nel tempo.

## `setTimeout`

Esegue una callback una volta dopo il ritardo indicato in millisecondi.

```javascript
const idTimeout = setTimeout(() => {
  console.log("Sono trascorsi circa due secondi");
}, 2000);

// Per annullare prima dell'esecuzione:
// clearTimeout(idTimeout);
```

## `setInterval`

Ripete una callback a intervalli indicativi finché non viene annullata.

```javascript
let secondi = 0;
const idIntervallo = setInterval(() => {
  secondi++;
  console.log(secondi);
  if (secondi >= 5) {
    clearInterval(idIntervallo);
    console.log("Timer terminato");
  }
}, 1000);
```

- `clearInterval(id)` arresta un intervallo.
- Memorizza l'identificatore restituito dal timer.
- I ritardi non sono scadenze precise: il browser può eseguire la callback più tardi se il thread è occupato o la scheda è sospesa.
- Per un cronometro visualizzato, calcola il tempo trascorso usando un riferimento temporale come `Date.now()` o `performance.now()` invece di assumere che ogni callback sia puntuale.

## Importante

Ferma i timer quando non servono più, per esempio quando termina un gioco o si abbandona una schermata. Timer dimenticati possono creare esecuzioni duplicate e comportamenti inattesi.
