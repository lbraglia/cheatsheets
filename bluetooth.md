# bluetooth

Fonte [qui](https://wiki.debian.org/BluetoothUser):

## Installazione e setup
```
apt install bluetooth bluedevil
service bluetooth start
```

## Pairing

Utilizziamo `bluedevil-wizard`, fatto partire ci dice i device che vede
per il pairing. Comandare `help` per info sui comandi

### Controller xbox

- Accendere il controller premendo sul pulsante con la x
- premere sul pulsante di pairing per 3 secondi e rilasicare
- far partire `bluedevil-wizard` da linea di comando
- effettuare il pairing

https://support.xbox.com/en-US/help/hardware-network/accessories/connect-and-troubleshoot-xbox-one-bluetooth-issues

### Controller ps4

- da controller spento tenendo premuto il tasto SHARE, tieni premuto
  il tasto PS finché la barra luminosa non inizia a lampeggiare
- far partire `bluedevil-wizard` da linea di comando
- effettuare il pairing

https://www.playstation.com/it-it/support/hardware/ps4-pair-dualshock-4-wireless-with-pc-or-mac/#blue
