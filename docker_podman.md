## Docker

## Macchina virtuale vs container

Una **macchina virtuale** è un sistema operativo completo; un container è
un insieme di app e librerie senza un kernel che si basa su un
container engine (es docker o podman). Anziché eseguire due kernel nei
container ne abbiamo solo uno (quello della macchina ospite)

Un **container** è piu efficiente per risorse (solo quando richieste) e
flessibile: nelle macchine virtuali per aumentare cpu o ram assegnata
è necessario spegnere/modificare/riaccendere, mentre nei container
possiamo cambiare le risorse allocate ad un container in tempo reale.

Le macchine virtuali sono però più isolate tra loro.

## Definizioni

- **container**: processo o insieme di processi che viene lanciato (es servizio `apache`)

- **immagine**: eseguibile che lancia il container (es
  `apache.exe`). Da una singola immagine posso avviare uno o più
  container (tutti basati sulla stessa immagine).  Una immagine docker
  assomiglia più ad un archivio o filesystem (di distribuzione linux
  con sopra installato tutto il necessario) piuttosto che ad un
  eseguibile. Il *formato/standard* è open container image.

- **Dockerfile**: file/ricetta dove si specifica come è costruita una immagine docker
  ```
  FROM ubuntu                  # installa librerie base che servono a tutte le app
  RUN apt install apache-deps  # installa le dep di apache
  COPY index.html .            # copiamo un file all'interno dell'immagine
  RUN apt install apache       # installiamo apache
  ```
  
- **docker compose**: in un file di configurazione scegliamo vari
  container di interesse (es pensa al lamp, serve linux, apache, mysql
  e php) e come vogliamo che siano configurati, al fine di
  avviarli/fermarli/gestirli tutti assieme

- **registry**: tipo elenco telefonico contiene tutti gli indirizzi di
  vari repository (es apache,
  nginx). [Dockerhub](https://hub.docker.com/) è un registry (altri
  GHCR github container registry o altri)

- **repository**: tipo magazzini, contengono tutte le
  immagini/versioni di un certo software (eg apache, 1.1, 1.0, 0.9)
  permettendo la scelta di varie versioni

## Docker vs podman
docker è indipendente e piu supportato, podman è sviluppato da redhat
e più compatibile li. Si dovrebbe poter usarli intercambiabilmente.

Security:
- In docker serve un servizio/daemon centrale (che fa partire i
  container), su podman no. Se crasha il demone crashano tutti i
  container mentre con podman no
- Podman esegue senza privilegi di root mentre docker ha bisogno di
  eseguire come utente root. Docker può essere eseugito in modalità
  rootless con alcune configurazioni aggiuntive e limitazioni

docker consolidato, podman emergente

## Installazione di podman
installare il pacchetto `podman` e se si vuole fare il compose podman-compose
```
apt install podman podman-compose
```
Se si vuole installare
`podman-docker` si avrà una cli experience simile a docker ma anche no
direi.

Per check installazione effettuata, da utente normale
```
podman run hello-world
```
Nel corso:
- al posto di `Dockerfile` si userà `Containerfile`
- al posto di `docker-compose.yml` si scriverà `podman-compose.yml`

Una volta fatto è necessario abilitare i registry in
`~/.config/containers/registries.conf` (`man
containers-registries.conf`)
```
l@ambrogio:~/.config/containers$ cp /usr/share/doc/podman/examples/registries.conf .
```

## Ricerca e info
Help ricerca
```bash
podman search --help
```
Ricerca
```bash
podman search debian                        # raw
podman search --compatible debian           # printa stats come docker (compatible)
podman search --filter=is-official debian   # filtra solo immagini uffuciali (altre
                                            # contengono debian nel nome
```
Le immagini non ufficiali (con debian nel nome) sono tipicamente una ufficiale cui è stato aggiunto qualcosa

Importante andare su dockerhub e guardare "how to use this image" se presente

## Installare immagine
Per l'ultima versione
```bash
podman pull debian
```
Installare una versione specifica di una certa immagine vedere quali sono disponibili su dockerhub
e scegliere il supported tags di interesse
```bash
podman pull debian:bullseye # a destra dei due punti c'è un tag da trovare sul sito
```
Sullo stesso sistema possiamo avere diverse versioni di uno stesso software

## Come è stata creata una immagine e sue features
```bash
podman history debian
podman inspect debian
```


## Rimuovere immagini
```bash
podman rmi hello-world
podman rmi --force hello-world
```
Per rimuovere i layer/dipendenze

## Listare immagini
```bash
podman image ls
```


## Eseguire una immagine e creare un container
```bash
podman run debian # non fa niente
```
Le immagini base come debian non hanno un entry point con servizio che rimane in esecuzione, ma 
```bash
podman run debian ls -l
```
Di default il terminale non è collegato/posto entro il container; se
vogliamo entrarci dobbiamo usare `-it` (interactive terminal) la shell
corrente viene agganciata al processo dato entro il container
```bash
podman run -it debian bash # prompt cambia (con utente@id_container)
root@0f4e5917ac08:/# apt update # e via dicendo
```


Ogni volta che si da un `podman run` viene creato un container
caratterizzato da un id esadecimale; possiamo dare un nome più facile mediante
```bash
podman run -it --name prova-debian debian bash 
root@0f4e5917ac08:/# apt update            # id non visualizzato ma pace 
```

Alcuni **avvii di interesse**:
- eliminare il container al termine dell'esecuzione  (non verrà eliminato con `Ctrl+p Ctrl+q`)
  ```bash
  podman run --rm -it --name asdomar debian bash
  # se esco è morto
  ```
- senza bloccare il terminale (modalità detouched)
  ```bash
  podman run -d debian sleep 60
  ```
- limitando risorse: *numero di core* 
  ```bash
  podman run --cpus 2 immagine # solo 2 core
  ```
- quantità di ram
  ```bash
  podman run --memory 1024m immagine # solo  1 giga di ram
  ```
- specificare restart policy: se/quando un container deve essere 
  riavviato a seguito di stop o riavvio del demone (se presente)
  ```bash
  podman run -restart opzione ..
  ```
  dove opzioni sono `"always"|"no"|"never"|"on-failure"|"unless-stopped"`


## Uscire e rientrare in un container
Se esco dalla bash di un container 
- con `Cltr+d` si stoppa il container
- con `Ctrl+p Ctrl+q` il container viene lasciato in esecuzione e si può rientrare con
  `podman attach` e fornendo il suo id

```bash
podman run -it --name asdomar debian bash
root@0f4e5917ac08:/#     #Cltr+p Ctrl+q
podman attach asdomar    # dare due invio o fare dare Ctrl+l per il clear
```

## Riavviare containers
In realtà quando si stoppa un container questo non muore
definitivamente
```bash
podman run -it --name asdomar debian bash
root@0f4e5917ac08:/# # Ctrl+d
```
per farlo ripartire usare start e poi attach
```
podman start asdomar
podman attach asdomar
```


## Eliminare un container
```bash
podman rm asdomar
```
dopodiché si potrà crearne uno nuovo con lo stesso nome.


## Listare container
In esecuzione
```bash
podman ps
```
Creati ma non in esecuzione
```bash
podman ps -a
```

## Fermare container in esecuzione
```bash
podman ps
podman stop id_o_name # uno solo
```
Per stopparli tutti o stoppare il demone o fare un ciclo sui container id oppure usare prune
```bash
podman container prune
# oppure
for container in $(podman ps| cut -d' ' -f1 | tail -n +2); do podman stop $container; done
```

Se si è piantato male e non chiude usare `kill`
```bash
podman kill id_o_name # uno solo
```

## Comandi utili
Creare un container, eseguire vari comandi e chiudere/pulire tutto
```bash
podman run --rm -it debian bash -c "comandi separati da ;"
```
leggere i log (credo stdout di un comando) di un container in esecuzione
```bash
podman logs asdomar    # vedere i log sino ad ora
podman logs asdomar -f # continua a seguire i log di un container
```

## Networking e volumi
I container sono isolati di default ma a volte abbiamo bisogno di
rendere disponibile porte/cartelle (es server web)

Web server: 
```bash
                                                               # permette accesso
podman run -p 8080:80 -v /tmp:/var/www/html:ro nginx           # a tutta la rete
podman run -p 127.0.0.1:8080:80 -v /tmp:/var/www/html:ro nginx # solo a localhost
```
Si ha che:
- esponiamo la porta 80 del container sulla porta locale 8080 mediante
  `-p portahost:portacontainer` (`-p` sta per port)
- quello che vogliamo nginx serva è una directory selezionata mediante
  `-v cartellahost:cartellacontainer` (nginx serve in `/usr/share/nginx/html`). Qui in `/home/l/sito` ci
  dovrebbe essere una index.html

Possiamo anche non scegliere la porta dell'host ma lasciare che sia
podman ad utilizzarne una disponibile (es per sistemi più
complessipotremmo avere la porta già occupata da un altro
container. Nel caso usiamo giusto

```bash
podman run -d -p 80 -v /tmp:/var/www/html:ro nginx # esponi la 80 del container da qualche parte
podman ps # trova su quale porta dell'host è mappata
```


## Docker/podman compose
Se abbiamo bisogno di coordinamento di servizi differenti (es
webserver, database etc) vogliamo creare una immagine che le includa
tutti senza dover far partire diversi container e farli comunicare.

Per questo serve compose: creiamo un file `podman-compose.yml`. qua una stack con server e php
```yml
services:                             # chiamato services ma è un container

  php:                                # un id a scelta giusto per identificare il container
    image: "php:latest"               # immagine base
    container_name: php_stack         # tipo --name da command line
    volumes:                          # volumi da montare
      - './mia_app_da_servire:/var/www/html' # tipo -v da command line

  nginx:                              # un id a scelta giusto per identificare il container
    image: "nginx:latest"             # immagine base
    container_name: nginx_stack       # tipo --name da command line
    ports:                            # porte da esporre
      - "8080:80"                     # tipo -p da command line
      - "8443:443"                   
    volumes:                          # volumi da montare
      - './mia_app_da_servire:/var/www/html:ro' # tipo -v da command line: ro sta per readonly
      - './config/nginx:/etc/nginx/conf.d'   
    depends_on:                        # elenco servizi da cui questo dipende (nell'ordine di avvio )
      - php                            # viene avviato prima php```
```
Nella cartella col file `.yml` per lanciare l'intero stack (i due container)
```bash
podman compose up    # logga in stdout
podman compose up -d # vai in background/detached
```

Poi per tirare giu il servizio o diamo Ctrl+c oppure se lo abbiamo
tirato su in detached, dalla cartella dove è il file `.yml` mediante
```bash
podman compose down
```


## Uso di variabili e file `.env` nei file compose
Roba tipo token e parametri di configurazione sensibili non vanno
hardcoded ma posti in un file `.env` e richiamati nel file compose
come `${VARNAME:?err}` con:
- VARNAME il nome della variabile ed 
- `:?err` significa che se non la trova si lamenta 

Ad esempio morro per dare i nomi alle varie componenti e impostare una
password (mediante il parametro environment che serve per impostare
variabili d'ambiente esportate all'interno del container: es mysql
cerca una variabile `MYSQL_ROOT_PASSWORD`):
```yaml

   container_name: ${APP_NAME:?err}-php
   ...
   container_name: ${APP_NAME:?err}-nginx
   
   mysql:
     ...
      environment:
        MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD:?err}
```
creiamo il file .env
```bash
touch .env
emacs .env
```
e impostiamolo in maniera tale da
```
APP_NAME=myapp
MYSQL_ROOT_PASSWORD=rootpass
```
chiaro che `.env` andrà diretto in `.gitignore`.

Per sapere quali variabili d'ambiente guarda il container leggere la
pagina del progetto su dockerhub



## Volumi e bind mounts
Per rendere i dati all'interno dei nostri container persistenti e
gestibili possiamo usare volumi o bind mounts.
- **volumi**: modo migliore per rendere persistenti dati. Possono
  essere pensati come spazi di lettura/scrittura persistenti che sono
  condivisibili tra container (e sono accessibili anche dall'host)
- **bind mounts**: (esempio di nginx) una cartella del sistema host è
  mappata in una cartella del container e vi è uno scambio
  bidirezionale. Hanno senso quando vogliamo rendere una risorsa
  residente sul sistema host all'interno del container (sito web, file
  di configurazione comuni etc).


Creazione di volume
```bash
podman volume create  # volume anonimo
podman volume create volumeprova # volume con nome (quello che vogliamo)
```
Una volta creato (o se no lo crea lui) per usarlo in un container lo
specifichiamo sotto volume nel file di configurazione col suo nome
(che non è più un path)
```yml
services:
  prova:
  ...
  volumes:
    - volumeprova:/app/data

volumes:
  volumeprova: # qui spazio bianco a dx di :
```
Per condividere un volume tra container semplicemente metterlo nella sezione `volumes`


Elencare volumi disponibili
```bash
podman volume ls
```
I volumi sono indipendenti dai container e ci possono esser volumi non
più usati/associati ad alcun container. Per fare pulizia
```bash
podman volume prune
```
Info su un volume, tra i quali il mountpoint
```bash
podman volume inspect 44d400f294a3243b3e47b7c7746343ec79440a74117db8631ccd1302a87a42ad
```
es se vogliamo fare un backup basta che andiamo nella cartella del mountpoint e facciamo
una copia magari da spostare in un altro volume o sul nostro disco



## Containerfile (Dockerfile)
Serve per creare la nostra immagine personalizzata; riempire un file di nome `Containerfile`
```
FROM ubuntu                                        # utilizza ubuntu come base

LABEL Description="ubuntu con curl preinstallato"  # LABEL
RUN apt update && apt install -y curl              # applica queste modifiche

ENTRYPOINT ["/usr/bin/curl"]

# BUILD: docker build -t mycurl .
# RUN: docker run mycurl https://morrolinux.it
```
Ogni riga che è posta nel file crea un nuovo *layer* (con molte righe
l'immagine sarà più grande/pesante). Questo il motivo per cui update e
install sono stati posti nella stessa riga.
Peraltro in creazione ad ogni riga *il container viene spento e
riacceso* quindi:
- più righe rendono anche più lento il tutto
- se impostiamo variabili di ambiente in una riga, in quella
  successiva non ci sono più

Una volta completato lo buildiamo e runniamo, es nel caso precedente
```bash
podman build -t mycurl .  # . è la directory dove si trova il Containerfile
podman run mycurl https://morrolinux.it
```

Comandi utili per il `Containerfile` sono:
- `ADD` per aggiungere file dell'host/esterni al container/dal web
- `COPY` copia proprio file e cartelle locali
- `ENTRYPOINT` imposta l'eseguibile lanciato di defualt quando
  lanciamo il container (es entrypoint = /bin/sh)
- `CMD` specifica i parametri di lancio dell'`ENTRYPOINT` (es cmd =
  sleep 600)
- `ENV` imposta variabili d'ambiente che saranno sempre presenti
  quando avremo il container
- `EXPOSE` specifica che questa applicazione container è in ascolto su
  una certa porta
- `FROM` usato per definire l'immagine di partenza da cui deriviamo la nostra
- `RUN` per eseguire comandi arbitrari


## Caricare su un registry
Da provare bene eh sono appunti approssimativi sotto
```bash
podman login
podman tag mycurl lbraglia/mycurl:latest
podman image push lbraglia/mycurl:latest
```

## Altri esempi di Containerfile
Un esempio di scriptino dockerizzato 
```
FROM python:3.8-bullseye                 # python 3.8 costruito su debian bullseye

WORKDIR /python-docker                   # imposta cartella lavoro corrente all'interno del container
                                         # la crea se non esiste gia

COPY requirements.txt requirements.txt   # importa il file delle dipendenze
RUN apt update && apt install -y python3 python3-pip  # installa pip
RUN pip3 install -r requirements.txt     # installa le dipendenze del progetto
RUN mkdir /hist                          # crea una cartella

COPY . .                                 # copia tutto il resto dalla cartella locale sull'host
                                         # nella cartella attuale
CMD [ "python3", "scriptino.py"]         # definisce cosa viene lanciato all'avvio
```
Una containerizzazione di un IDE comune per tutti gli sviluppatori di un progetto
```Dockerfile
FROM ubuntu:noble 

# se non specifica USER esegue come ROOT, sotto installo

RUN apt update && \
    apt -y install vim libxkbcommon-dev libglib2.0-dev libxcb-cursor0 qt6-wayland \
    build-essential git python3 python3-pip libgl1-mesa-dev nasm libpulse0 

RUN pip install --break-system-packages aqtinstall     

USER ubuntu              # D'ORA IN POI ESEGUI COME UTENTE UBUNTU (non root default su ubuntu:noble)
WORKDIR /home/ubuntu/Qt  # muoviti (e crea la) nella cartella di lavoro

# installa vari plugin di interesse comuni
RUN aqt install-qt linux desktop 6.8.0 linux_gcc_64 --archives icu qtbase qtdeclarative && \
    aqt install-tool linux desktop tools_qtcreator_gui qt.tools.qtcreator_gui && \
    aqt install-tool linux desktop tools_cmake qt.tools.cmake && \
    aqt install-tool linux desktop tools_ninja qt.tools.ninja

# setta varie variabili d'ambiente per il path etc
ENV PATH=$PATH:/home/ubuntu/Qt/Tools/CMake/bin/:/home/ubuntu/Qt/Tools/Ninja
ENV QT_QPA_PLATFORM_PLUGIN_PATH=/home/ubuntu/Qt/6.8.0/gcc_64/plugins/platforms
ENV CMAKE_PREFIX_PATH=/home/ubuntu/Qt/6.8.0/gcc_64/

# spostati in home e clona il progetto
WORKDIR /home/ubuntu/
RUN git clone https://github.com/morrolinux/qt-docker-demo-project.git
VOLUME /home/ubuntu/qt-docker-demo-project	# il percorso specificato viene reso persistente
                                            # con volume anonimo. Quando eseguito container, docker
											# crea al volo un volume anonimo e ci salva il contenuto 
											# di questa cartella. Questa contiene il codice
											# che elaboriamo e vogliamo salvarlo
											# per essere poi ritrovato con docker start (invece di run)

WORKDIR /home/ubuntu/qt-docker-demo-project # compila il progetto nella cartella
RUN cmake . && make 

USER root                                   # ritorna a ROOT, necessario per qtcreator quando il 
                                            # container sarà avviato

ENTRYPOINT ["/home/ubuntu/Qt/Tools/QtCreator/bin/qtcreator"] # eseguibile lanciato l'ide (es /bin/sh)
CMD ["/home/ubuntu/qt-docker-demo-project/CMakeLists.txt"]   # parametro: percorso progetto da aprire
```
Per cucinare l'immagine
```bash
podman build -t qtdemo .
```
In casi semplici non grafici per eseguire
```bash
podman run qtdemo # per casi semplici
```
In caso di app con grafica dobbiamo togliere l'isolamento mediante le cose di sotto
```bash
xhost +SI:localuser:$(id -un)
podman run --name qtdemo -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --ipc=host --net=host dove-dev
#   lavora nel volume ed esci
```
Dopo bisogna riattivare il container qtdemo se no configurazioni e
codice non è salvato e viene creato nuovamente
```bash
podman start qtdemo
```


## TODO
ghcr.io tutorial per installare da github?

https://gist.github.com/yokawasa/841b6db379aa68b2859846da84a9643c
