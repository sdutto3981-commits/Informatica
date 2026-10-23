---
date: 2025-09-12
time: 20:38
---
# Comandi base GitHub

Il comando `git congif` ti permette di configurare parametri all'interno della libreria per esempio:
- `git config --global user.name "..."`
- `git config --global user.email "..."`

Per vedere tutte le configurazioni fatte possiamo usare `git config --list`

Possiamo anche creare delle scorciatoie per altri comandi con il comando `git config --global alias.i init ` (init serve per inizializzare git in una nuova cartella) quindi ora la posto di usare `git init usiamo git i` 

Per inizializzare git in una nuova cartella usiamo il comando `git init` questo ci permette di attivare il programma ed iniziare il nostro controllo versione di quella cartella

Per controllare cosa succede all'interno della nostra cartella usiamo `git status` che ci permette di vedere se sono stati aggiunti nuovi file oppure ne siano stati modificati altri quando e seguiamo questo comando e il nome del file viene contrassegnato si rosso vuol dire che non  ancora stato aggiunto alla staging area 

Per aggiungere i file alla staging area possiamo usare il comando `git add .` che aggiunge tutti i file alla staging area oppure per aggiungere un file specifico allora usiamo `git add file_name` posso anche prendere singoli file con determinate estensioni con il comando `git add *.txt` 

Poi abbiamo un comando che permette di facilitare il tracciamento dei vari salvataggi del file in modo da chiamare la versione modifica non ancora nella staging area il nome presente tra le virgolette `git commit -m "nome_versione"`

Per clonare una cartella remota a cui ci viene dato un link usiamo il comando `git clone` seguito dall' url della cartella in modo che ora tu abbia accesso alla cartella remota in locale a cui puoi apportare modifiche

Ogni volta che apportiamo una modifica a una cartella è buona norma lavorare branch o ramo in modo da non interferire con altri  file e come creare una copia di un documento in modo da non rovinare l'originale per fare ciò usiamo `checkout -b nome_ramo`  e questo ci permette di crearlo e di spostarci direttamente ad esso

Per vedere i branch usiamo il comando `git branch`

Per spostarci da un branch ad un altro usiamo il comando `git switch branch_name` 

Ora proviamo a fare un esempio devo cambiare il nome di un sito web allora cosa faccio cambio il tutto dentro il codice poi uso il comando `git status` per vedere se è avvenuto il cambiamento allora poi eseguo il comando `git add .` per aggiornare il nostro salvataggio e poi usiamo il comando `git commint -m "nome_del_salvataggio"` per far si che rimanga il più ordinato possibile

Come facciamo a far si di aggiornare la cartella online che abbiamo appena modificato possiamo farlo con il comando `git push cartella_remota nome_branch` e usiamo `origin` si riferisce alla cartella remota e `nome_branch` si riferisce al branch da caricare online

Invece per ricevere eventuali aggiornamenti posso usare il comando `git pull ` in modo da aggiornare la nostra cartella sul pc

Per eliminare un branch localmente possiamo usare il comando `git branch -d nome_branch` per eliminarlo su GitHub possiamo usare `git push --delete origin nome_branch` 
## Riferimenti
1. 