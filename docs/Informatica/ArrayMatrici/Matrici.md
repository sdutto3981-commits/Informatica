---
date: 2025-10-08
time: 12:21
---

# Matrici

Possono esistere degli array multidimensionali essi possono essere identificati con delle coordinate che sono determinate dalla posizione rispetto alla riga e rispetto alla colonna

|     | 0   | 1   | 2   | 3   | 4    |
| --- | --- | --- | --- | --- | ---- |
| 0   |     |     |     |     |      |
| 1   |     |     |     |     |      |
| 2   |     |     |     |     |      |
| 3   |     |     |     |     | ciao |

`m[3,4] = ciao`

Per andare a caricare una matrice andiamo ad utilizzare due cicli for che ciclano per  i e j andiamo a caricarla

```python
for i in range(righe):
	for j in range(colonne):
		m[i,j] = input("Inserire il valore:")
```
