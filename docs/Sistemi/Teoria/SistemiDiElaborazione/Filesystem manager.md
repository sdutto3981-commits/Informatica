---
date: 2026-05-13
time: 10:08
---
# Filesystem manager

## Indice

1. [[#Attributi dei file]]
2. 
---

## Attributi dei file

Un file o un documento contentetne deid ati che possono essere letti psctitti da un utente oltre al suo contenuto ogni file ha dei prorprio attributi :
- Un nome
- Un tiopo
- L'indirizzo al primo blocco fisico LBA 
- Dimensione corrente
- Data dell'ultimo accesso e dell0ultima modifica
- Id ell utente proprietazio 
- Diritti di accesso

é un modulo del SO che organizza e gestisce i file presenti nella memoria di massa le principali funzioni che offre sono:
- Organizzare i dati in una struttura ad albero permettendo il trasferimento dei file piu veloce
- Ottimizzare il trasferimento dei dati 
- Minimizzare il tempo di risposta delle perifieriche durante la lettura e scrittura di un fil e
- Rendere trasparenti alel appluicazione lecarateridstcihe fisiche della memoria secondaria 
- Adottare politiche di sicurezza  in caso di perdite accidentatli dei dati o accessi non autorizzati
- Gestire in maniera automatica copie di backup
- Fornire un insieme standard di routine I/O
- Rendere disponibili le aree utilizzate da informazioni che sono state cancellate regolare l'accesso contemporaneo di più applicazioni allo steso insieme di file in caso si sistemi multiprogrammazione

Principali operazioni del FSM:
Le principali operazioni che può effetturare un FSM sono:
- Inizializzazione del FS
- Mount/unmount FS
- Creazione di una directory
- Creazione apertura scrittura lettura cancellazione e spostamento di un file

### Inizializzazione di un FS

Rappresenta la orima operazione che dovra effettuare il File system su un volyume vuoto consiste nella preparazione di una strittra printa a contenere file e directory

Il SO calcola il numero di liberi del volume e in vbase a questo vlaore memorizza in una area della memoria di massa anche: 
- Il nome del volume 
- La sua dimensione
- Se è integro o danneggiato il riferimento ai blocchi liberi
Viene creato inoltre la root directory memorizza il riferimento alla su aposizione fisica in. memoria in questa fase la root directory è vuota 

L'operazione di mount ga lo sopo di rendere ilfil esystem disponibile all'accesso da apete di utenti e applicazione è importante ch eili lfile syytem ch viene montato sia integro la verific a di integrita e molto importante a causadei continui acessi sui dati l'utilizzo di un file system corrotto in alcune sue parti può causare il danneggiamento di altri dati o determinare il crash del sistema.

Il modulo suystem check prigram ga il compito di svolgere il test di integrita Edeguire uncheck completo sui dati del disco richiede pero moto tempo ed è per questo motivo che il test viene svokti sikla quando le informazioni memorizzate su disco indicano che la struttura presenta errori 


Il file ststem è integro le strutture memorizzare su disco permettono l'accesso ai dati del volume sono caricate in memoria centrale rendendo il colume montato accessibil ea gli utenti e alle aoolicazioni 

In alcuni sistemi operativi conme Dos e Windows il mound di un volume avviene in modo automatico mentre nei sistem come Linue esistono dei comandi appositi

Speculare alll'operzione di mount l'operazione di unmount che può essere eseguita in modo autmatico allo shutdown del sistema operativo oppure manualmente con il comando unmount sintassi sistemi linux.

Una operazione di unmount non render piu dusponibili i dile del volumesmontato e il file system manager memoriazza nella memoria di massa le informazioni relatile al file system

Quando ariaa la richiest a di creazione di un file il file stsem manfare crea una descrittore ciopè una struttra deati agganciata alla directory che deve conteenre il fileche memoerizzza lcune informaizone che si irifreiscono al fil etra le quali:
- la data di creazione 
- l'indicazione che il file è vuoto che la sua dimensione  è uguale a ' l'idnetita dell owner  che ha creato il file i diritti di accesso al dile da aparte degli utent del So
Quando un file viene creato sono meomorizzate soltantot l einfomrazione bche permttono la sua festuione lo spazio difisco sdu disco che contiene i da ti del fi leallocato solao èè richiesta la scitttura di un vlocco di dati 

Un file puo essere creato da un programma che. ddeve meoomirare sum ,emoria di masss a il risultato delle elaborazionoi
da un utente da unprorgaramma he deve moemroiazzare us memosri a si mass ail risulato delle sue elaborazioni da un uteetnee che utilizza uyn qualsisasi applicativo 
da l sistema iierattovo e dalle sue operzioeni di log


SCrittura di un file quindi viene eseguita legendo l'area di memoria che contiene i dati che contene i fi. e èer fare questa operzione viene ewseguita l'operazione 

Nel file troviamo la sua fine k'eof end o file ceh serve per inserire le informazioni 
al termine della scrittura tutte le informazioinedevono esserea aggiornate

MEntre la cancelladi  di un file esso viene marcato e viene canceellato i l descrittore n3lla seconda fase i. file system manageer verifica la posizone del dile se puo essere cacncellata essa puo essere canceòòata s e mpm spmp èremsemto aòtro handel esso possono essere cancellatti e liverrare tutti i blocchi cancellati per unan uov amaemorizzazione tutte le operazioni sono eseguite sinoa lal chiusurra del file 

inizializzare la tipologia di elemento nel record un esempio di record con infomrazioni e file questo tipo di filesystem altre informazioni gestire nel NTFS erano gestite da una compressione dei file  e poi il loro utilizzo questa attivita e poi alla base di tutti quei processi in modo da poter navigare e lincare i vari elemnti in modo piu performante 
essi si basano su un concetto di base di lunghezza fisas chiamati cilinder groups alcuni blocchi sono utilizzati per le informazioni relative all'organizzazione quindi una struttura permette di avere i dati suddivi in blocchi quindi ogni blocco dev'essere diviso in entita autonome e poi gestire le tipologi e in modo molto piu rapido ed intelligente 

Esistono quindi dei blocchi ed ognuno è indipendente e ogni blocco a delle informazioni specifiiche nel file systema bbimao un ambiente dove possiamo andare a creare noi il files system ontandolo direttamente

Tutta l'organizazione delle strutture e directory mi vanno ad indicare tutte le infomazioni questa suddivisione una struttura di un inode e i diritti e il numero di data-block che compongono il file e possiamo gestire i file i tipi dinamico la versione d ext3 si basa sulla versione ext2 ma viene introdotta la tecnica del journaling questo è un elemento molto importante ma pemette di mantenere traccia delle modifiche 
## Riferimenti
1. 