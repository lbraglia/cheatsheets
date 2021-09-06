# help


## man
```
man <#sez> comando
```
Se `<#sez>` manca verrà restituito il comando della prima sezione disponibile; le sezioni del manuale sono:
1. comandi eseguibili dalla riga di comando; 
2. chiamate di sistema (funzioni fornite dal kernel); 
3. funzioni di libreria (fornite dalle librerie di sistema); 
4. dispositivi (sui sistemi Unix-like, questi sono file speciali, di solito posti nella directory /dev/); 
5. file di configurazione (formati e convenzioni); 
6. giochi; 
7. insiemi di macro e standard; 
8. comandi di amministrazione del sistema; 
9. routine del kernel. 

## pinfo
La documentazione del progetto GNU utilizza info; per visualizzarla
comodamente utilizzare `pinfo` dall'omonimo pacchetto

## Documentazione del pacchetto
Guardare in `/usr/share/doc` ogni pacchetto ha una cartella
`/usr/share/doc/pacchetto`; se la documentazione è molta vi potrebbe
essere un pacchetto ad hoc e bisogna dunque guardare in
`/usr/share/doc/pacchetto-doc`.

In particolare:
- `/usr/share/doc/pacchetto/README.Debian` le peculiarità della
  pacchettizzazione Debian (es rispetto all'originale)
- in `/usr/share/doc/pacchetto/examples/` sono forniti degli esempi di
  file di configurazione
