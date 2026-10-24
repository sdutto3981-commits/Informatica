# JavaScript

JavaScript aggiunge comportamento alle pagine web: reagisce agli eventi, legge dati dai form, aggiorna il DOM e gestisce timer. Nei browser viene eseguito da un motore JavaScript.

## Percorso di studio

1. [Introduzione](Introduzione%20JavaScript.md)
2. [Variabili e dichiarazioni](Variabili%20js.md) · [tipi e valori](Strutture%20e%20tipi%20di%20dati.md)
3. [Operatori e controllo del flusso](Operatori%20di%20controllo%20js.md)
4. [Funzioni](Funzioni%20JavaScript.md)
5. [Array e oggetti](Array%20e%20oggetti%20JavaScript.md)
6. [Stringhe, numeri e date](Stringhe%20numeri%20e%20date%20JavaScript.md)
7. [JSON e Web Storage](JSON%20e%20Web%20Storage%20JavaScript.md)
8. [Classi e moduli](Classi%20e%20moduli%20JavaScript.md)
9. [Promise, async/await e Fetch](Promise%20async%20e%20fetch%20JavaScript.md)
10. [DOM ed eventi](DOM%20ed%20eventi.md)
11. [Form e validazione](Form%20e%20validazione%20JavaScript.md)
12. [Timer](Timer%20JavaScript.md)
13. [Errori e debugging](Gestione%20errori%20JavaScript.md) · [strumenti di debug](Debug%20JavaScript.md)
14. [Esercizio: piccolo gioco](Piccolo%20gioco%20JavaScript.md)

## Esempio

```html
<button id="azione" type="button">Premi</button>
<p id="risultato" aria-live="polite">In attesa</p>
<script src="app.js" defer></script>
```

```javascript
const azione = document.querySelector("#azione");
const risultato = document.querySelector("#risultato");
azione.addEventListener("click", () => {
  risultato.textContent = "Evento ricevuto";
});
```

## Concetti da ricordare

- `const` impedisce la riassegnazione del binding; non rende automaticamente immutabile un oggetto.
- `===` e `!==` confrontano senza conversione automatica dei tipi.
- `querySelector()` può restituire `null` se non trova un elemento.
- Usa `textContent` per inserire testo fornito dall'utente; `innerHTML` richiede maggiore attenzione per evitare injection.

## Fonte di approfondimento

[W3Schools — JavaScript Tutorial](https://www.w3schools.com/js/)
