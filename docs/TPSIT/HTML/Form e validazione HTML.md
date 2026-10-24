# Form HTML e validazione

Un form raccoglie dati tramite controlli di input. L'HTML può eseguire controlli basilari nel browser; la validazione lato client **non sostituisce** la validazione lato server.

## Struttura

```html
<form action="/iscrizione" method="post">
  <div>
    <label for="nome">Nome</label>
    <input id="nome" name="nome" type="text" autocomplete="given-name" required>
  </div>
  <div>
    <label for="email">Email</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
  </div>
  <div>
    <label for="eta">Età</label>
    <input id="eta" name="eta" type="number" min="14" max="100">
  </div>
  <button type="submit">Invia</button>
</form>
```

## Attributi essenziali

- `action`: endpoint o URL a cui inviare il form.
- `method`: metodo HTTP; `get` mette normalmente i dati nella query string, `post` li invia nel corpo della richiesta.
- `name`: nome del campo trasmesso; senza `name` il controllo normalmente non contribuisce ai dati inviati.
- `id`: identificatore nel documento, usato anche per collegare `label` e input.
- `required`: rende obbligatorio il campo nel controllo del browser.
- `min`, `max`, `minlength`, `maxlength`, `pattern`: vincoli di validità specifici per il tipo di controllo.
- `autocomplete`: suggerisce al browser il tipo di dato atteso.

## Input comuni

`text`, `email`, `password`, `number`, `date`, `checkbox`, `radio`, `file`, `tel`, `url`, `search` e `hidden`. Scegli il tipo più adatto: `email` può offrire una tastiera mobile appropriata e un controllo di formato di base.

Per scelte multiple usa `select`; per testo esteso `textarea`; per raggruppare campi correlati usa `fieldset` con `legend`.

## Metodo GET e POST

GET è adatto a richieste che recuperano risorse e i dati possono comparire nell'URL, nella cronologia e nei log. POST invia i dati nel corpo della richiesta, ma **non è cifratura**: per proteggere il trasporto serve HTTPS e il server deve comunque verificare i dati.

## Buone pratiche

- Ogni controllo deve avere un'etichetta chiara.
- Spiega come correggere i campi non validi.
- Non affidarti a `required` o ai controlli del browser per proteggere un servizio.
- Non inviare password o dati riservati tramite HTTP non cifrato.

## Riferimento

[W3Schools — HTML Forms](https://www.w3schools.com/html/html_forms.asp)
