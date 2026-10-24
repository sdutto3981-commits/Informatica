# Dichiarazioni, assegnazioni e blocchi JavaScript

Dichiarare una variabile significa introdurre un nome; assegnare significa darle un valore.

```javascript
let prezzo;        // dichiarazione
prezzo = 12.5;     // assegnazione
prezzo = prezzo + 2;
const iva = 0.22;  // dichiarazione e inizializzazione
```

Una variabile `const` deve essere inizializzata quando viene dichiarata e non può essere riassegnata. Con `let`, è possibile dichiarare e inizializzare separatamente.

## Blocco di codice

Le parentesi graffe racchiudono un blocco, per esempio nel corpo di una condizione o di un ciclo.

```javascript
const x = 2;
if (x === 2) {
  const messaggio = "x vale due";
  console.log(messaggio);
}
```

Le variabili `let` e `const` dichiarate nel blocco non sono accessibili al di fuori di esso. Evita di usare la stessa variabile per dati concettualmente differenti solo perché il linguaggio lo permette.

## Conversione esplicita

```javascript
const testo = "42";
const numero = Number(testo);
const numeroComeTesto = numero.toString();
```

`Number("42")` produce `42`; `Number("ciao")` produce `NaN`, che indica un risultato numerico non valido. Per verificare `NaN` usa `Number.isNaN(valore)`.

## Riferimento

[W3Schools — JavaScript Let](https://www.w3schools.com/js/js_let.asp) · [JavaScript Const](https://www.w3schools.com/js/js_const.asp)
