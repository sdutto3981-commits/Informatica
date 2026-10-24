# Esercizi di ripasso — sistemi di numerazione

Prova a risolvere gli esercizi senza consultare le soluzioni, poi verifica i risultati espandendo i numeri secondo le potenze della base.

## Esercizi

1. Converti `45₁₀` in binario.
2. Converti `101101₂` in decimale.
3. Converti `294₁₀` in base 5.
4. Converti `7B₁₆` in decimale.
5. Converti `1101.1₂` in decimale.
6. Rappresenta `−13` in complemento a due su 8 bit.

## Soluzioni commentate

1. `45₁₀ = 101101₂`, perché `32 + 8 + 4 + 1 = 45`.
2. `101101₂ = 1·2⁵ + 0·2⁴ + 1·2³ + 1·2² + 0·2 + 1 = 45₁₀`.
3. `294₁₀ = 2134₅`, leggendo i resti delle divisioni successive dal basso verso l'alto.
4. `7B₁₆ = 7·16 + 11 = 123₁₀`.
5. `1101.1₂ = 8 + 4 + 1 + 0,5 = 13,5₁₀`.
6. `13₁₀ = 00001101₂`; invertendo i bit si ottiene `11110010`, aggiungendo 1 si ottiene `11110011₂`.

## Controllo del risultato

Una conversione è più affidabile se viene verificata con il procedimento inverso. Per le rappresentazioni con segno, specifica sempre quanti bit sono disponibili e quale convenzione stai usando.
