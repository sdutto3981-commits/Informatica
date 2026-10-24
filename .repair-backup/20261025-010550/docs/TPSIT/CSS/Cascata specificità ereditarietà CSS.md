# Cascata, specificità ed ereditarietà CSS

Quando più regole possono modificare la stessa proprietà, il browser deve determinare quale dichiarazione applicare. La cascata valuta, fra gli altri aspetti, origine/livello della dichiarazione, importanza, specificità e ordine.

## Specificità introduttiva

A parità di condizioni, un selettore con ID ha più specificità di uno con classe, che ne ha più di uno con elemento.

```css
p { color: black; }           /* selettore elemento */
.messaggio { color: blue; }   /* selettore classe */
#avviso { color: red; }       /* selettore ID */
```

Non utilizzare ID o `!important` come soluzione abituale a ogni conflitto. Prima controlla il selettore, la cascata e l'ordine delle regole.

## Ereditarietà

Alcune proprietà, come `color` e `font-family`, sono normalmente ereditate da discendenti. Proprietà come `margin`, `padding` e `border` normalmente non lo sono.

```css
body { font-family: system-ui, sans-serif; color: #222; }
button { font: inherit; }
```

`inherit`, `initial`, `unset` e `revert` permettono di controllare come un valore viene risolto in casi specifici.

## Regole di manutenzione

- Preferisci classi riutilizzabili e selettori poco profondi.
- Raggruppa le regole per componente o funzione.
- Evita duplicazioni e conflitti risolti soltanto con `!important`.
- Verifica il risultato negli strumenti per sviluppatori, dove si vedono le dichiarazioni attive e quelle sovrascritte.

## Riferimento

[W3Schools — CSS Specificity](https://www.w3schools.com/css/css_specificity.asp) · [CSS Inheritance](https://www.w3schools.com/css/css_inherit.asp)
