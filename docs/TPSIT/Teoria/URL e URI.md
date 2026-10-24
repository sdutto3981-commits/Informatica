# URI e URL

**URI** (*Uniform Resource Identifier*) è il termine generale per un identificatore di risorsa. **URL** (*Uniform Resource Locator*) è un tipo di URI che indica come individuare una risorsa, tipicamente attraverso uno schema e una destinazione.

Esempio di URL:

```text
https://www.example.com:443/documenti/manuale.html?lingua=it#capitolo-2
```

| Parte | Significato |
|---|---|
| `https` | Schema/protocollo usato per accedere alla risorsa. |
| `www.example.com` | Host o nome di dominio. |
| `443` | Porta esplicita, predefinita per HTTPS. |
| `/documenti/manuale.html` | Percorso della risorsa sul server. |
| `?lingua=it` | Query con parametri. |
| `#capitolo-2` | Frammento riferito a una parte della risorsa. |

L'espressione “URL assoluto” indica un indirizzo completo; un riferimento relativo, come `../immagini/logo.png`, viene risolto rispetto all'URL base del documento. Il frammento `#capitolo-2` normalmente non viene inviato al server nella richiesta HTTP: il browser lo usa per individuare una parte della risorsa.

Nell'uso quotidiano i due termini sono spesso usati in modo intercambiabile, ma URI è il concetto più ampio. Vedi anche [Struttura di un URL](Struttura%20di%20un%20URL.md).
