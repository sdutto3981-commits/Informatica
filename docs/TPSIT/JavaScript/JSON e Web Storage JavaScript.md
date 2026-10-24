# JSON e Web Storage in JavaScript

## JSON

JSON è un formato testuale usato per rappresentare dati strutturati. Non è la stessa cosa di un oggetto JavaScript, anche se i due formati sono simili.

```javascript
const persona = { nome: 'Ada', eta: 20 };
const testo = JSON.stringify(persona);
const ricostruita = JSON.parse(testo);
```

`JSON.stringify()` produce una stringa JSON; `JSON.parse()` la converte in un valore JavaScript e può lanciare `SyntaxError` se il testo non è valido.

```javascript
try {
  const dati = JSON.parse(testoRicevuto);
  console.log(dati);
} catch (errore) {
  console.error('JSON non valido');
}
```

Dopo il parsing, valida comunque la struttura e i tipi attesi: JSON sintatticamente valido non significa che i dati siano corretti o sicuri per l'applicazione.

## `localStorage`

Web Storage può memorizzare coppie chiave-valore nel browser. `localStorage` mantiene i dati tra sessioni e salva valori testuali; `sessionStorage` mantiene i dati per la sessione della scheda.

```javascript
localStorage.setItem('tema', 'scuro');
const tema = localStorage.getItem('tema');
localStorage.removeItem('tema');
```

Per salvare strutture dati, convertili in JSON. Lo storage può essere non disponibile o generare errori in certi contesti, quindi in progetti più robusti va gestito con controlli.

## Sicurezza

Non memorizzare in Web Storage password, token di sessione sensibili o segreti: gli script che possono eseguire nella stessa origine possono potenzialmente leggere quei dati. I dati recuperati dallo storage devono essere considerati input non fidato.

## Riferimento

[W3Schools — JavaScript JSON](https://www.w3schools.com/js/js_json.asp) · [Web Storage API](https://www.w3schools.com/js/js_api_web_storage.asp)
