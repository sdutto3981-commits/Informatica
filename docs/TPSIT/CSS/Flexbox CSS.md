# Flexbox CSS

Flexbox è un modello di layout monodimensionale: dispone elementi lungo un asse principale e li allinea lungo l'asse trasversale. È adatto a barre di navigazione, gruppi di pulsanti, righe di schede e allineamenti.

## Contenitore e proprietà

```css
.menu {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.menu a { flex: 0 1 auto; }
```

- `display: flex` attiva Flexbox sui figli diretti.
- `flex-direction`: `row`, `row-reverse`, `column` o `column-reverse`.
- `flex-wrap`: permette agli elementi di andare a capo.
- `justify-content`: distribuisce lo spazio lungo l'asse principale.
- `align-items`: allinea gli elementi sull'asse trasversale.
- `gap`: spazio tra gli elementi.
- `align-self`: sovrascrive l'allineamento di un singolo elemento.
- `flex`: scorciatoia per crescita, restringimento e base dell'elemento.

## Esempio di card

```css
.cards { display: flex; flex-wrap: wrap; gap: 1rem; }
.card { flex: 1 1 15rem; padding: 1rem; border: 1px solid #ccc; }
```

La base `15rem` indica una dimensione preferita; le card possono crescere o restringersi e andare a capo. Il risultato dipende dallo spazio disponibile, quindi va provato a larghezze diverse.

## Errori comuni

- Confondere asse principale e asse trasversale: cambiano in base a `flex-direction`.
- Applicare proprietà del contenitore al singolo figlio o viceversa.
- Usare `order` per cambiare arbitrariamente l'ordine visivo rispetto alla sequenza logica: può peggiorare l'esperienza con tastiera e screen reader.

## Riferimento

[W3Schools — CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp)
