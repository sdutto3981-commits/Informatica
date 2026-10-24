# Transizioni e animazioni CSS

## Transizioni

Una transizione rende graduale il cambiamento di una proprietà quando passa da un valore a un altro.

```css
.pulsante {
  background-color: #244b8f;
  color: white;
  transition: background-color 180ms ease-in-out;
}
.pulsante:hover { background-color: #17315e; }
```

`transition` può specificare proprietà, durata, funzione temporale e ritardo. Preferisci animare `transform` e `opacity` quando adatto, invece di animare continuamente proprietà che richiedono un ricalcolo costoso del layout.

## Animazioni con `@keyframes`

```css
@keyframes comparsa {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
.avviso {
  animation: comparsa 300ms ease-out both;
}
```

`animation-duration`, `animation-delay`, `animation-iteration-count` e `animation-direction` controllano aspetti diversi dell'animazione.

## Accessibilità e prestazioni

- Non usare movimento continuo senza uno scopo.
- Mantieni leggibile il contenuto anche se l'animazione non viene riprodotta.
- Rispetta la preferenza di riduzione del movimento:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Usa gli effetti per migliorare il feedback, non per rendere necessario attendere un'animazione prima di poter utilizzare la pagina.
