# `display`, overflow e float CSS

## `display`

La proprietà `display` determina il modello di formattazione dell'elemento.

- `block`: crea un box di blocco.
- `inline`: partecipa al flusso del testo.
- `inline-block`: si dispone in linea ma consente larghezza e altezza come un box.
- `none`: l'elemento non viene mostrato e non occupa spazio nel layout.
- `flex` e `grid`: attivano rispettivamente i modelli Flexbox e Grid per i figli diretti.

`display: none` è diverso da `visibility: hidden`: quest'ultimo nasconde la visualizzazione ma conserva lo spazio del box.

## Overflow

Quando il contenuto eccede il box, `overflow` definisce come gestirlo.

```css
.pannello {
  max-height: 12rem;
  overflow: auto;
}
```

Valori comuni: `visible`, `hidden`, `clip`, `scroll`, `auto`. Ritagliare il contenuto può nascondere informazioni o focus; usalo quando l'effetto è intenzionale.

## Float

`float: left` o `float: right` permette soprattutto di far scorrere testo attorno a un elemento, come una figura. Non è il metodo consigliato per costruire il layout generale di una pagina: per quello usa Flexbox o Grid.

```css
.immagine-articolo {
  float: left;
  width: min(40%, 12rem);
  margin: 0 1rem 1rem 0;
}
```

Un elemento flottante viene tolto dal normale flusso di blocco; il layout circostante va verificato con attenzione. Per allineare componenti, Flexbox e Grid sono normalmente più prevedibili.

## Riferimento

[W3Schools — CSS Display](https://www.w3schools.com/css/css_display_visibility.asp) · [CSS Overflow](https://www.w3schools.com/css/css_overflow.asp) · [CSS Float](https://www.w3schools.com/css/css_float.asp)
