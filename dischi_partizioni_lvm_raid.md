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
tutto quello che c'è sopra al disco:
```
(parted) mklabel msdos
Warning: The existing disk label on /dev/sdg will be destroyed and all data on
this disk will be lost. Do you want to continue?
Yes/No? Yes
(parted) print free
Model: SanDisk Ultra (scsi)
Disk /dev/sdg: 8004MB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start  End     Size    Type  File system  Flags
        1024B  8004MB  8004MB        Free Space
		
```

### Creazione
Si usa `mkpart`, rispondendo alle domande:
```
(parted) print free
Model: SanDisk Ultra (scsi)
Disk /dev/sdg: 8004MB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start  End     Size    Type  File system  Flags
        1024B  8004MB  8004MB        Free Space

(parted) mkpart 
Partition type?  primary/extended? primary                                
File system type?  [ext2]? fat32                                          
Start? 0%                                                                  
End? 100%
(parted) print                                                            
Model: SanDisk Ultra (scsi)
Disk /dev/sdb: 8004MB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  8004MB  8003MB  primary  fat32        lba
```

### Formattazione
La creazione della partizione non fa si che essa sia automaticamente
formattata; per farlo si usa il set di comandi `mkfs.*`
Per creare un filesystem FAT32, dopo aver installato `dosfstools`
```
mkfs.vfat -F32 /dev/sdg1
```

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
- dischi sorgente sono chiamati physical volume (/dev/sda e /dev/sdb)
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
