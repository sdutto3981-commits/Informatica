# Attributo `src` per le risorse

L'attributo `src` specifica l'URL della risorsa incorporata in elementi come `img`, `script`, `audio`, `video` e `iframe` nei casi previsti. `src` indica la risorsa da caricare; non va confuso con `href`, usato per collegare una risorsa, per esempio un foglio CSS o una destinazione di navigazione.

```html
<img src="immagini/logo.png" alt="Logo del sito">
<script src="app.js" defer></script>
<link rel="stylesheet" href="style.css">
```

I percorsi relativi sono calcolati rispetto all'URL del documento HTML. Controlla che il file esista e che maiuscole/minuscole corrispondano al nome reale quando il sito è pubblicato su un sistema che distingue il case.

> Il nome storico di questo file contiene `scr`; l'attributo HTML corretto è `src`.
