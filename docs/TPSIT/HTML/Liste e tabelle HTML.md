# Liste e tabelle HTML

## Liste

`ul` crea un elenco non ordinato; `ol` crea un elenco ordinato; ogni voce viene inserita in `li`.

```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>

<ol>
  <li>Analisi</li>
  <li>Progettazione</li>
  <li>Test</li>
</ol>
```

`dl`, `dt` e `dd` descrivono invece liste di termini e relative definizioni.

## Tabelle

Usa le tabelle per dati che hanno relazioni tra righe e colonne, non per impaginare una pagina.

```html
<table>
  <caption>Voti del progetto</caption>
  <thead>
    <tr><th scope="col">Materia</th><th scope="col">Voto</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Informatica</th><td>8</td></tr>
    <tr><th scope="row">Sistemi</th><td>7</td></tr>
  </tbody>
</table>
```

- `table` contiene la tabella; `tr` una riga.
- `th` identifica una cella d'intestazione, `td` una cella di dati.
- `thead`, `tbody` e `tfoot` aiutano a organizzare le parti della tabella.
- `caption` dà un titolo alla tabella; `scope` aiuta a collegare intestazioni e celle.
- `colspan` e `rowspan` permettono a una cella di occupare più colonne o righe.

## Stile con CSS

```css
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #777; padding: .5rem; text-align: left; }
thead { background: #eee; }
```

L'accessibilità dipende anche dalla struttura delle intestazioni e dalla complessità della tabella: per tabelle molto articolate può servire una progettazione specifica.

## Riferimento

[W3Schools — HTML Lists](https://www.w3schools.com/html/html_lists.asp) · [HTML Tables](https://www.w3schools.com/html/html_tables.asp)
