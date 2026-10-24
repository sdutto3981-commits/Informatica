# Posizionamento CSS

La proprietà `position` determina come un elemento partecipa al layout e come può essere spostato.

- `static`: valore normale predefinito; `top`, `right`, `bottom`, `left` non lo spostano.
- `relative`: resta nel flusso e può essere spostato rispetto alla posizione originale; può diventare riferimento per figli `absolute`.
- `absolute`: viene tolto dal flusso normale e posizionato rispetto al contenitore di riferimento più vicino idoneo.
- `fixed`: posizionato rispetto alla viewport (con eccezioni dovute ad alcuni antenati); resta nella stessa posizione durante lo scorrimento.
- `sticky`: si comporta in modo relativo fino a una soglia di scorrimento, poi resta agganciato entro i limiti del contenitore.

## Esempio

```css
.card { position: relative; }
.badge {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
}
```

La `.card` diventa il riferimento della `.badge`. Senza un antenato di riferimento, un elemento `absolute` può essere collocato rispetto a un contenitore più esterno.

## Attenzioni

- Elementi `absolute` e `fixed` non riservano spazio normale nel flusso: possono sovrapporsi al contenuto.
- `z-index` controlla l'ordine di sovrapposizione solo nel contesto di impilamento appropriato.
- `sticky` richiede spesso una soglia come `top: 0` e può essere influenzato dai contenitori di scorrimento.
- Per l'impaginazione principale, preferisci Flexbox/Grid anziché spostare tutto con coordinate assolute.
