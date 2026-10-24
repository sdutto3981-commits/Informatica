# CSS3

CSS (Cascading Style Sheets) descrive la presentazione dei contenuti HTML. Le regole si applicano in base alla cascata, specificità, ereditarietà e ordine delle dichiarazioni.

## Percorso

- [Selettori](Selettori.md)
- [Cascata, specificità ed ereditarietà](Cascata%20specificità%20ereditarietà%20CSS.md)
- [Box model](Box-Model.md)
- [Unità, colori e tipografia](Unità%20colori%20e%20tipografia%20CSS.md)
- [Flexbox](Flexbox%20CSS.md)
- [Posizionamento](Posizionamento%20CSS.md)
- [Responsive design e media query](Responsive%20design%20e%20media%20query%20CSS.md)
- [Transizioni e animazioni](Transizioni%20e%20animazioni%20CSS.md)

## Esempio mobile-first

```css
* { box-sizing: border-box; }
.container { width: min(100% - 2rem, 70rem); margin-inline: auto; }
.cards { display: flex; flex-wrap: wrap; gap: 1rem; }
.card { flex: 1 1 15rem; }
```

Il layout usa Flexbox e può adattarsi alle larghezze disponibili. [Bootstrap](../Bootstrap/index.md) offre una griglia e componenti già pronti, ma è utile comprenderne prima i fondamenti CSS.
