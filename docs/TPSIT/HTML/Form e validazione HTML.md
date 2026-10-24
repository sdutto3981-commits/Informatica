# Form HTML e validazione degli input

I form raccolgono dati. Il contenitore `form` usa `action` per indicare la destinazione e `method` per il metodo HTTP. La gestione reale dei dati richiede un server, se il programma prevede invio remoto.

## Esempio

```html
<form action="/registrazione" method="post">
  <fieldset>
    <legend>Dati personali</legend>

    <label for="nome">Nome</label>
    <input id="nome" name="nome" type="text" required maxlength="50">

    <label for="email">Email</label>
    <input id="email" name="email" type="email" required>

    <label for="eta">Età</label>
    <input id="eta" name="eta" type="number" min="14" max="99">

    <button type="submit">Invia</button>
  </fieldset>
</form>
```

- `label` deve essere associata al campo tramite `for` e `id`, oppure contenendo il campo.
- `name` è la chiave usata per trasmettere il dato; `id` identifica l'elemento nel documento.
- `required`, `min`, `max`, `minlength`, `maxlength` e `pattern` aiutano la validazione nativa.
- `type="email"` controlla un formato di base, non garantisce che l'indirizzo esista.
- `fieldset` e `legend` raggruppano controlli correlati.

## `GET` e `POST`

- `GET` aggiunge i dati all'URL come parametri di query: è adatto a ricerche non sensibili.
- `POST` invia i dati nel corpo della richiesta: non cifra i dati da solo e richiede HTTPS per la protezione durante il trasporto.

Non inserire password o altri dati sensibili in query URL. La validazione nel browser migliora l'esperienza ma non sostituisce i controlli lato server: un client può essere modificato o aggirato.

## Errori comuni

- dimenticare `name` e ricevere un campo non trasmesso;
- usare `placeholder` al posto di un'etichetta permanente;
- associare `for` a un `id` inesistente;
- usare un pulsante `submit` per un'azione che non deve inviare il form;
- pensare che la validazione HTML sia una protezione di sicurezza completa.
