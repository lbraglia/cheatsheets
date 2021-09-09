# Partizioni e Mounting

## Partizioni

### Listing 
Per listare dischi, partizioni e file system 
```
parted -l
```

## Mounting: 

### `/etc/fstab`
Il filesystem / è montato dal kernel al boot; altre device più tardi
mediante `mount`, e seguendo le configurazioni specificate in
`/etc/fstab`.

Ogni mountpoint è descritto da una linea con campi separati da spazi
(anche uno solo):

- *filesystem*: indica dove si trova il filesystem da montare; può
  essere locale (es disco) o remoto (es nfs). Solitamente questo campo
  è compilato con l'id univoco del filesystem prefissato da
  `UUID=` (per evitare problemi su cambi nome del device). Per ottenerlo 
  si usa `blkid` come segue:
  ```
  root@m740n:~# blkid /dev/sdb1 
  /dev/sdb1: UUID="788E-DC5F" BLOCK_SIZE="512" TYPE="vfat"
  ```
  ... e in fstab si tolgono le virgolette `UUID=788E-DC5F`

- *mountpoint*: dove nel filesystem root montare

- *type*: indica il tipo di filesystem, ad esempio `ext4`, `ext3`,
  `vfat`, `ntfs`, `smbfs`, `iso9660`, `auto` (quest'ultimo lascia a
  mount indovinare il tipo ed è utile per CD/DVD)
  
- *opzioni*: separate da virgole, le più comuni sono `rw` o `ro` (read
  write o read only), `auto`/`noauto` (per il mounting automatico al
  boot, o quando si comanda `mount -a`, o meno), `user`/`nouser`
  (autorizzare il mounting ad utenti non root o meno), `nofail`
  (permete al boot di procedere anche se il device non è presente, es
  per dischi esterni)
  
- *dump*: quasi sempre settato a 0 (viene settato a 1 si dice al
  tool `dump` che la partuzione contiene dati che devono essere backuppati)

- *pass*: l'integrità del filesystem viene eseguita nell'ordine dei
  numeri posti (se 0 non viene eseguita, tipicamente si pone 1 sul
  filesystem root e 2 su altri filesystem)

### `mount`
Se i device non sono specificati in fstab, il comando mount (che
necessita dei permessi di root se non diversamente previsto) ha la sintassi
```
mount -t type device dir
```
`-t` è opzionale (mount indovina abbastanza il tipo); se viene fornita
solo la device o la directory, mount vede se riesce a completare le info 
guardando `fstab` (possibile evitare ambiguità specificando `--source` e 
`--target`


### Listare i filesystem montati

```
findmnt
findmnt --fstab    ## solo quelli specificati in fstab
```


