# Bootstrap

Bootstrap è un framework CSS con una griglia responsive, classi di utilità e componenti riutilizzabili. Prima di usare una classe, verificane la funzione nella documentazione della versione adottata dal progetto.

## Struttura della griglia

La griglia usa container, righe e colonne. I breakpoint consentono di cambiare il layout a diverse larghezze.

```html
<div class="container">
  <div class="row g-3">
    <div class="col-12 col-md-6 col-lg-4">
      <article class="card h-100">
        <div class="card-body">
          <h2 class="card-title">Titolo</h2>
          <p class="card-text">Descrizione del contenuto.</p>
        </div>
      </article>
    </div>
  </div>
</div>
```

- `container` gestisce larghezza e allineamento della pagina.
- `row` crea una riga e `col-*` definisce colonne responsive.
- `col-12` occupa tutta la riga sui dispositivi piccoli; `col-md-6` usa metà riga dai breakpoint medi.
- `g-3` imposta lo spazio tra le colonne; `h-100` prova a uniformare l'altezza della card nel suo contenitore.

## Componenti previsti dal programma

- **Navbar:** navigazione tra sezioni del sito.
- **Form:** campi ed elementi di invio; ogni campo richiede un'etichetta.
- **Card:** raggruppamento visivo di contenuti correlati.
- **Carousel:** presentazione di contenuti a scorrimento; assicurati che i controlli siano accessibili e che il cambio automatico non ostacoli la lettura.

## Buone pratiche

1. Parti da un layout mobile-first e amplia il layout ai breakpoint più grandi.
2. Non usare Bootstrap come sostituto della semantica HTML.
3. Non affidarti solo al colore per comunicare stato o errore.
4. Mantieni separati contenuto HTML e personalizzazioni CSS quando possibile.
5. Controlla il sito a varie larghezze e con navigazione da tastiera.

Per il sito personale richiesto dal programma, crea almeno una pagina introduttiva, una sezione progetti e un form di contatto accessibile.
