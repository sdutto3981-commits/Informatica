# Pull request su GitHub

Una pull request (PR) propone di integrare le modifiche di un ramo in un altro, spesso `main`. Non è un commit: è uno strumento per discutere, confrontare e revisionare il cambiamento prima del merge.

## Flusso tipico

```bash
git switch -c docs/aggiorna-appunti
# modifica i file
git add docs/
git commit -m "docs: aggiorna gli appunti"
git push -u origin docs/aggiorna-appunti
```

Su GitHub apri una pull request dal ramo appena pubblicato verso il ramo di destinazione. Descrivi scopo, file principali e verifiche eseguite. Controlla il diff, rispondi ai commenti e risolvi eventuali conflitti prima del merge.

Mantieni una PR focalizzata su un cambiamento coerente. Non includere credenziali, cache o file generati senza motivo.
