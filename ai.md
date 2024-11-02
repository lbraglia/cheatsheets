# AI

## Ollama



Install ollama from [here](https://ollama.com/), 
```
wget https://ollama.com/install.sh
su
sh install.sh
```
Choose some models from https://ollama.com/library and run it
```
# eseguire un modello gerico con poca ram
ollama run dolphin-mistral

# list available models
ollama list

# delete a model
ollama rm llama2

# >>> What's in this image? /Users/jmorgan/Desktop/smile.png
# The image features a yellow smiley face, which is likely the central focus of 
# the picture.

```

Useful plugin
- logseq integration https://github.com/omagdy7/ollama-logseq
- telegram bot https://github.com/ruecat/ollama-telegram


## fabric

```
curl -L https://github.com/danielmiessler/fabric/releases/latest/download/fabric-linux-amd64 > fabric && chmod +x fabric && ./fabric --version
```
spostarlo in .local/bin per averlo nel path
```
mv fabric .local/bin
```
setup
```
fabric --setup
```
listare i pattern disponibili
```
fabric -l
```
alcuni utilizzi
```
cat knowledge.txt | fabric --pattern summarize
fabric -y "https://youtube.com/watch?v=uXs-zPc63kM" --pattern extract_wisdom > sintesi.txt
```
Installare alcune utility gagliarde (simulano `pbpaste` del mac)
```

#  versione 1
apt-get install xclip

# alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'

# copiare da web browser poi
pbpaste | fabric --pattern extract_wisdom

```

## Da approfondire

modelli trainati su dati medici

cheshire cat

train llm on personal data

private gpt

langchain

model finetuning for specific application (servizi)

https://youtu.be/WxYC9-hBM_g?si=6peOBaviKuWvBc2h&t=1088

https://github.com/zylon-ai/private-gpt

https://medium.com/@docteur_rs/installing-privategpt-on-wsl-with-gpu-support-5798d763aa31

https://github.com/langchain-ai/langchain
