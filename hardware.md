# Hardware

## Detection/stats

```
cat /proc/cpuinfo  # Processori
free -m            # Memoria RAM
df -hT             # Disco fisso
lspci              # Periferiche PCI
lsusb              # Periferiche USB
```

Altri tool: `hwinfo` o `lshw` (con interfaccia gtk se si installa
`lshw-gtk`).


## Sistema a 32 o 64 bit
Per individuarlo
```
l@m740n:~$ uname -a
Linux m740n 5.10.0-8-amd64 #1 SMP Debian 5.10.46-4 (2021-08-03) x86_64 GNU/Linux
```
dove `x86_64 GNU/Linux` ci dice che è un sistema a 64 bit
(se no avremmo avuto semplicemente `x86`
