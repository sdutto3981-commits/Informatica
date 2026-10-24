# Selettori CSS

Un selettore individua gli elementi HTML a cui applicare le dichiarazioni.

## Tipi principali

```css
p { color: #222; }                 /* tutti i paragrafi */
.avviso { color: darkred; }        /* classe */
#intestazione { font-weight: bold; } /* id */
input[type="email"] { width: 100%; } /* attributo */
nav a { text-decoration: none; }   /* discendente */
.lista > li { margin-block: .5rem; } /* figlio diretto */
```

- `A B`: seleziona un discendente `B` dentro `A`.
- `A > B`: seleziona un figlio diretto.
- `A + B`: seleziona il fratello immediatamente successivo.
- `A ~ B`: seleziona i fratelli successivi che corrispondono a `B`.

## Pseudoclassi e pseudoelementi

```css
button:hover { filter: brightness(0.9); }
input:focus { outline: 2px solid royalblue; }
li:first-child { font-weight: bold; }
p::first-letter { font-size: 1.5em; }
```

Una pseudoclasse descrive uno stato o una posizione dell'elemento, come `:hover`, `:focus`, `:checked`, `:first-child`. Uno pseudoelemento seleziona una parte o un elemento virtuale, come `::before`, `::after` e `::first-letter`.

## Gruppi di selettori

```css
h1, h2, h3 { line-height: 1.2; }
```

La virgola separa selettori indipendenti. Evita selettori troppo lunghi e dipendenti dalla struttura interna della pagina: rendono gli stili difficili da riutilizzare.
