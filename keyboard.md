# Tastiera

## Riconfigurazione layout/lingua
```
dpkg-reconfigure keyboard-configuration 
systemctl restart keyboard-setup
```

## Configurazioni comuni
```
xset b off   # Disattivazione system bell (sotto X)
numlockx on  # Attivazione tastierino numerico
```

## Rilevazione tasti X
```
xev
```

