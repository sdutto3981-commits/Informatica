---
date: 2025-10-02
time: 10:03
---
# Immagini

Le immagini sono delle matrici di pixel oppure strutture dati bidimensionali in cui ogni elemento è un pixel le funzioni delle immagini sono:
- Informatica
	- Trasmette informazioni
- Decorativa
	- Abbellire e rendere attraente
- Emotiva 
	- Suscitare emozioni
- Comunicativa
	- Può comunicare qualcosa

Quindi abbiamo colore contrasto linee ecc..

#### Metadato delle immagini

Che cosa sono i metadati sono delle informazioni nascoste associate all'immagine non salvati nell'immagine ma memorizzati nel file

1. **Metadati tecnici**
	- Dimensione
	- Risoluzione
	- Formato file
	- Estensione e formato 
2. **Caption (didascalie)**
	- Breve descrizione dell'immagine
	- Spiega cosa ce nel immagine
	- Utile per accessibilità

#### Metadati html

Si inseriscono in head

- Charset (codifica caratteri)
	- Definisce il set di caratteri utilizzati nel documenti
- Decriptin (descrizione della pagina)
	- Fornisce una breve riassunto del contenuto della pagina
- author (autore)
	- Specifica l'autore
- keyword
	- Utili per alcuni sistemi
- viewport 
	- Crea pagine responsive


Secondo rgb

(255,0,0)(0,255,0)(0,0,255)
(255,255,0)(0,255,255)(255,255,255)
(0,0,0)(128,128,128)(255,0,255)

Esistono anche altri formati per i colori le stampanti per esempio usano CMYK l'ultimo è black ovvero nero perché con gli altri tre non posso creare il nero

[[Conversione RGB to CMYK]]

Calcolo delle dimensioni  larghezza + altezza + bytes per pixel

La risoluzione dell'immagine è data da larghezza e altezza maggiore la definizione $1920*1080$ pixel Full HD  possiamo anche calcolare quanto tempo ci i impiega per scaricare un immagine questo è  dato da $$\Delta t = \frac{dimensione}{velocità}$$
Per questo usiamo delle compressioni delle immagini per permette uno scaricamento più veloci

#### PPI

Pixel per pollice è un qualcosa che non possiamo modificare  un pollice e 2,46 cm la scelta del PPi dev'essere scelta per quello che dovremo andare a  fare con l'immagine maggiore è il PPi più dettagli vengono catturati e di conseguenza la dimensione del file sul monitore la densità di pixel per determinare il numero di pixel di un lato la formula è $$L=Dimensione \ in \ pollici * PPI$$
Nella stampa di immagini serve un PPI sulle riviste troviamo una PPI di circa 300 mentre su monitor e schermi del telefono possono arrivare sino a 530 PPI perché andando oltre è inutile 

#### DPI

Pixel per dot è modificabile da noi  è utile per comprendere la stampa di un immagine siccome la stampante non può riprodurre tutti i colori ma tramite il divisionismo va a creare una matrice che permetta di rappresentarli tutti.

Per andare a riprodurre un singolo pixel se si usa una matrice 3x3 $$DPI=PPI*l\_matrice^2$$
Possiamo scegliere il DPI dalle impostazioni di stampa quando stampiamo il documento

#### Algoritmi di compressione

Possono essere:
- [[Lossless]]: applicando una compressione e decomprimendola riottengo la stessa immagine
- [[Lossy]]: applico la compressione e decomprimendo non riesco a riavere la stessa immagine




## Riferimenti2
1. [[Immagini HTML]]
