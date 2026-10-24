# Architettura pipeline

La **pipeline** suddivide l'esecuzione delle istruzioni in fasi che possono lavorare contemporaneamente su istruzioni differenti. Non rende necessariamente più veloce la singola istruzione; aumenta soprattutto il numero di istruzioni completate nell'unità di tempo (*throughput*), quando la pipeline è piena e non è bloccata.

## Esempio a cinque fasi

| Sigla | Fase | Funzione tipica |
|---|---|---|
| IF | Instruction Fetch | Preleva l'istruzione. |
| ID | Instruction Decode | Decodifica e individua gli operandi. |
| EX | Execute | Esegue l'operazione o calcola un indirizzo. |
| MEM | Memory Access | Accede alla memoria dati, se richiesto. |
| WB | Write Back | Scrive il risultato nel registro destinazione. |

Le fasi reali variano in base all'architettura; lo schema a cinque stadi è un modello didattico.

## Sovrapposizione

In una pipeline ideale ogni stadio impiega un ciclo e, dopo il riempimento, può completarsi circa un'istruzione per ciclo. La latenza di una singola istruzione resta approssimativamente pari alla somma delle fasi.

## Rischi (*hazards*)

- **Strutturali:** due istruzioni richiedono contemporaneamente una risorsa non duplicata.
- **Dati:** un'istruzione dipende da un risultato non ancora disponibile (RAW è il caso classico).
- **Controllo:** un salto rende incerto quale istruzione eseguire dopo.

Forwarding, stalli, duplicazione di risorse e predizione dei salti sono tecniche che aiutano a limitare i rischi. Un *flush* rimuove istruzioni già entrate nella pipeline ma diventate non valide a causa di una previsione errata.

## Esempio temporale semplificato

```text
Ciclo       1   2   3   4   5   6   7
Istruzione1 IF  ID  EX  MEM WB
Istruzione2     IF  ID  EX  MEM WB
Istruzione3         IF  ID  EX  MEM WB
```

Lo schema mostra la sovrapposizione ideale, senza stalli. La pipeline è una tecnica di microarchitettura; non va confusa con l'esecuzione parallela di più programmi indipendenti.
