# Git


## Aiuto 
La guida di riferimento si trova [qui](http://git-scm.com/book/en)

Per ottenere aiuto su un determinato comando
```
$ git help <verb>
$ git <verb> --help
```

## File di configurazione
I file di configurazione sono:
- `/etc/gitconfig`: per tutti gli utenti di una determinata macchina
- `~/.gitconfig`: contiene le impostazioni valide per un singolo
  utente
- `path_progetto/.git/config`: file di configurazione per uno
  specifico progetto

### Listare le configurazioni attive
```
l@np350v5c:~$ git config --list
```

### Impostare configurazioni
Per dare le configurazioni occorre utilizzare `git config`:

- per configurazioni globali a livello di singolo utente (per tutti i
  suoi repository) è necessario utilizzare l'opzione `--global`
  (scrive le configurazioni nel file di configurazione globale)
	```
	l@np350v5c:~$ git config --global user.name "lbraglia"
	l@np350v5c:~$ git config --global user.email "lbraglia@gmail.com"
	```
	
- per configurazioni (che sovrascrivono le globali se presenti) per un
  dato repository, da dentro la cartella del progetto diamo il config
  senza il `--global` (questo modifica il file `.git/config`
  all'interno della directory del progetto)
	```
	l@np350v5c:~/test-repo$ git config user.name "foo" 
	l@np350v5c:~/test-repo$ git config user.name
	foo 
	l@np350v5c:~/test-repo$ cd 
	l@np350v5c:~$ git config user.name
	lbraglia 
	``` 
	
	
	

## Creazione di un progetto
Per creare un nuovo progetto possiamo avere due strade:
- creare un nuovo progetto inizializzando una directory
  locale
- clonare un progetto esistente


### Inizializzare un nuovo progetto
Per iniziare a tenere sotto git una directory con codice
esistente, ci si sposta in tale directory e si comanda `git init`
```
l@np350v5c:~$ mkdir test-repo
l@np350v5c:~$ cd test-repo/
l@np350v5c:~/test-repo$ git init
Inizializzato un repository Git in /home/l/test-repo/.git/
```
Questo crea una nuova subdirectory `.git` che contiene i
file necessari al funzionamento. Allo stato attuale ancora nulla
è tenuto sotto git.

### Clonare un progetto esistente
Se si vuole una copia di un progetto esistente (es per fornire
contributi) il comando necessario è `git clone` (non è un
`checkout` che guarda solo all'ultima versione ma si porta
a dietro tutta la storia del repository). Ad esempio
```
git clone git://github.com/schacon/grit.git
```
creerà una directory `grit`, inizializza al suo interno la
directory `.git`, effettua il download del repository. Se
si vuole effettuare il download in un'altra directory comandare
```
git clone git://github.com/schacon/grit.git my_dir
```
Git ha diversi protocolli per il download (git, https, ssh)

## Modificare un progetto

### Stato dei file
In una directory git, i file possono essere
- \textbf{tracked}: presenti nell'ultimo snapshot. Questi
  file possono essere \emph{unmodified} (non modificato rispetto
  all'ultima versione), \emph{modified} (modificato rispetto
  all'ultima versione), \emph{staged} (segnato per il
  `commit`)
- \textbf{untracked}: tutti i restanti file non tracciati

Quando si effettua un `clone} tuti i file sono
\emph{tracked} e \emph{unmodified} .\\
Le fasi che bisogna seguire per aggiungere un file al repository
remoto sono
- \textbf{creare} il file
- \textbf{aggiungere} il file per far si che venga tracciato
  sotto `git`
- fare il \textbf{commit}, ovvero salvare una versione
  \emph{locale} delle modifiche effettuate sin ora
- fare il \textbf{push}, ovvero portare tutte le modifiche
  locali al server remoto


### Aggiungere file
Dopo aver creato un file
```
l@np350v5c:~/test-repo$ touch foo
l@np350v5c:~/test-repo$ echo "test" > foo 
```
Vediamo lo stato
```
l@np350v5c:~/test-repo$ git status 
Sul branch master

Commit iniziale

Untracked files:
  (use "git add <file>..." to include in what will be committed)

foo

nothing added to commit but untracked files present (use "git
add" to track)
```
il file non è tracckato: significa che git vede un file che non
vi era nell'ultimo snapshot.\\
Per \textbf{aggiungere} dei file si usa `git add`: 
```
l@np350v5c:~/test-repo$ git add foo
l@np350v5c:~/test-repo$ git status 
Sul branch master

Commit iniziale

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

new file:   foo
```
Ora si puo vedere che è il file è \textbf{staged} (ovvero tenuto
in conto per un `commit`)  perchè citato sotto
`Changes to be committed}

Si ha anche un \emph{file non staged} \textbf{se si modifica un
  file già tenuto sotto revisione}. In tal caso ridando
`git add` sul file modificato. Occorre fare git add ogni
volta che si effettua una modifica, alternativamente il file
pronto per lo stage sarà solamente l'ultima versione per la quale
si è fatto l'`add`

Alcune opzioni comode
```
git add .             # aggiunge tutti i NUOVI file
git add -u            # aggiorna per file rinominati/eliminati
git add -A            # aggiunge nuovi file e aggiorna rinom/elim
```

### Vedere le modifiche apportate
Per vedere non quali file sono cambiati ma come si usa
`git diff`. Ad esempio in seguito a modifica che non
abbiamo ancora aggiunto
```
l@np350v5c:~/test-repo$ cat foo 
test
l@np350v5c:~/test-repo$ echo bar >> foo
l@np350v5c:~/test-repo$ cat foo 
test
bar
```
comandiamo `git diff`, che confronta la versione attuale
con quella nella staging area
```
l@np350v5c:~/test-repo$ git diff

diff --git a/foo b/foo
index 9daeafb..2bdc76e 100644
--- a/foo
+++ b/foo
@@ -1 +1,2 @@
 test
+bar
```
Se si vuole vedere la differenza di quello che andrà in commit,
il comando è 
```
l@np350v5c:~/test-repo$ git diff --cached 

diff --git a/foo b/foo
new file mode 100644
index 0000000..9daeafb
--- /dev/null
+++ b/foo
@@ -0,0 +1 @@
+test
```

### Fare il commit
Arrivati a questo punto vogliamo salvare/markare lo stato attuale
della copia locale, con i nuovi file e le modifiche a vecchi,
aggiunte entrambe mediante `git add`.\\
Utilizziamo `git commit`
```
l@np350v5c:~/test-repo$ git commit 
[master (root-commit) b044d71] asd
 1 file changed, 1 insertion(+)
 create mode 100644 foo
```

Se si da `git commit -a` vengono date al commit tutte le
modifiche fatte ai file già tenuti sotto revisione, anche se in
precedenza non si era fatto l'add.

### Ottenere un log
Si usa `git log` che di default lista i \emph{commits}
effettuati nel repository in ordine dal più recente al più vecchio.\\
Vi sono diverse opzioni, una delle più utili è `-p` che
lista i diff intervenuti in ogni commit, o `--stat` che
lista alcune statistiche (file modificati e numero di lineee modificate)

### Annullare le modifiche
Se abbiamo effettuato delle modifiche ad un file che non vogliamo
tenere e vogliamo farlo tornare alla versione dell'ultimo commit comandiamo
```
git checkout -- file
```


### Rimuovere un file
Per rimuovere un file si usa
```
git rm nome_file
```

### Rinominare
Per rinominare un file si usa
```
git mv vecchio nuovo
```
il che è equivalente a 
```
mv vecchio nuovo
git rm vecchio
git add nuovo
```


### Ignorare alcuni file
A volte alcuni file o tipologie di file debbono esser ignorati/untracked
(compilazioni, log ecc); si può procedere
- creando un file `.gitignore` sotto la directory del
  progetto
- creare `~/.config/git/ignore` per una
  configurazione a livello di utente

e specificando in esso un pattern del genere, ad esempio:
```
$ cat .gitignore
*.[o]               # file oggetto
*~                  # file di backup
```
I commenti sono fatti con l'asterisco


## Lavorare con repository remoti
I repository remoti sono una versione del progetto che è hostata
in internet; per la gestione di repository remoti è necessario
sapere come:
- aggiungere/modificare/cancellare un repository remoto
- push/pull versioni dal repository
- altro


### Mostrare i repository
Per vedere quali remoti sono configurati bisogna comandare `git
remote` all'interno della cartella
```
l@np350v5c:~/test-repo$ git remote
l@np350v5c:~/test-repo$ 
```
Se non viene resitutito nulla vuol dire che non è stato
configurato nessun remote.\\
Se viene restituito `origin` significa che è lo stesso
repository dal quale si è clonato.\\
Per mostrare verbosamente il repository si aggiunge l'opzione `-v`
```
l@np350v5c:~/src/chtp$ git remote
origin

l@np350v5c:~/src/chtp$ git remote -v
origin https://github.com/lbraglia/chtp.git (fetch)
origin https://github.com/lbraglia/chtp.git (push)
```

### Aggiungere un repository remoto
Per aggiungere un repository remoto
```
git remote add nome git://githun.../asd.git
```
ad esempio dopo aver creato un repository su github senza
l'inizializzazione con readme
```
l@np350v5c:~/test-repo$ git remote add original https://github.com/lbraglia/test-repo.git
l@np350v5c:~/test-repo$ git remote -v
originalhttps://github.com/lbraglia/test-repo.git (fetch)
originalhttps://github.com/lbraglia/test-repo.git (push)
```

### Aggiornare un repository
Per aggiornare un repository locale in base a uno remoto
```
git fetch [remote-name]
```
se si è fatto il clone di un repository non serve specificare il
nome del remoto perchè git usa di default `origin`

E' importante dire che il comando fetch porta i dati al tuo
repository locale, non li mergia automaticamente con il lavoro
svolto in locale. Il merge è manuale

### Push
Una volta che abbiamo effettuato sufficienti modifiche locali, se
vogliamo pubblicare tali modifiche sul server remoto. La versione
minimale è 
```
git push
```
Se è necessario specificare un remote e un branch
```
git push [remote] [branch]
```

### Esempio: aggiungere un remote di backup
```
# primo setup
git remote add backup https://lbraglia@github.com/lbraglia/repo.git

# poi
git push         # push su origin
git push backup  # push su backup
```

## Usare il branching (diramazioni)
A volte si sta lavorando a un progetto con una versione che è
utilizzata da molta gente. Non volendo editare quella versione,
un modo è creare un branch. In molti strumenti come Git questo è
un processo dispendioso, spesso richiede la creazione di una
nuova copia della directory dell'intero codice sorgente .\\
Git crea ramificazioni in modo incredibilmente semplice e
leggero, permettendo operazioni di diramazione praticamente
istantanee come lo sono anche i passaggi da un ramo ad un altro.

### Cosa è un ramo
Git non salva i dati come una serie di cambiamenti o codifiche
delta, ma come una serie di istantanee (snapshot).
Quando si fa un commit, git salva un commit object che contiene
puntatori alla snapshot del contenuto che si è mandato in stage,
i metadati dell'autore, ed eventualmente dei puntatori al/ai
commit che erano diretti parenti (per un commit nomrale, più
parenti se il commit deriva dal mergere di due o piu branch) .

Ad esempio diciamo di iniziare un progetto con tre file
```
$ git add README test.rb LICENSE
$ git commit -m 'initial commit of my project'
```
con il commit:
- git fa i checksum di tutte le directory del progetto e lo
  salva come un oggetto `tree` nel repository di git
- in seguito crea un commit object che ha i metadati e i
  puntatori al root project tree object, pertanto può ricreare la
  snapshot quando necessario

Al momento attuale il repository contiene cinque oggetti:
- un `blob} per ognuno dei tre file che ne ha il
  contenuto (indirizzabili attraverso una chiave univoca)
- un `tree` che lista il contenuto della directory e
  specifica quali file sono memorizzati e quali blob gli
  corrispondono (mediante puntatori alle chiavi univoche)
- un `commit} object che ha punta al tree object e
  include anche altre informazioni 

Ad ogni commit successivo, viene creato un commit object che
oltre alla snapshot, include info sul commit object che è
parent.\\
Un branch in git è semplicemente un puntatore ad uno dei commit
fatti. Il nome del branch di defualt in git è `master`. Il
master branch punta sempre all'ultimo commit che si è fatti (dal
quale a sua volta può risalire a commit e snapshot precedenti).

Quando si \textbf{crea un nuovo branch} chiamato ad esempio
`testing` attraverso
```
git branch testing
```
git crea un nuovo puntatore (simile a master) che punta
all'ultimo commit (sul quale è anche master). \\
Per vedere su \textbf{quale branch si sta lavorando}
```
git branch
```
Tuttavia attualmente stiamo continuando a lavorare sul
`master`; per \textbf{switchare ad un branch esistente} si
usa il comando `checkout`
```
git checkout testing
```
Per creare un branch e switchargli dentro subito
```
git checkout -b testing2
```
Nel caso in cui si faccia un commit lavorando in testing: viene
creato un nuovo commit object che (a parte il resto) punta al
commit precedente, ovvero al commit del master. Attualmente
quindi la versione testing include cose che non vi sono nella
master.\\
Per ritornare al branch master
```
git checkout master
```
Se all'interno della `master` effettuiamo ora delle
modifiche e facciamo il commit viene creato un commit object che
punta al precedente (al quale punta anche la `testing`).
Quello che è accaduto è che la project history si è duplicata da
un certo commit in poi.

## Branching e merging di base
Ora vediamo un semplice esempio di branching(diramazione) e
mergin (fusione) in un flusso di lavoro che potresti
seguire. Supponiamo questi passaggi:
\begin{enumerate}
- Lavori su progetto.
- Crei un ramo per uno pezzo sperimentale su cui stai lavorando.
- Fai un po' di lavoro in questo nuovo ramo.
\end{enumerate}
A questo punto, ricevi una chiamata per un problema critico e hai
bisogno subito di risolvere il problema. Farai in questo modo:
\begin{enumerate}
- Tornerai indietro nel tuo ramo di produzione (`master`).
- Creerai un ramo in cui aggiungere la soluzione.
- Dopo aver testato il tutto, unirai il ramo con il fix
  al master, ponendolo in produzione.
- Ritornerai al ramo di sviluppo
\end{enumerate}


### Branching di base
Ad esempio per correggere l'issue numero 53, dal master
```
$ git checkout -b testing_new_feat
Switched to a new branch 'testing_new_feat'
```
modifico il file
```
emacs foo.cpp
git commit -a -m 'new_feature: xyz'
```
Se ci giunge la richiesta di fissazione del bug, non dobbiamo
necessariamente fixarlo dentro il branch della nuova
feature. Bisogna tornare al branch `master`
```
$ git checkout master
Switched to branch 'master'
```
Fatto questo, lo stato del master è esattamente come l'hai lasciato prima di
passare al branch sulla nuova feature (file inclusi); in seguito
ad aver cambiato il branch git ci ha messo a posto la directory a
come era.\\
Pertanto procediamo alla modifica creando un nuovo branch
```
$ git checkout -b fixbug51
Switched to a new branch 'fixbug51'
$ emacs bar.cpp
$ git commit -a -m 'fixed the broken email address'
```
Arrivati a questo punto dobbiamo incorporare la modifica nel
codice di produzione
```
$ git checkout master
$ git merge fixbug51
Updating f42c576..3a0874c
Fast-forward
 README | 1 -
 1 file changed, 1 deletion(-)
```
Ora che il bug è stato fixato:
- eliminiamo il branch di fix del bug, poichè non piu necessario
```
$ git branch -d fixbug51
Deleted branch fixbug51 (was 3a0874c).
```
- torniamo a lavorare sul ramo sperimentale
```
$ git checkout testing_new_feat
```


Da notare come attualmente `testing_new_feat` non includa
le modifiche fatte grazie a `fixbug51` e presenti in
`master`. Se abbiamo bisogno di tirarli dentro si può
- si puo fare il merge del `master` nel
  `testing_new_feat` 



### Merging di base
Supponendo che il lavoro su `testing_new_feat` sia
completo e funzionante e deve esser mergiato. Per farlo ci
spostiamo nel master e comandiamo il merge
```
$ git checkout master
$ git merge testing_new_feat
```
A questo punto dato che stiamo mergiando su un repository che nel
frattempo è cambiato, git deve fare qualcosa di piu. Consideriamo
che ci sono tre branch di interesse a nostra disposizione:
- il master attuale (in seguito ad integrazione) nel quale
  vogliamo aggiungere la feature derivante dal master precedente
- il master precedente (da cui master attuale e versione di
  sviluppo derivano
- la versione di sviluppo

Quello che fa git è un merge a tre vie di queste, e crea una
nuova snapshot e un oggetto di commit che punta ad essa.  Questo
tipo di commit è un merge commit ed è particolare nel senso che
ha più di un parente (differentemente da un commit normale).\\
Git fa tutto automaticamente, in particolare la scelta del
parente comune per creare il merge; per questo è molto facile
fare il merge.  

\textbf{A volte il processo automatico sopra presentato non va
  liscio} per la presenza di conflitti. Se si sono cambiate le
stesse parti del medesimo file, in maniera differente in due
branch che stiamo cercando di mergiare, Git non è in grado di
fare tutto automaticamente. Ad esempio un file `foo.cpp`
che crea problemi potrebbe dare origine
```
$ git merge testing_new_feat
Auto-merging foo.cpp
CONFLICT (content): Merge conflict in foo.cpp
Automatic merge failed; fix conflicts and then commit the result.
```
git qui non fa il merge ma stoppa il processo in attesa che il
programmatore risolva il conflitto.\\
Se si vuol guardare quali file non sono stati mergiati si usa 
```
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

        both modified:      foo.cpp

no changes added to commit (use "git add" and/or "git commit -a")
```
Git in questi casi aggiunge automaticamente delle linee al file
per denotare le differenze
```
<<<<<<<< HEAD
std::cout << foo;
=======
std::cout << bar;
>>>>>>>  testing_new_feat
```
HEAD contrassegna la versione in master (che si trova al di sopra
degli `===`, mentre al di sotto, `testing_new_feat`
quella nell'omonimo branch. Per risolverlo semplicemente editiamo
il file togliendo tutto il markup e lasciando una via di mezzo
delle due cose
```
std::cout << foo << bar;
```
Se si vogliono utilizzare tool grafici per risolvere gli issue si
usa:
```
git mergetool
```

In seguito rifacciamo `git status` per verificare che
tutto sia a posto
```
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   foo.cpp
```
Dopo aver risolto tutti i conflitti su tutti i file problematici,
comandiamo `git add` sui file con ex-conflitti per
marcarli come risolti; mandarli attraverso `git commit` in
stage attraver li marca come risolti in git.\\
Nel messaggio di commit si può specificare come si è deciso di
risolvere il conflitto.


## Gestione dei branch
git branch serve da solo per listare i branch disponibili
```
$ git branch
  iss53
* master
  testing
```
l'asterisco serve per indicare il branch attualmente in uso (e su
cosa hanno effetto i commit).

Per vedere l'ultimo commit su tutti i branch
```
$ git branch -v
  iss53   93b412c fix javascript issue
* master  7a98805 Merge branch 'iss53'
  testing 782fd34 add scott to the author list in the readmes
```

listare i branch che si ha giamergiato nel branch
correntemente in uso
```
$ git branch --merged
  iss53
  * master
```
listare i branch che non si ha gia mergiato nel branch
correntemente in uso
```
$ git branch --no-merged
  testing
```


## Workflow dei branch
Dato che Git usa un sistema semplice di fusione a tre vie, unire
un ramo con un altro più volte dopo un lungo periodo è
generalmente facile da fare

Molti sviluppatori Git hanno un un flusso di lavoro che abbraccia
questo approccio, 
- distribuzione stabile nel master
- distribuzione in testing in un altro branch (es `testing`)
- a partire dalla testing vengono creati dei branch specifici
  per l'aggiunta di features

Alcuni progetti molto grandi hanno inoltre un ramo proposed o pu
(proposed update) che integrano rami che non sono pronti per
entrare nel ramo master o testing. L'idea è che i tuoi rami sono
a vari livelli di stabilità; quando raggiungono un maggior
livello di stabilità, sono fusi nel ramo dal quale provengono .

I topic branch sono comunque utili in progetti di qualsivoglia
dimensione. I topic-branch è un branch di breve durata che si
crea per una feature particolare. Una volta aggiunta si mergia ed
elimina il branch


Per Julia dovrebbe essere andata cosi: ogni autore fa il fork del
progetto, poi crea un proprio branch con le iniziali del proprio
nome per indicizzare il proprio lavoro. Poi fa branch specifici
per i lavori. Regolarmente 

https://github.com/JuliaLang/julia/blob/master/CONTRIBUTING.md




<!-- % ## Branch remoti} -->
<!-- % I branch remoti sono riferimenti allo stato dei rami sui tuoi -->
<!-- % repository remoti. Sono rami locali che non puoi muovere; son -->
<!-- % modificati quando si effettua una comunicazione di -->
<!-- % rete.\\ -->
<!-- % I rami remoti sono come dei segnalibri per ricordarti dove i rami -->
<!-- % sui tuoi repository remoti erano quando ti sei connesso l'ultima -->
<!-- % volta. Prendono la forma -->
<!-- % ``` -->
<!-- % (remote)/(branch) -->
<!-- % ``` -->
<!-- % per esempio, se vuoi vederes come appariva il ramo master sul tuo -->
<!-- % ramo origin l'ultima volta che hai comunicato con esso, puoi -->
<!-- % controllare il ramo `origin/master}. -->


<!-- % Ad esempio hai un server Git nella tua rete raggiungibile a -->
<!-- % `git.ourcompany.com}. Se fai un `clone} da qui, Git -->
<!-- % automaticamente lo nomina `origin} per te, effettua il -->
<!-- % `pull} di tutti i dati, crea un puntatore dove si trova il -->
<!-- % ramo `master} e lo nomina localmente -->
<!-- % `origin/master}.  Git inoltre ti da il tuo ramo -->
<!-- % `master} che parte dallo stesso punto del ramo originario -->
<!-- % `master}, così hai qualcosa da cui puoi iniziare a -->
<!-- % lavorare. -->
<!-- % ``` -->
<!-- % l@np350v5c:~/src/cpphtp$ git branch -va -->
<!-- % * master                8478761 src/03_12.cpp src/04_18.cpp added -->
<!-- %   remotes/origin/HEAD   -> origin/master -->
<!-- %   remotes/origin/master 8478761 src/03_12.cpp src/04_18.cpp added -->
<!-- % l@np350v5c:~/src/cpphtp$ git remote  -->
<!-- % origin -->
<!-- % l@np350v5c:~/src/cpphtp$ git branch  -->
<!-- % * master -->
<!-- % ``` -->
<!-- % Se fai del lavoro sul tuo ramo principale locale, e, allo stesso -->
<!-- % tempo, qualcuno ha inviato degli aggiornamenti al ramo `master} -->
<!-- % di `git.ourcompany.com}, allora la tua storia si muoverà -->
<!-- % in avanti in modo differente. Inoltre, mentre non hai contatti -->
<!-- % con il tuo server di partenza, il tuo puntatore -->
<!-- % `origin/master} non si sposterà.\\ -->
<!-- % Per sincronizzare il master il tuo lavoro, devi avviare il comando  -->
<!-- % ``` -->
<!-- % git fetch origin -->
<!-- % ``` -->
<!-- % Questo comando guarda qual'è il server di origine (in questo -->
<!-- % caso, è `git.ourcompany.com}), preleva qualsiasi dato che -->
<!-- % ancora non possiedi, e aggiorna il tuo database locale, spostando -->
<!-- % il puntatore `origin/master} alla sua nuova, più -->
<!-- % aggiornata posizione. Non effettua il merge -->

<!-- % ### Pushing -->

<!-- % Quando vuoi condividere un ramo con il mondo, hai bisogno di -->
<!-- % inviarlo su di un server remoto su cui hai accesso in -->
<!-- % scrittura. I tuoi rami locali non sono automaticamente -->
<!-- % sincronizzati sul remoto in cui scrivi, devi esplicitamente dire -->
<!-- % di inviare il ramo che vuoi condividere. -->

<!-- % Se si ha un branch locale `serverfix} che si vuole -->
<!-- % condividere con il resto del mondo si fa -->
<!-- % ``` -->
<!-- % $ git push origin serverfix -->
<!-- % ``` -->
<!-- % `serverfix} mergera con master che `mergia} con -->
<!-- % `origin} -->

