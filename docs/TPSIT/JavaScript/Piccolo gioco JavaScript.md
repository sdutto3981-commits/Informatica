# Esercizio: gioco di indovinare un numero

Questo esercizio integra variabili, condizioni, funzioni, eventi DOM e validazione dell'input. Il giocatore prova a indovinare un numero da 1 a 20.

## HTML

```html
<label for="tentativo">Numero (1–20)</label>
<input id="tentativo" type="number" min="1" max="20" step="1">
<button id="controlla" type="button">Controlla</button>
<button id="nuova-partita" type="button">Nuova partita</button>
<p id="esito" aria-live="polite"></p>
<p id="tentativi">Tentativi: 0</p>
<script src="gioco.js" defer></script>
```

## JavaScript (`gioco.js`)

```javascript
const campo = document.querySelector("#tentativo");
const controlla = document.querySelector("#controlla");
const nuovaPartita = document.querySelector("#nuova-partita");
const esito = document.querySelector("#esito");
const outputTentativi = document.querySelector("#tentativi");

let segreto;
let conteggio;
let terminato;

function inizializza() {
  segreto = Math.floor(Math.random() * 20) + 1;
  conteggio = 0;
  terminato = false;
  campo.value = "";
  esito.textContent = "Inserisci un numero da 1 a 20.";
  outputTentativi.textContent = "Tentativi: 0";
  controlla.disabled = false;
}

function verifica() {
  if (terminato) return;
  const valore = Number(campo.value);
  if (campo.value.trim() === "" || !Number.isInteger(valore) || valore < 1 || valore > 20) {
    esito.textContent = "Inserisci un intero valido tra 1 e 20.";
    return;
  }

  conteggio++;
  outputTentativi.textContent = `Tentativi: ${conteggio}`;
  if (valore === segreto) {
    esito.textContent = `Corretto! Hai indovinato in ${conteggio} tentativi.`;
    terminato = true;
    controlla.disabled = true;
  } else if (valore < segreto) {
    esito.textContent = "Troppo basso. Riprova.";
  } else {
    esito.textContent = "Troppo alto. Riprova.";
  }
}

controlla.addEventListener("click", verifica);
nuovaPartita.addEventListener("click", inizializza);
inizializza();
```

## Come estendere l'esercizio

- Limita il numero massimo di tentativi.
- Aggiungi un messaggio di vittoria o sconfitta.
- Permetti l'invio con il tasto Invio.
- Separa il conteggio, lo stato della partita e il rendering in funzioni dedicate.
- Prova input vuoti, decimali, numeri fuori intervallo e più click dopo la vittoria.

## Riferimento

[W3Schools — JavaScript Tutorial](https://www.w3schools.com/js/)
