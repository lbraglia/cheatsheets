# laptop


## Illuminazione schermo
```
xbacklight -inc 10  # aumenta illuminazione
xbacklight -dec 10  # diminuisce illuminazione
xset dpms force off # schermo scuro
```


## Tasti multimediali

Nel caso di tasti speciali/multimediali, qualora xev non fornisca un nome del
pulsante per come è mappato da X (es XF86AudioRaiseVolume) si può inserire il
keycode (un numerico semplice); per ottenerlo, nel caso xev non lo stampi si
può installare evtest che da il keycode a livello kernel e aggiungere 8 per
ottenere il keycode a livello X (confrontare il valore restituito di keycode su
un tasto semplice es a).
