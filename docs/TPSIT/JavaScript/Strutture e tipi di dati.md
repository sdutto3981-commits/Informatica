# Strutture e tipi di dati in JavaScript

JavaScript è un linguaggio a tipizzazione dinamica: una variabile può contenere valori di tipo diverso durante l'esecuzione. Il tipo del valore è importante nelle operazioni, nelle conversioni e nei confronti.

## Tipi primitivi principali

- `number`: numeri, sia interi sia con parte decimale; comprende `NaN` e `Infinity`.
- `string`: sequenza di caratteri.
- `boolean`: `true` o `false`.
- `undefined`: valore tipico di una variabile dichiarata senza valore assegnato o di una proprietà assente.
- `null`: assenza intenzionale di un valore.
- `bigint` e `symbol`: tipi disponibili per casi d'uso specifici.

Gli array e gli oggetti sono valori di tipo riferimento. `typeof null` restituisce storicamente `"object"`: è un comportamento del linguaggio, non indica che `null` sia un normale oggetto.

## Conversioni esplicite

```javascript
Number("10");    // 10
Number("abc");   // NaN
Number(null);     // 0
Number(false);    // 0
Number(true);     // 1
String(10);       // "10"
Boolean(0);       // false
Boolean("test"); // true
```

`NaN` indica un risultato numerico non valido; per verificarlo usa `Number.isNaN(valore)`, non `valore === NaN`.

## Stringhe e template literal

```javascript
const nome = "Ada";
console.log("Ciao " + nome);
console.log(`Ciao ${nome}`);
console.log(`2 + 4 = ${2 + 4}`);
```

I template literal usano i backtick `` ` `` e permettono di interpolare espressioni con `${...}`. Non è necessario usare le virgolette singole per l'interpolazione.

## Valori truthy e falsy

I valori falsy principali sono `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` e `NaN`. Quasi tutti gli altri valori sono truthy, inclusi array vuoti `[]` e oggetti vuoti `{}`.

## Array e oggetti

```javascript
const voti = [7, 8, 6];
console.log(voti[0]); // 7

const studente = { nome: "Ada", classe: "3INF" };
console.log(studente.nome);
```

Gli array sono indicizzati da zero. Per evitare errori controlla la lunghezza prima di accedere agli indici. Le proprietà di un oggetto si possono leggere con la notazione punto o con parentesi quadre.

## Uguaglianza

- `===` confronta senza conversione automatica dei tipi.
- `==` può convertire i valori e produrre risultati meno intuitivi.

Negli esercizi ordinari preferisci `===` e `!==`, salvo quando la conversione implicita è intenzionale e compresa.
