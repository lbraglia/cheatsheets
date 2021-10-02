# Login, X e fluxbox

## Installazione componenti
```
apt install xorg fluxbox
# driver ATI
apt-get install firmware-linux-nonfree libgl1-mesa-dri xserver-xorg-video-ati
```

## Autologin e avvio del server grafico senza login manager
In assenza di login manager si usano i [servizi di systemd](https://unix.stackexchange.com/questions/401759) e nello specifico:
- cambiare in `/etc/systemd/logind.conf` , da `#NAutoVTs=6` a `NAutoVTs=1`
- creare `/etc/systemd/system/getty@tty1.service.d/override.conf`
  (eventualmente attraverso `systemctl edit getty@tty1`) inserendo il contenuto
  ```
  [Service]
  ExecStart=
  ExecStart=-/sbin/agetty --autologin root --noclear %I 38400 linux
  ```
- abilitare il servizio mediante
  ```
  systemctl enable getty@tty1.service
  ```
- fare il `reboot`
Per l'autoavvio del server grafico al login porre in `.profile` la linea:
```
startx
```


## Configurazione
Per fluxbox fare riferimento a https://wiki.debian.org/it/FluxBox


## `.fluxbox/startup`
Porre i programmi che si vogliono far partire assieme a fluxbox con
esecuzione in background (per evitare che lo script si interrompa
attendendo)␘
```
fbsetbg -r ~/.fluxbox/backgrounds/ &   # background random
xscreensaver -no-splash &              # screensaver
numlockx &                             # attiva blocnum
xset b off &                           # disattiva system bell
```

## `.fluxbox/keys`

```
! Applicativi essenziali
Control Mod1 t :ExecCommand urxvt
Control Mod1 f :ExecCommand urxvt -e mc
Control Mod1 i :ExecCommand firefox
Control Mod1 l :ExecCommand fbrun
Control Mod1 x :ExecCommand xkill
Control Mod1 r :ExecCommand urxvt -e R --no-save --no-restore
Control Mod1 p :ExecCommand urxvt -e python
Control Mod1 u :ExecCommand urxvt -e inizio-giornata
Control Mod1 w :ExecCommand work
Control Mod1 j :ExecCommand do_analysis
Control Mod1 m :ExecCommand compile_math
Control Mod1 s :ExecCommand flameshot # screenshot fighetto editabile
Control Mod1 a :ExecCommand scrot     # screenshot globale ignorante (in ~)

! Gestione del desktop
Control Mod1 d :ShowDesktop
Control Tab :NextWindow (workspace=[current]) !! FBCV13 !!
Control F1 :PrevWorkspace
Mod1 F1 :NextWorkspace
Mod1 F2 :Minimize
Mod1 F3 :Maximize
Mod1 F4 :Close
Mod1 F5 :MaximizeVertical
Mod1 F6 :MaximizeHorizontal

# Mod4 è il tasto Windows
Mod4 F6 :ExecCommand amixer set Master 2%-       # diminuisci volume
Mod4 F7 :ExecCommand amixer sset Master,0 toggle # mute/unmute
Mod4 F8 :ExecCommand amixer set Master 2%+       # aumenta volume

## Multimedia con tasti alternativi/ad-hoc (vedi xev)
# XF86AudioMute :ExecCommand amixer sset Master,0 toggle
# XF86AudioRaiseVolume :ExecCommand amixer set Master 2%+
# XF86AudioLowerVolume :ExecCommand amixer set Master 2%-
```

Nel caso di tasti speciali/multimediali, qualora `xev` non fornisca un
nome del pulsante per come è mappato da X (es `XF86AudioRaiseVolume`)
si può inserire il keycode (un numerico semplice); per ottenerlo, nel
caso `xev` non lo stampi si può installare `evtest` che da il keycode
a livello kernel e aggiungere 8 per ottenere il keycode a livello X
(confrontare il valore restituito di keycode su un tasto semplice es
`a`).
