# Gaming on Debian

## Configurazione scheda grafica

* Per il setup di base https://wiki.debian.org/AtiHowTo
* per controllo di problemi firmware vedere [qui](https://bugs.debian.org/cgi-bin/pkgreport.cgi?pkg=firmware-amd-graphics)
* per aggiornamento driver su debian per schede nuove, vedere [qui](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git):
  di base ho scaricato il firmware e rimpiazzato (rinominato lowercase) in `dpkg -L firmware-amd-graphics`.

## Testing delle performance/monitoraggio

* Per il testing delle performance vedere https://wiki.debian.org/Mesa
* Monitoraggio hardware CPU/GPU: mangohud, pacchetto lm-sensors (temperature)

## Configurazione pad bluetooth

Vedere la sezione [bluetooth](bluetooth.md).

## Steam

* istruzioni aggiornate qui https://wiki.debian.org/Steam

```
apt install steam mangohud lm-sensors
```

### FPS cap

Alternative in ordine decrescente di preferenza, allo stato attuale:

* installare https://gitlab.com/torkel104/libstrangle mediante `stow` o altri trick spiegati in https://wiki.debian.org/DontBreakDebian
* usare mangohud con `fps_limit` tra le opzioni
* studiare [gamescope](https://wiki.archlinux.org/title/Gamescope)


### Useful launch option

```
strangle 60 %command%                # cappare a 60 con libstrangle
PULSEAUDIO_LATENCY_MSEC=60 %command% # audio crackling
```
