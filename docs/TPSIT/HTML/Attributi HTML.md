---
date: 2025-09-19
time: 12:35
---
# Attributi HTML

- Tutti gli elementi possono avere attributi
- Gli attributi forniscono informazioni aggiuntive
- Gli attributi sono specificati nel tag  di inizio
- Sono normalmente composti come; nome="valore"

#### Attributo href

Il tag `<a>` definisce un collegamento ipertestuale l' `href` specifica l'URL

`<a href="https://www.w3schools.com">Visit W3Schools</a>`

#### Attributo scr

Il tag `<img>` viene utilizzato per le immagini e l'attributo `scr` serve per specificare il percorso dell'immagine

1. **URL assoluto** ovvero un immagine esterna ospitata su un altro sito web
2. **URL relativo** ovvero un immagine interna al computer e viene specificata da un percorso 

#### Gli attributi larghezza altezza

Per esempio sempre con il tag `<img>` ne specifichiamo la larghezza `width=` e l'altezza `height=` in pixel

#### Attributo alt

Questo attributo è obbligatorio è specifica un testo alternativo se non avviene il caricamento dell'immagine

`<img src="img_girl.jpg" alt="Girl with a jacket">`


#### Attributo style

L' style viene utilizzato per aggiungere stili a un elemento come colore, carattere, dimensione e altro ancora

#### Attributo lang

Dovrebbe sempre essere incluso l'attributo `lang` all'interno del tag `<html>` ovvero per richiamare la lingua della pagina web 

```html
<!DOCTYPE html>  
<html lang="en">  
<body>  
...  
</body>  
</html>
```

#### Attributo title 

Aggiunge informazioni aggiuntive all' tag in cui inserito quando il contenuto di esso viene evidenziato con il mouse

```html
<p title="I'm a tooltip">This is a paragraph.</p>
```

#### Regole generali per l'uso degli attributi

- l'attributi sempre in minuscolo
- Sempre bene usare le virgolette anche se non è sempre obbligatorio
- Si possono usare entrambe ma se all'interno del testo dobbiamo usare virgolette doppie o singole usiamo gli opposti 
## Riferimenti
1. 