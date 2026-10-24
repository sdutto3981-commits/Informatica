# Puntatori in C

Un puntatore contiene l'indirizzo di un oggetto o funzione compatibile. L'operatore `&` ottiene l'indirizzo di un oggetto; `*` in una dichiarazione indica un puntatore e, in un'espressione, dereferenzia un puntatore valido.

```c
int valore = 10;
int *p = &valore;

printf("%d\n", *p); /* 10 */
*p = 15;
printf("%d\n", valore); /* 15 */
```

## Puntatori e array

In molte espressioni il nome di un array si converte in puntatore al primo elemento, ma array e puntatori non sono lo stesso tipo. L'aritmetica dei puntatori avanza di elementi del tipo puntato, non di byte singoli.

```c
int numeri[] = {3, 6, 9};
int *p = numeri;
printf("%d\n", *(p + 1)); /* 6 */
```

Un puntatore può essere confrontato o dereferenziato solo nel rispetto delle regole del linguaggio. Dereferenziare `NULL`, un puntatore non inizializzato, liberato o fuori dall'oggetto valido produce comportamento indefinito.

## `NULL` e validità

Inizializza i puntatori quando possibile. Prima di dereferenziare un puntatore ricevuto come parametro, stabilisci se il contratto della funzione permette `NULL` e controllalo se necessario.

## Passaggio per indirizzo

```c
void raddoppia(int *n) {
    if (n != NULL) *n *= 2;
}
```

Chiamata: `raddoppia(&valore);`.

## Riferimento

[W3Schools — C Pointers](https://www.w3schools.com/c/c_pointers.php)
