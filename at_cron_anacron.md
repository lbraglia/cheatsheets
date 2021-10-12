# at cron e anacron

## at
permette di schedulare una operazione ad una certa datao o alla prima
occasione dopo tale scadenza; ideale per sistemi non necessariamente
accesi sempre.

Questo esegue il backup a mezzanotte o appena si accende il pc in seguito
```
at 00:00 -f /bin/backup
```
Per listare i job schedulati non ancora terminati
```
atq
```
mentre per rimuovere un certo job (restituito da `atq`)
```
atrm job_id
```

## cron

si specifica data e ora di un dato task (o intervalli di tempo regolari) 

utile soprattutto per sistemi attivi 24/7 tipo server

Si tratta di un applicativo utilizzato per automatizzare l’esecuzione di
determinati processi o programmi a scadenze temporali ben definite.  
Per il suo funzionamento e’ necessario avere il demone crond attivo e
sviluppare alcuni file di configurazione detti "crontab" `/etc/crontab`
quello di sistema; quelli degli utenti sono in
`/var/spool/cron/crontabs` (un file per ogni utente che ha creato un
crontab, con nome dell’utente).  
Cron ogni minuto controlla i vari crontab ed esegue il comando se e’
arrivato il suo momento. Qualora i crontab vengano modificati, non c’e
bisogno di far ripartire cron perche’ fa tutto lui; aggiorna da solo il
programma di esecuzione

    $ ~ : sudo ls -l  /var/spool/cron/crontabs/
    total 4
    -rw------- 1 luca crontab 235 2007-01-24 17:22 luca

I file tuttavia non sono pensati per esser modificati direttamente ma
mediante il comando crontab.  
Per far partire il demone cron

    $ ~ : sudo /etc/init.d/cron start
    Starting periodic command scheduler: crond.

se da

    $ ~ : sudo /etc/init.d/cron start
    Password:
    Starting periodic command scheduler: crond failed!

vuol dire che il demone era gia’ attivo.

Ora occorre modificare il file di configurazione mediante: per questo
abbiamo il comando "crontab". Se /etc/cron.allow esiste, l’utente deve
avere il proprio nome li segnato per potere usare usare crontab e
modificare i task di cron; se alternativamente cron.allow non esiste, ma
esiste /etc/cron.deny, non bisogna essere in questo file per potere
utilizzare cron.

Per creare o modificare il crontab di un utente:

    crontab -e

Importante: per modificare il crontab di un determinato utente e’
opportuno NON utilizzare su prima di dare il comando, ma di utilizzare
il flag -u prima del nome utente, nel comando crontab.  
L’editor utilizzato e’ quello specificato dalla variabile d’ambiente
VISUAL o EDITOR.  
Gli spazi sono rispettivamente

    minuti ora  gg_de_mese  mese gg_settimanale comando_eseguito

Vi sono alcuni operatori utilizzabili

  - The comma (’,’) operator specifies a list of values, for example:
    "1,3,4,7,8"

  - The dash (’-’) operator specifies a range of values, for example:
    "1-6", which is equivalent to "1,2,3,4,5,6"

  - The asterisk (’\*’) operator specifies all possible values for a
    field. For example, an asterisk in the hour time field would be
    equivalent to ’every hour’..

Ad esempio, per eseguire il comando echo ciao alle 17.30 di ogni giorno,
la configurazione sara’

    30 17 * * * /usr/bin/echo "ciao"

gli asterischi indicano "tutto", quindi il comando dovra’ esser eseguito
tutti i giorni del mese, tutti i mesi (e ovviamente tutti i giornidella
settimana) .  
Per vedere il file appena creato diamo

    crontab -l

Per eliminare il file crontab comandare

    crontab -r

Infine il comando

    crontab -u luca nome_file

serve per installare un novo crontab basandosi sul file mio\_crontab

    $ ~ : crontab mio_crontab 

## Anacron

Diversamente da cron non assume che la macchina funzioni continuamente:
nel primo se la macchina non e’ accesa all’ora programmata per il task,
questo non viene eseguito.  
Quando eseguito (e puo essere anche eseguito come demone in boot)
anacron legge anacron legge i file di configurazione (solitamente
`/etc/anacrontab`).  
Tale file ha due tipi di linee (escluse linee vuote e commenti, fatti
mediante asterisco):

  - linee di descrizione dei job

  - assegnazioni/variabili d’ambiente

Partendo dalle linee dei job, possono avere due forme:

``` 
gg minuti identificatore_job comando_shell
@period_name minuti identificatore_job comando shell        
```

I campi possono esser separati da spazi bianchi o tab. Due esempi
rispettivamente:

    7  5    ciao    echo ciao
    @monthly 5 ciao echo ciao

Nel primo il comando viene eseguito ogni sette giorni, dopo 5 minuti
dall’accensione del pc, viene identificato con ciao e semplicemente
saluta. Il secondo si differenzia per esser mensile.  
Per cio che riguarda le assegnazioni/variabili d’ambiente, la forma e’:

    VARIABILE=valore

ad esempio:

    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

Le assegnazioni prendono forma dalla linea successiva all’assegnazione
stessa, fino alla fine del file. E’ possibile spezzare una linea e
continuare nella seguente la definizione del medesimo task

Per ogni task quindi anacron controlla se esse e’ stato eseguito negli
ultimi n giorni di effettivo utilizzo del pc e se non e’ cosi’ lo
esegue, dopodiche’ aggiorna un file con data di esecuzione er ogni task:
tali file si trovano di default in /var/spool/anacron). S non ci sono
piu’ task anacron esce (a meno che non sia invocato come demome).

I giorni non funzionano come in cron; se ad esempio un utente accende il
pc un giorno e dopo lo tiene chiuso per un mese, dopodiche’ lo reinizia
ad utilizzare con frequenza tutti i giorni, il task verra’ eseguito dopo
6 giorni.

Se un job genera dello standart output o error, questo viene mandato in
mail all’utente che esegue anacron (solitamente root) o all’indirizzo
contenuto nella variable d’ambiente MAILTO, con campo From equivalente
alla variabile LOGNAME. Informazioni su cosa anacron stia facendo sono
inviate a syslog /var/log/syslog

Alcuni opzioni di invocazione utili:

  - `-s` :esegui, facendo si che ogni task non sia eseguito prima che il
    precedente abbia finito

  - `-n` :esegui i job ora ignorano i delay di time specificati
    nell’anacrontab (include l’esecuzione di `-s`)

  - `-t` anacrontab: specifica un determinato anacrontab anziche’ quelo
    di default

  - `-d` : anacron lavora in foreground

  - `-u` : aggiorna solo i tempi di esecuzione ad adesso, senza eseguire
    niente

  - `-S` spooldir: specifica la spooldir per la registrazione dei time
    stamp di esecuzione. Necessario se l’utente normale desidera
    eseguire di proprio conto anacron

  - `-T` : testing dell’anacrontab, se formattato bene ritornera’ 0
    altrimenti mostrera’ l’errore e uscira’ con 1.
