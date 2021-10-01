# Processi

## Listing: `ps`
`ps -elf` lista i processi di tutti gli utenti e nello specifico, tra
le altre cose:
- `UID` utente
- `PID` id del processo
- `PPID` id del processo genitore
- `PRI` valore di priorità (più alto e minore è la priorità)
- `NI` valore di niceness (influenza la priorità)
- `STIME` ora di inizio
- `TIME` tempo di utilizzo della cpu
- `CMD` comando

Per il monitoraggio interattivo utilizzare `top`:
- digitare `F` per muoversi con le frecce e abilitare/disabilitare
  voci con la barra spaziatrice; `s` per selezionare il criterio di
  sorting delle righe; quando si ha finito `q` per passare alla
  visualizzazione
- `R` per cambiare l'ordinamento (dal maggiore al minore o viceversa)
- `h` per l'help

## Killing
Per individuare il `PID`
```
ps -ef |grep nome
kill PID     # da l'indicazione di terminare al processo (SIGTERM)
kill -9 PID  # termina il processo (SIGKILL)
```
Per cancellare diversi processi che utilizzando lo stesso eseguibile
```
killall firefox  # termina tutti i processi di firefox
```


## Eseguire/gestire processi in background
Per:
- eseguire un processo in background porre `&` al termine del comando
  ```
  l@m740n:~$ comando_random &
  [1] 9834
  ```
  viene restituito il numero del job e il pid del processo.
- per listare i job in background e il loro stato attuale
  ```
  jobs
  ```
- per riportare a terminale un job posto in background si utilizza `fg
  numero_job` ad esempio
  ```
  fg 1
  ```
- per stoppare un processo/comando che sta occupando la shell  utilizzare 
  ```
  Ctrl + Z
  ```
  (mentre `Ctrl + C` lo termina proprio)
  Questo libera la shell ma lascia il processo stoppato (e in background)
- per far ripartire il processo stoppato (tenendolo in background)
  ```
  bg 1
  ```
  Es si può controllare con jobs che il processo è running


## `nohup`
Premesso al comando evita di stopparsi in seguito a segnali HUP che
tipicamente vengono dati quando il programma viene eseguito da un
terminale/shell che viene chiuso. Questo ha due applicazioni principalmente
- evita che 
  ```
  nohup k3b
  ```
- evita che un processo lungo sia stoppato quando spegniamo il sistema
  ```
  nohup comando_lento
  ```

## Niceness e priorità di esecuzione

La *nice*ness è quanto un processo è "gentile": va da -20 a +19 con
-20 che indica poco gentile (e si prende tutta la CPU) mentre +19 è
molto gentile e condivide di più il tempo di CPU con i processi che ne
bisognano

### Listing
`ps -l` lista le colonne `PRI` (priority) e `NI` (nice)


### Eseguire un comando con nice
```
nice -n 5 firefox
```

Gli utenti normali possono lanciare processi con nice da 0 (default) a
19 valore più basso (quindi gli utenti normali possono solo rallentare
un programma rispetto al default)


### modificare la niceness
Si può solo aumentare la niceness una volta che il processo è iniziato
(non diminuirla)
```
renice -n nuovo_valore pid_processo
```
Per farlo in `top`, una volta fatto partire digitare `r` e specificare
il pid


