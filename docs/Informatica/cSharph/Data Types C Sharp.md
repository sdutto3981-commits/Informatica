# Tipi di dati in C#

C# è tipizzato staticamente: ogni variabile ha un tipo noto al compilatore. I tipi numerici differiscono per intervallo, precisione e rappresentazione.

| Tipo | Uso tipico |
|---|---|
| `int` | interi a 32 bit con segno |
| `long` | interi a 64 bit con segno |
| `short`, `byte` | interi più piccoli, con o senza segno |
| `float` | numeri in virgola mobile a precisione singola; usa il suffisso `f` |
| `double` | numeri in virgola mobile a precisione doppia |
| `decimal` | decimali ad alta precisione usati spesso per importi; usa `m` |
| `bool` | `true` o `false` |
| `char` | singolo valore UTF-16 rappresentato da un'unità di codice |
| `string` | sequenza di caratteri testuale |

```csharp
int quantita = 12;
long popolazione = 8_000_000_000L;
float fattore = 1.5f;
double media = 7.25;
decimal prezzo = 19.99m;
bool disponibile = true;
char lettera = 'S';
string testo = "Ciao";
```

## Valori numerici e precisione

I tipi in virgola mobile (`float`, `double`) possono rappresentare alcuni decimali in modo approssimato. Per questo confrontare direttamente numeri `double` ottenuti da calcoli può produrre risultati inattesi. `decimal` è spesso preferibile per importi, ma non sostituisce la necessità di definire arrotondamento e regole di calcolo.

## Tipi valore e tipi riferimento

Tra i tipi valore rientrano tipi numerici, `bool`, `char`, `struct` ed enum. `string`, array e classi sono tipi riferimento. Questa distinzione influenza assegnazione, copia e valori `null`.

## Riferimento

[W3Schools — C# Data Types](https://www.w3schools.com/cs/cs_data_types.php)
