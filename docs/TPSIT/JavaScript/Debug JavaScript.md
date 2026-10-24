# Debugging JavaScript

Il debugging serve a individuare la causa di un comportamento errato. Gli strumenti per sviluppatori del browser mettono a disposizione Console, Sources/Debugger, Network e ispezione del DOM.

## Procedura

1. Riproduci l'errore con passaggi chiari.
2. Leggi il primo messaggio di errore nella console.
3. Individua la riga indicata e controlla i valori usati.
4. Imposta un breakpoint ed esegui il codice passo-passo.
5. Controlla scope, tipo dei dati, valori `null`/`undefined` e flusso degli eventi.
6. Correggi una causa alla volta e ripeti il test.

## Console

```javascript
const prezzo = 12;
console.log("prezzo:", prezzo);
console.table([{ nome: "Ada", voto: 8 }, { nome: "Luca", voto: 7 }]);
console.warn("Messaggio di attenzione");
console.error("Messaggio di errore");
```

Non lasciare nel codice pubblicato log che espongono password, token, dati personali o dettagli interni.

## Errori frequenti

- `ReferenceError`: identificatore non disponibile nel contesto attuale.
- `TypeError`: operazione non supportata dal valore, ad esempio chiamare come funzione qualcosa che non lo è.
- `SyntaxError`: codice non valido per il parser.
- Errore logico: il codice viene eseguito, ma il risultato non è quello atteso.

## Riferimento

[W3Schools — JavaScript Debugging](https://www.w3schools.com/js/js_debugging.asp)
