# Cascata, specificità ed ereditarietà CSS

Quando più regole possono applicarsi allo stesso elemento, il browser determina quale valore usare tramite la cascata.

## Cascata

Nel risultato influiscono origine e importanza della dichiarazione, livello di cascata, specificità e ordine delle regole. A parità degli altri fattori, una regola dichiarata dopo può prevalere su una precedente.

```css
p { color: navy; }
p { color: darkgreen; } /* prevale, a parità di specificità */
```

## Specificità

Come modello introduttivo si può confrontare il numero di selettori ID, classi/attributi/pseudoclassi e tipi/pseudoelementi:

```css
p { color: black; }          /* selettore di tipo */
.avviso { color: orange; }   /* classe */
#errore { color: red; }      /* ID */
```

Il selettore con ID ha specificità maggiore dei selettori di classe e di tipo in questo esempio. La specificità non è l'unico fattore della cascata: `!important`, origine, layer e altre regole possono cambiare il risultato.

## Ereditarietà

Alcune proprietà, come `color` e `font-family`, sono normalmente ereditate dai discendenti; altre, come `margin` e `border`, normalmente no.

```css
body { font-family: Arial, sans-serif; color: #222; }
.card { border: 1px solid #ccc; }
```

Gli elementi dentro `body` ereditano la famiglia di caratteri e il colore se non hanno un valore diverso; non ereditano automaticamente il bordo della `.card`.

## Buone pratiche

- Preferisci classi descrittive e selettori leggibili.
- Evita di usare ID come sistema generale di stile.
- Non aggiungere `!important` per risolvere ogni conflitto.
- Usa gli strumenti sviluppatore del browser per vedere le dichiarazioni applicate e quelle sovrascritte.
