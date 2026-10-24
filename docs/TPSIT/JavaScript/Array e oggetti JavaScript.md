# Array e oggetti JavaScript

## Array

Un array è una raccolta ordinata. Gli indici partono da zero.

```javascript
const voti = [7, 8, 6];
console.log(voti[0]); // 7
voti.push(9);         // aggiunge in fondo
console.log(voti.length);

for (let i = 0; i < voti.length; i++) {
  console.log(voti[i]);
}
```

Metodi utili includono `push`, `pop`, `includes`, `indexOf`, `slice`, `map` e `filter`. Studia prima scansione, ricerca e aggiornamento con cicli semplici.

## Oggetti

Un oggetto conserva proprietà associate a chiavi.

```javascript
const studente = {
  nome: "Ada",
  classe: "3INF",
  promosso: true
};

console.log(studente.nome);
studente.classe = "4INF";
```

Si può accedere alle proprietà con `oggetto.nome` oppure `oggetto[chiave]`. Se la chiave viene costruita a runtime, la notazione tra parentesi quadre è utile.

## Iterazione

```javascript
const persone = [
  { nome: "Ada", eta: 16 },
  { nome: "Alan", eta: 17 }
];

for (const persona of persone) {
  console.log(persona.nome);
}
```

`for...of` attraversa i valori iterabili. `for...in` attraversa invece le chiavi enumerabili di un oggetto ed è normalmente più appropriato per le proprietà dell'oggetto.

## Attenzioni

- Gli array possono contenere valori di tipi differenti, ma mantenere un tipo coerente rende il programma più chiaro.
- `const` impedisce di riassegnare il riferimento, non rende immutabili le proprietà dell'oggetto o gli elementi dell'array.
- L'indice non valido può restituire `undefined`; controlla che il valore esista prima di usarlo.
