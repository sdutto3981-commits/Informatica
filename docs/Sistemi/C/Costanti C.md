# Costanti in C

Una costante rappresenta un valore che il programma non deve modificare dopo la definizione o durante il normale flusso di esecuzione. In C si incontrano soprattutto `const` e le macro definite con `#define`, che hanno meccanismi diversi.

## Oggetto qualificato `const`

```c
const double PI = 3.141592653589793;
const int DIMENSIONE = 10;
```

`const` qualifica un oggetto: attraverso quel nome il programma non può assegnargli un nuovo valore. Non equivale sempre a una costante intera utilizzabile in ogni espressione richiesta dal compilatore; per gli array a dimensione compilata, per esempio, la regola dipende dal contesto e dallo standard C.

## Macro `#define`

```c
#define BUFFER_SIZE 256
#define IVA 0.22
```

Il preprocessore sostituisce il token della macro prima della compilazione: non crea necessariamente un oggetto tipizzato e non applica il controllo dei tipi come una variabile. Per macro con espressioni usa parentesi:

```c
#define QUADRATO(x) ((x) * (x))
```

Anche con le parentesi, una macro può valutare più volte il parametro; `QUADRATO(i++)`, per esempio, non è sicuro. Preferisci una funzione quando è appropriato.

## `const` o `#define`?

- Usa `const` quando vuoi un oggetto tipizzato con ambito e regole del linguaggio.
- Usa `#define` per macro del preprocessore, guardie degli header e valori di configurazione che richiedono sostituzione testuale.
- Non terminare una macro `#define` con `;`, perché il punto e virgola entra nel testo sostituito.

Per tipi e dichiarazione delle variabili consulta [Tipi e variabili in C](Tipi%20e%20variabili%20C.md).
