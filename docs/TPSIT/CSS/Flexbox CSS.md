# Flexbox in CSS

Flexbox è un sistema di layout monodimensionale: dispone gli elementi lungo un asse principale e gestisce l'allineamento sull'asse trasversale.

## Contenitore e figli

```css
.riga {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}
.elemento {
  flex: 1 1 14rem;
}
```

- `display: flex`: attiva il layout Flexbox sui figli diretti.
- `flex-direction`: imposta la direzione (`row`, `column`, ecc.).
- `justify-content`: distribuisce lo spazio lungo l'asse principale.
- `align-items`: allinea gli elementi sull'asse trasversale.
- `gap`: imposta lo spazio fra i figli.
- `flex-wrap`: permette il passaggio alla riga successiva.
- `flex-grow`, `flex-shrink`, `flex-basis` controllano crescita, riduzione e base degli elementi; `flex` è la forma abbreviata.

## Esempio: schede responsive

```html
<div class="schede">
  <article class="scheda">Scheda 1</article>
  <article class="scheda">Scheda 2</article>
  <article class="scheda">Scheda 3</article>
</div>
```

```css
.schede { display: flex; flex-wrap: wrap; gap: 1rem; }
.scheda { flex: 1 1 15rem; padding: 1rem; border: 1px solid #bbb; }
```

Ogni scheda parte da una base di `15rem` e può crescere o andare a capo. Flexbox riguarda i figli diretti del contenitore, non tutti i discendenti in modo automatico.

## Quando usarlo

È adatto a barre di navigazione, gruppi di pulsanti, righe di card e allineamento di elementi. Per griglie bidimensionali con righe e colonne coordinate, valuta CSS Grid.
