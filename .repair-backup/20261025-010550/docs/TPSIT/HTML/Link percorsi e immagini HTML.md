# Link, percorsi e immagini HTML

## Link

```html
<a href="contatti.html">Contatti</a>
<a href="https://www.w3schools.com/html/">Guida HTML</a>
<a href="#esempi">Vai agli esempi</a>
```

- URL assoluto: comprende schema e host, per esempio `https://example.com/pagina.html`.
- Percorso relativo: è interpretato rispetto alla posizione del documento corrente.
- Frammento: `#esempi` porta all'elemento che ha `id="esempi"`.
- `mailto:` apre un programma di posta se configurato; non invia da solo un messaggio.

Preferisci un testo di link che dica dove porta. Evita “clicca qui” quando non descrive la destinazione.

## Percorsi relativi

Supponendo questa struttura:

```text
sito/
├── index.html
├── pagine/
│   └── contatti.html
└── immagini/
    └── logo.png
```

Da `index.html`, il percorso è `pagine/contatti.html` o `immagini/logo.png`. Da `pagine/contatti.html`, per risalire alla cartella principale si usa `../`, quindi `../immagini/logo.png`.

## Immagine come link

```html
<a href="progetto.html">
  <img src="immagini/progetto.jpg" alt="Apri la pagina del progetto">
</a>
```

L'alternativa testuale dovrebbe descrivere l'azione o il contenuto utile del link, evitando una descrizione ridondante.

## Link che aprono una nuova scheda

Se usi `target="_blank"`, indica all'utente che si aprirà una nuova scheda quando questo è importante per l'esperienza. Nei browser moderni il contesto di apertura è in genere isolato tramite `noopener`; scrivere `rel="noopener noreferrer"` esplicita il comportamento desiderato.

## Riferimento

[W3Schools — HTML Links](https://www.w3schools.com/html/html_links.asp) · [HTML File Paths](https://www.w3schools.com/html/html_filepaths.asp)
