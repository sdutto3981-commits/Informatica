# Classi, ID e layout HTML

## `class` e `id`

`class` assegna una o più categorie a elementi che possono condividere uno stile. `id` identifica un elemento specifico nel documento e deve essere univoco.

```html
<section id="progetti" class="sezione sezione-evidenza">
  <h2 class="titolo-sezione">Progetti</h2>
  <p>Una sezione di esempio.</p>
</section>
```

Nel CSS il selettore `.sezione` individua la classe; `#progetti` individua l'ID. In JavaScript si possono usare `querySelector()` e `getElementById()`.

## Block e inline

Gli elementi block normalmente iniziano su una nuova riga e occupano la larghezza disponibile nel contesto; quelli inline partecipano al flusso del testo. Il comportamento visuale può essere modificato con la proprietà CSS `display`.

Esempi comuni: `div` e `p` si comportano tipicamente come block; `span` e `a` come inline. Il comportamento preciso dipende dallo stile CSS applicato.

## `div` e `span`

Sono contenitori generici senza un significato semantico specifico:

- `div` raggruppa contenuti a livello di blocco.
- `span` raggruppa testo o contenuti in linea.

Quando esiste un elemento semantico adatto, come `nav`, `main`, `section` o `article`, preferiscilo a un contenitore generico.

## Layout moderno

La struttura si definisce in HTML; il posizionamento deve essere controllato principalmente tramite CSS, per esempio Flexbox, Grid, margini e padding. Non usare tabelle HTML per costruire la griglia visiva della pagina.

## Riferimento

[W3Schools — HTML Classes](https://www.w3schools.com/html/html_classes.asp) · [HTML Id](https://www.w3schools.com/html/html_id.asp) · [HTML Block and Inline](https://www.w3schools.com/html/html_blocks.asp)
