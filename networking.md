# Rete

## La rete di computer

Una rete di computer e’ un insieme di calcolatori che possono parlare
fra loro: i singoli pc vengono chiamati nodi, i canali medianti cui
comunicano collegamenti. Solitamente per parlare di rete bisogna avere
piu’ di 2 pc collegati. Spesso poi le reti sono connese tra loro per
formare reti piu’ grosse: ogni rete piccola (chiamata sottorete) puo’
esser parte di una rete piu’ grande.  
Ci sono quattro cose di cui tener conto quando si parla di una rete:

  - dimensione: se si connettono pochi computer si ha una LAN (local
    area netword; altrimenti si parla di Wan, in caso di reti con nodi a
    grande distanza fra loro (internet e’ una wan).

  - forma: le reti possono aver diversa configurazione (ogni punto e’ un
    nodo, ogni linea un collegamento della rete)
    
    ``` 
        o   o   o
         \_ | _/
           \|/
      o-----o-----o     tipologia di rete a stella: ogni nodo comunica con un
          _/|\_         altro mediante un nodo centrale
         /  |  \
        o   o   o
    
    
    
        o------o------o-------o--------o
        |                              |
        |                              |
        |                              o rete "in linea": si comunica 
        |                              | facendo passando le informazioni 
        o                              | per gli altri nodi frapposti
                                       o
    
    
                    o
        o           |  o--o--o
        |           |  |
        o--o--o--o--o  o
               \       |
                o------o        questa potrebbe essere una wan: cio' che e' 
               /       |        evidente e' che formata da piu' (3) sottoreti
        o--o--o--o--o  o        Un nodo che connettte due o piu' reti e' 
        |           |  |        chiamato router
        o           |  o--o
                    o
    ```
    
    Esistono infine modelli decisamente piu’ complicati di connessione
    fra macchine.

  - di cosa e’ fatta: il sistema piu’ comune per connettere le reti
    casalinghe a reti maggiori consiste nel modem
    (modulatore/demodulatore), che permette di trasformare una normale
    linea telefonica in un collegamento fra macchine. Il modem ha il
    compito di trasformare gli input digitali del pc (0 e 1) in segnali
    analogici che possano viaggiare sulla linea telefonica. Dall’altra
    parte il modem ricevente fara’ il contrario e la comunicazione
    potra’ avvenire. Questo puo’ essere inefficiente, in effetti, e le
    linee telefoniche non sono state inizialmente pensate per questo,
    tuttavia e’ estremamente diffuso grazie al costo relativamente
    limitato della soluzione. All’estremo opposto della linea telefonica
    vi e’ la fibra ottica, utilizzata per collegamenti intercontinentali
    All’interno di una LAN invece, il modo piu’ comune di connettere due
    pc e’ la scheda Ethernet.  
    Solitamente ogni connessione ad un nodo viene definita *interfaccia
    di rete*. Linux chiama `eth0` la prima interfaccia ethernet, `fddi0`
    per la prima interfaccia in fibra e `wlan0` la prima interfaccia
    wireless. Il comando `/sbin/ifconfig` elenca le interfaccie
    disponibili sul sistema. Se evocato senza opzioni mostra le
    interfacce di rete attive al momento.

\- protocolli di comunicazione: quando due macchine parlano tra loro
devono parlare la stessa lingua: questa lingua consiste in un
protocollo, ossia un insieme di regole che servono per intepretare i
dati che arrivano e per inviare dati che possono esser compresi.

Internet e’ la piu’ grande rete di computer esistente: la dimensione e’
globale, quindi una wan. E’ una rete formata da numerose sottoreti e di
conseguenza e’ formata di molteplici e svariate configurazioni. E’
necessario un protocollo di comunicazione: o meglio di piu’ protocolli.
L’"internet protocol suite" e’ un set di protocolli di comunicazione:
esso puo’ esser visto come una serie di strati. Ogni strato risolve un
insieme diproblemi riguardanti la trasmissione di dati da qualcosa a
qualcosa. L’attuale suite di protocollo consiste in un modello a quattro
strati (layer).

``` 
  Strato                 Esempi di protocollo

4)Application layer      http, ftp, dhcp, pop3, smtp, irc, ssh, mime, 
3)Transport layer        tcp, udp, dccp, sctp, gtp
2)Internet               ip (IPv4, IPv6), icmp e altri
1)Network access         Ethernet, PPP, Wi-Fi
```

Ogni strato risolve una serie di problemi riguardanti la trasmissione di
dati. Gli strati superiori sono quelli piu’ vicini all’utente e lavorano
con dati piu’ astratti, affidandosi ai protocolli di strato inferiore
per la trasformazione dei dati in forme che possono esser trasmesse.

``` 
     [ Application: ask html ]           [ Application Layer: Serves html ]
                  |                                          ^
                  v                                          |
    [ TCP: Handles Retransmission ]          [ TCP: Handles Retransmission ]
                  |                                          ^
                  v                                          |
        [ IP: Handles Routing ]                   [ IP: Handles Routing ]
                  |                                          ^
                  v                                          |
    [ Link: Handles A Single Hop ]           [ Link: Handles A Single Hop ]
                  |                                          |
                  +------------------------------------------+
```

La sequenza di protocolli, in cui ognuno si basa su quello sottostante,
e’ chiamato stack (pila) di protocolli.

Questo e’ quello che accade quando richiediamo una pagina web con il
browser: il browser utilizza il protocollo tcp per inviare una richiesta
(sotto forma di pacchetto) al web server remoto. Tuttavia per fare cio’
deve sapere da dove la richiesta parte e dove deve arrivare; e qui
arriva il protocollo ip, che sta per internet protocol, il quale si
occupa di mappare univocamente tutte le macchine collegate alla rete, e
di rendere possibile l’instadamento (routing) della richiesta verso il
giusto destinatario. Infine la richiesta verra’ mandata fisicamente dal
livello piu’ basso della catena, che dovra’ disporre di regole per
l’invio materiale dei dati (es quando due modem dialogano hanno
bisogno di accordo sul significato dei segnali inviati e ricevuti). Alla
richiesta verra’ poi fornita risposta mediante un procedimento analogo.
Tenendo conto che il 90 e ip, spesso si fa rimferimento al protocollo
tcp/ip come il protocollo utilizzato in internet.

Qualsiasi pacchetto IP inizia con un header lungo almeno 20 bytes;
assomiglia alla seguente rappresentazione

``` 
      .-------+-------+---------------+-------------------------------.
      |Version|  IHL  |Type of Service|          Total Length         |
      |-------+-------+---------------+-------------------------------|
      |         Identification        |Flags|      Fragment Offset    |
      |---------------+---------------+-------------------------------|
      |  Time to Live |    Protocol   |         Header Checksum       |
      |---------------+---------------+-------------------------------|
      |                       Source Address                          |
      |---------------------------------------------------------------|
      |                    Destination Address                        |
      `---------------------------------------------------------------'
```

I campi importanti sono quello del protocollo che indica se questo sia
un pacchetto TCP (numero 6), un pacchetto UDP (17) o altro, quello
dell’indirizzo ip origine e l’indirizzo ip di destinazione Al header
IP segue il pacchetto tcp: un pacchetto (o segmento) tcp e’ composto un
header (ossia la parte iniziale del pacchetto) e dei dati veri e propri
(altrimenti detti il corpo del pacchetto). L’header, contiene
informazioni su da dove viene (porte sorgente e destinazione), il tipo
di pacchetto che e’ ed altri dettagli amministrativi. Piu’ precisamente
contiene:
