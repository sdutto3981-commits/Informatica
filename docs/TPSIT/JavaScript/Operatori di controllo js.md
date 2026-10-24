# Operatori e controllo del flusso JavaScript

## Operatori

| Categoria | Operatori | Esempio |
|---|---|---|
| Aritmetici | `+ - * / % **` | `7 % 2` restituisce `1` |
| Assegnazione | `= += -= *= /=` | `x += 2` |
| Confronto | `=== !== < > <= >=` | `eta >= 18` |
| Logici | `&& || !` | `a > 0 && b > 0` |
| Condizionale | `? :` | `eta >= 18 ? "adulto" : "minore"` |
| Nullish | `??` | `valore ?? "predefinito"` |

`+` può sommare numeri oppure concatenare stringhe. Per evitare risultati inattesi, converti esplicitamente i valori ricevuti da input quando devono essere numerici.

## Condizioni

```javascript
const voto = 7;
if (voto >= 8) {
  console.log("Ottimo");
} else if (voto >= 6) {
  console.log("Sufficiente");
} else {
  console.log("Da recuperare");
}
```

`switch` è utile quando si confronta una stessa espressione con più casi distinti:

```javascript
switch (giorno) {
  case 1: console.log("Lunedì"); break;
  case 2: console.log("Martedì"); break;
  default: console.log("Altro giorno");
}
```

`break` evita di proseguire ai casi successivi. In alternativa, alcune forme moderne di `switch` possono usare pattern diversi, ma per gli esercizi introduttivi è sufficiente conoscere i casi classici.

## Cicli

```javascript
for (let i = 0; i < 5; i++) console.log(i);

let tentativi = 0;
while (tentativi < 3) {
  tentativi++;
}
```

Usa `for` quando conosci la scansione o gli aggiornamenti, `while` quando il ciclo dipende da una condizione. Assicurati che la condizione possa diventare falsa per evitare cicli infiniti.

## Riferimento

[W3Schools — JavaScript Operators](https://www.w3schools.com/js/js_operators.asp) · [If Else](https://www.w3schools.com/js/js_if_else.asp) · [Loops](https://www.w3schools.com/js/js_loop_for.asp)
