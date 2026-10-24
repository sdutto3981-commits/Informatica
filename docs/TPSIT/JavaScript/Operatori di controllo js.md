# Operatori di confronto e logici in JavaScript

Gli operatori di confronto producono un valore booleano (`true` oppure `false`).

## Uguaglianza

- `===` e `!==`: confronto stretto, senza coercizione tra tipi; sono in genere preferibili.
- `==` e `!=`: confronto con conversioni implicite, che possono provocare risultati inattesi.

```javascript
2 === 2;   // true
2 === "2"; // false
2 == "2";  // true
```

## Confronto numerico

`>`, `<`, `>=`, `<=` confrontano valori. Se si confrontano stringhe, l'ordinamento è lessicografico secondo le regole del linguaggio, non necessariamente numerico.

## Operatori logici

| Operatore | Significato | Esempio |
|---|---|---|
| `&&` | AND logico | `eta >= 18 && haDocumento` |
| `||` | OR logico | `haBiglietto || èOspite` |
| `!` | negazione | `!completato` |

`&&` e `||` usano cortocircuito e restituiscono uno dei valori degli operandi, non sempre un booleano puro. Nelle condizioni, tuttavia, il valore viene valutato come truthy/falsy.

## Condizioni

```javascript
if (punteggio >= 60) {
  console.log("Superato");
} else {
  console.log("Da recuperare");
}
```

Consulta la sezione sul [controllo del flusso](Operatori%20di%20controllo%20js.md) e quella su [tipi e conversioni](Strutture%20e%20tipi%20di%20dati.md).
