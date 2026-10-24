# Stringhe, numeri e date in JavaScript

## Stringhe

Le stringhe sono sequenze testuali. I template literal usano i backtick e supportano l'interpolazione.

```javascript
const nome = 'Ada';
const messaggio = `Ciao, ${nome}!`;
const normalizzato = '  Web Dev  '.trim().toLowerCase();
```

Metodi utili: `trim`, `toLowerCase`, `toUpperCase`, `includes`, `startsWith`, `endsWith`, `slice`, `replace` e `split`. Le stringhe sono immutabili: questi metodi restituiscono normalmente una nuova stringa.

## Numeri e Math

```javascript
const intero = Number('12');
const arrotondato = Math.round(3.6);  // 4
const minimo = Math.min(4, 8, 2);     // 2
const casuale = Math.floor(Math.random() * 10) + 1; // da 1 a 10
```

`Number()` converte; `parseInt()` e `parseFloat()` leggono una parte numerica iniziale secondo regole proprie. Controlla i risultati con `Number.isNaN()` e `Number.isFinite()` quando l'origine del dato non è certa.

`Math.random()` restituisce un numero pseudo-casuale nell'intervallo `[0, 1)`: è adatto a giochi semplici, non a scopi crittografici.

## Date

```javascript
const adesso = new Date();
console.log(adesso.toISOString());
console.log(adesso.getFullYear());
```

Le date JavaScript rappresentano un istante nel tempo; metodi diversi usano ora locale o UTC. Per serializzazione e scambi tra sistemi, ISO 8601 (`toISOString()`) è spesso una scelta utile. Non presumere che la formattazione locale sia identica tra dispositivi.

## Riferimento

[W3Schools — JavaScript String Methods](https://www.w3schools.com/js/js_string_methods.asp) · [JavaScript Math](https://www.w3schools.com/js/js_math.asp) · [JavaScript Dates](https://www.w3schools.com/js/js_dates.asp)
