# Bash scripting

## Variabili

### Creazione
Sono stringhe e ve ne sono due tipi:
- le *variabili locali* prime sono disponibili solo nella shell attuale
  e si creano semplicemente mediante 
  ```
  identificatore=contenuto
  ```
  senza spazi (se no bash crede sia un comando); se il `contenuto` ha
  spazi quotarlo mediante ";
  
- le *variabili d'ambiente* vengono rese disponibili anche alle shell
  figlie di quella dove sono definite e vengono definite
  alternativamente come
  ```
  identificatore=contenuto
  export identificatore
  ## oppure
  export identificatore=contenuto
  ```
  È buona norma creare identificatori minuscoli (i maiuscoli sono
  utilizzati dalle variabili d'ambiente impostate dal sistema)

### Listing
Dando due tab dopo
```
echo $
```
vengono listate tutte le variabili attualmente disponibili 
mentre con `printenv` le variabili d'ambiente

### Utilizzo
La sostituzione viene effettuata mediante `$identificatore` nel
comando desiderato

### Rimozione
Per eliminare una variabile
```
unset identificatore
```
Altrimenti verranno eliminate alla chiusura della shell; se si
vuole impostare variabili permanentemente impostarle
in `.profile` o `.bashrc`


## Gestione del flusso

### Esecuzione condizionale (`if` e simili)
Si hanno diversi modi: 
- il costrutto `if`
- la builtin `test`, 
- il costrutto `case`
- gli operatori di parentesi, 

La struttura di un generico **if**:
```
\begin{verbatim}
if [[condizione]]; then 
    comandi
elif [[ condizione2 ]]; then
    comandi
else 
    comandi
fi
```
questo perché if/elif e then sono comandi separati e per esser
posti sulla stessa riga devono essere separati dal punto e virgola.

Un modo equivalente (ma meno efficiente di) è usare **test**:
```
if [[condizione]]
```
è 
```
if test condizione
```

Il **case** è simile allo switch del C:
```
case "$variable" in
 "$var1" )
 command...
 ;;
 "$var2" )
 command...
 ;;
esac
```
Per variabili è necessario quotare perché non viene effettuata la
sostituzione di default



### Loop (`for` e while)

Il **`for`** è costruito così 
```
for arg in lista; do
  commandi con $arg
done
```
Ad ogni passaggio successivo la variabile `$arg` assumerà il valore dell'elemento considerato nella lista.
```
for i in $( ls ); do
     echo item: $i
done
```
Si usa spesso `seq` per creare range numerici
```
for i in `seq 1 10`; do
    echo $i
done 
```

La sintassi del **`while`** è
```
while [[ condizione ]]; do
 commandi
done
```

**`break`** e **`continue`** funzionano come di consueto: il primo fa
uscire dal loop (`for` o `while`), il secondo fa saltare
all'iterazione successiva.









## Restituzione di valori
Sia funzioni che script possono ritornare al chiamante mediante `exit`
- tipicamente 0 se comando/funzione eseguiti con successo
- 1 o maggiori in caso di errore



## Funzioni

### Definizione
Vi sono due sintassi
``` bash
# sintassi 1
function function_name {
comandi
}

# sintassi 2 - più portabile
function_name () {
comandi
}
```
In entrambi i casi la seconda graffa deve esser posta su una riga a
se:
- eventuali argomenti sono disponibili all'interno attraverso i
  parametri di posizione `$1`, `$2`
- la restituzione di valori avviene mediante `exit` (equivalente di
  return di altri linguaggi)


### Chiamata
Si fa semplicemente
```
function_name
```






## Scripting

### Incipit del file
Uno script bash inizia con
```
#!/bin/bash
```
o, per maggiore portabilità sui sistemi Unix
```
#!/usr/bin/env bash
```

### Parametri di posizione
sono variabili speciali creati/associati all'esecuzione di uno script
- `$0` è il nome con cui è stato chiamato lo script
- `$1` è il primo parametro, `$2` il secondo


### Caricare altri file
Ipotizzando di aver definito variabili o funzioni in un file, per
caricarne i valori e poterle utilizzare si comanda alternativamente:
```
source file_path
. file_path
```
