# HTML5 e HTML moderno

HTML5 ha introdotto elementi semantici, supporto nativo per media e diverse API. Oggi il termine HTML viene usato per lo standard HTML moderno: non è necessario indicare una versione numerata nel doctype.

## Doctype e metadati

```html
<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Portfolio</title>
  <meta name="description" content="Progetti e appunti personali">
</head>
<body>
  <main><h1>Portfolio</h1></main>
</body>
</html>
```

- `charset="utf-8"` consente di rappresentare correttamente gran parte dei caratteri usati nelle lingue moderne.
- `viewport` aiuta a rendere il layout adatto alla larghezza del dispositivo.
- `title` identifica la pagina nella scheda del browser e nei risultati di ricerca.
- `description` fornisce una breve descrizione, utile in alcuni contesti di anteprima.

## Perché la semantica conta

Un gruppo di `<div>` può essere visualmente identico a una struttura semantica, ma fornisce meno informazioni sul ruolo delle parti. Preferisci `header`, `nav`, `main`, `section`, `article`, `aside` e `footer` quando descrivono davvero il contenuto.

```html
<header>
  <h1>Portale scolastico</h1>
  <nav aria-label="Navigazione principale">
    <a href="index.html">Home</a>
    <a href="progetti.html">Progetti</a>
  </nav>
</header>
<main>
  <article>
    <h2>Ultimo progetto</h2>
    <p>Descrizione del progetto.</p>
  </article>
</main>
<footer><small>Materiale didattico</small></footer>
```

## Elementi semantici principali

- `header`: intestazione di una pagina o di una sezione.
- `nav`: gruppo importante di link di navigazione.
- `main`: contenuto principale della pagina, normalmente unico.
- `section`: sezione tematica, di solito con un titolo.
- `article`: contenuto autonomo e riutilizzabile.
- `aside`: contenuto correlato ma secondario.
- `footer`: informazioni finali di una pagina o sezione.

Non è necessario sostituire ogni `div`: un contenitore generico è corretto quando nessun elemento semantico descrive meglio il suo ruolo.

## Riferimento

[W3Schools — HTML Semantics](https://www.w3schools.com/html/html5_semantic_elements.asp)
