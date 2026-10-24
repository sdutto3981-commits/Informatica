# Attributi globali e accessibilità HTML

Gli attributi globali possono essere usati su molti elementi HTML.

| Attributo | Scopo |
|---|---|
| `id` | Identificatore unico nel documento |
| `class` | Una o più classi usate soprattutto da CSS e JavaScript |
| `title` | Informazione supplementare; non sostituisce un'etichetta accessibile |
| `lang` | Lingua del contenuto dell'elemento |
| `hidden` | Indica che il contenuto non deve essere presentato |
| `data-*` | Conserva dati personalizzati associati all'elemento |
| `tabindex` | Controlla la partecipazione al focus da tastiera; usarlo con criterio |

## Principi essenziali

- Usa HTML nativo: un vero `button` è attivabile da tastiera e ha semantica corretta; un `div` cliccabile non lo è automaticamente.
- Fornisci testo alternativo per immagini informative e `alt=""` per immagini puramente decorative.
- Associa `label` ai controlli dei form e indica gli errori con testo comprensibile.
- Mantieni una gerarchia di titoli chiara e landmark semantici.
- Assicurati che link, pulsanti e controlli funzionino senza mouse.
- Non utilizzare soltanto il colore per comunicare uno stato.
- Il testo di un link deve indicare la destinazione, evitando formulazioni vaghe come “clicca qui” quando manca contesto.

## Esempio: `data-*` letto da JavaScript

```html
<button type="button" data-codice="A17">Apri dettaglio</button>
```

```javascript
const pulsante = document.querySelector("[data-codice]");
console.log(pulsante.dataset.codice); // "A17"
```

`data-*` memorizza dati, ma non sostituisce un modello applicativo ben progettato né un controllo di sicurezza lato server.
