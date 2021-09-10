# Recovery

## Boot con permessi di amministratore

Aggiungere 1 al termine della linea di GRUB per bootare il runlevel 1
(single user root).

## Boot con disco live
Alternativamente:
- utilizzare un disco di installazione Debian con `Graphical Rescue
  Mode` (tra le opzioni avanzate) che dopo aver mostrato le partizioni
  sulle quali è possibile intervenire (hanno il nome dell'host da
  salvare nel path) eventualmente permette l'avvio di una shell di root
  nel sistema considerato (es per reinstallare GRUB nel MBR).
- utilizzare una Debian live (ambiente grafico aiuta con la
  localizzazione) e ottenere i permessi di root con `sudo su`
