# Introduzione a HTML

**HTML** significa *HyperText Markup Language*. È un linguaggio di marcatura che descrive struttura e significato di una pagina web. Il browser interpreta gli elementi e costruisce il DOM (Document Object Model).

## Elemento, tag e attributo

```html
<p class="introduzione">Benvenuto nel sito.</p>
```

- Elemento: l'intero blocco composto da tag, contenuto ed eventuale chiusura.
- Tag di apertura: `<p class="introduzione">`.
- Contenuto: `Benvenuto nel sito.`
- Tag di chiusura: `</p>`.
- Attributo: `class`, con valore `introduzione`.

Alcuni elementi sono vuoti e non racchiudono contenuto, come `<img>` e `<br>`; non si scrive `</img>`.

## Scheletro del documento

```html
<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pagina di prova</title>
</head>
<body>
  <h1>Primo titolo</h1>
  <p>Primo paragrafo.</p>
</body>
</html>
```

`<!doctype html>` dichiara il documento HTML moderno. `html` contiene l'intera pagina; `head` contiene metadati e riferimenti a risorse; `body` contiene il contenuto mostrato nella pagina.

## Regole di base

- Annida gli elementi correttamente e chiudi quelli che richiedono un tag di chiusura.
- Usa un solo titolo principale `h1` quando riflette la struttura del contenuto; usa `h2`, `h3` ecc. in ordine gerarchico.
- Attribuisci al documento la lingua principale con `lang`.
- Non usare HTML per simulare spazi o impaginare: struttura con HTML e presenta con CSS.

## Collegamento con CSS e JavaScript

```html
<link rel="stylesheet" href="styles.css">
<script src="app.js" defer></script>
```

`href` indica il foglio di stile; `src` il file JavaScript. `defer` rinvia l'esecuzione dello script esterno fino al termine del parsing del documento.

## Verifica

Apri la pagina nel browser, controlla il titolo della scheda e usa gli strumenti per sviluppatori per osservare eventuali errori.

## Riferimento

[W3Schools — HTML Introduction](https://www.w3schools.com/html/html_intro.asp)
