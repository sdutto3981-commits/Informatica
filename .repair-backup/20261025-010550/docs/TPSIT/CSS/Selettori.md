# Selettori CSS

Un selettore individua gli elementi HTML a cui applicare le dichiarazioni CSS.

```css
p { color: #333; }                 /* tutti i paragrafi */
.avviso { color: #a00; }           /* class="avviso" */
#titolo-principale { font-size: 2rem; } /* id specifico */
nav a { text-decoration: none; }   /* link discendenti di nav */
.card > h2 { margin-top: 0; }      /* figli diretti */
input[type="email"] { width: 100%; }
a:hover { text-decoration: underline; }
button:focus-visible { outline: 3px solid orange; }
```

## Famiglie principali

- Elemento: `p`, `h1`, `button`.
- Classe: `.card`; può essere riutilizzata più volte.
- ID: `#menu-principale`; deve essere univoco nel documento.
- Attributo: `[required]`, `[type="email"]`.
- Relazione: discendente `A B`, figlio diretto `A > B`, fratello adiacente `A + B`.
- Pseudoclasse: `:hover`, `:focus`, `:focus-visible`, `:checked`, `:first-child`.
- Pseudoelemento: `::before`, `::after`, `::first-letter`.

## Gruppi e commenti

```css
h1, h2, h3 { line-height: 1.2; }
/* Commento: non viene mostrato nella pagina */
```

## Buone pratiche

Preferisci classi descrittive per gli stili riutilizzabili. Usa selettori troppo specifici soltanto quando necessario: rendono più difficile sovrascrivere le regole in seguito.

Approfondisci anche [cascata e specificità](Cascata%20specificit%C3%A0%20ereditariet%C3%A0%20CSS.md).

## Riferimento

[W3Schools — CSS Selectors](https://www.w3schools.com/css/css_selectors.asp)
