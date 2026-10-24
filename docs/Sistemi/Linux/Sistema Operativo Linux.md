---
date: 2025-10-03
time: 08:21
---
 # Sistema Operativo Linux

Il **Sistema Operativo** è il software che gestisce hardware e software di tutta la macchina.

**KERNEL** è il cuore del sistema operativo sistema operativo gestisce i driver dei dispositivi ed e il gestore della maggior parte dei processi che avvengono all'interno del computer
**FILESYSTEM** è la struttura dati con cui sono organizzati i dati all' interno del dispositivo di archiviazione  esso ci fornisce una struttura gerarchica per i nostri file e cartelle
UNIX/LINUX: struttura inode
INODE: struttura dati identificata da un numero univoco all'interno del filesystem, conserva e descrive dati di file e cartelle

GERARCHIA FILESYSTEM:
/root
	**/etc** contiene i file di configurazione di alcuni servizzi
	/bin comandi binari essenziali
	**/lib** librerie per il funzionamento dei programmi
	/home la cartella dell'utente
	**/boot** file di configurazione per il giusto avvio del sistema come il kernel e i file di configurazione del bootloader
	/tmp file temporanei
	/dev file relativi alle periferiche
	/sys file propri del sistema operativo
	/usr secondi livello di gerarchia per l'utilizzo multi utente

GUI: interfaccia grafica utente
SHELL: interprete dei comandi
TERMINALE: è un particolare tipo di attrezzatura hw o sw atta alla ricezione o invio di I/0

user@hostname:$
user: utente con sui si è collegati
hostname: il nome della macchina
cartella//posizione: dove ci troviamo
$: tipo di utenza. $ = utente normale, #=utente amministrazione

pwd  mostra cartella corrente

## Riferimenti

1.
