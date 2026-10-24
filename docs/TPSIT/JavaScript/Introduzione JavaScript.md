# Introduzione a JavaScript

JavaScript è un linguaggio che aggiunge comportamento alle pagine web. HTML definisce la struttura, CSS la presentazione e JavaScript la logica interattiva.

## Inserimento nella pagina

È consigliabile tenere il codice in un file esterno:

```html
<script src="app.js" defer></script>
```

`defer` fa eseguire lo script dopo il parsing del documento HTML.

## Primo esempio

```javascript
const nome = "Ada";
console.log(`Ciao, ${nome}!`);
```

- `const` impedisce la riassegnazione del binding; l'oggetto eventualmente contenuto può comunque essere mutabile.
- `let` si usa quando il binding deve essere riassegnato.
- `console.log()` scrive nella console degli strumenti per sviluppatori.
- JavaScript distingue maiuscole e minuscole.

## Interazione con il DOM

```html
<p id="messaggio">Testo iniziale</p>
<button id="azione" type="button">Cambia testo</button>
<script src="app.js" defer></script>
```

```javascript
const messaggio = document.querySelector("#messaggio");
const azione = document.querySelector("#azione");
azione.addEventListener("click", () => {
  messaggio.textContent = "Pulsante premuto.";
});
```

## Verifica del codice

1. Apri la pagina nel browser.
2. Consulta la console degli strumenti per sviluppatori.
3. Controlla che gli elementi selezionati esistano.
4. Prova anche input vuoti e casi limite.

Prosegui con [tipi e strutture dati](Strutture%20e%20tipi%20di%20dati.md) e [DOM ed eventi](DOM%20ed%20eventi.md).
