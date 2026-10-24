# `object`, `ToString()` e uguaglianza

Tutti i tipi classe C# derivano da `object` (`System.Object`). Tra i metodi più importanti ci sono `ToString()`, `Equals()` e `GetHashCode()`.

- `ToString()` restituisce una rappresentazione testuale dell'oggetto.
- `Equals()` verifica l'uguaglianza secondo la semantica definita dal tipo.
- `GetHashCode()` restituisce un codice usato, tra l'altro, dalle collezioni basate su hash.

```csharp
public class Studente
{
    public string Matricola { get; }
    public string Nome { get; }

    public Studente(string matricola, string nome)
    {
        Matricola = matricola;
        Nome = nome;
    }

    public override string ToString() => $"{Matricola} - {Nome}";
}
```

Senza un override, `ToString()` normalmente restituisce il nome completo del tipo, non un riepilogo personalizzato.

## Uguaglianza per riferimento e per valore

Per le classi, `==` in genere confronta i riferimenti se l'operatore non viene ridefinito; `Equals()` può essere ridefinito per confrontare i dati significativi. Se un tipo ridefinisce `Equals()`, deve mantenere coerente anche `GetHashCode()`: oggetti uguali secondo `Equals` devono avere lo stesso hash code.

Non ridefinire l'uguaglianza senza definire chiaramente che cosa significa “due oggetti uguali” nel dominio.
