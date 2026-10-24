# UCS e codifica dei caratteri

**UCS** (*Universal Character Set*) è il repertorio universale di punti di codice definito dallo standard Unicode e dagli standard ISO/IEC collegati. Ogni carattere a cui viene assegnato un punto di codice è identificato da un valore scritto convenzionalmente come `U+` seguito da cifre esadecimali, ad esempio `A` è `U+0041`.

## Repertorio, codifica e byte non sono la stessa cosa

- **Repertorio/carattere:** l'insieme dei caratteri e i punti di codice che li identificano.
- **Punto di codice:** numero assegnato a un carattere (o altro elemento del repertorio).
- **Codifica:** regole con cui i punti di codice sono trasformati in unità di memorizzazione.

UTF-8, UTF-16 e UTF-32 sono forme di codifica Unicode. UTF-8 usa da 1 a 4 byte per punto di codice; UTF-16 usa una o due unità da 16 bit; UTF-32 usa un'unità da 32 bit. Non sono intercambiabili byte per byte, anche se possono rappresentare lo stesso testo.

## Esempio

La lettera `A` con punto di codice U+0041 viene rappresentata in UTF-8 dai byte `41` in esadecimale. Un carattere fuori dal Basic Multilingual Plane, come molti emoji, richiede quattro byte in UTF-8 e una coppia di surrogate in UTF-16.

## Perché è importante

Una dichiarazione HTML come `<meta charset="utf-8">` indica al browser come decodificare i byte del documento. La dichiarazione deve corrispondere alla codifica realmente usata nel file; una discordanza può causare caratteri corrotti (*mojibake*).
