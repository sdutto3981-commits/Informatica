# DOM ed eventi JavaScript

Il DOM rappresenta il documento HTML come una struttura di nodi e oggetti. JavaScript può selezionare elementi, modificarne il contenuto, aggiornare attributi e reagire agli eventi.

## Selezionare e modificare elementi

```javascript
const titolo = document.querySelector("h1");
if (titolo !== null) {
  titolo.textContent = "Titolo aggiornato";
  titolo.classList.add("evidenziato");
}
```

- `querySelector()` restituisce il primo elemento che corrisponde al selettore oppure `null`.
- `querySelectorAll()` restituisce una NodeList con gli elementi corrispondenti.
- `textContent` legge o scrive testo.
- `classList.add()`, `remove()`, `toggle()` e `contains()` gestiscono classi CSS.
- `setAttribute()` e le proprietà DOM permettono di lavorare con attributi e valori.

## Eventi

```html
<button id="azione" type="button">Esegui</button>
<p id="stato" aria-live="polite"></p>
```

```javascript
const pulsante = document.querySelector("#azione");
const stato = document.querySelector("#stato");

pulsante?.addEventListener("click", event => {
  stato.textContent = "Hai attivato il pulsante.";
});
```

`addEventListener()` associa una callback senza sovrascrivere gli altri listener. L'oggetto evento contiene informazioni sull'evento; `event.target` indica l'origine dell'evento, mentre `event.currentTarget` indica l'elemento al quale è collegato il listener.

## `preventDefault()`

Per un form, il comportamento standard è inviare i dati. `event.preventDefault()` lo impedisce, per esempio se vuoi verificare i campi con JavaScript prima di gestire l'azione.

## Sicurezza

Per visualizzare testo inserito dall'utente, preferisci `textContent`. Inserire input non attendibile in `innerHTML` può creare vulnerabilità XSS. Non associare codice tramite stringhe in attributi `onclick`; usa listener e funzioni.

## Riferimento

[W3Schools — JavaScript HTML DOM](https://www.w3schools.com/js/js_htmldom.asp) · [JavaScript Events](https://www.w3schools.com/js/js_events.asp)
