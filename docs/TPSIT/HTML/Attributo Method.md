# Attributo `method` dei form

L'attributo `method` stabilisce il metodo HTTP usato per inviare un form.

- `GET`: i dati sono normalmente codificati nella query URL. È adatto a ricerche e operazioni che non modificano lo stato del server; l'URL può essere salvato o condiviso.
- `POST`: i dati vengono inviati nel corpo della richiesta; viene spesso usato per operazioni che creano o modificano dati.

```html
<form action="/contatti" method="post">
  <label for="email">Email</label>
  <input id="email" name="email" type="email" required>
  <button type="submit">Invia</button>
</form>
```

`POST` da solo non cifra i dati e non garantisce sicurezza. Per proteggere la comunicazione serve HTTPS; inoltre il server deve autenticare/autorizzare le operazioni e verificare gli input.
