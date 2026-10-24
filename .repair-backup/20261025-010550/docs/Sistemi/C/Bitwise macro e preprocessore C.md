# Macro, preprocessore e operatori bitwise in C

## Preprocessore

Le direttive iniziano con `#` e vengono elaborate prima della compilazione vera e propria.

```c
#include <stdio.h>
#define MASSIMO(a, b) ((a) > (b) ? (a) : (b))

int main(void) {
    printf("%d\n", MASSIMO(3, 7));
    return 0;
}
```

Una macro è una sostituzione testuale: racchiudere gli argomenti tra parentesi aiuta a evitare errori di precedenza, ma le macro con argomenti valutati più volte possono causare effetti collaterali. Quando possibile, preferisci funzioni tipizzate per comportamenti non banali.

## Include guard

Gli header personalizzati spesso proteggono le dichiarazioni dalla doppia inclusione:

```c
#ifndef MIO_HEADER_H
#define MIO_HEADER_H
/* dichiarazioni */
#endif
```

## Operatori bitwise

`&`, `|`, `^`, `~`, `<<` e `>>` operano sui bit degli interi. Non vanno confusi con gli operatori logici `&&`, `||` e `!`.

```c
unsigned int x = 0b0101;
unsigned int y = 0b0011;
unsigned int and_bit = x & y;
unsigned int or_bit = x | y;
unsigned int xor_bit = x ^ y;
```

La sintassi letterale binaria è disponibile negli standard moderni (C23); con compilatori/standard precedenti usa esadecimale o valori decimali. Gli shift su numeri signed e su conteggi fuori intervallo possono avere regole problematiche: per manipolazione bit, i tipi unsigned sono spesso più semplici.

## Riferimento

[W3Schools — C Preprocessor/Macros](https://www.w3schools.com/c/c_macros.php) · [C Bitwise Operators](https://www.w3schools.com/c/c_bitwise_operators.php)
