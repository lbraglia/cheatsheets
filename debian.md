# Debian cheatsheet

## Installazione da USB
Con i permessi di amministratore, senza aver montato la chiavetta (in
questo caso mappata come `sdb`
```
cat debian-10.0.0-amd64-netinst.iso > /dev/sdb 
sync
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
La prima domanda è quali locali supportare (inglesi utf8 anche is ok) mentre
la seconda quello di default (da porre a `it_IT.UTF-8`)

### Timezone
Per riconfigurare la zona, se necessario:
```
dpkg-reconfigure tzdata
```

### NTP
Su installazioni nuove `systemd-timesyncd` agisce da client NTP e ciò
è sufficiente per sincronizzare un sistema. Il demone `ntp`
dell'omonimo pacchetto è necessario solo quando è richiesto un server
NTP cui fare riferire le macchine locali.


### Tastiera

Per la riconfigurazione di layout/lingua
```
dpkg-reconfigure keyboard-configuration 
systemctl restart keyboard-setup
```
Per applicare le nuove impostazioni, dovrebbe essere sufficiente riavviare 
il servizio `keyboard-setup`; se così non è si può provare
a riavviare il sistema di input del kernel con udev:
```
udevadm trigger --subsystem-match=input --action=change 
```
o a riavviare l'intero sistema operativo. 

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
Sul sistema vi sono diversi eseguibili che forniscono un determinato
tipo di applicativo (es editor); il sistema delle alternative di
Debian fa si che il generico `/usr/bin/editor` sia linkato (via link
in `/etc/alternatives`) all'eseguibile scelto come alternativa
default.

Per listare le alternative per l'editor
```
l@m740n:~$ update-alternatives --list editor
/bin/nano
/usr/bin/emacs
/usr/bin/mcedit
/usr/bin/vim.tiny
```
Per impostare che l'editor standard sia Emacs
```
root@m740n:/home/l# update-alternatives --config editor
Sono disponibili 4 scelte per l'alternativa editor (che fornisce /usr/bin/editor).

Selezione    Percorso           Priorità  Stato
------------------------------------------------------------
* 0            /bin/nano           40        modalità automatica
  1            /bin/nano           40        modalità manuale
  2            /usr/bin/emacs      0         modalità manuale
  3            /usr/bin/mcedit     25        modalità manuale
  4            /usr/bin/vim.tiny   15        modalità manuale
		  
Premere Invio per mantenere il valore predefinito[*] o digitare il numero della selezione: 2
 update-alternatives: viene usato /usr/bin/emacs per fornire /usr/bin/editor (editor) in modalità manuale
```



Per aggiungere una alternative (con una priorità maggiore a quelle disponibili
diviene il default e non vi è bisogno di settarlo poi)


```
update-alternatives --install /usr/bin/x-www-browser x-www-browser /usr/bin/librewolf 100
```

Per ulteriori info `man update-alternatives` e https://www.baeldung.com/linux/update-alternatives-command
Altri gruppi di alternative possono esser trovati in
/etc/alternatives, tra essi x-www-browser


## Shutdown e riavvio
```
shutdown -h now   # spegni
shutdown -r now   # riavvia
```









