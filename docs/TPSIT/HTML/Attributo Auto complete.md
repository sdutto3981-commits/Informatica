# Attributo `autocomplete` nei form

L'attributo `autocomplete` suggerisce al browser se e come compilare un campo usando informazioni che l'utente ha salvato. Può essere specificato sul `form` o, quando serve, sul singolo controllo.

```html
<form action="/profilo" method="post" autocomplete="on">
  <label for="email">E-mail</label>
  <input id="email" name="email" type="email" autocomplete="email">

  <label for="nuova-password">Nuova password</label>
  <input id="nuova-password" name="new-password" type="password"
         autocomplete="new-password">
  <button type="submit">Salva</button>
</form>
```

## Valori e token comuni

- `on`: consente al browser di proporre il completamento automatico.
- `off`: richiede di non proporlo; il browser può comunque adottare comportamenti diversi per alcuni campi, per esempio quelli di autenticazione.
- `name`, `email`, `tel`, `street-address`, `postal-code`: identificano il tipo di informazione attesa.
- `current-password` e `new-password`: distinguono la password esistente da una da creare.
- `one-time-code`: codice temporaneo di verifica, se supportato dal browser.

Gli input devono avere un `name` significativo e una `label` associata. `autocomplete` migliora l'usabilità, ma non valida il dato e non garantisce che il browser compili un campo. Non raccogliere più dati personali del necessario; la sicurezza dei dati inviati dipende anche dal server e dal trasporto HTTPS.
