# Attributo `action` dei form

L'attributo `action` di un elemento `form` indica l'URL a cui viene inviata la richiesta quando il form è inviato.

```html
<form action="/ricerca" method="get">
  <label for="q">Cerca</label>
  <input id="q" name="q" type="search">
  <button type="submit">Cerca</button>
</form>
```

I valori dei controlli vengono normalmente inviati solo se i campi sono denominati (`name`) e fanno parte del form. Se `action` è omesso, il form invia alla URL corrente. L'effettiva elaborazione dipende dal server o dal codice client previsto.

La validazione nel browser migliora l'esperienza, ma un server deve validare nuovamente ogni dato ricevuto.
