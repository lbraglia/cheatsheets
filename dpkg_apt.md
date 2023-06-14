# Installazione software


## `apt`
Gestisce ricerca e reperimento di software, fungendo come intefaccia
ad altri programmi storici di più basso livello (`apt-get`,
`apt-cache`) e avvalendosi di `dpkg` per l'installazione

### Repo `/etc/apt/sources.list` utili

```
# Stable
deb http://deb.debian.org/debian stable main contrib non-free non-free-firmware
deb http://deb.debian.org/debian stable-updates main contrib non-free non-free-firmware
deb http://security.debian.org/debian-security stable-security main contrib non-free non-free-firmware

# backports
deb http://deb.debian.org/debian bullseye-backports main

# R aggiornato
deb http://cloud.r-project.org/bin/linux/debian bullseye-cran40
```



### Comandi comuni di `apt`
```
# Lista pacchetti installati
apt list

# Aggiornamento installazione
apt update
apt upgrade
apt full-upgrade

# Ricerca
apt search parole    # cerca in nome o descrizione
apt show pacchetto   # descrizione del pacchetto

# Installazione
apt install pacchetto
apt reinstall pacchetto

# Rimozione
apt remove pacchetto   # rm il software
apt purge pacchetto    # anche i file di configurazione

# Pulizia 
apt clean      # cache
apt autoremove # dipendenze non più necessarie
```

### Installazione dai backports
Abilitare l'opportuna riga nel `sources.list`, dipende dalla versione di debian, che possiamo indagare con `lsb_release`
```
m740n:~$ lsb_release -a
No LSB modules are available.
Distributor ID:Debian
Description:Debian GNU/Linux 11 (bullseye)
Release:11
Codename:bullseye
```
per bullseye la riga è 
```
deb http://deb.debian.org/debian bullseye-backports main
```
dopodiché
```
apt update
apt install <package>/bullseye-backports
```
Per approfondimenti [vedere qui](https://backports.debian.org).

### Ricerca software mediante `debtags`

```
# Lista pacchetti coi quali è possibile editare immagini raster
# escludendo librerie e dummy package
debtags search "use::editing && works-with::image:raster && \
	! (role::shared-lib || role::dummy)"

# Tutti i client mail
debtags search "works-with::mail && network::client"
```

### Aggiornamento di sistema automatico
Utilizzare il seguente script:
<!-- in `cron` (macchine sempre accese) o `anacron` (le -->
<!-- rimanenti)  -->
```
#!/bin/bash
apt update
apt upgrade -y
apt clean
apt autoremove
```

Dargli i permessi di esecuzione e spostarlo in `/usr/sbin` e linkarlo
in `/etc/cron.weekly`; `anacron` eseguirà lo script (se il computer è
connesso alla corrente).



## `dpkg`
È il programma utilizzato (tramite `apt`) per installazione/e
rimozione di software; memorizza il log in `/var/log/dpkg.log`.

Ogni pacchetto su una macchina può essere in diversi stati, principalmente:
- *not-installed*: il pacchetto non e' presente sul sistema
- *config-files*: nel sistema esistono solo i file di configurazione
- *half-installed*: l'installazione del pacchetto e' iniziata, ma non
  è stata terminata per qualche ragione
- *unpacked*: (depacchettato ma non configurato
- *half-configured*: spacchettato, ma la configurazione (iniziata) non
  è completata
- *installed*: installato (depacchettato) e configurato correttamente
	  
La sintassi di dpkg è:
```
dpkg [opzioni .. ] azione
```

### Stato del sistema
Il comando:
```
dpkg -l <eventuale_pattern>
```
lista i pacchetti rispettanti il pattern; se non fornito lista
tutti i pacchetti contenuti in `/var/lib/dpkg/status`, ad eccezione
di quelli marcati con "purged"
```
$ ~ : dpkg -l *speak
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Installed/Config-files/Unpacked/Failed-config/Half-installed
|/ Err?=(none)/Hold/Reinst-required/X=both-problems (Status,Err: uppercase=bad)
||/ Name           Version        Description
+++-==============-==============-============================================
un  emacspeak      <none>         (no description available)
un  erc-speak      <none>         (no description available)
ii  espeak         1.16-2         A multi-lingual software speech synthesizer
```


### Pacchetti deb
È un archivio `ar` che raggruppa dei `tar.xz` quindi per 
```
# Estrazione "raw"
ar -x file.deb
tar xvJf control.tar.xz
tar xvJf data.tar.xz
```

### Controllo contenuto e installazione
```
dpkg -I file.deb      # mostra info
dpkg -c file.deb      # lista i file contenuti
dpkg -x file.deb dir  # estrae contenuti in dir, se -X lista anche i file
dpkg -e file.deb dir  # estrae control file, script debian etc
```

### Installazione
```
dpkg -i file.deb
```
Nell'ordine l'installazione procede attraverso i seguenti passi:
- `dpkg` estrae il control file
- se un'altra versione del pacchetto è presente, viene eseguito lo
  script `prerm` della vecchia versione (se esistente);
- viene eseguito lo script `preinst` del nuovo pacchetto (se presente)
- vengono spacchettati i nuovi file e viene fatto un backup
  dei vecchi così se qualcosa va male si puo rimenttere a posto
- viene eseguito lo script `postrm` dell'eventuale versione precedente
- il pacchetto viene configurato; se qualcosa va male provare `dpkg -a`
  riconfigura tutti i pacchetti decompressi ma non ancora configurati

### Rimozione
```
dpkg -r pacchetto  # -P per rimuovere anche i file di configurazione (purge)
```
Nell'ordine:
- esegue `prerm`
- rimuove i file installati
- esegue `postrm`


### Riconfigurazione
Per riconfigurare un pacchetto (es cambio opzioni)
```
dpkg-reconfigure nomepacchetto
```

### Listing e ricerca di contenuti locali (pacchetti installati
```
dpkg -L coreutils   # quali file/path contiene un dato pacchetto
dpkg -S /bin/date   # greppa il pattern fornito tra i path di tutti
                    # i pacchetti installati; qui dice quale pacchetto
					# contiene /bin/date
```

