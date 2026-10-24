# Strumenti di sviluppo e debugger

## Ciclo di vita del software

Un progetto attraversa normalmente analisi del problema, progettazione, implementazione, test, rilascio e manutenzione. In un esercizio scolastico conviene separare il problema dai dettagli del codice e conservare piccoli test ripetibili.

## Compilatore ed errori

- **Errore di compilazione:** il programma non viene tradotto, per esempio per una parentesi mancante o un tipo incompatibile.
- **Errore a runtime:** il programma parte ma si interrompe o genera un'eccezione durante l'esecuzione.
- **Errore logico:** il programma termina ma il risultato è sbagliato.

## Debugging

1. Riproduci l'errore con un input preciso.
2. Inserisci un breakpoint sulla riga sospetta.
3. Avvia il programma in modalità Debug.
4. Usa passo-passo (*Step Over*, *Step Into*) per seguire l'esecuzione.
5. Controlla variabili locali, espressioni osservate (*Watch*) e stack delle chiamate.
6. Correggi la causa e ripeti gli stessi test.

## Test minimi

Per una funzione di somma controlla numeri positivi, negativi e zero. Per un array verifica array vuoto, un elemento e casi con valori ripetuti. Per l'input, prova dati mancanti o non validi.

Il debugger è uno strumento di osservazione: non sostituisce la comprensione dell'algoritmo.
