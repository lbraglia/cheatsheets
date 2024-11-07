# Associazione file a programmi

Le associazioni MIME applicate con `open`, `xdg-open` sono memorizzate
in `~/.config/mimeapps.list`. Vengono spesso usate da programmi vari
per scegliere con cosa aprire determinati file sulla base dell'estensione.

Ad esempio per okular come visore pdf
```bash
xdg-mime default okularApplication_pdf.desktop application/pdf
```
