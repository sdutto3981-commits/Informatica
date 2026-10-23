---
date: 2025-11-11
time: 11:26
---
# Flip Flop

Simile al latch sempre un circuito sequenziale in cui stati dipendono dagli stati precedenti nei latch sr nand e nor sono molto sensibili appena si modifica leggermente un entrata e molto delicata noi vorremo che l'acquisizione dei dati e rischiamo di avere delle lettura sbagliate.

Come funziona il flip flop ha la condizione di base di memoria prendendo per esempio con il clock utilizziamo questa peculiarità del clock ovvero il fronte di salita e il fronte di discesa ovvero il tempo che il clock impiega per passare da corrente pari a 0 al massimo e sarà in questo tempo che il flip flop mentre quando il fronte non è attivo rimane in stato di memoria.

Quindi per tabella quando non siamo sui fronti esso rimane in memoria ovvero Q(i-1) mentre per il fronte su cui è attivo in questo caso di salita l'altro sarà sempre in stato di memoria:

| S   | R   | CK                     | Q(i)   |         |
| --- | --- | ---------------------- | ------ | ------- |
| 0   | 0   | $\rightarrow \uparrow$ | Q(i-1) | Memoria |
| 0   | 1   | $\rightarrow \uparrow$ | 0      | Reset   |
| 1   | 0   | $\rightarrow \uparrow$ | 1      | Set     |
| 1   | 1   | $\rightarrow \uparrow$ | N.A    |         |




## Riferimenti
1. 