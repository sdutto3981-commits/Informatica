# Kernel e interrupt

## Kernel

Il kernel è la parte centrale del sistema operativo che gestisce risorse hardware e fornisce servizi fondamentali ai programmi. Tra le sue responsabilità tipiche ci sono pianificazione dei processi, memoria, driver, file system e comunicazione tramite chiamate di sistema.

Una separazione tra modalità utente e modalità kernel limita l'accesso diretto delle applicazioni a operazioni privilegiate. I dettagli variano tra sistemi operativi.

## Interrupt

Un interrupt è una richiesta di attenzione che interrompe temporaneamente il normale flusso di esecuzione per gestire un evento. Può essere generato da hardware (per esempio un dispositivo) o da condizioni/istruzioni gestite dal processore.

Schema concettuale:

1. Il processore sta eseguendo un programma.
2. Si presenta una richiesta d'interrupt.
3. Il processore salva le informazioni necessarie per riprendere l'esecuzione.
4. Il controllo passa a una routine di servizio appropriata.
5. Terminata la gestione, l'esecuzione riprende quando è possibile.

Le eccezioni sincrone, gli interrupt hardware e le chiamate di sistema sono concetti collegati ma non sinonimi perfetti.

## Perché servono

Gli interrupt permettono di reagire agli eventi senza costringere la CPU a controllare continuamente ogni periferica. La gestione deve essere attenta ai tempi e alla concorrenza, perché alcune routine hanno vincoli molto stretti.
