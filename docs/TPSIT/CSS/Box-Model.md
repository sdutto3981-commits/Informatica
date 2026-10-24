# Box model CSS

Ogni elemento HTML può essere rappresentato come una scatola composta da **content**, **padding**, **border** e **margin**.

- **Content:** area del contenuto; `width` e `height` la dimensionano nel modello predefinito.
- **Padding:** spazio interno tra contenuto e bordo; lo sfondo dell'elemento si estende in quest'area.
- **Border:** cornice del riquadro.
- **Margin:** spazio esterno che separa la scatola dagli elementi vicini.

## `content-box` e `border-box`

Con il valore predefinito `box-sizing: content-box`, la larghezza totale occupata è contenuto + padding sinistro/destro + bordi sinistro/destro.

```css
.box {
  width: 200px;
  padding: 20px;
  border: 10px solid black;
  box-sizing: content-box;
}
```

La larghezza esterna è `200 + 40 + 20 = 260px` (il margine è escluso dal calcolo). Con `box-sizing: border-box`, i 200 px comprendono contenuto, padding e bordo.

```css
* {
  box-sizing: border-box;
}
```

Questa regola è comune per rendere più prevedibile il dimensionamento.

## Dimensionamento e overflow

- Le dimensioni possono essere esplicite (`width: 300px`) o dipendere dal contenuto (`min-content`, `max-content`).
- `min()`, `max()` e `clamp()` permettono di combinare valori per layout adattivi.
- `overflow` regola il contenuto che eccede il riquadro (`visible`, `hidden`, `auto`, `scroll`). Non nascondere contenuti importanti senza offrire un modo per accedervi.
- `display: block`, `inline` e `inline-block` influenzano flusso, larghezza e comportamento del box.

## Esempio responsive

```css
.contenitore {
  width: min(100% - 2rem, 70rem);
  margin-inline: auto;
}
```

La larghezza si adatta allo schermo mantenendo un margine laterale e un limite massimo.
