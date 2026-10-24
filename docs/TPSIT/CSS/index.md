# CSS — selettori, layout e responsive design

CSS (*Cascading Style Sheets*) definisce la presentazione di HTML: colori, spaziature, tipografia, dimensionamento e disposizione degli elementi.

## Percorso

- [Selettori](Selettori.md)
- [Cascata, specificità ed ereditarietà](Cascata%20specificit%C3%A0%20ereditariet%C3%A0%20CSS.md)
- [Box model](Box-Model.md)
- [Unità, colori e tipografia](Unit%C3%A0%20colori%20e%20tipografia%20CSS.md)
- [Flexbox](Flexbox%20CSS.md)
- [Posizionamento](Posizionamento%20CSS.md)
- [Responsive design e media query](Responsive%20design%20e%20media%20query%20CSS.md)
- [Transizioni e animazioni](Transizioni%20e%20animazioni%20CSS.md)
- [CSS in HTML](CSS%20in%20HTML.md)

## Esempio di base

```css
* { box-sizing: border-box; }
.container {
  width: min(100% - 2rem, 70rem);
  margin-inline: auto;
}
.riga {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.card { flex: 1 1 15rem; }
```

`flex-wrap: wrap` permette agli elementi di andare a capo quando lo spazio non basta. Le media query modificano il layout in base alle caratteristiche del dispositivo o della finestra. Verifica il risultato su desktop e smartphone.

