# Unità, colori e tipografia CSS

## Unità di misura

- `px`: unità CSS assoluta comunemente usata per bordi e dettagli; non equivale sempre a un pixel fisico del display.
- `rem`: relativa alla dimensione del carattere dell'elemento radice.
- `em`: relativa alla dimensione del carattere del contesto per molte proprietà; può accumularsi nella nidificazione.
- `%`: riferimento dipendente dalla proprietà e dal contesto.
- `vw`, `vh`: percentuale della dimensione della viewport.
- `fr`: unità di distribuzione dello spazio nei layout CSS Grid.

Per testi e spaziature, `rem` spesso rende più facile rispettare le preferenze di dimensione del testo. Non impostare tutte le misure in pixel se questo impedisce al contenuto di adattarsi.

## Colori

```css
:root {
  --testo: #20242a;              /* HEX */
  --sfondo: rgb(250 250 252);    /* RGB */
  --accento: hsl(215 70% 42%);   /* HSL */
}
```

I colori possono essere definiti con nomi, HEX, `rgb()`/`rgba()` o `hsl()`/`hsla()`. Un contrasto sufficiente tra testo e sfondo è essenziale per la leggibilità.

## Tipografia

```css
body {
  font-family: system-ui, Arial, sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  color: var(--testo);
}

h1 { font-size: clamp(2rem, 4vw, 3.5rem); line-height: 1.1; }
p { max-width: 70ch; }
```

- `font-family`: famiglia del carattere e fallback.
- `font-size`: dimensione del testo.
- `font-weight`: peso, per esempio `400` o `700` se supportati dal font.
- `line-height`: altezza della riga, spesso senza unità.
- `text-align`: allineamento orizzontale del testo.
- `text-decoration`: decorazioni come sottolineatura.
- `clamp(min, preferito, max)`: valore fluido compreso tra due limiti.

## Riferimento

[W3Schools — CSS Colors](https://www.w3schools.com/css/css_colors.asp) · [CSS Fonts](https://www.w3schools.com/css/css_font.asp)
