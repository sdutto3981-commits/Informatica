# CSS

CSS (*Cascading Style Sheets*) definisce presentazione e layout di una pagina HTML. Una regola è composta da un selettore e da una o più dichiarazioni `proprietà: valore`.

## Percorso

1. [Selettori](Selettori.md)
2. [Cascata, specificità ed ereditarietà](Cascata%20specificit%C3%A0%20ereditariet%C3%A0%20CSS.md)
3. [Box model](Box-Model.md)
4. [Unità, colori e tipografia](Unit%C3%A0%20colori%20e%20tipografia%20CSS.md)
5. [Posizionamento](Posizionamento%20CSS.md)
6. [Flexbox](Flexbox%20CSS.md) e [Grid](Grid%20CSS.md)
7. [Responsive design e media query](Responsive%20design%20e%20media%20query%20CSS.md)
8. [Display, overflow e float](Display%20overflow%20e%20float%20CSS.md)
9. [Variabili e funzioni CSS](Variabili%20CSS%20e%20funzioni.md)
10. [Transizioni e animazioni](Transizioni%20e%20animazioni%20CSS.md)

## Inserire CSS

```html
<link rel="stylesheet" href="styles.css">
```

Il foglio esterno è di norma preferibile per mantenere stile e struttura separati e riutilizzare le regole in più pagine. Gli stili inline sono difficili da riutilizzare e possono complicare la manutenzione.

## Esempio

```css
:root { --colore-accento: #2457a7; }
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, sans-serif; line-height: 1.5; }
.container { width: min(100% - 2rem, 70rem); margin-inline: auto; }
a { color: var(--colore-accento); }
```

## Fonte di approfondimento

[W3Schools — CSS Tutorial](https://www.w3schools.com/css/)
