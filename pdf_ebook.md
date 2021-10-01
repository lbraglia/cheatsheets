# PDF e e-book

## PDF

### Manipulation
Installare `pdftk`.
```
## Collage di due pdf
pdftk in1.pdf in2.pdf cat output out1.pdf

## Selezione di alcune pagine (qui elimina la 13)
pdftk in.pdf cat 1-12 14-end output out1.pdf

## Ruota la prima pagina di 90 gradi (in senso orario)
pdftk in.pdf cat 1east 2-end output out.pdf

## Ruota tutto il pdf di 180 gradi
pdftk in.pdf cat 1-endsouth output out.pdf

## Rimozione di password
pdftk secured.pdf input_pw foopass output unsecured.pdf

## Prova a riparare la tabella XREF e altro
pdftk broken.pdf output fixed.pdf

## Splitta in molteplici pdf da una pagina (dati in doc_data.txt)
pdftk input.pdf burst
```

### OCR
Per trasformare una scansione `original.pdf` in un file con testo
riconosciuto `ocred.pdf`, installare i pacchetti `ocrmypdf
tesseract-ocr-ita` e dare
```
ocrmypdf -l ita -j 8 -c -d -i original.pdf ocred.pdf
```


## e-book
`fbreader`
