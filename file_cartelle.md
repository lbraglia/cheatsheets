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

<!-- Per brevità considereremo come file il file vero e proprio, la -->
<!-- direcory, il link simbolico ed ogni cosa abbia una "directory -->
<!-- entry" ossia un nome.  L'albero di una directory consiste nel suo -->
<!-- contenuto e nel contenuto delle sottodirectory. -->

<!-- I programmi sopra elencati permettono di cercare files in una o -->
<!-- più alberi di directory che: -->
<!-- - presentano nomi che contengono un certo testo o rispettano un -->
<!--   determinato pattern -->
<!-- - sono link a determinati file -->
<!-- - si trovano all'interno di un determinato range di grandezza del file -->
<!-- - sono stati utilizzati durante un certo periodo di tempo -->
<!-- - sono di un certo tipo (file regolari directory, link) -->
<!-- - sono di proprietà di un certo soggetto o di un determinato gruppo -->
<!-- - hanno determinati permess -->
<!-- - contengono testo che rispetta un determinato pattern -->
<!-- - si trovano ad un certo livello di profondità nell'albero della -->
<!--   directory -->
<!-- - una combinazione dei criteri precedenti -->

### find
Cerca nell'albero di directory specificato vi sono file o cartelle che
rispettano il pattern fornito, dopodichè ne printa il path allo
stdout.

```
l@m740n:~$ find -name asd
./.doc/todo/asd
./asd
l@m740n:~$ find -name BRG*
./.doc/dichiarazione_redditi/2021/BRGLCU83S04H223C.pdf
./.doc/dichiarazione_redditi/2020/BRGLCU83S04H223C.pdf
./.doc/dichiarazione_redditi/2020/BRGRNI27M11H223Z.pdf
```
ha la sintassi (semplificata)
```
   find [-H] [-L] [-P] [paths] [espressione]
```
con:
- H,L e P per il trattamento dei link simbolici (`P`, il default, non
  segue il link stampando info del file linkato ma del link stesso;
  `L` segue il link quindi stampa info del file linkato)
- paths dove effettuare la ricerca (default  `.`)
- espressione espressione può essere formata da: operatori,
  opzioni, test e azioni. L'azione di default è `-print`, che consiste nel
  stampare a terminale i file che rispettano il criterio di ricerca.

Le **opzioni** riguardano il comportamento nella ricerca; per chiarezza è
meglio porle all'inizio dell'espressione. Alcune utili: 
-`maxdepth numero`: scendi nella ricerca al massimo a n sottolivelli
  della directory. Se numero = 1 cerca solo nella dir corrente, se 0
  ci si chiede se il nome della dir corrente rispetta il pattern;
-`mindepth numero`: non processa niente che sia almeno nel sottolivello n;
-`mount`: non discende in directory su altri filesystem montati;
- `noleaf`: opzione necessaria quando si cerca in cdrom, msdos
  filesystem e in filesystem non Unix. Nei filesystem UNIX vi sono per
  ogni cartella due link (. e ..), pertanto per sapere se ci sono
  sottocartelle in una cartella basta contare hard link -2 (). Viceversa
  i fs non unix non hanno questi 2 hard link quindi per determinare se
  vi sono file o cartelle non bisogna fare il -2;
- `regextype` tipo: cambia la sintassi date a `-regex` o `-iregex` da
  `emacs` (default) al tipo specificato (`find -regextype help`).

Alcuni test:
- `-name pattern`: matcha nomi file con globbing (`iname` per case insensitive)
- `-regex pattern`: matcha nomi file con regex (`iregex` per case insensitive)

Azioni:
- `-print` (default), stampa il path seguito da newline
- `-exec comando` esegue
- `-delete` rimuove il file

### locate

### xargs

## Cartelle

### Creazione nidificata
```
mkdir /tmp/foo/long/path
cd
```
