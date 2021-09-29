# Processi

## Processi in background
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
