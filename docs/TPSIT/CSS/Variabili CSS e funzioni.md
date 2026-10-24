# Variabili e funzioni CSS

Le proprietà personalizzate permettono di riutilizzare valori e aggiornare in un unico punto i colori, le spaziature o altre scelte di design.

```css
:root {
  --colore-testo: #222;
  --colore-accento: #2457a7;
  --spazio-base: 1rem;
}

.card {
  color: var(--colore-testo);
  padding: var(--spazio-base);
  border: 1px solid var(--colore-accento);
}
```

Le variabili iniziano con `--` e vengono lette con `var()`. Il loro valore segue la cascata e lo scope dell'elemento sul quale è definito.

## Funzioni utili

- `calc()`: esegue calcoli tra valori compatibili, per esempio `width: calc(100% - 2rem)`.
- `min()` e `max()`: scelgono un valore minimo o massimo tra più espressioni.
- `clamp(min, preferito, max)`: limita un valore fluido a un intervallo.
- `var(--nome, fallback)`: può usare un valore alternativo se la variabile non è disponibile.

```css
.contenitore { width: min(100% - 2rem, 70rem); }
.titolo { font-size: clamp(2rem, 5vw, 4rem); }
```

## Riferimento

[W3Schools — CSS Functions](https://www.w3schools.com/cssref/css_functions.php)
