# Installazione software

## dpkg


## sources.list

```
# Stable
deb http://deb.debian.org/debian stable main contrib non-free
deb http://deb.debian.org/debian stable-updates main contrib non-free
deb http://security.debian.org/debian-security stable-security main contrib non-free

# Backports & Testing
# deb http://deb.debian.org/debian bullseye-backports main contrib non-free
# deb http://deb.debian.org/debian testing main contrib non-free
```

## apt
Funge come intefaccia ad altri programmi (`apt-get`, `apt-cache`) 

```
# Lista pacchetti installati
apt list

# Aggiornamento installazione
apt update
apt upgrade
apt full-upgrade

# Ricerca
apt search parole
apt show pacchetto

# Installazione
apt install pacchetto
apt reinstall pacchetto

# Rimozione
apt remove pacchetto   # rm il software
apt purge pacchetto    # anche i file di configurazione

# Pulizia (dipendenze non più necessarie)
apt autoremove
```

## Ricerca con debtags


## backports

```
apt show pacchetto -a
apt -t bullseye-backports install pacchetto
```
