---
date: 2025-09-25
time: 20:15
---
# HTML-Usare CSS

Possiamo aggiungere CSS ai documenti in 3 modi:
- **In linea** - usando l'attributo `style=""`
- **Interno**-usando il tag `<style>` nel elemento `<head>`
- **Esterno**-usando il tag `<link>` per aggiungere il file CSS esterno

#### In linea CSS

Un CSS in line viene utilizza per applicare uno stile univoco lo si usa tramite il comando `style` 

```html
<h1 style="color:blue;">A Blue Heading</h1>
```
#### CSS interno

Per definire un CSS interno viene definito all'interno del  tag `<head>` all'interno del tag `<style>` 

```html
<head>  
<style>  
body {background-color: powderblue;}  
h1   {color: blue;}  
p    {color: red;}  
</style>  
</head>
```

#### CSS esterno

Possiamo usare un file di stile esterno CSS il link a questo file viene inserito all'interno del tag `<head>` 

```html
<head>  
  <link rel="stylesheet" href="styles.css">  
</head>
```


## Riferimenti
1.