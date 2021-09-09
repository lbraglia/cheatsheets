# ISO e masterizzazione

## File `.iso`

### Creazione a partire da un cdrom
```
dd if=/dev/cdrom of=file.iso
```
### Creazione con path del filesystem
```
genisoimage -v -J -r -V ETICHETTA_DISCO -o file.iso path1 path2 ...
```
con:
- `-J` da usare se i dischi devono essere leggibili su Windows
- `-r` per ritenere (mediante Rock Ridge) le proprietà POSIX dei
  file (possessore, permessi etc)
- `-v` per la verbosità e `-V` per l'eventuale etichetta

### Listing del contenuto
```
isoinfo -l -i file.iso
```
### Estrazione di un file
```
isoinfo -x /path/in/minuscolo.txt -i file.iso > file.txt
```
Il file viene estratto sullo stdout

## Mounting
Per montare una iso con i privilegi di root
```
mkdir /tmp/mioiso
mount -o loop -t iso9660 file.iso /tmp/mioiso
```
Per farlo senza i privilegi occorre installare `archivemount` che permette di montare file compressi e archivi; poi
```
archivemount file.iso /tmp/mioiso   # montare
fuserumount -u /tmp/mioiso          # smontare
```

## Masterizzazione

### Ricerca unità
```
xorriso -devices
```

### Scrittura
```
xorriso -as cdrecord  -v dev=/dev/sr0 -dao my.iso
```
