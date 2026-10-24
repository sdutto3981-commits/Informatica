# Form e validazione con JavaScript

La validazione migliora l'esperienza utente fornendo feedback immediato, ma il server deve controllare nuovamente ogni dato ricevuto.

```html
<form id="form-contatto">
  <label for="email">Email</label>
  <input id="email" name="email" type="email" required>
  <button type="submit">Invia</button>
  <p id="feedback" role="status"></p>
</form>
```

```javascript
const form = document.querySelector("#form-contatto");
const email = document.querySelector("#email");
const feedback = document.querySelector("#feedback");

form.addEventListener("submit", event => {
  event.preventDefault();
  if (!form.reportValidity()) return;

  feedback.textContent = `Indirizzo inserito: ${email.value.trim()}`;
});
```

## API di validazione

- `required`: richiede un valore.
- `type="email"`, `type="url"`, `min`, `max`, `minlength`, `maxlength` e `pattern` applicano vincoli nativi.
- `checkValidity()` restituisce un booleano.
- `reportValidity()` verifica i campi e può mostrare i messaggi del browser.
- `setCustomValidity(messaggio)` imposta un messaggio personalizzato; per rimuoverlo usa `setCustomValidity("")`.

## Buone pratiche

- Spiega il problema in modo specifico e vicino al campo.
- Non usare colore rosso come unica indicazione di errore.
- Non fidarti dei valori inviati dal browser: i client possono essere modificati o aggirati.
- Non mostrare o registrare dati sensibili nelle console durante la produzione.

## Riferimento

[W3Schools — JavaScript Form Validation](https://www.w3schools.com/js/js_validation.asp)
