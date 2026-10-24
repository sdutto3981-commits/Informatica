# Funzioni in JavaScript

Una funzione raggruppa istruzioni che eseguono un compito e può essere riutilizzata più volte.

## Dichiarazione e chiamata

```javascript
function somma(a, b) {
  return a + b;
}

const risultato = somma(3, 4);
console.log(risultato); // 7
```

- `a` e `b` sono parametri.
- `3` e `4` sono argomenti della chiamata.
- `return` restituisce il risultato e termina la funzione.
- Se manca `return`, il risultato della chiamata è `undefined`.

## Funzione espressa e arrow function

```javascript
const doppio = function (n) {
  return n * 2;
};

const triplo = n => n * 3;
```

Le arrow function sono comuni nei callback degli eventi. Non sono identiche alle funzioni normali in tutti i contesti: per esempio non definiscono un proprio `this`.

## Ambito delle variabili

Una variabile dichiarata dentro una funzione è locale a quella funzione secondo le regole dello scope. Preferisci passare i valori come parametri invece di dipendere da variabili globali.

## Esempio: validare un numero

```javascript
function quadrato(n) {
  if (!Number.isFinite(n)) {
    return null;
  }
  return n * n;
}

console.log(quadrato(5)); // 25
```

Una funzione dovrebbe avere una responsabilità chiara. Provala con valori normali, limiti e input non validi.
