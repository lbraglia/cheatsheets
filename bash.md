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
  
## File e configurazioni di Bash
I file principali per la configurazione di bash:
- `/etc/profile`: eseguito in fase di login
- `~/.bash_profile`: come sopra
- `~/.bashrc`: eseguito all’avvio della shell
- `~/.bash_logout`: eseguito al logout
- `~/.bash_history`: contiene la history


## Caratteri speciali
```
#          commento
`comando`  sostituisce l'output dato comando nella linea di bash
$(comando) sostituisce l'output dato comando nella linea di bash
$variabile sostituisce la variabile nella linea di bash
\          andare a capo senza interrompere il comando 
\          il carattere che lo segue viene preso alla lettera
*          uno o più caratteri qualsiasi in un nome di un file/percorso
?          un carattere qualsiasi
[]         uno qualsiasi dei caratteri inclusi tra parentesi
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

## Variabili
Sono stringhe e ve ne sono due tipi, locali e d'ambiente:
- le prime sono disponibili solo nella shell attuale e si creano
  semplicemente mediante ```identificatore=contenuto``` senza spazi
  (se no bash crede sia un comando); se il `contenuto` ha spazi
  quotarlo mediante ";
  
- le seconde vengono rese disponibili anche alle shell figlie di quella 
  dove sono definite e vengono definite alternativamente come
  ```
  identificatore=contenuto
  export identificatore
  ## oppure
  export identificatore=contenuto
  ```
	È buona norma creare identificatori minuscoli (i maiuscoli sono
    utilizzati dalle variabili d'ambiente impostate dal sistema)

Dando due tab dopo
```
echo $
```
vengono listate tutte le variabili attualmente disponibili.
Per eliminare una variabile
```
unset identificatore
```
