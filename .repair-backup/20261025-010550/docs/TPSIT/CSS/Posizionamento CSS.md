# Posizionamento CSS

La proprietà `position` definisce come un elemento viene collocato e come interagisce con il flusso normale del documento.

- `static`: valore predefinito; `top`, `right`, `bottom` e `left` non spostano l'elemento.
- `relative`: resta nel flusso e può essere spostato rispetto alla posizione normale; spesso stabilisce il riferimento per discendenti `absolute`.
- `absolute`: esce dal flusso normale e viene posizionato rispetto al suo contenitore di riferimento posizionato, oppure a un altro riferimento previsto dal browser.
- `fixed`: si colloca rispetto alla viewport e resta nella stessa posizione durante lo scroll, con alcune eccezioni dovute al contesto di contenimento.
- `sticky`: si comporta normalmente finché non raggiunge una soglia di scorrimento; richiede almeno una soglia come `top` e può essere limitato dal contenitore.

```css
.card { position: relative; }
.badge {
  position: absolute;
  top: .5rem;
  right: .5rem;
}

.intestazione-fissa {
  position: sticky;
  top: 0;
  z-index: 10;
}
```

`z-index` regola l'ordine di sovrapposizione all'interno dei contesti di stacking; non sempre un numero più alto porta l'elemento sopra ogni altro elemento della pagina.

Prima di ricorrere a `position: absolute`, valuta Flexbox o Grid: spesso creano layout più robusti e adattabili.

## Riferimento

[W3Schools — CSS Layout](https://www.w3schools.com/css/css_positioning.asp)
