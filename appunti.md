# Appunti

## latex-ocr
See here https://github.com/lukas-blecher/LaTeX-OCR

```
apt install gnome-screenshot
pip install -U "pix2tex[gui]"
latexocr
```



## Download video
Libraries for YT
```
pip install -U --upgrade yt-dlp
pip install -U --upgrade youtube-dl
```
Download
```
yt-dlp url
```

## Estrazione audio
Installare [whisper](https://github.com/openai/whisper)
```
## installazione
pip install -U openai-whisper
## aggiornamento
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
```
Estrazione testo
```
## man
whisper --help

## Estrazione di inglese
whisper --output txt --language en english_video.webm
whisper --output txt --language it italian_video.webm
```

## Sintesi
Proviamo i transformers di huggingface
```
pip install -U transformers
```

```python
from transformers import pipeline

 summarizer = pipeline(task="summarization")
text = """
The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.
"""

res = summarizer(text)
res[0]['summary_text']
```

https://medium.com/@sarowar.saurav10/6-useful-text-summarization-algorithm-in-python-dfc8a9d33074
https://medium.com/@veejeah/python-summarization-a-comparative-exploration-62c030bd28e1
