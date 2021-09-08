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
