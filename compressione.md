# Compressione

I pacchetti fondamentali sono `rar unrar zip unzip bzip2 gzip`.

## tar, gz e bz
Alla compressione è tipicamente preceduta la creazione di un archivio
(accorpare più file in un unico) mediante `tar`; si usa quest'ultimo
per orchestrare il tutto:
- `t` serve per listare `x` per estrarre `c` per creare;
- `v` per aggiungere verbosità/info sui file ma è opzionale; 
- `z` per la compressione `gzip`, `j` per la `bzip2` (più recente,
  potente e lenta);
- `f` per iniziare la specifica di file e cartelle.

```
## Ottenere info sul contenuto
tar tvf  file.tar
tar tvzf file.tar.gz
tar tvjf file.tar.bz2

## Estrazione/Decompressione
tar xvf archivio.tar
tar xvzf archivio.tar.gz
tar xvjf archivio.tar.bz2

## Creazione di archivio
tar cvf file.tar file1 file2 cartella ..
## Creazione di archivio e compressione
tar cvzf file.tar.gz file1 file2 cartella ..
tar cvjf file.tar.bz2 file1 file2 cartella ..
```

## zip

```
## Ottenere info su contenuto
zipinfo file.zip

## Decompressione (tutto)
unzip file.zip
## Decomprimere solo alcuni file
unzip file.zip long/long/long/path quite/long/path2
## Solo alcuni file, nella directory corrente, senza ricreare il path
unzip -j file.zip long/long/long/path quite/long/path2

## Compressione di file
zip disney.zip pippo.txt pluto.txt paperino.txt
## Compressione di file e cartelle
zip -r disney.zip pippo.txt paperopoli topolinia
```

## rar
```
## Listare contenuto 
unrar l file.rar

## Decompressione
unrar e file.rar    # tutto nella directory corrente
unrar x file.rar    # ricrea i path

## Compressione
rar file.rar file1 file2 cartella
```



