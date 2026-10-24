# Sistemi sequenziali

Un circuito sequenziale contiene memoria: l'uscita dipende dagli ingressi e dallo stato memorizzato. Nei circuiti sincroni il clock coordina gli istanti di aggiornamento.

## Percorso

- [Circuito sequenziale](Circuito%20sequenziale.md)
- [Latch SR con NAND](Latch%20sr%20NAND.md)
- [Latch SR con NOR](Latch%20sr%20NOR.md)
- [Latch D](Latch%20D.md)
- [Flip-flop SR](Flip%20Flop%20sr.md)
- [Flip-flop D](Flip%20Flop%20D.md)
- [Flip-flop JK](Flip%20Flop%20jk.md)
- [Flip-flop T](Flip%20Flop%20T.md)

## Confronto rapido

| Dispositivo | Comportamento da ricordare |
|---|---|
| Latch SR | Set e Reset; attenzione alla combinazione proibita secondo la realizzazione e la polarità |
| Flip-flop D | al fronte attivo copia D in Q |
| Flip-flop T | con T=1 commuta; con T=0 mantiene lo stato al fronte attivo |
| Flip-flop JK | J=K=1 commuta; 10 setta; 01 resetta; 00 mantiene (al fronte attivo) |

Per ogni dispositivo studia tabella caratteristica, simbolo, temporizzazione, ingressi asincroni eventualmente presenti e condizioni non ammesse. Le convenzioni esatte del simbolo dipendono dal componente trattato.

Dopo i flip-flop, affronta la progettazione di registri e contatori e la rappresentazione tramite automi.
