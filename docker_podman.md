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
installare il pacchetto `podman`; se si vuole installare
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
docker ps -a
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
podman run -p 8080:80 -v /tmp:/var/www/html:ro nginx # 
```
Si ha che:
- esponiamo la porta 80 del container sulla porta locale 8080 mediante
  `-p portahost:portacontainer` (`-p` sta per port)
- quello che vogliamo nginx serva è una directory selezionata mediante
  `-v cartellahost:cartellacontainer` (`-v` sta per volume, e poi
  nginx serve in `/usr/share/nginx/html`). Qui in `/home/l/sito` ci
  dovrebbe essere una index.html


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

```


```bash

```


```bash

```


