# Debugging JavaScript nel browser

## Console ed errori

Apri gli strumenti per sviluppatori del browser e usa la scheda Console per vedere errori e output di `console.log()`.

## Breakpoint

1. Apri la scheda Sources/Debugger.
2. Individua il file JavaScript.
3. Fai clic sul numero di riga per inserire un breakpoint.
4. Ripeti l'azione che genera l'errore.
5. Controlla variabili, stack delle chiamate e flusso delle istruzioni.
6. Continua l'esecuzione passo-passo e rimuovi i breakpoint non più utili.

## Errori ricorrenti

- `ReferenceError`: viene usato un nome non definito nell'ambito corrente.
- `TypeError`: un'operazione non è valida per il valore effettivo.
- Errore di sintassi: il parser non riesce a interpretare il codice.
- `querySelector()` restituisce `null` perché l'elemento non esiste o lo script viene eseguito troppo presto.
- Un evento non si attiva perché il gestore non è stato registrato o il selettore non individua il controllo.

## Metodo

Riduci il problema a un caso minimo, individua la prima riga in cui il valore diventa scorretto, correggi la causa e ripeti gli stessi test. Rimuovi i log temporanei dopo la diagnosi quando non sono più utili.
