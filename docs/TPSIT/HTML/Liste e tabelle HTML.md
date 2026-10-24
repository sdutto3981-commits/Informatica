# Liste e tabelle HTML

## Liste

- `ul` crea una lista non ordinata.
- `ol` crea una lista ordinata.
- `li` rappresenta ciascun elemento di una lista.
- `dl`, `dt` e `dd` rappresentano una lista di termini e descrizioni.

```html
<ul>
  <li>HTML: struttura</li>
  <li>CSS: presentazione</li>
  <li>JavaScript: comportamento</li>
</ul>
```

## Tabelle di dati

Le tabelle sono destinate a dati tabellari, non a costruire il layout della pagina.

```html
<table>
  <caption>Voti del trimestre</caption>
  <thead>
    <tr><th scope="col">Materia</th><th scope="col">Voto</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Informatica</th><td>8</td></tr>
    <tr><th scope="row">TPSIT</th><td>7</td></tr>
  </tbody>
</table>
```

- `caption` descrive lo scopo della tabella.
- `thead` e `tbody` raggruppano le righe.
- `th` è una cella di intestazione; `scope` chiarisce a quali celle si riferisce.
- `td` è una cella di dati.

Per il layout moderno usa CSS (Flexbox o Grid) anziché tabelle di impaginazione.
