# Variabili in JavaScript

Una variabile associa un identificatore a un valore. In JavaScript si usano principalmente `const` e `let`.

```javascript
let punteggio = 0;
punteggio = punteggio + 10;

const nome = "Ada";
console.log(`${nome}: ${punteggio}`);
```

- `const`: il binding non può essere riassegnato; se contiene un oggetto o un array, le proprietà o gli elementi possono comunque essere modificati.
- `let`: consente la riassegnazione e ha scope di blocco.
- `var`: dichiarazione legacy con scope di funzione; nei nuovi esempi è generalmente preferibile evitarla.

JavaScript distingue maiuscole e minuscole. I nomi sono spesso scritti in `camelCase`. Una variabile locale dovrebbe essere dichiarata il più vicino possibile al punto in cui serve.
