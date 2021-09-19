# dnla

## server
Installare `minidlna` dopodiché editare `/etc/minidlna.conf` per
configurare:
```
# specifica delle cartelle condivise 
media_dir=A,/media/shared/musica
media_dir=P,/media/shared/foto
media_dir=V,/media/shared/video

# e volendo tag del device human friendly
friendly_name=serverinodlna
```
L'utente `minidlna` dovrà avere i permessi di lettura sulle cartelle
condivise (quindi es aggiungerlo ad un gruppo ad hoc che ha accesso in
lettura alla cartella `/media/shared`)
