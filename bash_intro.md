# bash

## Scelta della shell
Alcuni file generali sulle shell:
- `/etc/shells` lista tutte le shell conosciute dal sistema
- per spostarcisi momentaneamente basta comandarla, es `zsh`
- la shell di login di ogni utente è memorizzata in `/etc/passwd`, 
  ma per impostarla utilizzare `chsh`, ad esempio
  ```
  chsh -s /usr/bin/zsh
  ```
  chsh modifica `/etc/passwd` anche se non si è root (setuiddato con root)

## Shell di login e non, file di configurazione
Una: 
- **shell di login** è il primo processo che viene eseguito dall'utente e
  viene utilizzata per impostare diverse variabili/configurazioni
  globali/d'ambiente che saranno disponibili ai processi figli. 
  Una shell di login di fatto si ha quando
  - ci si logga per la prima volta in locale o mediante ssh
  - ci si logga con su - (o sudo -)
  Nel caso di bash i file di configurazione sono
  ```
  /etc/profile
  ~/.bash_profile
  ~/.bash_login
  ~/.profile
  ```
  nello specifico bash prima legge ed esegue comandi da `/etc/profile`
  se esiste; dopodiché esegue comandi dal primo di
  `~/.bash_profile`, `~/.bash_login`, e
  `~/.profile` in quest'ordine.
  Quando una shell di login esce esegue `~/.bash_logout` (se esiste).
- **shell non di login** è quella che tipicamente si ottiene aprendo un
  terminale; esegue nell'ordine
  ```
  /etc/bash.bashrc
  ~/.bashrc
  ```

Spesso però al fine di avere **uniformità** tra login shell e non-login
shell in `.profile` si fa il source di `.bashrc` e si modifica
quest'ultimo. Questo anche perché non è detto che il `.profile` sia
valutato (es login/display manager grafico)


## Scheletro configurazioni 
In `/etc/skel` è posto uno scheletro di configurazione di file e cartelle
della home di ogni utente (utile es in  contesti aziendali):
```
l@m740n:~$ ls -la /etc/skel/
totale 28
drwxr-xr-x   2 root root  4096 30 ago 10.44 .
drwxr-xr-x 155 root root 12288  1 ott 07.56 ..
-rw-r--r--   1 root root   220 15 mag  2017 .bash_logout
-rw-r--r--   1 root root  3526 15 mag  2017 .bashrc
-rw-r--r--   1 root root   807 18 apr  2019 .profile
```
Quindi se ad esempio si vogliono aggiungere/modificare file di
configurazioni o directory procedere la.


## Opzioni di bash (set/shopt)
Il listing si ottiene con `set +o`
```
l@m740n:~$ set +o
set +o allexport
set -o braceexpand
set -o emacs
set +o errexit
```
quando vi è il + significa che l'impostazione è disattivata, mentre se c'è il -
è attiva: per maggiori informazioni sulle opzioni disponibili vedere 
`help set`, ad esempio per impostare che tutte le variabili create siano esportate per le shell figlie
```
set -o allexport
```
Altre opzioni sono disponibili in `shopt`

## Alias

### Definizione
```
alias dataset="echo dataset_$(date +'%Y_%m_%d')"
```

### Rimozione
```
unalias dataset
```
Anche gli alias valgono solo per la sessione corrente 
quindi impostarli in `.profile` o `.bashrc`


## history
Si interroga mediante `history` mentre se:
- voglio rieseguire un comando `!#_comando`
- voglio utilizzare un parametro dato nell'ultimo comando uso `!$`
  ```
  mkdir /tmp/test
  cd !$
  ```
- per rilanciare l'ultimo comando eseguito `!!`
- per lanciare l'ultimo comando che inizia con una stringa
  ```
  !apt
  ```
- per effettuare una ricerca all'interno della history
  - `Ctrl+R` 
  - digitare la stringa, viene restituita l'ultima occorrenza che matcha
  - ridare `Ctrl+R` per scorrere le altre che matchano fino a trovare 
	la desiderata
  - `Invio` per eseguire il comando scelto oppure `Esc` per modificare 
	la ricerca usandola come punto di partenza
- per pulire la history, `history -c`
- per evitare che un comando finisca in history iniziarlo con uno spazio
  ```
  $: asd <- finisce in history 
  $:  asd <- no
  ```

## Caratteri speciali e quoting
```
#          commento
`comando`  sostituisce l'output dato comando nella linea di bash
$(comando) sostituisce l'output dato comando nella linea di bash
$variabile sostituisce la variabile nella linea di bash
\          andare a capo senza interrompere il comando 
\          il carattere che lo segue viene preso alla lettera (es spazio, 
	       no altro parametro)
*          uno o più caratteri qualsiasi in un nome di un file/percorso
?          un carattere qualsiasi
[]         uno qualsiasi dei caratteri inclusi tra parentesi
```
Il quoting con apici singoli serve per stringhe che si voglion tenere
assieme in presenza di spazi (non effettua sostituzioni di variabili
ed è il massimo del safe); con apici doppi effettua la sostituzione
```
l@m740n:~$ echo 'ciao $USER'
ciao $USER
l@m740n:~$ echo "ciao $USER"
ciao l
```

## stdin, stdout, stderr
Lo standard:
- input è l'input fornito dall'utente (tastiera)
- output è l'output di un certo programma
- error è l'output di errore eventualmente derivante
  dall'esecuzione di un comando che non va a buon fine. 
  Stampato a video come lo standard output non è bufferizzato.

## pipe
```
comando1 | comando2
```
redirige lo stdout di `comando1` allo stdin di `comando2`.
Vediamo alcuni comandi comodi

### tee
Stampa a video il risultato ricevuto da stdin e lo salva anche su file
```
ls -l | tee unsorted.txt | sort -r -k9 | tee sorted-rev.txt
```
salverà in unsorted e sorted i contenuti ordinati
o meno per nome del file (oltre a stamparne il contenuto a
video dell'ultimo che non essendo redirezionato non viene salvato)

### xargs
prende dallo standard input i valori passati come se fossero parametri
di un comando ed esegue un comando specificato (di default echo) con i
parametri passati.

Di default effettua l'echo
```
l@m740n:~$ echo {1..9} | xargs
1 2 3 4 5 6 7 8 9
```
Possiamo dirgli di processare anche di gestire tot parametri alla volta
ed eseguire il comando sui tot
```
l@m740n:~$ echo {1..9} | xargs -n 3
1 2 3
4 5 6
7 8 9
```
Per utilizzarlo su un comando si procede come segue (facciamo il tar dei 
file `.c`):
```
ls *.c | xargs tar cvjf asd.tar.bz
```


## Redirezione
È possibile gestire input e output in modo da farli provenire e finire
in diverse direzioni

```
<    specificare stdin da file
<<<  here string: stdin da stringa

>  redirige stdout su file, sovrascrivendolo
>> accoda stdout su file

2>  redirige stderr sovrascrive
2>> appende stderr su file

&>  redirige sia stdout che stderr su un file, sovrascrivendolo
&>> sia stdout e stderr appende
```
Es per prendere da input e redirigere stdout e stderr su file diversi
```
comando < file_input > file_risultati 2> file_errori
```
Spesso si usa `2> /dev/null` per sopprimere gli errori.

L'operatore `<<<` serve per prendere in input da una stringa invece
che da file: es
```
xargs -n1 <<< "testo1 testo2 testo3"
```
invece di (e notando le virgolette manganti)
```
echo testo1 testo2 testo3 | xargs -n1
```

## Lista di comandi
```
comando1 ; comando2 ; comando3 
comando1 && comando2 && comando3 
comando1 || comando2 || comando3
```
Il:
- primo esegue tutti i comandi in sequenza
- secondo esegue ogni comando in sequenza se il precedente non è fallito 
  (l'ultimo ad essere eseguito è il comando che restituisce non zero);
- terzo esegue ogni comando a turno indipendentemente dall'esito del
  precedente; il primo che termina correttamente (ritorna un valore pari a 0)
  termina l'esecuzione della catena.

L'exit status in entrambi i casi è l'exit status dell'ultimo comando
eseguito.



## Terminatori di riga o di comando
```
\   spezza un comando e prosegue sulla linea successiva
;   separa dal comando successivo sulla stessa linea
&   esegue il comando in background in una sottoshell
```


## Esecuzione in background
Se un processo sta occupando la shell e ne abbiamo bisogno momentaneamente:
- dare `Ctrl+Z` per porre il processo in background
- utilizzare la shell per altro
- comandare `bg 1` per rimettere a schermo il processo posto in background

Per la lista dei processi in esecuzione in background comandare `jobs`
(dal quale si ricava l'id numerico diverso da 1, nel caso di
molteplici processi in background)


