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
- shell di login è il primo processo che viene eseguito dall'utente e
  viene utilizzata per impostare diverse variabili/configurazioni
  globali/d'ambiente che saranno disponibili ai processi figli. Nel
  caso di bash legge ed esegue, nell'ordine
  ```
  /etc/profile
  ~/.bash_profile
  ~/.bash_login
  ~/.profile
  ```
  Quando una shell di login esce esegue `~/.bash_logout` (se esiste).
  Una login shell di fatto si ha quando
  - ci si logga per la prima volta in locale o mediante ssh
  - ci si logga con su - (o sudo -)
- shell non di login è quella che tipicamente si ottiene aprendo un
  terminale; esegue nell'ordine
  ```
  /etc/bash.bashrc
  ~/.bashrc
  ```

Spesso però al fine di avere uniformità tra login shell e non-login
shell in `.profile` si fa il source di `.bashrc`.


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
redirige lo stdout di `comando1` allo stdin di `comando2`

## Redirezione
È possibile gestire input e output in modo da farli provenire e finire
in diverse direzioni

```
<  specificare stdin da file

>  stdout su file, sovrascrivendolo
>> stdout su file, in coda

2>  stderr sovrascrive  (es per scrittura su file)
2>> stderr appende

&>  sia stdout che stderr sovrascrive
&>> sia stdout e stderr appende
```

## Lista di comandi
```
comando1 && comando2 && comando3 
comando1 || comando2 || comando3
```
Il:
- primo esegue ogni comando in sequenza, ma al primo ritorno non
  uguale a zero, la catena termina (l'ultimo ad essere eseguito è il
  comando che restituisce non zero;
- secondo esegue ogni comando a turno indipendentemente dall'esito del
  precedente, ma il primo che ritorna un valore pari a 0 termina
  l'esecuzione della catena.

L'exit status in entrambi i casi è l'exit status dell'ultimo comando
eseguito.

## Terminatori di riga o di comando
```
\   spezza un comando e prosegue sulla linea successiva
;   separa dal comando successivo sulla stessa linea
&   esegue il comando in background in una sottoshell
```
