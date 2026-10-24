# Form HTML — indice e flusso

Un form raccoglie dati dall'utente e li invia o li elabora. L'elemento `form` contiene i controlli; ogni controllo dovrebbe avere un'etichetta accessibile.

## Elementi e attributi

- `input`: campo il cui comportamento dipende da `type` (`text`, `email`, `number`, `date`, `checkbox`, `radio`, `password`, ecc.).
- `label`: etichetta associata al controllo con `for` e `id`, oppure avvolgendo il controllo.
- `textarea`: testo multilinea.
- `select` e `option`: selezione da un elenco.
- `button`: pulsante; specificare `type="submit"` per inviare oppure `type="button"` per azioni non di invio.
- `fieldset` e `legend`: raggruppano controlli correlati.
- `required`, `min`, `max`, `minlength`, `maxlength`, `pattern`: vincoli di validazione supportati dai controlli interessati.

## Esempio

```html
<form action="/contatti" method="post">
  <label for="email">Email</label>
  <input id="email" name="email" type="email" required autocomplete="email">
  <label for="messaggio">Messaggio</label>
  <textarea id="messaggio" name="messaggio" required></textarea>
  <button type="submit">Invia</button>
</form>
```

`name` determina il nome del dato inviato. `action` definisce la destinazione e `method` il metodo HTTP. `GET` trasporta normalmente i dati nella query URL e si adatta a ricerche; `POST` invia dati nel corpo della richiesta, ma **non** rende da solo una trasmissione sicura: per proteggere il trasporto serve HTTPS e il server deve validare i dati.

La validazione HTML aiuta l'utente, ma non sostituisce mai la verifica lato server.

Approfondimenti: [form e validazione HTML](Form%20e%20validazione%20HTML.md), [fieldset e legend](Elementi%20fielset%20e%20legend.md), [attributo action](Attributo%20Action.md) e [method](Attributo%20Method.md).
