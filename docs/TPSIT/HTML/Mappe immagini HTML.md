# Mappe immagine HTML

Una *image map* associa aree cliccabili di un'immagine a collegamenti differenti. Si definisce l'immagine con `usemap`, poi una `<map>` con elementi `<area>` e coordinate.

```html
<img src="pianta.png" alt="Pianta dell'edificio: seleziona una zona"
     width="600" height="400" usemap="#edificio">

<map name="edificio">
  <area shape="rect" coords="20,20,180,120"
        href="laboratorio.html" alt="Laboratorio">
  <area shape="circle" coords="300,200,45"
        href="biblioteca.html" alt="Biblioteca">
</map>
```

## Forme e coordinate

- `rect`: `x1,y1,x2,y2` (angolo in alto a sinistra e angolo in basso a destra).
- `circle`: `x,y,raggio`.
- `poly`: coppie successive di coordinate dei vertici.
- `default`: area residua, se necessaria.

Le coordinate sono riferite alle dimensioni della mappa e possono non adattarsi automaticamente quando l'immagine viene ridimensionata via CSS. Per pagine responsive considera SVG con elementi `<a>` accessibili o una lista di link equivalenti accanto all'immagine. Non fare affidamento esclusivamente sul colore o su un'area cliccabile senza descrizione.
