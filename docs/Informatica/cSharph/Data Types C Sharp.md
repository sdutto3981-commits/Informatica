# Tipi di dati in C#

Il tipo determina quali valori una variabile può rappresentare e quali operazioni sono consentite. C# è un linguaggio staticamente tipizzato: il tipo della variabile è noto in compilazione.

```csharp
int eta = 17;
long popolazione = 8_000_000_000L;
float temperatura = 21.5f;
double media = 7.25;
decimal prezzo = 19.99m;
char iniziale = 'A';
bool promosso = true;
string nome = "Ada";
```

## Tipi comuni

| Tipo | Significato | Esempio |
|---|---|---|
| `int` | intero a 32 bit con segno | `int x = -12;` |
| `long` | intero a 64 bit con segno | `long n = 5_000_000_000L;` |
| `float` | numero binario in virgola mobile a 32 bit | `float f = 1.5f;` |
| `double` | numero binario in virgola mobile a 64 bit | `double d = 1.5;` |
| `decimal` | numero decimale ad alta precisione decimale, utile per importi | `decimal p = 1.50m;` |
| `char` | singolo carattere UTF-16 code unit | `char c = 'A';` |
| `bool` | `true` o `false` | `bool ok = false;` |
| `string` | sequenza di caratteri, immutabile | `string s = "Ciao";` |

## Conversioni

```csharp
int numero = Convert.ToInt32("42");
if (int.TryParse(Console.ReadLine(), out int valore))
    Console.WriteLine(valore);
else
    Console.WriteLine("Valore non valido");
```

`TryParse` è utile per validare input che possono essere errati. `Convert.ToInt32` può generare un'eccezione se la stringa non rappresenta un intero valido.

Attenzione: la divisione tra due `int` produce un risultato intero (`5 / 2 == 2`); usare `5.0 / 2` oppure un tipo decimale se serve la parte frazionaria. Per `float`, `double` e `decimal` i letterali hanno suffissi specifici (`f`, `d` opzionale, `m`).
