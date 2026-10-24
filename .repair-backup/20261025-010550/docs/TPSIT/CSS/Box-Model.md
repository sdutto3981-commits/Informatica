# Box model CSS

Ogni elemento visualizzato come box è composto da quattro aree: **content**, **padding**, **border** e **margin**.

- Content: area occupata dal contenuto.
- Padding: spazio interno tra contenuto e bordo; lo sfondo dell'elemento si estende normalmente anche qui.
- Border: bordo intorno a contenuto e padding.
- Margin: spazio esterno che separa il box dagli altri elementi; lo sfondo dell'elemento non lo riempie.

## `content-box` e `border-box`

Con `box-sizing: content-box`, `width` indica la larghezza del contenuto. Con `border-box`, la larghezza comprende contenuto, padding e bordo.

```css
.box-a {
  box-sizing: content-box;
  width: 200px;
  padding: 20px;
  border: 5px solid;
}
/* Larghezza esterna: 200 + 40 + 10 = 250px */

.box-b {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 5px solid;
}
/* Larghezza esterna totale: 200px */

* { box-sizing: border-box; }
```

## Margini e overflow

I margini verticali di alcuni elementi block possono collassare: il margine risultante non è sempre la somma dei due. Flexbox e Grid trattano diversamente le spaziature tra elementi; `gap` è spesso più prevedibile per layout moderni.

Se il contenuto supera lo spazio assegnato, si verifica overflow. `overflow: auto` consente lo scorrimento quando necessario, mentre `hidden` ritaglia il contenuto e può nascondere parti importanti.

## Esempio pratico

```css
.card {
  max-width: 30rem;
  padding: 1.25rem;
  border: 1px solid #bbb;
  border-radius: .5rem;
  margin-inline: auto;
}
```

## Riferimento

[W3Schools — CSS Box Model](https://www.w3schools.com/css/css_boxmodel.asp)
