# Debian cheatsheet


## Permessi di amministratore
```
su -
sudo -i
```

## Spegnere, riavviare, sospendere
```
shutdown -h now   # spegni
shutdown -r now   # riavvia
```

## Rete

```
ip addr              # lista interfacce disponibili (tra cui es wlan0) e stato
ip link set wlan0 up # attiva/alimenta l'interfaccia
iwlist wlan0 scan    # scan delle reti disponibili
```
Configurazioni comuni per `/etc/network/interfaces`
```
# ethernet
auto eth0
allow-hotplug eth0
iface eth0 inet dhcp

# wifi device, setup principale
allow-hotplug wlan0    # <- per fare la configurazione al boot
iface wlan0 inet dhcp  # <- info sulla configurazione di default
        wpa-ssid ESSID
        wpa-psk PASSWORD

# Altra connessione WPA
iface uni inet dhcp
      wpa-ssid ESSID2
      wpa-psk PASSWORD2
	  
# Altra connessione non criptata
iface lavoro inet dhcp
	wireless-essid ESSID3
```
Al boot dovrebbe andare, poi per switchare ad altre reti:
```
ifdown wlan0 && ifup wlan0=lavoro
```

## Systemd
Una volta c'era `init` a ad essere il primo processo avviato dal
kernel, ora sostituito da `systemd`; i runlevel di init sono stati
sostituiti dai target di `systemd`.

I task di systemd sono organizzati per *units*: le units più comuni sono
servizi (`.service`), punti di mount (`.mount`), devices (`.device`),
sockets (`.socket`), o timers (`.timer`). Ad esempio per far partire
il server ssh è fatto attraverso l'unità `ssh.service`.

Gli unit file di sistema sono in `/lib/systemd/system`; nuovi unit
(servizi ecc) vanno posti in `/etc/systemd/system` (per i servizi seguire la
documentazione qui: https://wiki.debian.org/systemd/Services)

Alcuni comandi generali:
```
systemctl                    # listare i servizi (tra le altre cose)
systemctl list-unit-files    # listare tutti gli unit files
systemctl status             # quale servizio ha fatto partire quali eseguibili
```

### Servizi

```
systemctl list-units --type service  # listare i servizi
systemctl status service      # status (per service digitare cron.service o solo cron)
systemctl start service       # avviare un servizio
systemctl stop service        # terminare un servizio
systemctl restart service     # riavviare un servizio
systemctl enable service      # avviare un servizio al boot
systemctl is-enabled service  # testare se avviato al boot
systemctl disable service     # togliere il servizio dal boot
```


### Target (ex-runlevel)

I *target* sono gruppi di units chiamate in un dato ordine per fare il
setup del sistema (ad esempio `graphical.target` chiama tutte le unità
per fare il setup di un ambiente grafico); i target possono
costruirsi/basarsi su altri target. I target di default sono:

```
poweroff.target    # spegne
rescue.target      # single user (root)
multi-user.target  # multi user
graphical.target   # multi user con interfaccia grafica
reboot.target      # riavvia
```

Al boot systemd attiva il target `default.target` che è un alias per
un altro target (`graphical.target`). 

<!-- I *control group* sono invece una aggregazione di un piu units che il -->
<!-- kernel tratta assieme per quanto riguarda l'allocazione di risorse (e -->
<!-- isolamento processi). -->

Comandi utili per i target
```
systemctl get-default                 # ottenere il target di default
systemctl set-default target.target   # settare il target di default
```

### Analisi del boot

Per vedere quali servizi ci mettono molto al boot (vedere i relativi log 
per casi particolarmente lenti)
```
systemd-analyze blame
```


## Log

```
journalctl -b                   # log del boot corrente
journalctl -b -r                # log del boot corrente, reversed
journalctl --since "1 hour ago" # log timeframe specificato
journalctl -f                   # ultimi eventi in aggiornamento continuo
journalctl -u nginx.service     # log di una unit di systemd
journalctl _UID=1000            # log di un utente (uid ottenibile con id user)
```

## Configurazione layout tastiera

```
dpkg-reconfigure keyboard-configuration 
systemctl restart keyboard-setup
```

## alternatives
`man update-alternatives`


## Creazione di chiavetta di installazione
Con i permessi di amministratore, senza aver montato la chiavetta (in
questo caso mappata come `sdb`
```
cat debian-10.0.0-amd64-netinst.iso > /dev/sdb 
sync
```

## Recovery di sistema

Aggiungere 1 al termine della linea di GRUB per bootare il runlevel 1
(single user root).

Alternativamente è possibile bootare un disco di installazione Debian
con Graphical Rescue Mode (tra le opzioni avanzate) che dopo aver
mostrato le partizioni sulle quali è possibile intervenire (hanno il
nome dell'host da salvare nel path) eventualmente permette l'avvio di
una shell di root nel sistema considerato (es per reinstallare GRUB
nel MBR).
