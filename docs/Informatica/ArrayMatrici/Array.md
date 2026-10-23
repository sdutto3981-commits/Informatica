---
date: 2025-10-08
time: 12:21
---
# Array

L'array ha una dimensione predefinita o data da me oppure chiesta in input.
#### Scorrimento
Posso cercare un valore se sappiamo la posizione lo troviamo come nome del vettore più posizione oppure altrimenti scorriamo  l'intero vettore.
#### Modifica
Volendo modificare un valore in una posizione se già occupata il valore viene sostituito.
#### Caricamento vettore
Posso chiedere in input la lunghezza del vettore e poi usando un ciclo for richiedere ogni valori nella posizione da `i=0`  a `i<n` e aggiungere un valore in posizione i rispetto l vettore `v [i]` 

La dichiarazione di questi vettori avviene all'interno della RAM dove viene allocata della memoria rispetto a un indirizzo quindi quella parte della memoria viene riservata quindi quando usiamo `new` ci porta a questo indirizzo per salvare i dati del vettore  

Volessimo copiare il vet1 sul vet2 dobbiamo usare un ciclo for per fare scorrere il primo e copiare quei valori dall'indice del vettore uno altro:
```C#
for(i=0;i<vet1.Lenght;i++){
	vet1[i] = vet2[i]
}
```


#### Codifica

```C#
//Dichiarazione con lunghezza
int[] vet = new int[10];

//Dichiarazione senza lungezza

int[] vet;
int dim;

Console.WriteLine("Dimmi la dimesione de vettore-> ");
dim = Convet.ToInt32(Console.ReadLine());
vet = new int[dim];

//Caricamento del vettore
for(i=0; i<dim; i++){
	Console.Write("Dimmi l'elemento di indice {0} del vettore", i);
	vet[i] = Convert.ToInt32(Console.ReadLine());
}

//Visualizzazione del vettore
for(i=0;i<vet.Lenght;i++){
	Console.WriteLine("v[{0}]->{1}",i,v[i]);
}

Console.ReadKey();
```


## Riferimenti
1. [[WikiPediaArray]]
2. [[Array nella RAM]]
