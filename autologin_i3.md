# Login, X e window manager (i3/fluxbox)

## Installazione componenti
```
apt install xorg xinit i3
# per scheda grafica vedere la pagina del wiki debian
```

## Autologin
In assenza di login manager si usano i [servizi di systemd](https://unix.stackexchange.com/questions/401759) e nello specifico:
- cambiare in `/etc/systemd/logind.conf` , da `#NAutoVTs=6` a `NAutoVTs=1`
- creare `/etc/systemd/system/getty@tty1.service.d/override.conf`
  (eventualmente attraverso `systemctl edit getty@tty1`) inserendo il contenuto
  ```
  [Service]
  ExecStart=
  ExecStart=-/sbin/agetty --autologin nomeutente --noclear %I 38400 linux
  ```
- abilitare il servizio mediante
  ```
  systemctl enable getty@tty1.service
  ```
- fare il `reboot`

## Avvio del server grafico senza login manager

Per l'autoavvio del server grafico al login porre al termine in `.profile` la linea:
```
startx
```

## i3
File di configurazione: `.config/i3/config` gestito automaticamente mediante 
le `make user-setup-script`.
