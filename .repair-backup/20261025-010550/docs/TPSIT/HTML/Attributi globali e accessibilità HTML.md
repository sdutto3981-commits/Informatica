# Attributi globali e accessibilità HTML

Gli attributi globali possono essere utilizzati su molti elementi HTML:

- `id`: identifica un elemento in modo univoco nel documento.
- `class`: associa uno o più elementi a una categoria, usata spesso dal CSS e JavaScript.
- `title`: fornisce informazioni supplementari; non deve essere l'unico modo per comunicare un'informazione importante.
- `lang`: specifica la lingua del contenuto.
- `hidden`: indica che il contenuto non è attualmente pertinente e non dovrebbe essere mostrato.
- `tabindex`: controlla la possibilità e l'ordine di ricevere il focus da tastiera; usalo con cautela.
- `data-*`: conserva dati personalizzati associati all'elemento.

## Accessibilità di base

1. Usa la struttura semantica e una gerarchia di titoli coerente.
2. Associa le etichette ai campi tramite `label for` e `id`.
3. Scrivi testi alternativi per le immagini informative.
4. Rendi tutte le funzioni utilizzabili da tastiera e assicurati che il focus sia visibile.
5. Verifica contrasto, dimensione del testo e reflow su schermi piccoli.
6. Evita di comunicare gli stati solo tramite colore.

```html
<label for="ricerca">Cerca un argomento</label>
<input id="ricerca" name="q" type="search">
<button type="submit">Cerca</button>
```

L'accessibilità non si ottiene aggiungendo ARIA a caso: quando esiste un elemento HTML nativo con il comportamento desiderato, normalmente è preferibile usarlo.

## Riferimento

[W3Schools — HTML Attributes](https://www.w3schools.com/html/html_attributes.asp) · [HTML Accessibility](https://www.w3schools.com/html/html_accessibility.asp)
