# Trasmissione seriale asincrona e Arduino

## Seriale e parallela

Nella trasmissione **seriale** i bit sono inviati uno dopo l'altro su un canale. Nella trasmissione **parallela** più bit sono inviati contemporaneamente su linee diverse. La seriale richiede meno linee e spesso è pratica su distanze maggiori; la parallela può inviare più bit per trasferimento, ma richiede più collegamenti e sincronizzazione tra linee.

## Trama asincrona

Una comunicazione seriale asincrona tipica comprende:

1. **Start bit**, che segnala l'inizio della trama.
2. **Bit dati**, spesso 7 o 8.
3. **Parità opzionale**, usata per una semplice rilevazione di alcuni errori.
4. **Stop bit**, che indica la fine della trama.

Baud rate, numero di bit dati, parità e bit di stop devono essere configurati in modo coerente ai due estremi. UART descrive il trasmettitore/ricevitore asincrono; USART può supportare modalità sincrone e asincrone a seconda dell'hardware.

## Esempio Arduino: temporizzazione non bloccante

```cpp
const unsigned long intervallo = 1000;
unsigned long ultimoInvio = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  const unsigned long adesso = millis();
  if (adesso - ultimoInvio >= intervallo) {
    ultimoInvio = adesso;
    Serial.println("Messaggio periodico");
  }
  // Il resto del programma continua senza attendere con delay().
}
```

`millis()` restituisce il numero di millisecondi trascorsi dall'avvio. La sottrazione fra valori `unsigned long` gestisce il rollover per gli intervalli brevi, se si usa il confronto `adesso - ultimoInvio >= intervallo`.

## Multitasking cooperativo

Il programma può suddividere il lavoro in attività brevi e controllare quando ognuna deve essere eseguita. Ogni iterazione di `loop()` verifica gli eventi e aggiorna gli stati; le singole attività devono evitare attese bloccanti lunghe.

## Limiti

Una parità semplice non rileva tutti gli errori e non corregge il dato. Nei protocolli più completi si possono aggiungere delimitatori, lunghezza del messaggio, checksum/CRC, numeri di sequenza e conferme di ricezione.
