# Paginazione e segmentazione

Sono due tecniche di gestione della memoria, spesso presentate come parte della memoria virtuale.

## Paginazione

- Lo spazio degli indirizzi virtuali è diviso in blocchi di dimensione fissa chiamati **pagine**.
- La memoria fisica è divisa in blocchi della stessa dimensione chiamati **frame**.
- Una tabella delle pagine associa una pagina virtuale al frame fisico che la ospita.
- L'indirizzo virtuale è interpretato come numero di pagina e offset all'interno della pagina.
- Una pagina non presente in RAM può causare un page fault e richiedere interventi del sistema operativo.

La paginazione riduce la necessità di allocare memoria fisica contigua per un intero processo, ma richiede strutture di traduzione e può causare spreco interno nell'ultima pagina.

## Segmentazione

- Lo spazio è suddiviso in segmenti logici di dimensione variabile, ad esempio codice, dati e stack.
- Un indirizzo logico può essere espresso come coppia segmento/offset.
- Tabelle e controlli verificano esistenza, limite e permessi del segmento.

La segmentazione rispecchia unità logiche del programma ma l'allocazione a dimensione variabile può provocare frammentazione esterna.

## Confronto

| Aspetto | Paginazione | Segmentazione |
|---|---|---|
| Dimensione dei blocchi | Fissa | Variabile |
| Divisione | Blocchi tecnici | Parti logiche del programma |
| Frammentazione tipica | Interna | Esterna |
| Traduzione | Pagina → frame + offset | Segmento + offset e controlli di limite |

I sistemi moderni possono combinare idee diverse; la spiegazione dettagliata dipende dall'architettura trattata a lezione.
