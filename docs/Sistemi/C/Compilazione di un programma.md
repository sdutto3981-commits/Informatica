# Compilare un programma

Vengono suddivise in vari fasi per prima cosa:
1. Viene creato un file Assembler linguaggio più prossimo alla macchina vengono generati in fase di compilazione rispetto a ciò che viene  scritto inoltre 

2. avviene la creazione di uno o più fil oggetto forniti dall'assemblatore infine viene creato un file unico che ha dei link automatici per i vari file di compilazione

3. Poi la creazione di un fil eseguibile .exe

Esse poi vengono caricate in memoria per poi essere eseguite dall'processo di avviamo che 

Utente-> Codice sorgente -> Compilatore -> Codice oggetto -> Linker -> Codice eseguibile -> Loader -> Codice macchina -> CPU

[]()## COMPILATORE

E un programma in grado di tradurre quello che è un contenuto testuale in un linguaggio assembler ovvero al più basso livello successivamente...

## ASSEMBLATORE

L'assemblatore simile al compilatore permette di tradurre undile assemble cib estensione .s del file con codice binario corrispondente .o compilatori modermi fanno avvenitre questa fase nello stesso momento

## LINKER

Molto spesso una applicazione è costruita da più file sorgenti ognuno dei quali contienne specifiche procedure uno di questi file puo contenere una funzione necessario esso crea delle note nel file .o e ne connette  i componenti in modo che l'esguibile en cfaccia riferimento

## LOADER

Il loader ci permette di far si di richiamarlo automaticamente quando viene eseguito da riga di comando l'esecuzione del programma in modo da dare inizio alla fase di fatch e cosi via 

## Esempio

Quando noi vogliamo compilare un file per esempio un file c in ambiente linux usiamo 
- `gcc nome_file.c -a nome_eseguibile`
Per visualizzare il file assembler
- `gcc -S nome_file.c`
Per eseguire il file:
- `nome_eseguibile`
