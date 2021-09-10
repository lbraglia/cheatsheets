# Smartphone

## Mounting di dispositivi Android

Dopo aver installato il pacchetto `jmtpfs` (per montare dispositivi
mediante MFS - media transfer protocol) da utente normale:
- connettere lo smartphone mediante USB e in `Impostazioni` -> 
  `Dispositivi Collegati` -> `USB` scegliere "Trasferimento di file";
- listare i dispositivi disponibili mediante
  ```
  jmtpfs -l
  ```
- montare un dispositivo (da utente normale)
  ```
  mkdir /tmp/phone
  jmtpfs /tmp/phone
  ```
  Viene utilizza il primo device disponibile/listato, alternativamente si 
  può scegliere quale montare mediante mediante l'opzione
  `-device` (vedere il man)
- per smontare
  ```
  umount /tmp/phone
  ```

## Configurazione con /etc/fstab (da ArchWiki)
Per far si che funzioni come gli altri mount

```
ln -s /usr/bin/jmtpfs /sbin/mount.jmtpfs
```
Poi modificare `fstab` aggiungend:
```
#jmtpfs <mount path> fuse nodev,allow_other,<other options> 0    0
jmtpfs /home/l/motog fuse nodev,allow_other,rw,user,noauto  0    0
```
effettuare il refresh 
```
systemctl daemon-reload
```
e decommentare la linea
```
# user_allow_other
``` 

in `/etc/fuse.conf`. Fatto l'utente `l` potrà montare e smontare
normalmente lo smartphone
```
l@m740n:~$ mount motog
Device 0 (VID=22b8 and PID=2e82) is a Motorola Moto G (ID2).
Android device detected, assigning default bug flags
l@m740n:~$ l motog
totale 0
drwxr-xr-x 20 l l 0 15 ago  4458541 'Memoria interna condivisa'
drwxr-xr-x  9 l l 0 19 feb  4458541 'Scheda SD SanDisk'
l@m740n:~$ umount motog
```
