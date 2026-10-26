# XML

Per poter inviare dati tra un client-server bisofna utilizzare un formato adeguato come XML.

### Esempio

Se devo leggere un file contenenete una playlist e inviare  questi dati a una pagina web se fossero scrivi di semplice testo questi non sarebbero letti in modo tale che possano essere usati come oggetti.

```XML
<?xml version="1.0" encoding="UTF-8"?>
<playlist nome="Classici italiani">
  <canzone anno="1958" durata="215">
    <titolo>Nel blu dipinto di blu</titolo>
    <artista>Domenico Modugno</artista>
  </canzone>
  <canzone anno="1968" durata="218">
    <titolo>Azzurro</titolo>
    <artista>Adriano Celentano</artista>
  </canzone>
  <canzone anno="1971" durata="328">
    <titolo>La canzone del sole</titolo>
    <artista>Lucio Battisti</artista>
  </canzone>
  <canzone anno="1981" durata="193">
    <titolo>Sarà perché ti amo</titolo>
    <artista>Ricchi e Poveri</artista>
  </canzone>
  <canzone anno="2022" durata="210">
    <titolo>Brividi</titolo>
    <artista>Mahmood &amp; Blanco</artista>
  </canzone>
</playlist>
```