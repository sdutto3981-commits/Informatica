---
date: 2025-10-24
time: 08:11
---

# Permessi in Linux

Per vedere i permessi dei file possiamo usare `ls -l`

Categoria di utenti:
- u =user
- g = group
- o = others

Come categoria di permessi possiamo avere:
- r = read
- w = write
- x = execute

Se si presenta con la prima lettera `d` è una cartella se il primo carattere è `-` è un file

`-rwxr--r--`
`-  rwx  r--  r--`

-: file
rwx: utente può leggere scrivere ed eseguire
r--: gruppo può leggere
r--: altri possono leggere

Per modificare usiamo `chmod`

`chmod+utente+categoria di permesso+file`

per esempio aggiungere all'utente il permesso per scrivere al file file.txt

`chmod u+w file.txt`

per togliere al utente il permesso di scrittura

`chmod u-w file.txt`

per aggiungere al gruppo il permesso di scrittura

`chmod g+w file.txt`

## Riferimenti

1.
