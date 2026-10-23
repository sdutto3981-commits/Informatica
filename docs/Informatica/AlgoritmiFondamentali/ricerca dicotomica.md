---
date: 2025-12-03
time: 12:45
---
# ricerca dicotomica

Funziona solo nel caso ordinato 

```
Start
Sup = 0
inf = N-1
meta = (sup+inf)\2
Se v[meta] != X
	(vero)
		Se v[meta] > x
			(vero)
				inf = meta-1
			(falso)
				inf = meta+1
	(falso)
	
Se v[meta] == x
	(vero)
		output: oltre la meta
	(falso)
		output: non trovato
Fine
```
## Riferimenti
1. 