# DOM ed eventi JavaScript

Il DOM (*Document Object Model*) rappresenta la pagina come una struttura di nodi accessibili e modificabili tramite JavaScript.

## Selezionare e aggiornare elementi

```html
<p id="stato">Pronto</p>
<button id="azione" type="button">Avvia</button>
```

```javascript
const stato = document.querySelector("#stato");
const azione = document.querySelector("#azione");

azione.addEventListener("click", () => {
  stato.textContent = "Pulsante premuto";
  stato.classList.add("attivo");
});
```

- `querySelector()` restituisce il primo elemento che corrisponde al selettore oppure `null`.
- `textContent` aggiorna il testo senza interpretarlo come HTML.
- `classList.add()`, `remove()` e `toggle()` gestiscono le classi CSS.

## Eventi

Un evento è una notifica di un'azione, per esempio `click`, `input`, `change`, `submit` o `keydown`.

```javascript
const campo = document.querySelector("#nome");
campo.addEventListener("input", event => {
  console.log(event.target.value);
});
```

`event.target` indica l'elemento che ha originato l'evento; `event.currentTarget` indica l'elemento a cui è collegato il gestore.

## Prevenire il comportamento predefinito

```javascript
form.addEventListener("submit", event => {
  event.preventDefault();
  // Controlli prima di elaborare i dati
});
```

Usa `preventDefault()` solo quando l'applicazione deve sostituire il comportamento standard. Se si inserisce JavaScript in una pagina con elementi generati dinamicamente, verifica che i selettori vengano eseguiti quando gli elementi sono già presenti, per esempio usando uno script con `defer`.

## Sicurezza e robustezza

Preferisci `textContent` quando visualizzi testo inserito dall'utente. `innerHTML` interpreta markup e può introdurre vulnerabilità se usato con dati non fidati. Controlla che un selettore non restituisca `null` prima di accedere alle proprietà dell'elemento.
