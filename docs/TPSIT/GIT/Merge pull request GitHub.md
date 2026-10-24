# Merge di una pull request

Il *merge* integra nel ramo di destinazione i commit proposti dalla pull request. Prima di procedere, verifica che il diff sia quello atteso, le revisioni siano concluse e i controlli automatici siano verdi.

## Strategie comuni

- **Merge commit:** conserva i commit del ramo e crea un commit di merge.
- **Squash and merge:** combina i commit della PR in un unico commit sul ramo di destinazione.
- **Rebase and merge:** riapplica i commit su una nuova base, mantenendo una storia lineare.

La strategia dipende dalle regole del repository. Dopo il merge, aggiorna la copia locale:

```bash
git switch main
git pull --ff-only
git branch -d docs/aggiorna-appunti
```

Elimina un ramo soltanto dopo aver verificato che le modifiche siano state integrate e che il ramo non contenga lavoro esclusivo.
