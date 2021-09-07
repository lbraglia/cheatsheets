# Rete

## Setup
```
ip addr              # lista interfacce disponibili (tra cui es wlan0) e stato
ip link set wlan0 up # attiva/alimenta l'interfaccia
iwlist wlan0 scan    # scan delle reti disponibili
```
Configurazioni comuni per `/etc/network/interfaces`
```
# ethernet
auto eth0              # configurazione al boot (per schede sempre attaccate)
iface eth0 inet dhcp

# wifi device, setup principale
allow-hotplug wlan0    # <- schede rimovibili (configura quando rilevate)
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

## Risoluzione indirizzi

### hostname e hosts
Ogni macchina è identificabile con un nome ottenibile con `hostname`;
per esigenze di comodità di rete si possono porre coppie indirizzo
nome nel file `/etc/hosts` come segue
```
127.0.0.1    localhost
192.168.0.1  gw
192.168.0.2  stampante
```

Questo file è particolarmente utile se duplicato (con i dovuti
aggiustamenti, es su localhost) negli altri pc della rete (i più
importanti/stabili). Se la rete locale inizia a diventare corposa (5-6
macchine almeno) inizia a convenire installare un dns ad-hoc.

### DNS
I DNS consultati (in seguito ad `/etc/hosts`) per la risoluzione degli
indirizzi sono indicati in `/etc/resolv.conf`, uno per linea, con la
keyword nameserver a precedere
``` 
nameserver 212.27.32.176
nameserver 212.27.32.177
nameserver 8.8.8.8
```
Ci sono varie opzioni che si possono introdurre (vedi `man resolv.conf`).

Se si usa DHCP il file potrebbe essere gestito/sovrascritto; per
averne controllo editare `/etc/dhcp/dhclient.conf` aggiungendo la
seguente riga dopo quella di `request`
```
supersede domain-name-servers 12.34.56.78, 12.34.56.79;
```
oppure per dare priorità ai custom lasciando quelli forniti da dhcp
```
prepend domain-name-servers 12.34.56.78, 12.34.56.79;
```
