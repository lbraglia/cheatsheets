# Appunti (AI and other tools)

## estrarre immagini
installare imagemagick e 
```
apt install imagemagick flameshot
```
poi avviare flameshot  e fare lo screenshot per convertirlo con `convert` di imagemagick
```
# convertire un singolo file
convert file.png file.pdf
# convertire una intera cartella a pdf
mogrify -format pdf *.*
```
per inserirla in latex con (vedi logseq per finetuning)
```tex
\begin{figure}
  \centering
  \includegraphics[scale=0.4]{path/file/pdf}
  \caption{Caption .}
  \label{fig:}
\end{figure}
```

## Estrarre latex da immagine
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
whisper --language en english_video.webm
whisper --language it italian_video.webm
```

## Sintesi
```
pip install -U transformers
```

```python
from transformers import pipeline

text = """
The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.
"""
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
res = summarizer(text)
res[0]['summary_text']

```

https://medium.com/@sarowar.saurav10/6-useful-text-summarization-algorithm-in-python-dfc8a9d33074

https://medium.com/@veejeah/python-summarization-a-comparative-exploration-62c030bd28e1


## Traduzione
```python
## pip install -U sentencepiece
## Translation EN-IT
text = "Hello, my name is Luca"
translate = pipeline("translation", model="Helsinki-NLP/opus-mt-en-it")
translate(text)
## Translation IT-EN
text = "Ciao, mi chiamo Luca"
translate = pipeline("translation", model="Helsinki-NLP/opus-mt-it-en")
translate(text)

# altri modelli da testare This sentences has has bads grammar 
# facebook/m2m100_418M

```



## Grammar improve
```python
text = "This sentences has has bads grammar"
from transformers import pipeline
correct = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")
correct(text)
```


## Modelli/utilizzi da approfondire

`google/flan-t5-large`




## Ollama as frontend to chatgpt-like models

Install ollama from [here](https://ollama.com/), then choose some models from https://ollama.com/library and run it
```
ollama run llama2
ollama run mistral
```

## Private GPT like

https://youtu.be/WxYC9-hBM_g?si=6peOBaviKuWvBc2h&t=1088

https://github.com/zylon-ai/private-gpt

https://medium.com/@docteur_rs/installing-privategpt-on-wsl-with-gpu-support-5798d763aa31

https://github.com/langchain-ai/langchain
