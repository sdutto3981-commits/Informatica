---
date: 2025-12-04
time: 08:14
---
# Strutture e tipi di dati

## Numeri interi

Quando usiamo la funzione `Number()` il valore al so interno viene convertito in un numero equivalente

```js
Number("10")
>10
Numeber(null)
>0
Number(false)
>0
Number(true)
>1
```

Se il valore non può essere convertito in un valore numerico restituisce `NaN`

## Stringhe

Qualsiasi carattere numeri simboli e cosi via tra `" ' '` è una stringa 

```js
console.log("Hello World.");
>Hello World.
```

Otteniamo lo stesso risultato se la stringa fosse contenuta in pedici singoli o altro carattere alcuni caratteri per essere stampati dobbiamo usare `\`

 ### Oggetto stringa

Quando viene chiama l'oggetto stringa `String` forza un valore  a essere specificato come una stringa

```js
let myString = String( 10 );

myString
> "10"

typeof myString
> string
```

### Concatenazione

```js
console.log( "My" + " string." );
> My string.
```

Possiamo concatenare anche valori stringa e variabili utilizzando `${}`
pero per fare cio serve `''`

```js
console.log( `The result is ${ 2 + 4 }.` );
> The result is 6.
```

## Valori booleani

Possono avere due tipi di dati primitivi ovvero `true o false`

I valori che generano `false` includono `0,null,undefined,NaN, ""` un valore omesso è un valore booleano `false` tutti gli altri generano `true`.

## Riferimenti
1. 