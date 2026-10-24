# Classi e moduli JavaScript

## Classi

Le classi forniscono una sintassi per creare oggetti con proprietà e metodi. La parola chiave `constructor` inizializza le nuove istanze.

```javascript
class Contatore {
  constructor(iniziale = 0) {
    this.valore = iniziale;
  }

  incrementa() {
    this.valore++;
    return this.valore;
  }
}

const contatore = new Contatore();
console.log(contatore.incrementa()); // 1
```

`this` nei metodi tradizionali si riferisce al ricevente della chiamata. Se si passa un metodo come callback, il contesto può cambiare; una funzione freccia cattura invece il `this` del contesto esterno.

JavaScript usa un modello basato su prototipi; `class` è una sintassi più strutturata per lavorare con quel modello. Non coincide in ogni aspetto con le classi di C#.

## Moduli

I moduli ES consentono di suddividere il codice tra file con `export` e `import`.

```javascript
// matematica.js
export function somma(a, b) {
  return a + b;
}
```

```javascript
// app.js
import { somma } from './matematica.js';
console.log(somma(2, 3));
```

Per il browser, la pagina può caricare il file principale con `<script type="module" src="app.js"></script>`. I moduli vengono eseguiti in modalità strict; gli import hanno bisogno di percorsi e origine validi, perciò è preferibile provare il progetto tramite un server locale invece di aprire direttamente il file `file://`.

## Riferimento

[W3Schools — JavaScript Classes](https://www.w3schools.com/js/js_classes.asp) · [JavaScript Modules](https://www.w3schools.com/js/js_modules.asp)
