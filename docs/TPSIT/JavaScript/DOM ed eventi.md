# DOM ed eventi in JavaScript

Il **DOM** (Document Object Model) rappresenta il documento HTML come una struttura di nodi accessibile tramite JavaScript. Si può selezionare un elemento, leggerne o modificarne il contenuto e reagire alle azioni dell'utente.

## Selezionare e modificare elementi

```javascript
const titolo = document.querySelector("h1");
if (titolo !== null) {
  titolo.textContent = "Titolo aggiornato";
  titolo.classList.add("evidenziato");
}
```

- `querySelector()` restituisce il primo elemento che corrisponde al selettore, oppure `null`.
- `textContent` modifica il testo; `classList` gestisce le classi CSS.
- Per testo digitato dall'utente preferisci `textContent` a `innerHTML`, che interpreta markup HTML.

## Event listener

```html
<button id="conta" type="button">Incrementa</button>
<p id="valore" aria-live="polite">0</p>
<script src="app.js" defer></script>
```

```javascript
let conteggio = 0;
const pulsante = document.querySelector("#conta");
const valore = document.querySelector("#valore");

if (pulsante !== null) {
  pulsante.addEventListener("click", () => {
    conteggio += 1;
    if (valore !== null) valore.textContent = String(conteggio);
  });
}
```

`addEventListener()` collega una funzione a un evento, per esempio `click`, `input` o `submit`. Il punto interrogativo `?.` evita la chiamata se il riferimento è `null`; usarlo non elimina la necessità di capire perché un elemento potrebbe mancare.

## Form e validazione

```javascript
const form = document.querySelector("#form-contatto");
form?.addEventListener("submit", (evento) => {
  evento.preventDefault();
  // Leggi i campi, verifica i dati e mostra un esito comprensibile.
});
```

`preventDefault()` impedisce l'azione predefinita solo quando il programma la gestisce intenzionalmente. I campi devono avere etichette accessibili e gli errori vanno descritti anche in testo.

## Timer

```javascript
const idTimer = setInterval(() => {
  console.log("Un secondo");
}, 1000);

// Quando il timer non serve più:
clearInterval(idTimer);
```

`setInterval` ripete una funzione approssimativamente ogni intervallo specificato; non è una garanzia di precisione assoluta. Conserva l'identificatore per poter fermare il timer.
