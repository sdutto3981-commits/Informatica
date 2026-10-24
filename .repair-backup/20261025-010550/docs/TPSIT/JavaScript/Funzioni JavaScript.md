# Funzioni JavaScript

Una funzione raggruppa istruzioni riutilizzabili. Può ricevere parametri e restituire un valore con `return`.

```javascript
function somma(a, b) {
  return a + b;
}

const risultato = somma(3, 4); // 7
```

- Parametri formali: nomi presenti nella dichiarazione.
- Argomenti: valori forniti quando la funzione viene chiamata.
- `return`: termina quella chiamata e restituisce il risultato.
- Se manca `return`, il risultato della funzione è `undefined`.

## Funzione espressa e arrow function

```javascript
const quadrato = function (n) {
  return n * n;
};

const doppio = n => n * 2;
const sommaBreve = (a, b) => a + b;
```

Le arrow function hanno una semantica di `this` differente dalle funzioni tradizionali: questo diventa importante negli oggetti e nelle classi. Non sostituirle automaticamente a ogni metodo.

## Parametri predefiniti

```javascript
function saluta(nome = "utente") {
  return `Ciao, ${nome}!`;
}
```

## Scope e progettazione

Le funzioni possono leggere variabili accessibili nello scope, ma ricevere i dati necessari tramite parametri rende il comportamento più chiaro e facile da testare.

Una funzione dovrebbe avere una responsabilità comprensibile. Suddividi una funzione lunga in operazioni con nomi significativi.

## Riferimento

[W3Schools — JavaScript Functions](https://www.w3schools.com/js/js_functions.asp)
