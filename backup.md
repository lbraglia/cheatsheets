# Backup

## `pcloud` con `rclone`
Setup [qui](https://rclone.org/pcloud/) poi
```bash
rclone ls pcloud: # lista tutto
rclone lsd pcloud: # lista directory
rclone ls pcloud:fotine/ # lista tutto nella directory
```
per il backup che segua i link ed ignori da exclude.txt
```
rclone copy --copy-links --exclude-from .backup/exclude.txt .backup pcloud:
```




## Backup rete locale con `netcat` e `tar`

Sulla macchina destinazione:
```
netcat -l -p 9000 | tar xv
```
Sulla macchina che invia

```
tar cvf - cartella | netcat ip_macchina_destinazione 9000
```

## Backup su stesso filesystem mediante rsync
```
rsync -arvh dir1 dir2
```
copia e sincronizza da dir1 su dir2

