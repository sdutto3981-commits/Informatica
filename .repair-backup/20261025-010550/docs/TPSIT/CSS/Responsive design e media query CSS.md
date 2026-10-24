# Responsive design e media query

Il responsive design adatta struttura, dimensioni e contenuti alle caratteristiche dello schermo. Un layout responsive deve restare leggibile, navigabile e funzionale, non soltanto diventare più stretto.

## Principi fondamentali

- Inserisci il meta viewport in HTML: `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- Parti da un layout fluido; evita larghezze rigide che provocano scorrimento orizzontale.
- Usa `max-width`, unità relative, Flexbox e Grid.
- Aggiungi breakpoint quando il contenuto richiede un cambiamento, non soltanto perché un dispositivo ha una certa etichetta.
- Verifica con strumenti di sviluppo e, quando possibile, dispositivi reali.

## Media query mobile-first

```css
.layout { display: grid; gap: 1rem; }
img { max-width: 100%; height: auto; }

@media (min-width: 48rem) {
  .layout { grid-template-columns: 16rem minmax(0, 1fr); }
}
```

Lo stile di base è adatto agli schermi stretti; la media query aggiunge due colonne quando lo spazio è sufficiente.

## Immagini e tipografia fluidi

```css
.titolo { font-size: clamp(1.75rem, 4vw, 3rem); }
.contenitore { width: min(100% - 2rem, 72rem); margin-inline: auto; }
```

`clamp()` limita il valore tra minimo e massimo, mentre `min()` sceglie il valore più piccolo tra le opzioni fornite.

## Riferimento

[W3Schools — CSS Responsive](https://www.w3schools.com/css/css_rwd_intro.asp) · [HTML & CSS Responsive Design](https://www.w3schools.com/htmlcss/htmlcss_responsive_design.asp)
