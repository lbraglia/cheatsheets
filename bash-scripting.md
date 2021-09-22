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

### Esecuzione condizionale: `if`/`test`, `case` 
Si hanno diversi modi: 
- il costrutto `if` (e `test`)
- il costrutto `case`

Formalmente la struttura di un generico **if**:
```
if COMANDI; then COMANDI; [ elif COMANDI; then COMANDI; ]... [ else COMANDI; ] fi
```
Viene eseguito l'elenco dei COMANDI che fungono da condizione e se lo
stato di uscita è 0 viene eseguito il blocco then; come valore di uscita 
restituisce lo stato dell'ultimo comando eseguito. Spesso si trova
riadattato come
```
\begin{verbatim}
if [[ condizione ]]; then 
    comandi
elif [[ condizione2 ]]; then
    comandi
else 
    comandi
fi
```
dove:
- è importante che dentro parentesi ci sia uno spazio bianco all'inizio e 
  uno alla fine;
- di fatto bash sostituisce `[[ condizione ]]` al comando `test
  condizione`; spesso è quindi la builtin `test` che effettua le
  comparazioni quindi rifarsi al suo help per vedere i test
  disponibili;
- non si pone punto e virgola dopo comandi posti sulla stessa riga
  devono essere separati dal punto e virgola.
- non si pone punto e virgola dopo `comandi` dato che l'`elif`, l'`else` e il `fi` sono su un'altra

È possibile nidificare gli if come:
```
if [[condizione]]; then
   if [[condizione]]; then
      comando
   fi
else
   comando
fi
```



Il **case** è simile allo switch del C; formalmente 
```
case PAROLA in [MODELLO [| MODELLO]...) COMANDI ;;]... esac
```
Esegue in modo selettivo COMANDI basati sulla PAROLA corrispondente al MODELLO
e restituisce lo stato dell'ultimo comando eseguito; spesso riparafrasato 
come segue:
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

### Input dall'utente
\subsection{Prendere in input dall'utente}
Utilizzare read
\begin{verbatim}
echo Please, enter your name
read NAME
echo "Hi $NAME!"
\end{verbatim}
o per prendere più input nella stessa linea
\begin{verbatim}
echo Please, enter your firstname and lastname
read FN LN 
echo "Hi! $LN, $FN !"
\end{verbatim}


\subsection{Here documents}
Sono un modo di programmare la shell per ottenere un effetto
simile a
\begin{verbatim}
programma < file_di_comandi
\end{verbatim}
dove a un programma (es ftp) viene passato in stdin una serie di
comandi da effettuare che sono contenuti in un file. Il fatto è
che prima bisogna definire tali comandi in apposito file e il
funzionamento dello script dipende dall'esistenza e la
correttezza di tale file.\\
Mediante l'here document si specificano i comandi all'interno
della sintassi di bash e poi si passano gli stessi al comando
speicficato. La sintassi è
\begin{verbatim}
programma << EOF
comando1
comando2
...
EOF
\end{verbatim}
Al posto di EOF ci può essere qualsiasi cosa: i due delimitatori
(EOF in questo caso) conterranno i comandi che saranno passati al
programma.

Come nelle altre parti degli script vi è sostituzione delle
variabili con il loro contenuto.

