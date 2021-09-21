# fluxbox

## keys

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
Control Mod1 s :ExecCommand scrot --focused # screenshot focus
Control Mod1 a :ExecCommand scrot           # screenshot globale

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
# None XF86AudioMute :ExecCommand amixer sset Master,0 toggle
# None XF86AudioRaiseVolume :ExecCommand amixer set Master 2%+
# None XF86AudioLowerVolume :ExecCommand amixer set Master 2%-
```
