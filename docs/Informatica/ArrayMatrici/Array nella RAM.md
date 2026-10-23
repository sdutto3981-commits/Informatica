---
date: 2025-10-29
time: 12:20
---
# Array nella RAM


### Come viene dichiarato un array in RAM

Quando dichiari un array (o vettore) in un linguaggio come **C**, succedono diversi passaggi a livello di **memoria RAM**:

1. **Dichiarazione del vettore**
    
 ```c
    int v[5];
    ```
    
    Quando scrivi questa istruzione, **il compilatore riserva uno spazio contiguo in memoria RAM** abbastanza grande da contenere 5 elementi di tipo `int`.
    
2. **Allocazione della memoria**
    
    - Ogni elemento occupa una certa quantità di byte (per esempio, `int` = 4 byte).
        
    - Quindi `v[5]` occuperà 5 × 4 = 20 byte di memoria **contigua**.
        
    - L’indirizzo del **primo elemento** (`v[0]`) rappresenta anche **l’indirizzo dell’intero vettore**.
        
3. **Puntatore implicito**
    
    - Il nome dell’array (`v`) **si comporta come un puntatore costante** al primo elemento.
        
    - In pratica, `v` equivale a `&v[0]` (indirizzo del primo elemento).
        
4. **Valori iniziali**
    
    - Se l’array è **locale** (dichiarato dentro una funzione) → **non è inizializzato** automaticamente → contiene valori casuali (spazzatura).
        
    - Se è **globale o statico**, allora viene **riempito con zeri** automaticamente.
        
5. **Accesso agli elementi**
    
    - Quando scrivi `v[i]`, il compilatore calcola l’indirizzo:  
        [  
        \text{indirizzo}(v[i]) = \text{indirizzo base} + i \times \text{dimensione tipo}  
        ]
        
    - Poi accede a quella posizione di memoria.
        

---

### Se la dimensione non è specificata

- Se scrivi:
    
    ```c
    int v[];
    ```
    
    questo **non è valido** senza un’inizializzazione o un’allocazione dinamica, perché il compilatore **non sa quanto spazio riservare**.
    
- Puoi però scrivere:
    
    ```c
    int v[] = {1, 2, 3};
    ```
    
    In questo caso la dimensione viene dedotta automaticamente (`v[3]`).
    

Oppure, con **allocazione dinamica**:

```c
int *v;
v = malloc(5 * sizeof(int));
```

In questo caso `v` è **un puntatore** e la memoria viene riservata **durante l’esecuzione (runtime)**.

## Riferimenti
1. 