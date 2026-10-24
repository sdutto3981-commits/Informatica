---
date: 2025-11-18
time: 11:43
---

# Diagramma

Reti combinatorie riceve in ingresso l'ingresso I e lo stato attuale x1 e x0 e ci da in output x0'  e x1' e y=x1x0 le funzioni di stato fuyure vanno in ingresso che salvano lo stato attuale dche le posrtonao allarete comninatoria in vase alle o stato huturo di x0 e x1 e gli stati futuri si sostituiscono agli attuali con il colpo di clock se no sta fermo li e quelli attuali rientrano in input e vengono ricalcolati i futuri.

Il clock entra nel flip flop mentre i è smepre la funzione di stato futuro x0' mentre la rete combinatoria è

```
	x1 x0  x1 x0 I | x1 x0
A-> 0  0   0  0  0   0  0
B-> 0  1   0  0  1   0  1
C-> 1  0   0  1  0   1  0
D-> 1  1   0  1  1   0  1
		   1  0  0   0  0
		   1  0  1   1  1
		   1  1  0   1  0
		   1  1  1   0  1
```

Per calcolare usiamo le mappe K una per ogni variabile di stato futura

$x1' = x0I+x1\not x0I$

| I\x1x0 | 00  | 01  | 11  | 10  |
| ------ | --- | --- | --- | --- |
| 0      |     | 1   | 1   |     |
| 1      |     |     |     | 1   |

x0'=I

| I\x1x0 | 00  | 01  | 11  | 10  |
| ------ | --- | --- | --- | --- |
| 0      |     |     |     |     |
| 1      | 1   | 1   | 1   | 1   |

y=x1x0
