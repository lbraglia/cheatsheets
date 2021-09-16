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


## Integrità dei filesystem

### Controllo automatico
Ad ogni montaggio di una partizione/filesystem un contatore viene
incrementato. Si può impostare che un controllo automatico avvenga
ogni tot montaggi.

In fstab il controllo automatico è abilitato se la sesta colonna
(pass) ha un numero diverso da 0. Questo campo viene usato da `fsck`
per determinare l'ordine di verifica dei file system in fase di
avvio. Il file system root dovrebbe essere specificato con 1, mentre
altri con valori pari a 2 (file system nello stesso disco verranno
verificati in sequenza, mentre file system su dischi diversi verranno
verificati parallelamente)
```
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
UUID=9cf52461-2e6c-4f62-bd74-75c19575a71b / ext4 errors=remount-ro 0 1
UUID=2150130e-761f-42b8-9776-36f3679e100e none swap sw 0 0
```
Se abilitata la funzione di check in `fstab`, il filesystem viene
controllato ogni tot montaggi. Per controllare ogni quanto, su fs ext si usa
(verificato con `df -hT` che la partizione di root è `/dev/sda1`)
```
# tune2fs -l /dev/sda1 # varie info
# tune2fs -l /dev/sda1 | grep -i "maximum mount count"
Maximum mount count:      -1
```
Se `-1` il check automatico è disabilitato; per impostare un
valore custom (sfruttando l'UUID stavolta)
```
# tune2fs -c 20 /dev/sda1 
tune2fs 1.46.2 (28-Feb-2021)
Impostazione del numero massimo di mount a 20
```

### Controllo manuale
Avviene mediante `fsck` (che wrappa tanti altri eseguibili specifici
per filesystem) su partizioni non montate (o montate in sola lettura)
```
fsck.vfat /dev/sdb1
```

