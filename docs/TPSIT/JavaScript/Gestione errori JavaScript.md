# Errori e gestione delle eccezioni JavaScript

Gli errori possono essere di sintassi, di runtime o logici. Gli strumenti di sviluppo mostrano posizione, messaggio e stack trace, ma è il programmatore a dover comprendere la causa.

## `try`, `catch` e `finally`

```javascript
try {
  const dati = JSON.parse('{"attivo": true}');
  console.log(dati.attivo);
} catch (errore) {
  console.error("Impossibile leggere i dati", errore);
} finally {
  // Operazioni che devono avvenire sia in caso di successo sia di errore
}
```

`catch` intercetta eccezioni lanciate nel blocco `try`. `finally` viene eseguito dopo la gestione dell'errore o il completamento normale, salvo casi estremi come l'interruzione del processo.

## Sollevare un errore

```javascript
function dividi(a, b) {
  if (b === 0) throw new Error("Il divisore non può essere zero");
  return a / b;
}
```

Usa eccezioni per condizioni anomale che il chiamante deve gestire. Per un controllo ordinario e previsto può essere più chiaro restituire un valore o un risultato esplicito.

## Debugging

- Leggi il primo errore della console: altri errori possono esserne una conseguenza.
- Usa breakpoint per ispezionare le variabili.
- Controlla i valori `null`/`undefined` e i tipi effettivi.
- Non catturare un errore per ignorarlo silenziosamente.
- Evita di mostrare agli utenti finali dettagli interni o dati sensibili dell'errore.

## Riferimento

[W3Schools — JavaScript Errors](https://www.w3schools.com/js/js_errors.asp)
