---
date: 2025-10-16
time: 08:37
---
# User input C Sharp

Per avere input dall'utente usiamo  la funzione `Console.ReadLine()`.
Esempio:

```csharp
// Type your username and press enter
Console.WriteLine("Enter username:");

// Create a string variable and get user input from the keyboard and store it in the variable
string userName = Console.ReadLine();

// Print the value of the variable (userName), which will display the input value
Console.WriteLine("Username is: " + userName);
```

Per avere dei numeri in input dobbiamo usare la funzione `ReadLine` pero prima si essa usare la funzione `Convert.ToInt32()` per convertirla da stringa a intero