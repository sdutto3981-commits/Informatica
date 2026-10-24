# Comandi Linux

La shell permette di interagire con il sistema operativo tramite comandi. Per sapere come funziona un comando puoi consultare `man nome_comando` oppure, quando disponibile, `nome_comando --help`.

## Navigazione

| Comando | Funzione | Esempio |
|---|---|---|
| `pwd` | mostra la directory corrente | `pwd` |
| `ls` | elenca file e directory | `ls -la` |
| `cd` | cambia directory | `cd Documenti` |
| `cd ..` | sale di un livello | `cd ..` |
| `clear` | pulisce la schermata del terminale | `clear` |
| `date` | mostra data e ora del sistema | `date` |

Un percorso che parte da `/` è assoluto. Un percorso relativo viene interpretato rispetto alla directory corrente. `.` indica la directory corrente e `..` quella superiore.

## File e directory

| Comando | Funzione | Esempio |
|---|---|---|
| `mkdir` | crea una directory | `mkdir progetto` |
| `rmdir` | elimina una directory vuota | `rmdir vecchia_cartella` |
| `touch` | crea un file vuoto o aggiorna i timestamp | `touch note.txt` |
| `cp` | copia | `cp origine.txt copia.txt` |
| `mv` | sposta o rinomina | `mv vecchio.txt nuovo.txt` |
| `rm` | rimuove file | `rm file.txt` |
| `cat` | visualizza o concatena file | `cat note.txt` |
| `less` | legge un file in modo scorrevole | `less note.txt` |
| `head` / `tail` | mostra inizio/fine file | `tail -n 20 log.txt` |

**Attenzione:** `rm` elimina senza spostare nel cestino. `rm -r` può eliminare un'intera directory e il suo contenuto; controlla sempre il percorso prima di eseguirlo. Non copiare comandi distruttivi senza comprenderli.

## Ricerca e filtri

```bash
find . -name "*.c"
grep -n "main" programma.c
ls -la | less
```

- `find` ricerca file e directory a partire da un percorso.
- `grep` cerca righe che corrispondono a un testo o a un'espressione.
- `|` (pipe) passa l'output di un comando come input al successivo.

## Reindirizzamento

```bash
comando > output.txt     # crea/sovrascrive l'output
comando >> output.txt    # aggiunge in fondo
comando < input.txt      # usa il file come input
```

Lo standard output e lo standard error sono flussi distinti. `2>` consente di reindirizzare gli errori in modo separato.

## Utenti, gruppi e permessi

- `whoami`: utente corrente.
- `id`: UID, GID e gruppi associati.
- `chmod`: modifica i permessi.
- `chown`: cambia il proprietario (richiede spesso privilegi).
- `sudo`: esegue un comando con privilegi elevati se autorizzato.

I permessi base sono lettura (`r`), scrittura (`w`) ed esecuzione (`x`) per proprietario, gruppo e altri. Approfondisci nelle note [Permessi in Linux](Permessi%20in%20Linux.md) e [Utenti](Utenti.md).

## Codice di uscita

Un programma restituisce un codice di uscita: per convenzione `0` indica successo, mentre valori non zero indicano un errore o un esito specifico. `echo $?` mostra il codice dell'ultimo comando eseguito.
