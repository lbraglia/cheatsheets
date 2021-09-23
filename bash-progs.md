# Utilities da shell


## cat
Concatena file

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

## sed
Sed è un comando per l'editing in streaming. Il formato è 
```
sed 's/to_be_replaced/replaced/g' 
```
un esempio
```
ls -l | sed 's/[aeio]/u/g'
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



