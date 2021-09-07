# Debian cheatsheet

## Installazione
Con i permessi di amministratore, senza aver montato la chiavetta (in
questo caso mappata come `sdb`
```
cat debian-10.0.0-amd64-netinst.iso > /dev/sdb 
sync
```

### Shutdown e riavvio
```
shutdown -h now   # spegni
shutdown -r now   # riavvia
```

## Setup

### Localizzazione
Il locale è un insieme di configurazioni legate alla posizione
geografica (formati per numeri, date, tempo, valute); per
listare le opzioni attuali
```
locale
```
Per riconfigurare il locale
```
dpkg-reconfigure locales
```
La prima domanda è quali locali () supportare mentre la seconda quello
di default (da porre a `it_IT.UTF-8`)

### Tastiera

Per la riconfigurazione di layout/lingua
```
dpkg-reconfigure keyboard-configuration 
systemctl restart keyboard-setup
```
Per altre configurazioni comuni
```
xset b off   # Disattivazione system bell (sotto X)
numlockx on  # Attivazione tastierino numerico
```
Per la rilevazione dei tasti sotto X
```
xev
```


### alternatives
`man update-alternatives`









