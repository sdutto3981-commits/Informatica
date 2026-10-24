# Intestazioni HTML (`h1`–`h6`)

I titoli HTML indicano la gerarchia dei contenuti. `<h1>` rappresenta il titolo di livello più alto del contenuto della pagina; `<h2>` introduce una sezione e `<h3>` una sottosezione di quella sezione, e così via fino a `<h6>`.

```html
<main>
  <h1>Progetto di robotica</h1>
  <h2>Hardware</h2>
  <h3>Sensori</h3>
  <p>Descrizione dei sensori montati.</p>
  <h2>Software</h2>
  <p>Descrizione del programma di controllo.</p>
</main>
```

## Buone pratiche

- Scegli il livello in base alla struttura logica, non alla dimensione grafica desiderata.
- Evita di saltare livelli solo per ottenere un titolo più piccolo; usa CSS per lo stile.
- I titoli dovrebbero descrivere il contenuto che segue e aiutare a navigare la pagina, anche con tecnologie assistive.
- Non usare `<h1>`–`<h6>` solo per rendere il testo grande o in grassetto: per questi scopi esistono le proprietà CSS.
