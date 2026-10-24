# Progetto: gioco semplice con JavaScript

Questo esempio implementa un gioco in cui bisogna trovare un numero da 1 a 10. Permette di esercitarsi con variabili, input, condizioni, funzioni, eventi e DOM.

```html
<label for="tentativo">Numero (1–10)</label>
<input id="tentativo" type="number" min="1" max="10">
<button id="controlla" type="button">Controlla</button>
<button id="nuova-partita" type="button">Nuova partita</button>
<p id="messaggio" aria-live="polite">Indovina il numero.</p>
```

```javascript
const campo = document.querySelector("#tentativo");
const messaggio = document.querySelector("#messaggio");
const controlla = document.querySelector("#controlla");
const nuovaPartita = document.querySelector("#nuova-partita");
let segreto = generaNumero();
let tentativi = 0;

function generaNumero() {
  return Math.floor(Math.random() * 10) + 1;
}

function verificaTentativo() {
  const valore = Number(campo.value);
  if (!campo.value || !Number.isInteger(valore) || valore < 1 || valore > 10) {
    messaggio.textContent = "Inserisci un intero da 1 a 10.";
    return;
  }
  tentativi++;
  if (valore === segreto) {
    messaggio.textContent = `Corretto in ${tentativi} tentativi!`;
  } else if (valore < segreto) {
    messaggio.textContent = "Troppo basso. Riprova.";
  } else {
    messaggio.textContent = "Troppo alto. Riprova.";
  }
}

function reset() {
  segreto = generaNumero();
  tentativi = 0;
  campo.value = "";
  messaggio.textContent = "Nuova partita: indovina il numero.";
  campo.focus();
}

controlla.addEventListener("click", verificaTentativo);
nuovaPartita.addEventListener("click", reset);
```

## Miglioramenti da provare

1. Limitare il numero massimo di tentativi.
2. Disabilitare il pulsante dopo una vittoria e riabilitarlo al reset.
3. Aggiungere punteggio o livelli di difficoltà.
4. Gestire l'invio con il tasto Invio usando un form.
5. Separare lo stato della partita dalla visualizzazione dei messaggi.

L'esempio usa `textContent`, così il messaggio viene mostrato come testo e non interpretato come HTML.
