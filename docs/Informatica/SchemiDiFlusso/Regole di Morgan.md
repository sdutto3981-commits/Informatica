# Leggi di De Morgan

Le leggi di De Morgan descrivono come distribuire la negazione sulle operazioni logiche. Sono utili nell'algebra booleana, nella semplificazione delle condizioni e nella progettazione dei circuiti.

## Formule

- `¬(A ∧ B) = ¬A ∨ ¬B`
- `¬(A ∨ B) = ¬A ∧ ¬B`

In parole: negare una AND equivale a fare OR delle negazioni; negare una OR equivale a fare AND delle negazioni.

## Esempio con condizioni

La condizione “non sono vere entrambe A e B” si scrive `!(A && B)` e, per De Morgan, è equivalente a `!A || !B`.

```csharp
if (!(haBiglietto && documentoValido))
{
    Console.WriteLine("Accesso non consentito");
}

// Equivalente:
if (!haBiglietto || !documentoValido)
{
    Console.WriteLine("Accesso non consentito");
}
```

Per verificare le equivalenze, costruisci la tabella della verità per tutte le combinazioni di ingressi. Non confondere la negazione di un'espressione composta con la negazione di un solo operando.
