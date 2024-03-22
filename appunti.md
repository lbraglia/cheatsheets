# Appunti

## Download video
Libraries for YT
```
pip install -U --upgrade yt-dlp
pip install -U --upgrade youtube-dl
```
Download
```
yt-dlp
```

## Estrazione audio
Installare [whisper](https://github.com/openai/whisper)
```
## installazione
pip install -U openai-whisper
## aggiornamento
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
```
Estrazione
```
## man
whisper --help

## Estrazione di inglese
whisper --output txt --language en english_video.webm
whisper --output txt --language en italian_video.webm
```


## Sintesi
