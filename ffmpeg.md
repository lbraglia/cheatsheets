# ffmpeg

## ottenere info su qualcosa

```
ffmpeg -i video.flv
```

## Conversione

Un template generico per il transcoding 
```
ffmpeg -i input_file -c:v codec -b:v bitrate -c:a audio_codec -b:a audio_bitrate output_file
```
Viceversa se si vuole diminuire le dimensioni di un video usare quanto riportato sotto

### Formato encoding video
Per il video usare il formato h264 dove in base alla qualità si avrà
un file di più o meno grandi dimensioni. 

La guida è https://trac.ffmpeg.org/wiki/Encode/H.264 

I parametri su cui giocare sono `crf`: the range of the CRF scale is
0–51, where 0 is lossless, 23 is the default, and 51 is worst quality
possible.  the lower the value, the better the quality, and the larger
the output.  a sane range is 17–28. Consider 17 or 18 to be visually
lossless or nearly so

```
ffmpeg -i input.mov -c:v libx264 -crf 22 output.mp4
```
Choose the highest CRF value that still provides an acceptable
quality. If the output looks good, then try a higher value. If it
looks bad, choose a lower value.


### Formato encoding audio

Per l'audio vedere https://trac.ffmpeg.org/wiki/Encode/HighQualityAudio.
Comunque l'audio transcoding from a lossy format like MP3, AAC,
Vorbis, Opus, WMA, etc. to the same or different lossy format might
degrade the audio quality even if the bitrate stays the same (or
higher). Quindi se non vi sono esigenze particolari, copiare senza apportare modifiche
come segue.
```
ffmpeg -i someFile.webm -c:a copy -c:v libx264 outFile.mkv
```
Se c'è da convertire invece i formati audio supportati più importanti
```
Dolby Digital: ac3
Dolby Digital Plus: eac3
TrueHD 0xFBA: truehd
MP2: libtwolame, mp2
Windows Media Audio 1: wmav1
Windows Media Audio 2: wmav2
AAC LC: libfdk_aac, aac
HE-AAC: libfdk_aac
Vorbis: libvorbis, vorbis
MP3: libmp3lame, libshine
Opus: libopus
```
con ordine di qualità
```
libopus > libvorbis >= libfdk_aac > libmp3lame >= eac3/ac3 > aac > libtwolame > vorbis > mp2 > wmav2/wmav1
```
The highest quality internal/native encoder available in FFmpeg without any external libraries is aac.

Per la cronaca DLNA supporta i seguenti formati audio
```
AAC (.m4a,.mp4,.3gp)
Linear PCM (.wav)
MP3 (.mp3)
WMA 
```




## Conversione easy peasy
Versione semplice (non so cosa faccia btw)
```
ffmpeg -i input.mp4 output.avi
```
Versione specificando i formati di encoding
```
ffmpeg -i source.mov -c:v libx264 -c:a aac output.mp4
```
libx264 is one of the most popular H.264 encoders. libx264 + aac combo supports IE11.



## Accorciare/estrarre una parte di video

Da 00:00:00 (punto partenza) per una ora e mezza non modificando nulla
se non il formato
```
ffmpeg -i input.mkv -ss 00:00:00 -t 01:30:00 -c:v copy -c:a copy output1.mp4
```

Da punto di partenza a punto di arrivo
```
ffmpeg -i input.mkv -ss 00:02:00 -to 00:03:00 -c:v copy -c:a copy output1.mp4
```

## Estrarre audio da un video

```
ffmpeg -i input.mp4 -vn output.mp3
```

## Rimuovere audio da un video

```
ffmpeg -i input.mp4 -an mute-output.mp4
```

## Aggiungere audio ad un video

```
ffmpeg -i audio.mp3 -i video.mp4 video_audio_mix.mkv
```


## Concatenare video
In `file-list.txt` i path così specificati
```
file '/home/l/asd.mp4'
file '/home/l/foo.mp4'
```
poi dare
```
ffmpeg -f concat -i file-list.txt -c copy output.mp4
```

## Creare una gif

Di base
```
ffmpeg -i input.mp4 output.gif
```
Più elaborato
```
ffmpeg -ss 00:00:20 -i input.mp4 -to 10 -r 10 -vf scale=200:-1 output.gif
```
con:
* `-ss`: indicates the start point of the GIF
* `-to` : indicates the end position of the GIF
* `-r` : means frame rate
* `-vf` scale: is to scale the GIF image in the desired size


## Da mkv ad avi (per dlna)

Usare lo scriptino `mkv2avi`


## Scalare una immagine

```
ffmpeg -i input.png -vf "scale=1920:1080" output.png
```

## Creare una video sequenza di immagini

Follow command create a video from img001.png, img002.png, etc.;
-r 1/5 indicates that each image will have a duration of 5 seconds
```
ffmpeg -r 1/5 -i img%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4
```
