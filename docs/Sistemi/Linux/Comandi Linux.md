# Comandi Linux essenziali

I comandi vengono digitati in una shell. Per conoscere le opzioni disponibili usa `man comando` oppure `comando --help` quando supportato.

## Navigazione e file

| Comando | Funzione | Esempio |
|---|---|---|
| `pwd` | mostra la directory corrente | `pwd` |
| `ls -la` | mostra file e dettagli, inclusi quelli nascosti | `ls -la` |
| `cd` | cambia directory | `cd Documenti` |
| `mkdir` | crea directory | `mkdir progetto` |
| `touch` | crea un file vuoto o aggiorna i timestamp | `touch note.txt` |
| `cp` | copia file/directory (con opzioni per directory) | `cp a.txt b.txt` |
| `mv` | sposta o rinomina | `mv vecchio.txt nuovo.txt` |
| `rm` | elimina file; irreversibile senza backup | `rm note.txt` |
| `rmdir` | rimuove directory vuota | `rmdir vuota` |
| `cat` | stampa il contenuto | `cat note.txt` |
| `less` | consulta un file scorrendolo | `less note.txt` |
| `head` / `tail` | mostra inizio/fine file | `tail -n 20 log.txt` |

Attenzione: `rm -r` rimuove directory e contenuti; `rm -rf` è particolarmente pericoloso. Prima di eseguire comandi distruttivi, controllare percorso e argomenti.

## Ricerca

```bash
find . -type f -name '*.c'
grep -n "main" sorgente.c
```

`find` ricerca file in base a criteri; `grep` ricerca testo. I nomi dei file Linux distinguono generalmente maiuscole e minuscole.

## Informazioni e permessi

- `whoami`: utente corrente.
- `id`: UID, GID e gruppi.
- `chmod`: modifica i permessi.
- `chown`: modifica proprietario/gruppo, normalmente richiedendo privilegi adeguati.
- `sudo`: esegue un comando con privilegi elevati, se autorizzati.

Esempio di permessi simbolici: `chmod u+x script.sh` aggiunge il permesso di esecuzione al proprietario. Non usare `sudo` come soluzione automatica a ogni errore.

## Pipeline e redirezioni

```bash
ls -la | less
comando > output.txt
comando >> output.txt
```

`|` invia l'output di un comando al successivo; `>` sovrascrive un file e `>>` aggiunge in fondo. Prima di usare `>` su file importanti, verificare l'effetto.
