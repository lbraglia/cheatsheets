# Debian (and Gnu/Linux) cheatsheet


## Amministrazione

### Ottenere permessi di amministratore
```
su -
sudo -i
```

### Spegnere la macchina
```
shutdown -h now # spegni
shutdown -r now # riavvia

```

### Systemd, servizi e target (runlevel)
Una volta c'era `init` a ad essere il primo processo avviato dal
kernel, ora sostituito da `systemd`; i runlevel di init sono stati
sostituiti dai target di `systemd`.

I task di systemd sono organizzati per *units*: le units più comuni sono
servizi (`.service`), punti di mount (`.mount`), devices (`.device`),
sockets (`.socket`), o timers (`.timer`). Ad esempio per far partire
il server ssh è fatto attraverso l'unità `ssh.service`.

I *target* sono gruppi di units chiamate in un dato ordine per fare il
setup del sistema (ad esempio `graphical.target` chiama tutte le unità
per fare il setup di un ambiente grafico); i target possono
costruirsi/basarsi su altri target.

I *control group* sono invece una aggregazione di un piu units che il
kernel tratta assieme per quanto riguarda l'allocazione di risorse (e
isolamento processi).

Al boot systemd attiva il target `default.target` che è un alias per
un altro target (`graphical.target`). 

```
systemctl                    # listare i servizi (tra le altre cose)
systemctl list-unit-files    # listare tutti gli unit files
systemctl status             # quale servizio ha fatto partire quali eseguibili


systemctl list-units --type service  # listare i servizi
systemctl status service      # status (per service digitare cron.service o solo cron)
systemctl start service       # avviare un servizio
systemctl stop service        # terminare un servizio
systemctl restart service     # riavviare un servizio
systemctl enable service      # avviare un servizio al boot
systemctl is-enabled service  # testare se avviato al boot
systemctl disable service     # togliere il servizio dal boot

systemctl get-default               # ottenere il target di default
systemctl set-default target.target # settare il target di default
```

Gli unit file di sistema sono in `/lib/systemd/system`; nuovi unit
(servizi ecc) vanno posti in `/etc/systemd/system`, seguire la
documentazione qui: https://wiki.debian.org/systemd/Services

Per vedere quali servizi ci mettono molto al boot (vedere i relativi log 
per casi particolarmente lenti)
```
systemd-analyze blame
```


### Log

```
journalctl -b                   # log del boot corrente
journalctl -b -r                # log del boot corrente, reversed
journalctl --since "1 hour ago" # log timeframe specificato
journalctl -f                   # ultimi eventi in aggiornamento continuo
journalctl -u nginx.service     # log di una unit di systemd
journalctl _UID=1000            # log di un utente (uid ottenibile con id user)
```

### Layout tastiera

```
dpkg-reconfigure keyboard-configuration 
systemctl restart keyboard-setup
```


### Recovery di sistema

Aggiungere 1 al termine della linea di GRUB per bootare il runlevel 1
(single user root).

