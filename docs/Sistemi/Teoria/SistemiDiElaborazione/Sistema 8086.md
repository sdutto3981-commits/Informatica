---
date: 2026-02-01
time: 16:08
---

# Sistema 8086

## I BUS

I bus, sono dei componenti che permettono la comunicazione fra la CPU la Memoria Centrale e le varie periferiche.

I BUS sono suddivisi in:
- **Address Bus:** utilizzato dalla CPU per indirizzare la memoria centrale. Unidirezionale di dimensione pari a 20bit nell'8086
- **Data Bus:** trasportano i dati dalla CPU verso la Memoria Centrale e le altre periferiche, E condiviso fra tutti i moduli dell'elaboratore. Bidirezionale la sua dimensione è pari a 16bit
- **Control Bus:** serve  a controllare l'hardware esterno alla CPU, indicando il tipo di operazione che il sistema deve eseguire. Stabilisce tra le altre cose chi in un determinato momento può leggere/scrivere sul Data Bus

## Componenti principali

- **EU (Execution Unit)**
- **CU (Control Unit)**
- **BIU (Bus Interface Unit)**

### Execution Unit

Si occupa di eseguire le istruzioni, decodificate dalla CU.

L'elemento principale contenuto nella EU è la ALU componente basato sulla logica combinatoria che svolge le operazioni logico matematiche esso ammette al massimo sue operandi alla volta.

*Risorsa non inclusa: Pasted image 20260201162026.png*

### Bus Interface Unit

Si occupa del interfacciamento ai bus.

Tra le altre cose, contiene un sommatore simile alla ALU che permette di determinare dati i registri segmento e puntatore l'indirizzo assoluto su 20 bit si una qualsiasi locazione di memoria a cui si deve accedere

*Risorsa non inclusa: Pasted image 20260201162234.png*

### Control Unit

Permette l'esecuzione di una singola istruzione oridina alla BIU di caricare la prossima istruzione la decodifica e chiede alla EU di eseguirla le seguenti operazioni sono iterate fino al termine del programma in esecuaione.

Gestisce la sincronizzazione delle attività di tutti i dispositivi esterni grazie tra le altre cose al clock un segnale periodico.

*Risorsa non inclusa: Pasted image 20260201162510.png*

## Il clock

L'attività della CPU è regolata mediante un clock esterno generato mediante un oscillatore ad elevata precisione, IN corrispondenza di ogni colpo di clock la CPU esegue una certa operazione la sua unità di misura è l'Herz.

# Esempi

***Un processore riesce ad eseguire 2.5 miliardi di istruzioni al secondo. Determinare la frequenza del clock del processore.***

**Soluzione:**
N istruzioni: $2,5*10^9$
$f = N \ istruzioni \ al \ sec = 2,5*10^9Hz=2,5GHz$

***Un processore RISC ha una frequenza di 5KHz. Quante istruzioni riesce a eseguire in un secondo? Quanto tempo il processore ad eseguire un istruzione?***

**Soluzione:**
$f=5*10^3Hz$
$N\ istruzioni = 5000$
$t\ istruzione = \frac{1}{5000Hz}=0,0002s$
