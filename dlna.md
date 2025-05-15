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
friendly_name=hostname
```
L'utente `minidlna` dovrà avere i permessi di lettura sulle cartelle
condivise (quindi es aggiungerlo ad un gruppo ad hoc che ha accesso in
lettura alla cartella `/media/shared`)

## file supportati
MiniDLNA supports a wide variety of video and audio file formats.

* Video: Files ending with .avi, .mp4, .mkv, .mpg, .mpeg, .wmv, .m4v,
  .flv, .mov, .3gp, etc.
* Audio: Files ending with .mp3, .ogg, .flac, .wav, .pcm, .wma, .fla, .aac, etc.
* Image: Files ending with .jpg, .jpeg
* Playlist: Files ending with .m3u, .pls
* Captions: Files ending with .srt, .smi 

Arrabattarsi con [ffmpeg](ffmpeg.md) nel caso sia necessario il transcoding.
