# Commenti HTML

Un commento HTML inserisce una nota nel sorgente senza mostrarla come contenuto normale della pagina.

```html
<!-- La navigazione principale inizia qui. -->
<nav aria-label="Navigazione principale">
  <a href="index.html">Home</a>
</nav>
```

## Regole

- Inizia con `<!--` e termina con `-->`.
- I commenti possono aiutare a documentare sezioni complesse, ma non dovrebbero ripetere ciò che il codice rende già evidente.
- I commenti HTML non supportano commenti annidati affidabili: una sequenza `-->` interna può chiudere il commento prima del previsto.
- I commenti sono presenti nel sorgente scaricato dal browser: non inserirvi password, token, dati personali o segreti.
- Per commentare JavaScript usa `//` o `/* ... */`; per CSS usa `/* ... */`. Le regole di un linguaggio non si applicano automaticamente agli altri.
