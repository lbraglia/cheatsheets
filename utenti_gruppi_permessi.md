# Utenti, gruppi e permessi

## Intro
`ls -l` mostra la tripletta di permessi (`rwx`) concessi dal
proprietario del file (o da root) a:
- se stesso
- al gruppo cui è assegnato il file
- ai soggetti rimanenti.
È preceduto da:
- `-` per i file normali
- `d` per le directory
- `l` per i collegamenti
- `c` file speciali per IO (maggior parte in /dev)
- `s` socket (simili a socket TCP/IP) per comunicazione tra processi
- `p` pipe (simili ai socket)
- `b` block device (es /dev/sda)
Lettura, scrittura ed esecuzione:
- su file sono immediati (esecuzione pertinente solo per file script o 
  binari eseguibili) 
- su cartelle lettura indica la possibilità di listare il contenuto
  (mediante ls), scrittura di creare file al loro interno, esecuzione
  di spostarsi al proprio interno

## Permessi e cambio
Il modo ottale è il più veloce e i permessi concessi sono identificati
dalla somma
```
4 lettura
2 scrittura
1 esecuzione
```
Ad esempio:
```
chmod 660 file.txt
```
concede lettura e scrittura a proprietario e facenti parti del gruppo sul file
che ha proprietà del file


## Utenti

### Creazione/rimozione
Per la creazione o rimozione di un utente, da root
```
adduser utente
deluser utente
```

### A quali gruppi appartiene
```
id utente
```

## Gruppi

### Creazione/rimozione
```
addgroup utente
delgroup utente
```

### Assegnazione/rimozione di utente ad un gruppo
```
adduser utente gruppo
deluser utente gruppo
```

### Assegnazione di un file
```
chgrp gruppo file
```

## Cambio login utente (a root)
```
su -
sudo -i
```
