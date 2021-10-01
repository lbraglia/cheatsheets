# Grub2

Il file di configurazione utilizzato dal programma è
`/boot/grub/grub.cfg` che viene generato a partire da:
- il file di configurazione`/etc/default/grub`
- gli script in `/etc/grub.d/`

Per configurare GRUB 2 bisogna modificare `/etc/default/grub` quindi
eseguire `update-grub`; le configurazioni avanzate si ottengono
modificando i file in `/etc/grub.d/`.

