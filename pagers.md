# pagers


## head, tail
Stampano le prime o ultime righe di un file (di default 10,
modificabili con `-n`)

In `tail` vi è l'opzione `-f` (follow) che permette di vedere gli
aggiornamenti in coda ad un file o anche più file contemporaneamente
```
tail -f file1.txt file2.txt
```
Se la visualizzazione di tanti log contemporaneamente diviene scomoda
- se non ci interessa sapere da quale file provenga l'aggiornamento utilizzare
  `-q` (quiet)
- alternativamente provare `multitail`.

## less e famiglia (zless, bzless, xzless)


## more (zmore, bzmore)
