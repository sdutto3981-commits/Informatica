---
date: 2025-09-30
time: 09:53
---
# Generazione numeri Random C Sharp

```C#
int numero;
Ramdom rnd;
```

Da int  a Random  come ami perché esso è orientato agli oggetti detto Object Oriented gli oggetti sono strutture definite da classi come andiamo a definire degli oggetti con un tipo possiamo definire un oggetto con una classe

```C#
int(tipo) numero(variabile);
Ramdom(Classe) rnd(Oggetto);
```

rnd ha a disposizione delle funzioni specifiche.

Siccome rnd è un oggetto bisogna prima dichiarare l'oggetto e poi in stanziare l'oggetto

```C#
int numero;
Ramdom rnd;
rnd = new Random();

-----

int numero;
Random rnd = new Random();


```

#### Metodi di Random

##### Numeri interi

```C#
int numero;
Ramdom rnd = new Random();

//metodi di Random (funzioni)
numero=rnd.next(1, 10); //genera un numero compreso casuale int compreso tra 1 e 9 il rpimo è incluso il secondo non lo è quindi primo a secondo-1
Console.writeLine(numero);
Console.readKey;
 ```

Questo ci restituisce in output un numero compreso tra 1 e 9 per esempio volessimo generare una serie di numeri come voti di scuola quindi da 1 a 9
possiamo usare un for e poi comprende i valori tra 1 e 11.

##### Numeri con la virgola

```C#
double num_v;

num_v=rnd.NextDouble(); //Genera numeri tra 0 - 1(escluso) quindi da 0 - 0.9999999999...

//Generare numeri compreso tra 0.00 e 10.00
num_v = rnd.NextDouble() * 10;

math.Round(num_v, 2) //arrotondare alla seconda cifra dopo la virsola arrivati 0.995 inzia ad arrotondare a dieci 

Console.readKey;

/*
usiamo la classe math
math.Sqrt(); Radice Quadrata
math.Pow(); Potenza
math.Ceiling(); Arrotondare all intero superiore
math.Floor(); Arrotonda all interno precedente
math.Round(); Arrotondare da 5 in su arrotonda alla cifra superiore
Ceiling(n) 9.85 -> 10
Floor(n) 9.85 -> 9
*/

 ```

Volessimo generare numeri compresi tra 15 e 20

```C#
double num_v;

num_v=rnd.NextDouble(); //Genera numeri tra 0 - 1(escluso) quindi da 0 - 0.9999999999...

//Generare numeri compreso tra 15.00 e 20.00
num_v = rnd.NextDouble() * 5; // 5 cifre quindi 0*5=0+15=15 invece 0.999*5=4.999=5+15=20
num_v =math.Round(num_v, 2) +15;

Console.readKey;
```

Volessimo generare numeri compresi tra -5 e 10

```C#
double num_v;

num_v=rnd.NextDouble(); //Genera numeri tra 0 - 1(escluso) quindi da 0 - 0.9999999999...

//Generare numeri compreso tra -5.00 e 10.00
num_v = rnd.NextDouble() * 15; // 15 cifre quindi 0*15=0+-5=-5 invece 0.999*15=14.999=15-5=10
num_v =math.Round(num_v, 2) -5;

Console.readKey;
```


## Riferimenti
1. 