# Box model CSS

Il box model descrive come il browser calcola lo spazio occupato da un elemento: **content**, **padding**, **border** e **margin**.

- **Content:** area del contenuto; `width` e `height` si riferiscono a questa area con `box-sizing: content-box`.
- **Padding:** spazio interno tra contenuto e bordo; lo sfondo dell'elemento si estende normalmente anche qui.
- **Border:** bordo intorno al padding e al contenuto.
- **Margin:** spazio esterno al bordo, che separa l'elemento dagli altri. Lo sfondo dell'elemento non dipinge il margine.

## `content-box` e `border-box`

```css
.content-box {
  box-sizing: content-box;
  width: 200px;
  padding: 20px;
  border: 10px solid;
}

.border-box {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 10px solid;
}
```

Con `content-box`, la larghezza esterna di base è `200 + 20×2 + 10×2 = 260px`, senza contare il margine. Con `border-box`, la larghezza complessiva comprensiva di padding e bordo è `200px`.

È comune applicare:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

## Overflow e dimensionamento

Se il contenuto non entra nel box si verifica overflow. `overflow: auto` mostra le barre di scorrimento quando necessarie; `hidden` taglia l'eccesso; `visible` è il comportamento iniziale comune. `min-content` e `max-content` possono essere usati per il dimensionamento intrinseco.

Il `outline` è disegnato fuori dal bordo ma non occupa spazio nel calcolo del box; anche `box-shadow` non modifica le dimensioni di layout. Il margine, invece, partecipa alla spaziatura esterna e i margini verticali di elementi a blocco possono collassare in determinate condizioni.
