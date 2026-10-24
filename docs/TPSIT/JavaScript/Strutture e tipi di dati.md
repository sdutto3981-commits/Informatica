# Tipi e valori JavaScript

JavaScript è dinamicamente tipizzato: una variabile può ricevere in momenti diversi valori di tipi differenti, anche se una buona progettazione mantiene i tipi coerenti quando possibile.

## Tipi primitivi principali

- `number`: numeri, interi e decimali; comprende `NaN`, `Infinity` e `-Infinity`.
- `string`: sequenze di caratteri.
- `boolean`: `true` o `false`.
- `undefined`: valore di una variabile dichiarata ma non inizializzata, o proprietà assente in alcune operazioni.
- `null`: assenza intenzionale di un valore oggetto; per un comportamento storico, `typeof null` restituisce `"object"`.
- `bigint`: interi di grandi dimensioni, con suffisso `n` nei letterali, per esempio `123n`.
- `symbol`: identificatore univoco usato in casi specifici.

Array, funzioni e oggetti sono valori di tipo oggetto o categorie correlate; non sono tipi primitivi.

## Conversioni

```javascript
Number("12");       // 12
Number("ciao");     // NaN
String(12);          // "12"
Boolean(0);          // false
Boolean("testo");   // true
```

`Number()` tenta di convertire un valore in numero. `String()` produce una rappresentazione testuale. `Boolean()` converte secondo le regole di truthiness: valori come `0`, `NaN`, `""`, `null` e `undefined` diventano false; la maggior parte degli altri valori diventa true.

## Confronto stretto

Usa in genere `===` e `!==` per evitare conversioni automatiche in fase di confronto.

```javascript
2 === 2;   // true
2 === "2"; // false
2 == "2";  // true, per conversione implicita
```

## Array e oggetti

```javascript
const colori = ["rosso", "verde"];
const persona = { nome: "Ada", eta: 20 };
```

Gli array conservano elementi in una sequenza indicizzata; gli oggetti associano proprietà a valori. Per approfondire consulta [Array e oggetti JavaScript](Array%20e%20oggetti%20JavaScript.md).

## Riferimento

[W3Schools — JavaScript Data Types](https://www.w3schools.com/js/js_datatypes.asp)
