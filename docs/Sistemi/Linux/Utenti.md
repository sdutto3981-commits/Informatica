---
date: 2025-11-14
time: 08:24
---
# Utenti

Per visualizzare le informazioni riguardanti l'utente usiamo il comando `id` che così senza parametri ci da informazioni sull'utente attuale possiamo anche specificare un singolo utente

### Creazione utenti

`adduser`:aggiunge un nuovo utente questo è un comando di alto livello 
Lancia la creazione di cartelle dell'utente e dei suoi permessi insieme alle sue periferiche di input ecc...
`sudo adduser nomeutente`

`useradd`:aggiunge un utente ma questo è un comando di basso livello.
Aggiunge solo l'utente e non ne configura nient'altro quindi non crea cartelle ossia la home directory

Possiamo andare alla ricerca degli utenti in /etc/passwd
`pippo :x:2001:2001:Pippo Utente:/home/pippo:/usr/bin`

pippo >nome utente
x >password
2001> UID
2001 >GID gruppo principale
Pippo utente >full name nome completo 
`/home/pippo` >directory home dell'utente
`/usr/bin` >percorso della shell per l'utente

sintassi per passwd:
username: `password:UID:GID:FullName:Home:Shell`

modificare passwd modifica anche il file shadow
usermod > mi permette di modificare gli attributi di un utente gia esistente: login, UID, GID, hoem,shell, gruppi stTO

es.
`usermod -d /homr/dir2` Cambio cartella home
`usermod -a -G 3D inf gallo` Aggiunto a un gruppo 3D inf l'utente gallo 
Per vedere invece i gruppi in `/etc/group`

`sudo groupadd nomegruppo `
## Riferimenti
1. 