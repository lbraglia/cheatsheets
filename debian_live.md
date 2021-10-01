# Debian Live

## Setup
```
apt install live-build live-manual-html
```

## Creazione di una live
```
mkdir /tmp/test
cd /tmp/test
lb config
sudo lb build
```


## Old stuff (RELUG)
```
#!/bin/bash

HOME=`pwd`

lh_config \
    --syslinux-timeout 10 \
    --username relug \
    --hostname relug \
    --mirror-bootstrap 'http://localhost' \
    --mirror-chroot 'http://localhost' \
    --mirror-binary 'http://mi.mirror.garr.it/mirrors/debian/' \
    --architecture i386 \
    --apt apt \
    --binary-images iso \
    --packages "xorg lxde abiword amsn  gtkpod gnumeric vlc epdfview ntfs-3g gnomebaker xarchive 
kazehakase sylpheed zip unzip rar unrar bzip2 xarchive amule msttcorefonts w32codecs sun-java6-plugin" \
    --debian-installer enabled \
    --debian-installer-distribution lenny \
    --distribution lenny \
    --categories "main contrib non-free" \
    --bootappend-live "locale=it_IT.UTF8 keyb=it" \
    --language it

# aggiunta repository per la creazione del cd
echo "deb http://mi.mirror.garr.it/mirrors/debian/ stable main contrib non-free" > config/chroot_sources/garr.chroot
echo "deb http://www.debian-multimedia.org lenny main" >> config/chroot_sources/debian_multimedia.chroot 
echo "deb http://download.skype.com/linux/repos/debian/ stable non-free" >> config/chroot_sources/skype.chroot 

# aggiunta repository sources.list del live cd
echo "deb http://mi.mirror.garr.it/mirrors/debian/ stable main contrib non-free" > config/chroot_sources/skype.binary
echo "deb http://www.debian-multimedia.org lenny main" >> config/chroot_sources/debian_multimedia.binary 
echo "deb http://download.skype.com/linux/repos/debian/ stable non-free" >> config/chroot_sources/skype.binary 

# per mettere pacchetti personalizzati, porli nella cartella
# config/chroot_local-package (vedere il debian new maintainer
# manual, devono esser pacchetti dal nome regolare)

cd config/chroot_local-packages 
wget http://http.us.debian.org/debian/pool/contrib/f/flashplugin-nonfree/flashplugin-nonfree_2.6_i386.deb
wget http://www.skype.com/go/getskype-linux-deb
cd $HOME

# per avere file che saranno presenti nella distro live,
# apporli nella cartella config/chroot_local-includes, ricreando
# all'interno della stessa il path con le cartelle, ad es.
# config/chroot_local-includes/etc/fetchmailrc 
```
