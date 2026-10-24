# CSS

CSS (*Cascading Style Sheets*) descrive la presentazione degli elementi HTML: colori, spaziature, tipografia e layout responsive.

## Percorso

- [Selettori](Selettori.md)
- [Box model](Box-Model.md)
- [CSS in HTML](CSS%20in%20HTML.md)

## Competenze del programma

1. Selettori per elemento, classe, ID, attributo, discendenti e pseudoclassi.
2. Cascata, specificità, ereditarietà e ordine delle dichiarazioni.
3. Box model, unità CSS, dimensionamento e overflow.
4. Flexbox e proprietà di posizionamento.
5. Transizioni e animazioni.
6. Media query e approccio responsive mobile-first.
7. Integrazione con Bootstrap.

```css
* { box-sizing: border-box; }
.contenitore {
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

`flex-wrap: wrap` permette agli elementi di andare a capo quando lo spazio non basta. Le media query permettono di modificare il layout a determinati intervalli di larghezza. Verifica il risultato su desktop e smartphone.

Per il collegamento con griglia e componenti, consulta [Bootstrap](../Bootstrap/index.md) e il [programma TPSIT](../../Programmi/tpsit.md).
