---
date: 2025-11-18
time: 10:06
---
# Algoritmi ricerca

## Caso 1

Non ordinato disgiunto quindi segue un ordine casuale e gli elementi si presentano una volta sola e sono disgiunti quindi 1 volta oppure mai.

```
Start
i=0
trovato = false
while i < n && !trovato
	(vero)->
		if v[i] == x
			(vero)->
				trovato = true
				pos = i
			(falso)->
				i ++ 
	(falso)->
		if trovato
			(vero)->
				O: elemento tovato in {pos}
			(falso)->
				O: elemento non trovato 
Quit
```

## Caso 2

Caso 2 non ordinato e no disgiunto non segue un ordine e l'elemento se esiste può presentarsi più volte e bisogna darle tutte

```
Start
trovato = false
k=0
for i=0 i<n i++
	if v[i] == x
		(vero)
			trovato = true //almeno un elemento c'è
			pos[k] = i
			k ++
		(falso)
if trovato 
	(vero)
		Vis(Pos, k) //Funzione per la visualizzazione di un vettore
	(Falso)
		O: Elemento non trovato 

Quit			 
```

Per la ricerca di 0 è possibile grazie a k che fa da contatore poi per la ricerca di elementi totalmente uguali al vettore di partenza inizializziamo il vettore pos con la sua stessa dimensione 

## Caso 3

Ordinato e disgiunto 

```
Start
i=0
Trovato = false
Sup = false
while i<n && !Trovato && !Sup
	(vero)
		if v[i] == x
			(vero) 
				Trovato = false
				Pos = i
			(falso)
				if v[i] > x
					(vero)
						Sup = true
					(falso)
						i ++
	(falso)
		if trovato 
			(vero)
				O: Elemento trovato in {Pos}
			(falso)
				O: Elemento non trovato 
Quit
```


## Caso 4 

ordinato non disgiunto

```
Start
k = 0
i=0
Trovato = false
Sup = false
while i<n && !Sup
	(vero)
		if v[i] == x
			(vero)
				Trovato =true
				Pos[k] = i
				k ++
			(falso)
				if v[i] > x
					(vero)
						Sup = true
					(falso)
				i++
	(falso)
		if trovato 
			(vero)
				Vis(Pos, k) //Funzione per la visualizzazione di un vettore
			(Falso)
				O: Elemento non trovato
```


## Riferimenti
1. 