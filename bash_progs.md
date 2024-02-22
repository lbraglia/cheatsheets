# Utilities da shell

## cat e famiglia (zcat, bzcat, xzcat)
Concatena file; le varianti servono per preprocessare le compressioni
dei file di testo da visualizzare

## wc
```
wc file.txt    # conta linee, parole, bytes di un file di testo

wc -l file.txt # linee
wc -w file.txt # parole
wc -c file.txt # bytes
wc -L file.txt # lunghezza linea più lunga in caratteri
```

## split
Fa l'inverso di `cat` e divide un file in molteplici file ciascuno con al 
max tot righe. Ad esempio per dividere un file di 5000
righe in 10 da 500 righe 
```
l@m740n:~$ for l in $(seq 5000); do
> echo "linea $l" >> file.txt
> done
l@m740n:~$ split file.txt -l 500 splitted_
l@m740n:~$ ls splitted_*
splitted_aa  splitted_ac  splitted_ae  splitted_ag  splitted_ai
splitted_ab  splitted_ad  splitted_af  splitted_ah  splitted_aj
```
split può anche splittare in base a tot byte mediante `-b` (quindi 
es si presta anche a file binari (che potranno essere rimessi assieme
con `cat`)
```
l@m740n:~$ l modulo.pdf 
-rw-r--r-- 1 l l 54K 21 set 11.15 modulo.pdf
l@m740n:~$ split -b 10000 modulo.pdf modulo_spl_
l@m740n:~$ ls -l modulo_spl_a*
-rw-r--r-- 1 l l 10000 23 set 09.20 modulo_spl_aa
-rw-r--r-- 1 l l 10000 23 set 09.20 modulo_spl_ab
-rw-r--r-- 1 l l 10000 23 set 09.20 modulo_spl_ac
-rw-r--r-- 1 l l 10000 23 set 09.20 modulo_spl_ad
-rw-r--r-- 1 l l 10000 23 set 09.20 modulo_spl_ae
-rw-r--r-- 1 l l  4345 23 set 09.20 modulo_spl_af
```

## tr
Sta per translate ed è un recoder per caratteri. Ad esempio 
- per sostituire un carattere r con s
  ```
  cat test.txt | tr 'r' 's'
  ```
- per eliminare i caratteri r ed s
  ```
  cat test.txt | tr -d 'rs'
  ```
- per tenere solo qualcosa si fa il complementare, es per tenere solo r ed s
  ```
  cat test.txt | tr -dc 'rs'
  ```
  per tenere solo i caratteri stampabili (es non gli a capo):
  ```
  cat test.txt | tr -dc [:print:]
  ```
- per fare l'upcase di un file
  ```
  cat test.txt | tr [:lower:] [:upper:] 
  ```

## cut
serve per estrarre testo da un file/stdin

```
# Estrazione di colonne
cut -c 12-15 file.txt    # estrae dalla 12a alla 15a colonna
cut -c 12- file.txt      # estrae dalla 12a colonna alla fine
cut -c "-12" file.txt      # estrae fino alla 12a colonna

# Estrazione da un file con delimitatore
cut -d ',' -f 2 file.csv  # stampa secondo campo (colonna) di un csv
cut -d ',' -f 2,4 file.csv  # stampa secondo campo (colonna) di un csv
```
Altre opzioni interessanti sono
- `--output-deliter=';'` assieme a -d e selezione multipla di
  campi, per sostituire il delimitatore dei campi nell'output;
- `-s` (in aggiunta a `-d`) che stampa solo se il carattere di
  delimitazione è trovato nella riga);
- `--complement` (stampa tutto ad eccezione della selezione
  specificata).

## paste
Serve per incollare righe di diversi file o di un unico file (in questo caso crea su unica riga da molteplici), utilizzando come delimitatore di default il tab. Se `test.txt` è 
```
asd
foo
bar
```
e `test2.txt`
```
baz
poi
hoy
```
si ha
```
l@m740n:~$ paste test.txt test2.txt 
asd  baz
foo  poi
bar  hoy
l@m740n:~$ paste -s -d ' ' test.txt
asd foo bar
l@m740n:~$ cat test.txt test2.txt | paste - - -     
asd  foo  bar 
baz  poi  hoy
```
tre trattini significa fai tre colonne nell'output

## fmt
Serve a wrappare, non spezzando parole un file di testo
```
cat file.txt | fmw -w 72
```

## pr
Serve per preprocessare un file di testo da inviare a stampa: aggiunge
intestazione e spezza per far si che sia leggibile in stampa
```
pr file.txt | lp- 
```
Utile soprattutto per file lunghi


## sort
Serve per ordinare secondo diversi criteri linee di testo

```
du -s * | sort -n           # ordina per dimensione file/cartelle di .
cat elenco.txt | sort -k 2  # ordina elenco Cognome, Nome Tel sulla base di Nome
```

## uniq
Elimina righe adiacenti duplicate; pertanto quasi sempre utilizzato
con `sort` per mettere tutte le righe simili vicine.


## sed
Sed è un comando per l'editing in streaming. Il formato è 
```
sed 's/to_be_replaced/replaced/g' 
```
un esempio
```
ls -l | sed 's/[aeio]/u/g'
```
Sostituire una parola in tutti i file in una directory
```
sed -i -- 's/{absabs}/{norm}/g' */*/*
```
  
## awk
Ricerca un pattern e poi svolge l'azione specificata.
Se ad esempio abbiamo un file `/tmp/dummy` con:
```
test123
test
tteesstt
```
e comandiamo
```
awk '/test/ {print}' /tmp/dummy
```
awk restituisce
```
test123 
test
```



