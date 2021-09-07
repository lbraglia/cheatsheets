# Installazione software

## `dpkg`
È il programma utilizzato (tramite `apt`) per installazione/e
rimozione di software; memorizza il log in `/var/log/dpkg.log`.

Ogni pacchetto su una macchina può essere:
- *installed*: installato (depacchettato) e configurato correttamente
- *half-installed*: l'installazione del pacchetto e' iniziata, ma non
  è stata terminata per qualche ragione
- *not-installed*: il pacchetto non e' presente sul sistema
- *half-configured*: spacchettato, ma non configurato
- *config-files*: nel sistema esistono solo i file di configurazione
	  
La sintassi di dpkg è:
```
dpkg [opzioni .. ] azione
```

### Pacchetti deb
È un archivio `ar` che raggruppa dei `tar.xz` quindi
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
dpkg -e file.deb dir  # estrae control file, script debian ()

```
### Installazione
```
dpkg -i file.deb
```
Nell'ordine

L'installazione procede attraverso i seguenti passi:
\begin{itemize}
\item dpkg estrae il control file nel nuovo pacchetto
\item se presente una versione precedere del pacchetto nel
  sistema, viene eseguito il suo script prerm
\item viene eseguito lo script preinst del nuovo pacchetto, s
  presente
\item vengono spacchettati i nuovi file e viene fatto un backup
  dei vecchi cosi' se qualcosa va male si puo rimenttere a posto
\item  viene eseguito lo script postrm dell'eventuale vecchi pacchetto
\item  il pacchetto viene configurato (vedi --configure)
\end{itemize}



```
dpkg -S /bin/date   # a quale pacchetto appartiene questo file
dpkg -L coreutils   # quali file contiene un dato pacchetto
```



## `apt`
Gestisce ricerca e reperimento di software, fungendo come intefaccia
ad altri programmi storici di più basso livello (`apt-get`,
`apt-cache`) e avvalendosi di `dpkg` per l'installazione

### Configurazione `/etc/apt/sources.list`

```
# Stable
deb http://deb.debian.org/debian stable main contrib non-free
deb http://deb.debian.org/debian stable-updates main contrib non-free
deb http://security.debian.org/debian-security stable-security main contrib non-free
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

## Ricerca software mediante `debtags`

```
# Lista pacchetti coi quali è possibile editare immagini raster
# escludendo librerie e dummy package
debtags search "use::editing && works-with::image:raster && \
	! (role::shared-lib || role::dummy)"

# Tutti i client mail
debtags search "works-with::mail && network::client"
```

## Aggiornamento di sistema automatico
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
