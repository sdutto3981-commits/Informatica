# Generatore reale

Un generatore ideale di tensione mantiene la tensione ai propri terminali costante indipendetemente dalla corrente erogata.

Un generatore reale si comporta diversamente : presenta una resistenza interna che provoca una caduta di tensione quando eroga corrente

Per studiarlo si usa il modello equivalente formato da:
- un generatore ideale di tensione $V_0$
- una resistenza interna $R_1$ collegata in serie
- un carico esterno $R_L$

Qui $V_0$ rappresenta la tensione a vuoto del generatore mentre $R_L$ rappresenta la resistenza del dispositivo alimentato

## Corrente erogata

Poichè la resistenza interna e il carico sono in serie, la resistenza totale vale:

$$
R_{tot}=R_i+R_L
$$

La corrente erogata è:

$$
I=\frac{V_0}{R_i+R_L}
$$

La tensione al capo del carico è:

$$
V_L =I*R_L
$$

Sostiteundo la formula della corrente:

$$
V_L = \frac{V_0*R_L}{R_i+R_L}
$$

## Tensione a vuoto

La tensione a vuoto è la tensione misurata ai teminali del generatore quando non è collegato un carico che assorba corrente.

Idealmente:

$$
I=0
$$

Di conseguenza la caduta di tensione sulla resistenza interna è:

$$
V_i=R_i*I=0
$$


### Esempio

Un generatore reale ha:

$$
V_0=12V, \ \ R_i=2\Omega, \ \ R_L=4\Omega
$$

Calcola la corrente eroga e la tensione sul carico
1. Resistenza totale

$$
R_{tot}=2+4=6\Omega
$$

2. Corrente

$$
I=\frac{12}6=2A
$$

3. Tensione sul carico

$$
V_L=I*R_L=2*4=8V
$$

4. Caduta sulla resistenza interna

$$
V_i=I*R_i=2*2=4V
$$
verifica:

$$
V_0=V_i+V_L=4+8=12V
$$

La tensione di 12V a vuoto è dunque scesa a 8V ai capi del carico.

## Potenza e rendimento

La potenza erogata dal generatore ideale interno è:

$$
P_G=V_0*I
$$

La potenza dissipata dalla resistenza interna è:

$$
P_i=I^2*R_i
$$

La potenza utile ricevuta dal carico è:

$$
P_L=V_L*I=I^2*R_L
$$

Vale il bilancio:

$$
P_G=P_i+P_L
$$

Il rendimento si misura qunata parte della potenza generata arriva al carico:

$$
\boxed{\eta=\frac{P_L}{P_G}}
$$

Per un generatore reale puramente resistivo:

$$
\boxed{\eta=\frac{R_L}{R_i+R_L}}
$$

Per rendere il rendimento in percentuale bisogna moltiplicare il risultato per 100.

Nell esempio precedente:

$$
\eta=\frac{4}{2+4}=0,667 \\
\eta=66,7%
$$

## Adattamento del carico

Il concetto di adattamento è importante nelle telecomunicazionie e nelle trasmissioni di segnali.

Nel mdodelo resistivo in corrente continua la condizione di adattamento per il massimo trasferimento di pteza si ha quando: 

$$
R_L=R_i
$$

La resistenza del carico deve quindi essere uguale alla resistenza interna del generatore.

### Che cosa succede quando il carico è adattato

Se $R_L = R_i$ la resistenza totale è:

$$
R_{tot}=r_i+R_L=2R_i
$$

La tensione sul carico diventa:

$$
V_L=\frac{V_0*R_L}{R_i+R_L}=\frac{V_0*R_i}{2R_i}
$$

Quindi:

$$
v_L=\frac{V_0}2
$$

La tensione sul carico è meta della tensione a vuoto.

La potenza trasferita al carico è massima per quel generatore, am il rendimento è:

$$
\eta=\frac{R_i}{R_i+R_i}=\frac12 \\
\eta=50\%
$$

Questo è il punto da ricordare: massimo trasferimento di potenza non significa massimo rendimento.

Quanod il carico è adattato metà delal potenza del generatore viene dissipata nella resistenza interna
