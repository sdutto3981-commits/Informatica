# Transizioni e animazioni CSS

Una transizione interpola una proprietà quando cambia valore; un'animazione CSS può definire più passaggi con `@keyframes`.

## Transizione

```css
.pulsante {
  background: #2457a7;
  color: white;
  transition: background-color 180ms ease, transform 180ms ease;
}
.pulsante:hover { background: #173d79; transform: translateY(-2px); }
.pulsante:focus-visible { outline: 3px solid orange; outline-offset: 2px; }
```

## Animazione

```css
@keyframes comparsa {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
.card { animation: comparsa 300ms ease-out both; }
```

Le animazioni devono essere brevi e avere uno scopo. Il movimento non deve impedire la lettura o rendere difficile l'interazione.

## Rispetto delle preferenze

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Questa regola riduce i movimenti non essenziali per chi ha attivato la preferenza di sistema.

## Riferimento

[W3Schools — CSS Animations](https://www.w3schools.com/css/css3_animations.asp) · [CSS Transitions](https://www.w3schools.com/css/css3_transitions.asp)
