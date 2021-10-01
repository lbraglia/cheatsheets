# Make

## Il problema

Programmi di grandi dimensioni non possono eser contenuti in un solo
file; essi vengono solitamente suddivisi in moduli, unità di codice a se
stanti.  
Ogni modulo disporra di file `.c` che contengono le implementazioni
delle funzioni e di file `.h` che contengono i prototipi ed eventuali
costanti; i moduli vengono compilati in codice oggetto separatamente, e
alla fine viene creato un eseguibile tramite il linking degli stessi.

Ipotizziamo di avere un programma che calcoli la media di tre numeri: in
`main.c` abbiamo la main che richiede i numeri all'utente e stampa il
risultato, basandosi sulla funzione `average`, il cui prototipo si trova
in `mymath.h` ed è definita in `mymath.c`. La funzione si basa su un
altra funzione di nome `sum` definita ed implementata anch'essa in
`mymath.[ch]`.  
La compilazione di tale progetto richiederebbe i comandi:

    gcc -c mymath.c
    gcc -c main.c
    gcc -o average main.o mymath.o 

La compilazione manuale e il linking divengono scomodi quando si ha a
che fare con molti file, e qui interviene l'utility `make` che permette
l'automatizzazione del tutto. Esso legge un file denominato `Makefile` o
`Makefile` che esegue le operazioni necessarie alla compilazione, una
volta che queste sono state specificate.

## `Makefile`

Il `Makefile` specifica una serie di regole di compilazione: `make`
verifica le regole ed esegue solo le operazioni (ricompilazioni)
necessarie (ad esempio non ricompila sorgenti che non sono stati
modificati. Un esempio di `Makefile` per il caso precedente potrebbe
esser:

    # my first Makefile
    
    average:        main.o mymath.o
        cc -o average main.o mymath.o
    
    main.o:     main.c mymath.h
        cc -c main.c
    
    mymath.o:   mymath.c mymath.h
        cc -c mymath.c
    
    clean:
        rm average *.o

Le regole da stabilire nel `Makefile` presentano il seguente formato:

    target: dependencies
            command

con `command` indentato da un TAB. I command sono eseguiti ognuno con
una sub-shell  
Il `target` è il nome di un file da generare o un'azione da svolgere; le
`dependencies` costituiscono file utilizzati come input per creare il
file target; i `command` leazioni da eseguire per creare il target.  
La prima regola è quella eseguita di default se si comanda semplicemente

    make

è comunque convenzione chiamare la prima regola con l'identificatore
`all`

Si salva il `Makefile` nella dir del progetto dopodichè si comanda
semplicemente `make`, che svolgerà le operazioni opportune: per ogni
target, make controlla la data di modifica delle corrispondenti
dipendenze e decide se e cosa ricompilare.  
Ad esempio se è stato modificato solo `main.c`, si eseguirà la target
`main.o` (che dipende da `main.c`) e `average` (che dipende da
`main.o`).

Come detto se si comanda solo `make` viene eseguito il primo target;
alternativamente possiamo specificare di quale target eseguire le
operazioni connesse comandando:

    make nome_target

Nell'ultimo caso, mediante un `make clean` si faceva eseguire la
rimozione dei file specificati. Il target clean non ha dipendenze e si
limita ad eseguire il comando di rimozione indicato.  

## Più `Makefile`

Se il progetto aumenta di dimensioni, si può organizzare il tutto come
segue:

  - una directory per modulo (tutti i file `.c` di ogni modulo
    all'interno della dir relativa, i file `.h` alternativamente
    all'interno di essa o in una dir specifica)

  - un Makefile per ogni modulo-directory che gestisce la creazione dei
    file `.o`

  - un Makefile nella dir radice per la creazione dell'eseguibile

in sostanza utilizzare più Makefile, uno per modulo.

Per esempio consideriamo un progetto con in root il main e il Makefile,
due moduli (==dir) di nome foo e bar, e una terza cartella contenente
tutti gli header.

    [12:09:14] luca@debian: tree project/
    project/
    |-- Makefile
    |-- bar
    |   |-- Makefile
    |   `-- bar.c
    |-- foo
    |   |-- Makefile
    |   `-- foo.c
    |-- include
    |   |-- bar.h
    |   `-- foo.h
    `-- main.c
    
    3 directories, 8 files

Ad esempio il `Makefile` del modulo `bar` sarà simile a:

    all:    bar.o
    
    bar.o:  bar.c \
                ../include/bar.h
        gcc -I../include -c bar.c
    
    clean:
        rm -f *.o

Il `Makefile` in root sarà simile a

    all:    main.o foodir bardir 
        gcc -o main main.o foo/foo.o bar/bar.o
    
    main.o: main.c include/*.h
        gcc -Iinclude -c main.c
    
    foodir:
        cd foo; make all
    
    bardir:
        cd bar; make all
    
    clean:
        rm -f *.o main
    
    cleanall:
        rm -f *.o main
        cd foo; make clean
        cd bar; make clean

## Utilizzo di variabili (macro)

La specificazione di variabili serve a facilitare la gestione del
Makefile; per definirle, la sintassi è

    name = value

Per utilizzarle si usi `$(name)` o `${name}`. Si sono formate alcune
convenzioni sugli identificatori utilizzati:

  - `CC` il compilatore

  - `CFLAGS` le opzioni da passargli

  - `HDIR` la directory degli header

  - `DEPH` file di dipendenza

  - `SOURCE` file sorgenti

  - `OBJECTS` file oggetto

Un esempio rivisto per il `Makefile` di `foo`:

    CC          =   gcc
    HDIR        =   ../include
    INCPATH =   -I$(HDIR)
    DEPH        =   $(HDIR)/foo.h
    SOURCE  =   foo.c
    OBJECTS =   foo.o
    
    all:    $(OBJECTS)
    
    foo.o:  $(SOURCE) $(DEPH)
        $(CC) $(INCPATH) -c $(SOURCE)
    
    clean:
        rm -f *.o

un esempio di `Makefile` per `main`:

    CC      =   gcc
    HDIR        =   include
    INCPATH     =   -I$(HDIR)
    DEPH        =   $(HDIR)/foo.h  \
                    $(HDIR)/bar.h 
    OBJECTS  =  foo/foo.o bar/bar.o
    
    all:    main
    
    main: main.o foodir bardir 
        $(CC) -o main main.o $(OBJECTS)
    
    main.o: main.c $(HDIR)/*.h
        $(CC) $(INCPATH) -c main.c
    
    foodir:
        cd foo && make all
    
    bardir:
        cd bar && make all
    
    clean:
        rm -f *.o main
    
    cleanall:
        rm -f *.o main
        cd foo && make clean
        cd bar && make clean
