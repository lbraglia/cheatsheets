# logseq

## installazione
https://logseq.com/downloads
scaricare l'appimage, rinominarla in `logseq` e porla da qualche parte nel path

## installazione di logseq-query (esportare query)
https://github.com/cldwalker/logseq-query
```
# npm install logseq-query -g
```
poi
l@m740n:~$ mkdir .lq
l@m740n:~$ echo '{:default-options {:graph ".brain"}}' > ~/.lq/config.edn

lq q has-property type -t
lq q block-content

lq q property type activity

lq sq "(property :type [[activity]])"
