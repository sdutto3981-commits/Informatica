# Introduzione a JavaScript

JavaScript è un linguaggio di programmazione usato nello sviluppo web per aggiungere comportamento e interazione. HTML descrive la struttura, CSS l'aspetto e JavaScript la logica dinamica.

## Collegare uno script

```html
<script src="app.js" defer></script>
```

Un file esterno facilita la manutenzione e il riuso del codice. Con uno script classico esterno, `defer` permette di eseguirlo dopo il parsing del documento HTML.

## Primo esempio

```javascript
const nome = "Ada";
console.log(`Ciao, ${nome}!`);
```

`console.log()` scrive nella console degli strumenti per sviluppatori; i template literal usano backtick e possono includere espressioni con `${...}`.

## Modificare una pagina

```html
<p id="messaggio">Testo iniziale</p>
<button id="cambia" type="button">Cambia</button>
<script src="app.js" defer></script>
```

```javascript
const testo = document.querySelector("#messaggio");
const pulsante = document.querySelector("#cambia");
pulsante.addEventListener("click", () => {
  testo.textContent = "Il contenuto è cambiato.";
});
```

Il browser costruisce un DOM con cui lo script può accedere agli elementi. L'evento `click` esegue la callback quando l'utente attiva il pulsante.

## Debugging di base

1. Apri gli strumenti per sviluppatori del browser.
2. Leggi gli errori in Console.
3. Verifica nomi e maiuscole/minuscole degli identificatori.
4. Controlla che gli elementi esistano prima di usarli.
5. Aggiungi breakpoint e osserva i valori durante l'esecuzione.

## Riferimento

[W3Schools — JavaScript Introduction](https://www.w3schools.com/js/js_intro.asp)
