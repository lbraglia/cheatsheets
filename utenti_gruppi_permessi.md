# Utenti, gruppi e permessi

## Intro
`ls -l` mostra la tripletta di permessi (`rwx`) concessi dal
proprietario del file (o da root) a:
- se stesso
- al gruppo cui è assegnato il file
- ai soggetti rimanenti.
È preceduto da:
- `-` per i file normali
- `d` per le directory
- `l` per i collegamenti
- `c` file speciali per IO (maggior parte in /dev)
- `s` socket (simili a socket TCP/IP) per comunicazione tra processi
- `p` pipe (simili ai socket)
- `b` block device (es /dev/sda)
Lettura, scrittura ed esecuzione:
- su file sono immediati (esecuzione pertinente solo per file script o 
  binari eseguibili) 
- su cartelle lettura indica la possibilità di listare il contenuto
  (mediante ls), scrittura di creare file al loro interno, esecuzione
  di spostarsi al proprio interno

## Permessi, cambio, umask
Il modo ottale è il più veloce e i permessi concessi sono identificati
dalla somma
```
4 lettura
2 scrittura
1 esecuzione
```
Ad esempio:
```
chmod 660 file.txt
```
concede lettura e scrittura a proprietario e facenti parti del gruppo sul file
che ha proprietà del file.
Per la *modifica permessi ricorsiva* su cartelle e loro file inclusi:
```
chmod -R 740 directory
```

`umask` permette di impostare i permessi di default sui nuovi
file/cartelle creati (definito come complemento all'ottale). L'umask
di un sistema viene impostata dall'amministratore, può essere indagato mediante
```
umask
```
Di fatto l'umask riportato è quello per le cartelle, mentre per i file
viene ignorata l'istruzione sull'eseguibile (che va data con `chmod`).
Per impostare un umask differente di solito in `~/.bashrc` si da
```
umask 077
``` 


## Utenti

### Creazione/rimozione
Per la creazione o rimozione di un utente, da root
```
adduser utente
deluser utente
```

### A quali gruppi appartiene
```
id utente
```

## Gruppi

### Creazione/rimozione
```
addgroup utente
delgroup utente
```

### Assegnazione/rimozione di utente ad un gruppo
```
adduser utente gruppo
deluser utente gruppo
```

### Assegnazione di un file
```
chgrp gruppo file
```

## Cambio login utente (a root)
```
su -
sudo -i
```

<!-- % \subsection{Suid e Sgid} -->
<!-- % Oltre ai permessi elencati in precedenza per ogni file ci sono -->
<!-- % altri 3bit che indicano ulteriori proprieta' del file SUID (set -->
<!-- % user identification), SGid (set group identification) e Sticky -->
<!-- % (save text image). Si trattadi attributi speciali che riguardano -->
<!-- % prevalentemente i file eseguibili  -->
<!-- % \begin{verbatim} -->
<!-- % 		  `rwxrwxrwx' -->

<!-- % SUID = 4 =	  `--s------' -->
<!-- % SGID = 2 =	  `-----s---' -->
<!-- % Sticky = 1 =	  `--------t' -->
<!-- % \end{verbatim} -->
<!-- % L'indicazione prende il posto del permesso di esecuzione. Nel -->
<!-- % caso in cui il permesso di esecuzione corrispondente non sia -->
<!-- % attivato, la lettera (s o t= appare maiuscola.  -->

<!-- % Su un determinato file eseguibile (non uno script, perche' in tal -->
<!-- % caso l'ID del processo e' quello dell'interprete, non dello -->
<!-- % script) e' anche possibile impostare il bit di permesso relativo -->
<!-- % a SUID, SGID e Sticky Bit  -->

<!-- % SUID sta per Set User ID: il bit SUID del permesso. Se il -->
<!-- % proprietario di un file binario setta il bit SUID rende possibile -->
<!-- % agli altri utenti di eseguire il file come se essi ne fossero i -->
<!-- % proprietari. Se ad esempio il root setta il SUID sui suoi -->
<!-- % programmi (ossia tutti quelli in /bin /sbin e /usr/bin/) da la -->
<!-- % possibilita' agli utenti di utilizzarli come se essi fossero -->
<!-- % root. Se si desidera concedere agli utenti la possibilita' di -->
<!-- % eseguire alcuni binari come superuser, si stia ben attenti a -->
<!-- % quali si sceglie. -->

<!-- % Il proprietario dell'eseguibile che setta il SGID (Set Group ID), -->
<!-- % permette agli altri utenti di eseguire il file come facessero -->
<!-- % parte del gruppo cui appartiene lui stesso. Anche in questo caso -->
<!-- % attenzione ad una gestione troppo leggera di questo strumento. -->

<!-- % Settando lo Sticky Bit fa si che una volta che l'applicazione va -->
<!-- % in esecuzione essa dovrebbe rimanere in memoria cosi' se un nuovo -->
<!-- % (o lo stesso) utente vuole utilizzare quel programma risparmia un -->
<!-- % po di tempo in apertura/caricamento/inizializzazione -->

<!-- % Come impostare suid e sgid e sticky bit? -->
<!-- % \begin{verbatim} -->
<!-- % SUID	       chmod u+s roba -->
<!-- % SGID	       chmod g+s roba -->
<!-- % Sticky bit     chmod  +t roba -->
<!-- % \end{verbatim} -->
<!-- % Possono esser settati anche mediante numero: SUID(4), SGID(2), -->
<!-- % sticky bit(1). Una quarta cifra viene posta prima delle 3 cifre -->
<!-- % solite di permesso  -->
<!-- % \begin{verbatim} -->
<!-- % SUID	       chmod 4xxx roba (dove xxx e' il permesso normale su roba, es 644) -->
<!-- % SGID	       chmod 2xxx roba -->
<!-- % Sticky bit     chmod 1xxx roba -->

<!-- % SUID+SGID      chmod 6xxx roba (come nei permessi sono possibili combinazioni tra i tre sopra) -->
<!-- % SGID+Sticky    chmod 3xxx roba -->
<!-- % \end{verbatim} -->
<!-- % Ovviamente per deimpostarlo si usa sempre la notazione con - al posto di +. -->
<!-- % Per deselezionare, dal punto di vista numerico -->
<!-- % \begin{verbatim} -->
<!-- % chmod 0xxx roba -->
<!-- % \end{verbatim} -->

<!-- % Cosa ( settato in un file eseguibile che contiene un file -->
<!-- % eseguibile, il sistema cambia temporaneamente lo User-ID -->
<!-- % dell'utente corrente con quello del creatore di quel file durante -->
<!-- % l'esecuzione del programma. Il cambiamento perdura SOLO per -->
<!-- % l'esecuzione del programma specificato contenuto nel file -->
<!-- % eseguibile. Un esempio di SUID settato ) Succede ( il comando -->
<!-- % passwd che consente di cambiare la password al proprio utente. -->

<!-- % - SGID (set group id) valgono le stesse considerazioni fatte per il SUID, cambia solo il riferimento che ) Se ( il gruppo e non l'utente. -->
<!-- % - STICKY: se ) Impostati ( settato consente di cancellare i file al suo interno solamente al proprietario, anche se l'utente ha i permessi di scrittura su quel file. -->

<!-- % Il primo campo, a seconda del simbolo che ha impostato indica: -->
<!-- % d = Directory; -->
<!-- % - = File; -->
<!-- % l = Link; -->
<!-- % b = Block device; -->
<!-- % c = Character device; -->
<!-- % Dove b e c risiedono all'interno della directory dei device (/dev) -->

<!-- % Si definiscono con la cifra delle migliaia -->
<!-- % 1) SETUID: -->
<!-- % NOTAZIONE: Viene identificato con s sul permesso di execute in User (se User non ha il permesso di execute si denota con S). Es. -rwsrw-r-- -->
<!-- % USO: Si imposta col codice numerico 4. Es. # chmod 4xxx nome_file -->
<!-- % 2) SETGID: -->
<!-- % NOTAZIONE: Viene identificato con s sul permesso di execute in Gruppo (se Gruppo non ha il permesso di execute si denota con S). Es. -rwxrwsr-- -->
<!-- % USO: Si imposta col codice numerico 2. Es. # chmod 2xxx nome_file -->
<!-- % 3)Sticky Bit: -->
<!-- % NOTAZIONE: Viene identificato con t sul permesso di execute in Other (se Other non ha il permesso di execute si denota con T). Es. -rwxrw-r-t -->
<!-- % USO: Si imposta col codice numerico 1. Es. # chmod 1xxx nome_file ) sulle cartelle o su altri file non script?? TODO -->
<!-- % If SGID is set on a directory, all new created files inside this folder won't get the main group id of the creator. Instead, they will be created with the group id of the folder. E.g. the SGID is set for the testfolder "folder1" and it has the group id for "www". Now, if the root user creates a file inside folder1 the group id for this file will not be "root" but "www". SUID and SGID can be set at the same time. -->
<!-- % Normally, if a folder can be written by others, all files inside can be deleted or modified by others, no matter who the owner of the file is. If the sticky bit is set, files inside this directory can only be deleted or modified by the owner of the file. -->

<!-- % ###### ##### #### -->

<!-- % What do capital letters mean when I use the "ls -l" command ? -->
<!-- % There are capital letters for t (sticky bit) or s (SUID or SGID) if the right for execution is not set at this postion (user, group, others). That's because the SUID/SGID and the right for execution have the same position. A capital letter indicates that the underlying executable bit is not set. And this is also a warning signal. Such a configuration is at least strange. SUID, SGID and sticky bit make no sense without the right for execution. -->
<!-- % Here's an example: -->
<!-- % In the first part the executable bit of the user is not set and the result is a capital S. In the second part the executable bit of the user is set and the result is a normal s. -->

<!-- % ls -l -->
<!-- % d-----x--x ... -->
<!-- % chmod u+s folder1/ -->
<!-- % ls -l -->
<!-- % d--S--x--x ... -->

<!-- % ls -l -->
<!-- % d--x--x--x ... -->
<!-- % chmod u+s folder1/ -->
<!-- % ls -l -->
<!-- % d--s--x--x ... -->


<!-- % What does readable, writeable and "executable" for directories exactly mean ? -->
<!-- % -To be able to read a directory means that a process can get a list of the content which is inside it -->
<!-- % (if it is allowed to enter) -->
<!-- % -To be able to write to a directory means that a process can create and delete things inside it -->
<!-- % (if it is allowed to enter) -->
<!-- % -To be able to "execute" a directory means that a process is allowed to enter it, nothing else -->

<!-- % Without the right "executable" the process cannot enter a directory. That means, the right readable or writeable alone doesn't help at all. The same happens if "executable" is the only right the process has. Then it cannot get a list of the content and it cannot create or delete things inside the directory. -->
