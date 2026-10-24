# Tipi e strutture di dati in JavaScript

JavaScript è tipizzato dinamicamente: una variabile può riferirsi a valori di tipi diversi nel corso dell'esecuzione. I tipi primitivi includono `string`, `number`, `bigint`, `boolean`, `undefined`, `symbol` e `null` (con una particolarità storica di `typeof null`). Oggetti, array e funzioni sono tipi riferimento.

## Conversioni

```javascript
Number("10");    // 10
Number("ciao");  // NaN
Number(null);     // 0
Number(false);    // 0
Number(true);     // 1
String(10);       // "10"
Boolean(0);       // false
Boolean("test"); // true
```

`NaN` indica un risultato numerico non valido; per verificarlo usare `Number.isNaN(valore)`. Un valore falsy non è automaticamente uguale a `false`: `0`, `-0`, `0n`, `NaN`, `""`, `null`, `undefined` e `false` sono falsy; gli altri valori sono truthy, compresi `[]` e `{}`.

## Stringhe

```javascript
const nome = "Ada";
console.log(`Ciao, ${nome}!`);
```

Le stringhe sono immutabili. I template literal delimitati da backtick consentono interpolazione `${espressione}` e stringhe multilinea.

## Array

```javascript
const voti = [7, 8, 6];
voti.push(9);
console.log(voti.length); // 4
```

Gli indici degli array iniziano da zero. `const` impedisce di riassegnare il riferimento contenuto nella variabile, ma non impedisce di modificare un array.

## Oggetti

```javascript
const studente = {
  nome: "Ada",
  anno: 3,
  descrizione() {
    return `${this.nome}, classe ${this.anno}`;
  }
};
```

Gli oggetti raggruppano proprietà e metodi. `this` dipende da come viene chiamato il metodo; le arrow function non definiscono un proprio `this`.

## `==` e `===`

`===` confronta senza conversione implicita dei tipi ed è generalmente la scelta preferibile. `==` effettua conversioni che possono creare risultati inattesi.
