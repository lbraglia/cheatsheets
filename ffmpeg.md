# ffmpeg

## Accorciare un video

Da 00:00:00 (punto partenza) per una ora e mezza non modificando nulla
se non il formato
```
ffmpeg -i input.mkv -ss 00:00:00 -t 01:30:00 -c:v copy -c:a copy output1.mp4
```
