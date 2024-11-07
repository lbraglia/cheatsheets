# Associazione file a programmi

Le associazioni MIME applicate con `open`, `xdg-open` sono memorizzate
in `~/.config/mimeapps.list`. Vengono spesso usate da programmi vari
per scegliere con cosa aprire determinati file sulla base
dell'estensione.

I programmi disponibili sono qui:
```
/usr/share/applications
```
Interrogare le impostazioni di qualche tipo:
```bash
xdg-mime query default inode/directory # file manager
```
Impostare cose:
```bash
## settare krusader come filemanager
xdg-mime default org.kde.krusader.desktop inode/directory
## okular come visore pdf
xdg-mime default okularApplication_pdf.desktop application/pdf
```
