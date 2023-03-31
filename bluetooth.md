# bluetooth

Fonte [qui](https://wiki.debian.org/BluetoothUser):

## Installazione e setup
```
apt install bluetooth
service bluetooth start
```

## Pairing
Utilizziamo `bluetoothctl` da linea di comando

```
l@ambrogio:~$ bluetoothctl 
Agent registered
[CHG] Controller 04:42:1A:5A:3B:88 Pairable: yes
```
Dare `help` per i comandi disponibili.
Attivare il power sulla chiavetta usb con
```
power on
```
Procedere alla ricerca di device da associare
```
# scan on
Discovery started
[CHG] Controller 04:42:1A:5A:3B:88 Discovering: yes
```
Se non mostra niente staccare e riattaccare lo scan fino a che non
mostra devices
```
[bluetooth]# scan off
Discovery stopped
[CHG] Controller 04:42:1A:5A:3B:88 Discovering: no
[bluetooth]# scan on
Discovery started
[CHG] Controller 04:42:1A:5A:3B:88 Discovering: yes
[NEW] Device 3C:FA:06:6A:E1:B4 Xbox Wireless Controller
[bluetooth]# pair 3C:FA:06:6A:E1:B4
Attempting to pair with 3C:FA:06:6A:E1:B4

```

### Controller xbox

- Accendere il controller premendo sul pulsante con la x
- premere sul pulsante di pairing per 3 secondi e rilasicare

https://support.xbox.com/en-US/help/hardware-network/accessories/connect-and-troubleshoot-xbox-one-bluetooth-issues

### Controller ps4

- da controller spento tenendo premuto il tasto SHARE, tieni premuto
  il tasto PS finché la barra luminosa non inizia a lampeggiare
- effettuare il pairing

https://www.playstation.com/it-it/support/hardware/ps4-pair-dualshock-4-wireless-with-pc-or-mac/#blue
