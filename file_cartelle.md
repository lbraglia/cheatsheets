# File e cartelle


## File

### Informazioni
```
l@m740n:~$ echo "ciao" > prova
l@m740n:~$ stat prova
  File: prova
  Dim.: 5         	Blocchi: 8          Blocco di IO: 4096   file regolare
Device: 801h/2049d	Inode: 6819390     Coll.: 1
Accesso: (0600/-rw-------)  Uid: ( 1000/       l)   Gid: ( 1000/       l)
Accesso  : 2021-09-28 08:24:00.286290509 +0200
Modifica : 2021-09-28 08:24:00.286290509 +0200
Cambio   : 2021-09-28 08:24:00.286290509 +0200
Creazione: 2021-09-28 08:24:00.286290509 +0200
```

## Attributi
`chattr` serve per cambiare gli attributi ai file e alle cartelle,
attributi che sono visualizzabili mediante `lsattr`. 
Il funzionamento di base è 
```
chattr +/-/=attributo  file_o_directory
```
dove:
- `+` aggiunge l'attributo selezionato
- `-` toglie il selezionato
- `=` imposta quello dopo come l'unico attributo del file
e gli attributi principali sono:
- `a` (append): non e' possibile scrivere sul file, solo
  appendergli la roba. Solo root puo' dare questa opzione.
- `d` (no dump): il file non e' candidato se viene eseguito
  dump
- `i` (immutable): il file diviene immutabile. Solo root puo'
  far questo
- `A` (no atime updates): il momento di accesso non viene
  registrato
- `S` (synchronous updates) in presenza dell'opzione, le
  modifiche al file sono scritte sincronicamente sul disco
- `c` (compressed): il file viene automaticamente compressato
- `u` (undeletable): il file e' incancellabile
- `s` (secure deletion): se cancellato i suoi blocchi sono
  azzerati/riscritti
Ad esempio consideriamo il file ciao
```
$ ~ : sudo chattr +i ciao	# lo rendiamo immutabile
$ ~ : lsattr ciao 
----i------------- cia
$ ~ : sudo chattr -i +au ciao	# togliamo l'immutabilita'
$ ~ : lsattr ciao		        # e mettiamo che non si puo' cancellare
-u---a------------ ciao		    # e che si possa solo appendere
```

Se si vuole modificare gli attributi di una dir e dei suoi
contenuti, occorre porre l'opzione `-R` (recursive) prima di
`+/-/=`.  Ad esempio per rendere una cartella immutabile:
```
$ ~ : mkdir mia_cartella
$ ~ : sudo chattr -R +i mia_cartella/
$ ~ : echo ciao >> mia_cartella/ciao
bash: mia_cartella/ciao: Permission denied
```
Per rimuovere tutti gli attributi creati, si puo' usare `=` seguito da 
niente:
```
$ ~ : sudo chattr = ciao mia_cartella/
```

## Ricerca
Può esser fatta principalmente mediante `find`, `locate` e `xargs`

Per brevità considereremo come file il file vero e proprio, la
direcory, il link simbolico ed ogni cosa abbia una "directory
entry" ossia un nome.  L'albero di una directory consiste nel suo
contenuto e nel contenuto delle sottodirectory.

I programmi sopra elencati permettono di cercare files in una o
più alberi di directory che:
\begin{itemize}
\item presentano nomi che contengono un certo testo o rispettano
  un determinato pattern
\item sono link a determinati file
\item si trovano all'interno di un determinato range di grandezza
  del file
\item sono stati utilizzati durante un certo periodo di tempo
\item sono di un certo tipo (file regolari directory, link)
\item sono di proprietà di un certo soggetto o di un determinato
  gruppo
\item hanno determinati permess
\item contengono testo che rispetta un determinato pattern
\item si trovano ad un certo livello di profondità nell'albero
  della directory
\item una combinazione dei criteri precedenti
\end{itemize}
Una volta ndividuati il/i file ricercati è possibile fare molto di
più che del semplice dichiarazione di path.

### find
Find cerca nell'albero di directory specificato vi sono file o
cartelle che rispettano il pattern fornito, dopodichè ne printa
il path allo stdout.  Un esempio: cerco la roba il cui nome
inizia per linux
\begin{verbatim}
$ ~ : sudo find -name "linux*"
Password:
./.Mail/linux
./.fluxbox/backgrounds/linux_story.png
./linux
./linux/linux_kernel
./back_conf_29012007-115939/.fluxbox/backgrounds/linux_story.png
./back_conf_29012007-115939/.Mail/linux
./linux_non_e_windows.pdf

$ ~ : sudo find . -name "linux*.p*"
./.fluxbox/backgrounds/linux_story.png
./back_conf_29012007-115939/.fluxbox/backgrounds/linux_story.png
./linux_non_e_windows.pdf
\end{verbatim}
L'utilizzo è il seguente
\begin{verbatim}
	   find [-H] [-L] [-P] [path...] [expression]
\end{verbatim}
Le opzioni H,L e P gestiscono il trattamento dei link simbolici:
per ora lasciamole stare.

Path consiste nella cartella il cui albero deve esser esaminato
per la ricerca del file: se path non è specificato di default è
settato .

L'espressione si compone di opzioni, tests, azioni ed
operatori. L'operazione di default è -print, che consiste nel
stampare a terminale i file che rispettano il criterio di
ricerca.

% Le opzioni 
% ----------
% riguardano il comportamento nella ricerca; per chiarezza è meglio porle all'inizio. Ecco alcune opzioni

% - depth: cerca prima nel contenuto delle directory che nella dir stessa. Facciamo un esempio da confrontare con il primo dei due proposti in precedenza

% $ ~ : sudo find  -depth  -name "linux*"
% ./.Mail/linux
% ./.fluxbox/backgrounds/linux_story.png
% ./linux/linux_kernel
% ./linux
% ./back_conf_29012007-115939/.fluxbox/backgrounds/linux_story.png
% ./back_conf_29012007-115939/.Mail/linux
% ./linux_non_e_windows.pdf

% L'unico cambiamento è nella terza e quarta riga dell'output: ossia laddove sia la dir che un suo contenuto rispettano la richiesta; con quest'ultima opzione viene però prima processata e stampata il contenuto della directory (./linux/linux_kerne) che la dir stessa (./linux)

% -help --> printa un help riassuntivo del comando find

% $ ~ : find -help
% Usage: find [path...] [expression]

% default path is the current directory; default expression is -print
% expression may consist of: operators, options, tests, and actions:

% ...

% -maxdepth numero_non_negativo: scendi nella ricerca al massimo a n sottolivelli della directory. Se numero = 1 cerca solo nella dir corrente, se 0 ci si chiede se il nome della dir corrente rispetta il pattern

% $ ~ : sudo find  -maxdepth 0  -name "linux*"

% $ ~ : sudo find  -maxdepth 1  -name "linux*"
% ./linux
% ./linux_non_e_windows.pdf

% $ ~ : sudo find  -maxdepth 2  -name "linux*"
% ./.Mail/linux
% ./linux
% ./linux/linux_kernel
% ./linux_non_e_windows.pdf

% -mindepth numero_non_negativo: non processa niente che sia almeno nel sottolivello n

% $ ~ : sudo find  -mindepth 2  -name "linux*"
% ./.Mail/linux
% ./.fluxbox/backgrounds/linux_story.png
% ./linux/linux_kernel
% ./back_conf_29012007-115939/.fluxbox/backgrounds/linux_story.png
% ./back_conf_29012007-115939/.Mail/linux

% -mount: non discende in directory su altri filesystem montati

% -noleaf: opzione necessaria quando si cerca in cdrom, msdos filesystem e in filesystem non Unix. In questi ultimi per sapere se ci sono sottocartelle da esaminare basta fare hard link -2 (). Se il risultato non è 0 vuol dire che ci sono sottocartelle (qualsiasi cartella, anche vuota, ha almeno due hard link, che consistono nel suo nome e nella cartella ".")

% $ ~ : mkdir ciccio
% $ ~ : ls -l 
% drwxr-xr-x  2 luca 2007-01-29 20:46 ciccio
% $ ~ : mkdir ciccio/luca
% $ ~ : l
% drwxr-xr-x  3 luca 2007-01-29 20:47 ciccio

% I fs non unix non hanno questi 2 hard link di default e se avesser 1 o più sottocartelle lo scan non avvertito potrebbe ignorarle 

% -regextype tipo_regex: cambia la sintassi della regex data al -regex o -iregex (visti più tard) da emacs (di deault) al tipo specificato, che puo' esser posix-awk, posix-basic, posix-egrep and posix-extended. 


### locate

### xargs

## Cartelle

### Creazione nidificata
```
mkdir /tmp/foo/long/path
cd
```
