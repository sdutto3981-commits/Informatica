# Promise, `async`/`await` e Fetch

Molte operazioni web sono asincrone: il programma avvia una richiesta e continua a eseguire altre attività invece di fermare tutto finché la risposta non arriva.

## Promise

Una `Promise` rappresenta il risultato futuro di un'operazione che può riuscire o fallire. Si gestisce con `then`, `catch` e, quando serve, `finally`.

## Fetch con `async`/`await`

```javascript
async function caricaDati() {
  try {
    const risposta = await fetch('/api/dati');
    if (!risposta.ok) {
      throw new Error(`HTTP ${risposta.status}`);
    }
    const dati = await risposta.json();
    return dati;
  } catch (errore) {
    console.error('Richiesta non riuscita', errore);
    throw errore;
  }
}
```

`await` si usa normalmente dentro una funzione `async` e attende la risoluzione della Promise senza bloccare il thread del browser. `fetch()` normalmente non rigetta la Promise soltanto perché il server risponde con status HTTP 404 o 500: controlla `response.ok` o `response.status`.

## Note operative

- Il percorso `/api/dati` è un segnaposto e deve essere sostituito da un endpoint reale.
- CORS, autenticazione, rete e server possono influire sul risultato.
- La gestione degli errori deve distinguere errori di rete, status HTTP non riusciti e dati non validi.
- Non esporre credenziali segrete in codice JavaScript inviato al browser.

## Riferimento

[W3Schools — JavaScript Asynchronous](https://www.w3schools.com/js/js_asynchronous.asp) · [JavaScript Fetch API](https://www.w3schools.com/js/js_api_fetch.asp)
