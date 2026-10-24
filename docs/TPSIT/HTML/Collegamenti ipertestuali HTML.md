# Collegamenti ipertestuali HTML

L'elemento `<a>` crea un collegamento. L'attributo `href` indica la destinazione, che può essere una pagina, una risorsa, un indirizzo e-mail o un'ancora nella stessa pagina.

```html
<a href="progetti.html">I miei progetti</a>
<a href="https://developer.mozilla.org/it/">Documentazione MDN</a>
<a href="#contatti">Vai ai contatti</a>
<a href="mailto:info@example.com">Scrivi un'e-mail</a>

<section id="contatti">
  <h2>Contatti</h2>
</section>
```

## Percorsi relativi e assoluti

- `progetti.html` punta a una risorsa relativa alla posizione del documento.
- `/progetti.html` parte dalla radice del sito.
- `https://example.com/progetti.html` è un URL assoluto completo.
- `#contatti` sposta la navigazione a un elemento con ID `contatti` nel documento corrente.

Usa un testo link descrittivo: “Scarica il PDF del progetto” è più utile di “clicca qui”. Non usare l'elemento `<a>` come pulsante per eseguire azioni locali; usa `<button>` quando l'utente attiva un comportamento.
