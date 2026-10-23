---
date: 2025-11-11
time: 12:36
---
# HTML5

Da HTML 5 semantico il problema del div coi fino a con tutti i div questo codice non si capisce cosa contiene questo div 
```html
<!DOCTYPE html>

  

<html>

    <head>

  

    </head>

    <body>

        <div>

            <h1>Titolo Sito</h1>

        </div>

        <div>

            <p>Testo della pagina</p>

        </div>

        <div>

            <p>Copyright 2025</p>

        </div>

    </body>

</html>
```
HTML 5 risolve con i tag semantici semantico significa che è nome del tag dice cosa contiene 

```html
<!DOCTYPE html>

  

<html>

    <head>

  

    </head>

    <body>

        <header>

            <h1>Titolo</h1>

        </header>

        <main>

            <p>Contenuto della pagina</p>

        </main>

        <footer>

            <p>© 2025</p>

        </footer>

    </body>

</html>
```

1. HEADER
il tag `<header>`  l'intestazione della pagina contiene il logo il titolo il menu principale
2. NAV
Il tag `<nav>` contiene i link di navigazione il menu
3. MAIN
il tag `<main>` contiene il contenuto principale della pagina. Ce ne può essere uno solo per pagina
4. SECTION
il tag `<section>` è una sezione tematica 
5. ARTICLE
il tag `<article>` è una sezione tematica che ha senso da solo 
6. ASIDE
il tag `<aside>`  è contenuto  correlato ma secondario una sidebar un box informativo
7. FOOTER
il tag `<footer>` è il pie di pagina contatti link ai social 
## Riferimenti
1.