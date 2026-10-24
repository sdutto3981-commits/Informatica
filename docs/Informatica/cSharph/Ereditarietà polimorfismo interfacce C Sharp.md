# Ereditarietà, polimorfismo, classi astratte e interfacce

## Ereditarietà

Una classe derivata specializza una classe base mediante `:`. Usala quando esiste una vera relazione “è un”, non soltanto per riutilizzare codice.

```csharp
class Animale
{
    public virtual string Verso() => "Suono generico";
}

class Cane : Animale
{
    public override string Verso() => "Bau";
}
```

`virtual` consente l'override; `override` sostituisce l'implementazione ereditata. `base` permette di richiamare membri della classe base nei contesti previsti.

## Polimorfismo

```csharp
Animale animale = new Cane();
Console.WriteLine(animale.Verso()); // Bau
```

Il tipo della variabile è `Animale`, ma il comportamento selezionato per il metodo virtuale dipende dal tipo effettivo dell'oggetto (`Cane`). Questo consente di trattare oggetti diversi tramite un contratto comune.

## Classe astratta

Una classe dichiarata `abstract` non può essere istanziata direttamente. Può contenere implementazioni e membri astratti che le classi derivate devono completare.

```csharp
abstract class Forma
{
    public abstract double Area();
}
```

## Interfaccia

Un'interfaccia definisce un contratto che una classe o struct implementa. Una classe può implementare più interfacce, ma può derivare direttamente da una sola classe base.

```csharp
interface IStampabile
{
    void Stampa();
}

class Documento : IStampabile
{
    public void Stampa() => Console.WriteLine("Documento stampato");
}
```

## Composizione

La composizione costruisce un oggetto utilizzando altri oggetti. Spesso è preferibile all'ereditarietà quando una classe “ha un” componente invece di “essere un” altro tipo.

## Principi di progettazione

- Programma verso interfacce/contratti quando rende il codice più flessibile.
- Mantieni basse le dipendenze tra classi.
- Non introdurre gerarchie profonde senza una ragione concreta.
- Distingui override (ridefinizione polimorfica) da overload (stesso nome, firma diversa).

## Riferimento

[W3Schools — C# Inheritance](https://www.w3schools.com/cs/cs_inheritance.php) · [Polymorphism](https://www.w3schools.com/cs/cs_polymorphism.php) · [Abstraction](https://www.w3schools.com/cs/cs_abstract.php) · [Interfaces](https://www.w3schools.com/cs/cs_interface.php)
