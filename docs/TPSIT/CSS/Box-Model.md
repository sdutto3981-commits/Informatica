---
date: 2025-11-30
time: 10:15
---
# Box-Model

Se prendiamo un paragrafo cona  all' interno del testo e in css andiamo a esplicitare delle dimensioni specifiche il testo può uscire fuori.

Questo dipende dal valore del display alle dimensioni impostate e ai contenuti che contengono possiamo controllare questo dimensionamento utilizzando il **dimensionamento estrinseco** oppure con il **dimensionamento intrinseco** il browser prende decisioni per te.

Prendendo una casella con delle dimensioni esplicitate esse sono dimensioni estrinseche per renderlo intrinseco e rendere cosi il dimensionamento della casella come `widht: min-content;` ovvero impostando la dimensione alla minima larghezza del contenuto

Termine chiave: l'overflow si verifica quando i contenuti sono troppo grandi per la casella in cui si trovano. Puoi gestire il modo in cui un elemento gestisce i contenuti in eccesso utilizzando la proprietà `overflow`.

## Le aree del modello a scatola

Le scatole sono costituite da aree distinte del modello di scatola, ognuna delle quali svolge una funzione specifica.
![[a-diagram-showing-four-m-af72960a9e79a.svg]]
La content box è l'area con le dimensioni più variabili 

L'area di spaziatura interna o `padding` si trova all'interno della casella m ostra anche lo stesso sfondo se ce impostazione di `overflow: auto; overflow:scroll;` le barre di scorrimento vengono incluse nella `padding box`

Il riquadro di bordo viene definito dalla proprietà `border` che crea una cornice del limite di ciò che puoi vedere.

Il riquadro di margine è lo spazio intorno a tutto cio viene definito dalla regola `margin` proprietà come `outline o box-shadow` occupano questo spazio 


## Controllare il modella della casella

Se non vengono esplicitamente definite delle proprietà specifiche il browser applica il valore `display` agli elementi come `div box` `li` di `list-item` e uno `span` valore di `inline-block`.

Un elemento `inline` ha un margine di blocco, ma altri non lo rispettano `inline-block` antine la maggior parte dei comportamenti di un `inline`.
Un elemento `block` riempie lo spazio in linea disponibile per impostazione predefinita mentre gli altri due sono grandi quanto i loro contenuti.

Inoltre per il `box-sizing` indica come la casella deve calcolare la propria dimensione di base ha valore di `box-sizing: content-box;` in questo caso se impostiamo `width e height` essi si riferiscono solo alla parte dei contenuti a cui si va a sommare poi la dimensione del padding e del border

```css
.my-box {
  width: 200px;
  border: 10px solid;
  padding: 20px;
}
```

Per esempio qui il `box-sizing: content-box;` fa si che la dimensione della scatola in totale sia pari a `260px`

Se invece inseriamo il valore di `box-sizing: border-box;` quando andiamo a inserire `width e height` esse si riferiranno già alla massima dimensione del rendering del blocco contenendo sia il border che il padding 

```css
.my-box {
  box-sizing: border-box;
    width: 200px;
    border: 10px solid;
    padding: 20px;
}
```

Per esempio qui il `box-sizing: border-box;` fa si che la dimensione della scatola in totale sia pari a `200px` come impostato

## Riferimenti
1. 