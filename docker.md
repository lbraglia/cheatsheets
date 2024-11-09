# docker

## macchina virtuale vs container

Una **macchina virtuale** è un sistema operativo completo; un container è
un insieme di app e librerie senza un kernel che si basa su un
container engine (es docker o podman). Anziché eseguire due kernel nei
container ne abbiamo solo uno (quello della macchina ospite)

Un **container** è piu efficiente per risorse (solo quando richieste) e
flessibile: nelle macchine virtuali per aumentare cpu o ram assegnata
è necessario spegnere/modificare/riaccendere, mentre nei container
possiamo cambiare le risorse allocate ad un container in tempo reale.

Le macchine virtuali sono però più isolate tra loro.

## definizioni

- **container**: processo o insieme di processi che viene lanciato (es servizio `apache`)

- **immagine**: eseguibile che lancia il container (es `apache.exe`). Da
  una singola immagine posso avviare uno o più container (tutti basati
  sulla stessa immagine).  Una immagine docker assomiglia più ad un
  archivio o filesystem (di distribuzione linux con sopra installato
  tutto il necessario) piuttosto che ad un eseguibile

- **Dockerfile**: file/ricetta dove si specifica come è costruita una immagine docker
  ```
  FROM ubuntu                  # installa librerie base che servono a tutte le app
  RUN apt install apache-deps  # installa le dep di apache
  COPY index.html .            # copiamo un file all'interno dell'immagine
  RUN apt install apache       # installiamo apache
  ```
  
- **docker compose**: in un file di configurazione scegliamo vari
  container di interesse (es pensa al lamp, serve linux, apache, mysql e
  php) e come vogliamo che siano configurati
