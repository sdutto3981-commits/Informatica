# Metodi e sottoprogrammi C#

Un metodo raccoglie un comportamento nominato, riutilizzabile e testabile. Può ricevere parametri e restituire un valore; se non restituisce un valore si dichiara `void`.

```csharp
static int Somma(int a, int b)
{
    return a + b;
}

static void Main()
{
    int risultato = Somma(3, 4);
    Console.WriteLine(risultato);
}
```

## Firma e parametri

La dichiarazione specifica tipo restituito, nome e parametri. I parametri nella dichiarazione sono formali; i valori forniti nella chiamata sono argomenti.

C# passa gli argomenti **per valore** per impostazione predefinita. Per i tipi valore viene copiato il valore; per i tipi riferimento viene copiato il riferimento, quindi il metodo può modificare l'oggetto indicato dal riferimento, ma riassegnare il parametro non riassegna la variabile del chiamante.

```csharp
static void Incrementa(int n) { n++; }
static void Rinomina(Persona p) { p.Nome = "Nuovo"; }
```

`ref` e `out` permettono di passare una variabile per riferimento con regole specifiche. `out` deve essere assegnato dal metodo; `ref` deve essere inizializzato prima della chiamata.

## Overload e parametri predefiniti

Si possono dichiarare metodi con lo stesso nome e firme differenti (overloading). I parametri opzionali possono avere valori predefiniti; evita combinazioni ambigue.

## Ricorsione

Un metodo ricorsivo richiama sé stesso e deve avere un caso base che termina la catena di chiamate.

## Buone pratiche

- Usa nomi che descrivano l'azione.
- Mantieni una responsabilità chiara.
- Preferisci restituire il risultato invece di usare variabili globali.
- Verifica casi limite, input non validi ed eventuali divisioni per zero.

## Riferimento

[W3Schools — C# Methods](https://www.w3schools.com/cs/cs_methods.php)
