# Pulsante o collegamento?

Per spostare l'utente verso un'altra pagina o risorsa si usa un collegamento `<a href="...">`. Per eseguire un'azione nella pagina (aprire una finestra, aggiornare un contatore, inviare un comando) si usa un pulsante `<button>`.

```html
<a class="pulsante" href="progetti.html">Vai ai progetti</a>
<button type="button" id="salva">Salva impostazioni</button>
```

Il link rimane un link anche se viene stilizzato con CSS per sembrare un pulsante. Questo mantiene il comportamento corretto con apertura in una nuova scheda, copia dell'indirizzo e tecnologie assistive.

```css
.pulsante {
  display: inline-block;
  padding: 0.6rem 1rem;
  border-radius: 0.4rem;
  text-decoration: none;
  background: #2457a7;
  color: white;
}
```

Se un pulsante si trova dentro un form, specifica il tipo: `type="submit"` invia il form, `type="reset"` ripristina i campi e `type="button"` non invia automaticamente. Non creare link fittizi con `href="#"` per simulare un'azione.
