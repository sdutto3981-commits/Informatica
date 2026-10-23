---
date: 2025-10-17
time: 08:12
---
# Comandi Linux

Con il comando **man** ci è possibile visualizzare tutte le informazioni riguardanti un certo comando per esempio tutti i metodi e cosa fanno come funziona e cosi via.

Con il comando **clear** è possibile eliminare tutto il contenuto del terminale scritto sino ad ora.

Con il comando **date** è possibile visualizzare data e ora locale del sistema  

1. Gestione file e directory
### **pwd**
Il comando `pwd` ci permette di vedere il percorso della cartella corrente in cui siamo 
### **ls**
Il comando `ls` ci permette di vedere tutto ciò che contiene la cartella corrente sia cartelle che file inclusi
`ls -l` ci permette di vedere l'elenco di file compreso di permessi per i vari utenti 

### **cd**
Il comando `cd` ci permette di spostarci tra le varie cartelle possiamo spostarci sia avanti nella cartella successiva semplicemente:
```linux
cd test_dir/
```

oppure nella cartella precedente con:
```
cd ..
```
ogni puntino corrisponde a una cartella precedente se dovessimo tornare indietro di due cartelle `../..` per tornare due cartelle indietro

### **mkdir**
Questo comando permette di creare una cartella nel seguente modo:
```
mkdir new_dir
```
Quindi come comando + nome cartella 

### **touch**
Permette di creare un file vuoto nel seguente modo:
```
touch file1.txt
```
crea un file1 completamente vuoto
### **cp**
Copia un file dalla cartella corrente ad un percorso inserito
```shell
cp file.txt ../file
```
In questo modo possiamo copiare il primo file nella cartella file che si trova nella cartella corrente `../` 
### **mv**
Il comando ci permette di rinominare e spostare dei file tra una cartella e l'altra per esempio posso cambiare il nome del file  nel seguente modo:
```
mv file1.txt file_r_1.txt
```
Quindi modifica il nome del file1 in file_r_1

### **rm**
Rimuovere un file dalla cartella corrente nel seguente modo:
```
rm file1.txt
```
posso anche rimuovere più file di fila aggiungendo i nomi uno dopo l'altro:
```
rm file1.txt file2.txt file3.txt ...
```

Posso anche rimuovere il cartelle vuote nel seguente modo:
```
rm -d dir1
```
solo se vuota.

Posso rimuovere le cartelle piene nel seguente modo:
```
rm -r dir2
```
se è piena eliminerà anche i. contenuto di essa

### **rmdir**
Usiamo questo comando per eliminare delle cartelle vuote:
```
rmdir dir1
```
con questo comando non posso rimuovere le cartelle piene siccome non è progettato per questo 
### **cat** 
Visualizzare il contenuto di un file

### **less**
Visualzizzare il contenuto di un file scorrendolo dall'interno

### **more**
Abbinato al cat/less pemette di visualizzare a pagine il contenuto del file 

### **tail**
Visualizzare il contenuto del file dal fondo

2. Funzioni di ricerca

### **find**
Ricerca di un file all'interno di una cartella
2. Gestione di file compressi
3. Gestione Informazioni S.O.
4. Gestione amministrazione utenti
5. Eseguire comandi

## Riferimenti

1. 