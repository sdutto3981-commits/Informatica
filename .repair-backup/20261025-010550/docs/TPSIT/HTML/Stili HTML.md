# Stili HTML e proprietà CSS

L'attributo `style` permette di applicare CSS direttamente a un elemento, ma per un progetto mantenibile è preferibile usare un file CSS esterno.

Esempio in linea:

```html
<p style="color: #b00020; text-align: center;">Testo di esempio</p>
```

Le proprietà usate sono CSS:

- `background-color`: colore di sfondo;
- `color`: colore del testo;
- `font-family`: famiglia tipografica;
- `font-size`: dimensione del testo;
- `text-align`: allineamento orizzontale del testo.

Attenzione ai nomi esatti: `background-color` è corretto, non `background-color`; `text-align` è corretto, non `text-align` o `text-align`.

Per separare contenuto e presentazione, definire una classe nel file CSS:

```html
<p class="avviso">Testo di esempio</p>
```

```css
.avviso {
  color: #b00020;
  text-align: center;
}
```

Vedi [collegare CSS a HTML](HTML-Usare%20CSS.md) e la sezione [CSS](../CSS/index.md).
