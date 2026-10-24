# Aggiungere codice a una cartella GitHub

Una volta clonato il repository, la cartella locale corrisponde al contenuto versionato. Crea o modifica il file nella directory giusta, poi usa Git per registrarlo.

```bash
git status --short
git diff -- nomefile
# Dopo aver verificato il contenuto
git add percorso/nomefile
git diff --cached
git commit -m "feat: aggiunge una funzionalità"
git push
```

Se il file non compare nel diff, controlla che si trovi dentro il repository e che non sia escluso da `.gitignore`. Non usare `git add .` alla cieca: prima verifica che non vengano inclusi file generati, segreti o dati personali.
