# Responsive design e media query

Il responsive design adatta contenuto e layout a schermi e finestre differenti. Conviene partire da un layout utilizzabile su schermi piccoli e aggiungere miglioramenti quando c'è spazio.

## Principi

- Usa il meta viewport in HTML.
- Preferisci dimensioni flessibili e contenitori con larghezza massima.
- Evita larghezze fisse che causano scorrimento orizzontale.
- Fai andare a capo gli elementi quando lo spazio non basta.
- Verifica immagini, form, navigazione e testo a diverse larghezze.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

```css
* { box-sizing: border-box; }
.container { width: min(100% - 2rem, 70rem); margin-inline: auto; }
.griglia { display: flex; flex-wrap: wrap; gap: 1rem; }
.card { flex: 1 1 17rem; }

@media (max-width: 600px) {
  .navigazione { flex-direction: column; align-items: stretch; }
}
```

La media query applica la regola solo quando la viewport rispetta la condizione. Il breakpoint dovrebbe derivare dal momento in cui il layout non funziona più, non da una lista rigida di dispositivi.

## Query comuni

- `(max-width: 600px)`: larghezza massima della viewport.
- `(min-width: 800px)`: larghezza minima.
- `prefers-reduced-motion: reduce`: preferenza di sistema per ridurre le animazioni.

## Verifica

Ridimensiona la finestra, usa gli strumenti responsive del browser e verifica che non appaia uno scorrimento orizzontale involontario. L'adattamento responsive non sostituisce l'accessibilità da tastiera o il contrasto corretto.
