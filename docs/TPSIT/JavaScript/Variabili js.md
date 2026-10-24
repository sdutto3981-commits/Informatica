# Variabili JavaScript

> Questa pagina si concentra su `let`, `const` e scope. Per dichiarazione senza inizializzazione, assegnazione, conversioni esplicite e blocchi, consulta anche [Dichiarazioni variabili](Dichiarazioni%20variabili%20js.md).


Una variabile associa un nome a un valore. JavaScript usa `let` e `const` nella maggior parte del codice moderno.

```javascript
let punti = 0;
punti = punti + 1;

const nome = "Ada";
const studente = { nome: "Luca" };
studente.nome = "Marta"; // l'oggetto può cambiare anche se il binding è const
```

- `let`: permette la riassegnazione.
- `const`: impedisce di assegnare un valore diverso allo stesso binding dopo l'inizializzazione.
- `var`: dichiarazione storica con regole di scope differenti; nei nuovi esempi, preferisci `let` e `const`.

## Scope

`let` e `const` hanno scope di blocco. Una variabile dichiarata all'interno di una funzione non è accessibile direttamente dall'esterno, salvo che venga restituita o esposta in altro modo.

```javascript
const soglia = 10;
if (soglia > 5) {
  const messaggio = "Superata";
  console.log(messaggio);
}
// messaggio non è definita fuori dal blocco
```

## Convenzioni

Usa nomi descrittivi in `camelCase`, per esempio `numeroTentativi`. Le costanti che rappresentano configurazioni stabili possono usare nomi più evidenti, ma la maiuscola non è una regola obbligatoria del linguaggio.

## Riferimento

[W3Schools — JavaScript Variables](https://www.w3schools.com/js/js_variables.asp)
