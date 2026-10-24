# Form e validazione con JavaScript

La validazione lato client può mostrare errori chiari prima dell'invio. Non sostituisce la validazione server quando i dati vengono inviati a un servizio.

## Esempio

```html
<form id="form-iscrizione">
  <label for="email">Email</label>
  <input id="email" name="email" type="email" required>
  <button type="submit">Invia</button>
  <p id="esito" role="status"></p>
</form>
```

```javascript
const form = document.querySelector("#form-iscrizione");
const email = document.querySelector("#email");
const esito = document.querySelector("#esito");

form.addEventListener("submit", event => {
  event.preventDefault();
  if (!email.checkValidity()) {
    esito.textContent = "Inserisci un indirizzo email valido.";
    email.focus();
    return;
  }
  esito.textContent = "Dati controllati: puoi proseguire.";
});
```

Gli attributi HTML come `required`, `type="email"`, `min`, `max`, `minlength` e `pattern` possono offrire controlli nativi. JavaScript può usare `checkValidity()` e `reportValidity()`.

## Linee guida

- Leggi `.value` dai campi; per ripulire spazi iniziali/finali, usa `trim()`.
- Mostra l'errore vicino al campo e con un messaggio testuale.
- Non considerare regolari espressioni o controlli nel browser come una garanzia di sicurezza.
- Non inserire i dati sensibili nei messaggi di errore o nei log senza necessità.
- Sul server convalida nuovamente tutti i dati prima di salvarli o usarli.
