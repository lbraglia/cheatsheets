# Backup

## Backup rete locale con `netcat` e `tar`

Sulla macchina destinazione:
```
netcat -l -p 9000 | tar xv
```
Sulla macchina che invia

```
tar cvf - cartella | netcat ip_macchina_destinazione 9000
```



