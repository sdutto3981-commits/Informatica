---
date: 2026-10-25
---
# Flip-flop SR

Il **flip-flop SR** è un circuito sequenziale con due ingressi di controllo, `S` (*Set*) e `R` (*Reset*), e un'uscita memorizzata `Q`. La tabella seguente descrive un modello attivo alto, attivato sul fronte di salita del clock. Varianti con ingressi attivi bassi o ingressi asincroni richiedono una tabella coerente con il simbolo e il componente specifico.

## Tabella caratteristica

| S | R | Fronte attivo del clock | `Q(t+1)` | Significato |
|---:|---:|---|---|---|
| 0 | 0 | salita `↑` | `Q(t)` | Mantiene lo stato |
| 0 | 1 | salita `↑` | 0 | Reset |
| 1 | 0 | salita `↑` | 1 | Set |
| 1 | 1 | salita `↑` | Non ammesso | Combinazione proibita nel modello SR attivo alto |
| X | X | nessun fronte attivo | `Q(t)` | Mantiene lo stato memorizzato |

`X` significa che il valore non è rilevante in quella riga. Il flip-flop campiona ingressi sincroni al fronte attivo; tra due fronti l'uscita mantiene lo stato, salvo la presenza di ingressi asincroni come preset o clear.

## Significato di Set, Reset e memoria

- **Set (`S=1`, `R=0`):** porta `Q` a 1 al fronte attivo.
- **Reset (`S=0`, `R=1`):** porta `Q` a 0 al fronte attivo.
- **Memoria (`S=0`, `R=0`):** conserva il valore precedente.
- **Combinazione non ammessa (`S=1`, `R=1`):** nel modello SR attivo alto, non è una condizione valida per un normale stato Set/Reset; non va assegnata arbitrariamente a 0 o 1.

L'uscita complementare viene spesso indicata `Q̅` e, negli stati validi, è il complemento di `Q`. Nella condizione proibita non si deve assumere che l'uscita complementare continui a rispettare il comportamento normale.

## Flip-flop e latch non sono la stessa cosa

Un **latch** è sensibile a un livello di abilitazione: quando è abilitato può seguire l'ingresso. Un **flip-flop** edge-triggered campiona gli ingressi al fronte specificato del clock. Nei disegni didattici i simboli e i tempi di commutazione devono essere interpretati secondo la documentazione del componente.

## Equazione caratteristica

Per gli ingressi ammessi del modello SR attivo alto, una forma utile è `Q(t+1) = S + ¬R·Q(t)`. Questa equazione non elimina la condizione non ammessa `S=R=1`: l'equazione e la tabella devono essere usate rispettando il dominio valido del circuito.

## Metodo di verifica

1. Individua polarità e fronte attivo dal simbolo.
2. Scrivi la riga della tabella per tutti i valori di `S` e `R`.
3. Controlla che `00` sia memoria, `01` reset e `10` set per questa convenzione.
4. Segna esplicitamente la condizione non ammessa.
5. Se il componente ha `PRE` o `CLR` asincroni, studiane la priorità e la polarità separatamente.
