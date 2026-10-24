# Dichiarazioni e ambito in JavaScript

```javascript
const massimo = 100;
let tentativi = 0;
tentativi++;
console.log(typeof tentativi); // "number"
```

`const` richiede un'inizializzazione al momento della dichiarazione. `let` può essere dichiarata e assegnata in seguito, ma non va letta prima dell'inizializzazione.

## Scope di blocco

```javascript
if (true) {
  const messaggio = "Dentro il blocco";
  console.log(messaggio);
}
// messaggio non è visibile qui
```

`let` e `const` hanno scope di blocco. Evita dichiarazioni globali non necessarie: rendono il codice più difficile da mantenere e possono entrare in conflitto con altri script.

## Conversione esplicita

```javascript
const testo = "100";
const numero = Number(testo);
const testoNuovo = String(numero);
```

Attenzione al nome della variabile: `myVariable.toString()` funziona soltanto se `myVariable` è stata dichiarata e contiene un valore che supporta quel metodo.
