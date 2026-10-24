# Caricare file e cartelle su GitHub

Il modo più affidabile per caricare una cartella di progetto è usare Git dal terminale, dopo aver clonato il repository.

```bash
git clone https://github.com/utente/repository.git
cd repository
git status
# Copia o modifica qui i file necessari
git add percorso/file-o-cartella
git commit -m "docs: aggiunge gli appunti"
git push
```

`git add` prepara le modifiche per il prossimo commit; `git commit` crea una registrazione locale; `git push` invia i commit al remoto. Non aggiungere token, password, file `.env` o chiavi private.

L'interfaccia web di GitHub consente di caricare file dal browser, ma per cartelle grandi o aggiornamenti ripetuti è preferibile Git. Verifica `git status` e l'anteprima del diff prima del commit.
