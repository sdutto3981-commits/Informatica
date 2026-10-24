# Array e oggetti JavaScript

## Array

Un array rappresenta una sequenza ordinata. Gli indici partono da zero e `length` restituisce il numero di elementi.

```javascript
const voti = [7, 8, 6];
console.log(voti[0]); // 7
voti.push(9);         // aggiunge alla fine
voti[1] = 10;         // modifica l'indice 1
```

Metodi comuni: `push`, `pop`, `shift`, `unshift`, `includes`, `indexOf`, `slice`, `splice`, `map`, `filter`, `find`, `some`, `every` e `reduce`. Controlla sempre se un metodo modifica l'array originale: `slice` non lo modifica, `splice` sì.

```javascript
const numeri = [1, 2, 3, 4];
const pari = numeri.filter(n => n % 2 === 0);
const doppi = numeri.map(n => n * 2);
```

## Oggetti

Gli oggetti rappresentano entità con proprietà nominate.

```javascript
const persona = {
  nome: "Ada",
  eta: 20,
  saluta() { return `Ciao, sono ${this.nome}`; }
};

persona.eta = 21;
console.log(persona.saluta());
```

Si accede alle proprietà con `persona.nome` o `persona[chiave]`. `this` dipende da come viene chiamata la funzione; nelle arrow function non viene creato un `this` proprio.

## Copia e riferimenti

Assegnare un oggetto a un'altra variabile copia il riferimento, non crea automaticamente una copia indipendente:

```javascript
const a = { valore: 1 };
const b = a;
b.valore = 2;
console.log(a.valore); // 2
```

Lo spread (`{ ...a }` o `[...array]`) crea una copia superficiale: oggetti annidati possono restare condivisi.

## Riferimento

[W3Schools — JavaScript Arrays](https://www.w3schools.com/js/js_arrays.asp) · [JavaScript Objects](https://www.w3schools.com/js/js_objects.asp)
