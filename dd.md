# dd

Che sta per data duplicator copia (in modalità grezza) da file su
file.  Tenendo conto che quando si va in lettura/scrittura su dischi
occorrono i privilegi di amministrazione ( o fare parte del gruppo
`disk`), alcuni esempi a seguire:
- creare un file vuoto (di zeri) di 1kb
  ```
  dd if=/dev/zero of=zeri.dat bs=1024 count=1
  ```
  si nota che definiamo la dimensione dei blocchi con `bs` (1024 byte
  ossia un kb) e quanti blocchi copiare con count. Si possono
  specificare i bs con altre unità (es per ottenere lo stesso potevamo
  fare `bs=1K` o per i megabyte `bs=1M`)
- eliminare in maniera sicura (sovrascrivendolo) un file e poi 
  eliminandolo con `rm`
  ```
  l@m740n:~/dd_test$ unalias ls
  l@m740n:~/dd_test$ ls -l
  totale 1060
  -rw-r--r-- 1 l l 1083944 23 set 13.31 file.pdf
  l@m740n:~/dd_test$ dd if=/dev/urandom of=file.pdf bs=1083944 count=1
  1+0 record dentro
  1+0 record fuori
  1083944 bytes (1,1 MB, 1,0 MiB) copied, 0,00955853 s, 113 MB/s
  l@m740n:~/dd_test$ xpdf file.pdf 
  Syntax Warning: May not be a PDF file (continuing anyway)
  Syntax Error (136): Illegal character '{'
  l@m740n:~/dd_test$ rm file.pdf 
  ```
  così anche se dovessimo recuperare gli indici del file, il suo
  contenuto sarebbe compromesso

- piallare un disco (es prima di smaltirlo)
  ```
  dd if=/dev/urandom bs=1M of=/dev/sda
  ```

- per fare un dump di un **device su un'altro**
  ```
  dd if=/dev/sda of=/dev/sdb
  ```
  mettendo eventualmente `bs=4k` per velocizzare (invece dei 512 byte di 
  default)	

- per fare un dump **device su un file**
  ```
  dd if=/dev/sda of=/home/username/sdadisk.img
  ```
  Per il restore su un altro disco (posto che lo spazio sia sufficiente):
  ```
  dd if=sdadisk.img of=/dev/sdb
  ```
  mentre per montarla come disco
  ```
  modprobe loop # caricare il modulo loop (crea i device /dev/loop)
  losetup -P /dev/loop0 partition2.img
  parted -l /dev/loop0
  mkdir disco
  mount /dev/loop0p2 disco
  # do things
  umount disco
  losetup -D # elimino i dispositivi di loopback
  ```
- fare il dump di **partizione su file**
  ```
  dd if=/dev/sda2 of=partition2.img bs=4096
  ```
- creare il file **.iso di un cd/dvd** masterizzato:
  ```
  dd if=/dev/cdrom of=cdrom.iso
  ```
- creare un **backup dell'MBR** (i primi 512 byte del disco)
  ```
  dd if=/dev/sda of=mbr.img bs=512 count=1
  ```
  mentre per il restore basta invertire `if` e `of`
