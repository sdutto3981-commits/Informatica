# Unità, colori e tipografia CSS

## Unità di misura

- `px`: pixel CSS; utile per bordi o dettagli, ma non è sempre la scelta più flessibile per le dimensioni del testo.
- `%`: spesso relativo alla dimensione del contenitore.
- `em`: relativo al font-size dell'elemento/genitore secondo la proprietà interessata.
- `rem`: relativo al font-size dell'elemento radice (`html`).
- `vw` e `vh`: percentuali della dimensione della viewport; usarle con attenzione nei layout mobili.
- `fr`: frazione dello spazio disponibile, usata nel CSS Grid.

## Colori

CSS consente nomi, esadecimali, `rgb()` e `hsl()`. La scelta deve mantenere un contrasto sufficiente tra testo e sfondo.

```css
body {
  color: #202124;
  background-color: #ffffff;
}
.link {
  color: hsl(220 80% 35%);
}
```

## Tipografia

```css
body {
  font-family: system-ui, Arial, sans-serif;
  font-size: 1rem;
  line-height: 1.5;
}
h1 {
  font-size: clamp(1.8rem, 4vw, 3rem);
  line-height: 1.15;
}
```

`font-family` definisce i caratteri preferiti, `font-size` la dimensione, `line-height` l'altezza della riga e `font-weight` lo spessore. Specifica una famiglia di riserva (`sans-serif`, `serif` o `monospace`).

Non comunicare un significato solo tramite il colore e non ridurre il testo a dimensioni difficili da leggere.
