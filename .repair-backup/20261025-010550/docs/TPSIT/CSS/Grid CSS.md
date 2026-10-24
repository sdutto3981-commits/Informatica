# CSS Grid

CSS Grid organizza gli elementi in una griglia bidimensionale di righe e colonne. È particolarmente utile per layout di pagina, gallerie e schede con colonne regolari.

```css
.galleria {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
  gap: 1rem;
}

.galleria img { display: block; width: 100%; height: auto; }
```

## Proprietà principali

- `display: grid`: attiva Grid.
- `grid-template-columns` e `grid-template-rows`: definiscono tracce/colonne e righe.
- `fr`: distribuisce lo spazio libero.
- `repeat()`: ripete una definizione.
- `minmax(min, max)`: definisce limiti per una traccia.
- `auto-fit` e `auto-fill`: automatizzano la disposizione delle colonne.
- `gap`: distanza tra righe e colonne.
- `grid-column` e `grid-row`: collocano o estendono elementi su più tracce.

## Confronto con Flexbox

- Flexbox è principalmente monodimensionale: gestisce una riga o una colonna alla volta.
- Grid è bidimensionale: controlla simultaneamente righe e colonne.
- I due modelli possono essere combinati nello stesso componente.

## Riferimento

[W3Schools — CSS Grid](https://www.w3schools.com/css/css_grid.asp)
