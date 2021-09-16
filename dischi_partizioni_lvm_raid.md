# Dischi, Partizioni, LVM, RAID

## Dischi e partizioni

### Listing 
Per listare dischi, partizioni e file system 
```
parted -l
```
Dopodiché si può entrare nel disco considerato (il che diminuisce la possibilità di errori da linea di comando) con
```
parted /dev/sdg
```
dopodiché comandare `help` per la lista comandi
o `help comando` per info sullo stesso.

In qualsiasi momento per vedere lo status delle partizioni (similmente a quanto fatto da fuori `parted`):
```
print       # solo le partizioni
print free  # anche lo spazio libero
```

### Creazione nuova tabella delle partizioni
Partiamo dal creare una nuova tabella delle partizioni, rasando al suolo
tutto quello che c'è sopra al disco.

Se vogliamo:
- creare un sistema classico con MBR utilizziamo `mklabel msdos`: 
  supporta fino a 4 partizioni primarie e se vogliamo piu partizioni
  dobbiamo rendere una di queste estesa (accrocchio non più
  necessario), supporta dischi non più grandi di 2TB
- creare una tabella di nuova generazione, GPT, `mklabel gpt`:
  supporta fino a 128 partizioni primarie (e tanti altri benefit)

In entrambi i casi tutto ciò che c'è sul disco verrà cancellato.
```
(parted) print
Model: SanDisk Ultra (scsi)
Disk /dev/sdb: 8004MB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  8004MB  8003MB  primary  fat32        lba
 
(parted) mklabel
New disk label type? gpt
Warning: The existing disk label on /dev/sdb will be destroyed and all data on
this disk will be lost. Do you want to continue?
Yes/No? Yes
(parted) print
Model: SanDisk Ultra (scsi)
Disk /dev/sdb: 8004MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start  End  Size  File system  Name  Flags
```

### Creazione partizione
Si usa `mkpart`, rispondendo alle domande (il filesystem specificato
qui non sembra avere particolare importanza, sarà determinato
soprattutto in sede di formattazione, qui è più che altro importante
la dimensione specificata)

```
(parted) mkpart 
File system type?  [ext2]? fat32
Start? 0%
End? 100%
(parted) print
Model: SanDisk Ultra (scsi)
Disk /dev/sdb: 8004MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  8004MB  8003MB  primary  fat32        lba
```

### Formattazione
La creazione della partizione non fa si che essa sia automaticamente
formattata; per farlo si usa il set di comandi `mkfs.*`.

In ambito **Windows** alcune note su FAT:
- `FAT32` è il filesystem più diffuso nei sistemi di memorizzazione di
  piccola taglia (USB), leggibile/scrivibile da tutti i sistemi
  operativi senza grossi problemi, ma ha limitazioni (file di dimensione
  massima di 4GB, soggetto a frammentazione e degradamento
  prestazioni). Gli strumenti per gestirle sono in `dosfstools`.
- `exFAT` risolve queste limitazioni (gli strumenti per
  gestirle sono in `exfat-fuse` ed `exfat-utils`)

Per creare un filesystem FAT
```
mkfs.vfat -F32 /dev/sdg1 #FAT32
mkfs.exfat /dev/sdg1
```

In ambito **UNIX**
[`btrfs`](https://wiki.debian.org/Btrfs) è un
filesystem avanzato (ancora in sviluppo) che fornisce feature come:
- supporto nativo per RAID
- compressione zlib
- snapshot
- conversione diretta da ext4

### Eliminazione
Ipotizzando di dover cancellare la prima partizione (`/dev/sdb1`) 
dopo `parted /dev/sdb`
```
(parted) rm 1
```


## LVM
Software/configurazione che permette di fare apparire più dischi
fisici come un'unica unità virtuale (es si monta solo quella)
permettendo maggiore flessibilità/comodità nel ri-dimensionamento in
aggiunta

Terminologia:
- dischi sorgente sono chiamati physical volume (`/dev/sda` e `/dev/sdb`)
- aggregato dei dischi (es data, aggregato di sda e sdb, verrà
  visto come disco)
- logical volume sono i dischi virtuali basati sull'aggregato (es
  video, web, doc sono visti come normali partizioni di data); si può
  specificare ovviamente la dimensione di ciascuno

Vantaggi:
- se un domani ho bisogno di più spazio aggiungo un physical volume e lo
  configuro come facente parte di data e alloco il relativo spazio al
  logical volume che mi interessa
- è possibile spostare i dati a sistema avviato: i dati su un disco
  fisico possono essere spostati su un altro facente parte del volume
  group senza interrompere il servizio (es se si vuole sostituire un
  disco fisico)
- velocità di trasferimento incrementano perché si scrive in parallelo 
  su più dischi (stripe come nel raid 0 su due o più dischi)

Per la pratica Morro, LPI - Exam 101, 25.102.1
