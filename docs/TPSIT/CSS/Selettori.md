---
date: 2025-11-30
time: 14:33
---
# Selettori

Possiamo applicare caratteristiche specifiche a dei determinati elementi per esempio:

```html
<article>
  <p>I want to be red and larger than the other text.</p>
  <p>I want to be normal sized and the default color.</p>
</article>
```

```css
article p:first-of-type {
  color: red;
  font-size: 1.5em;
}
```

così la prima riga sarà rossa

## Parti della regola CSS

![[an-image-a-css-rule-the-ced38545b4bec.svg]]

IN questo caso il selettore è `.my-css-rule` che trova tutti gli elementi con quella classe nella pagina al suo interno ci sono 3 dichiarazioni che si compongono di una proprietà e del valore di essa

## Selettori semplici

Il gruppo di selettori più semplice composto dagli elementi di HTML non che classi  ID che possono essere aggiunti un tag HTML

### Selettore universale

Il selettore universale chiamato anche carattere jolly fa riferimento a qualsiasi elemento
```css
* {
  color: hotpink;
}
```

### Selettore di tipo

Corrisponde direttamente  a un elemento HTML  
## Riferimenti
1. 