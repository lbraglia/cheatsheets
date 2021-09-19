# torrent

## Transmission
Sul server
- installare `transmission-daemon` 
- stoppare l'esecuzione del server
- configurare `/etc/transmission-daemon/settings.json` e nello specifico 
  settare le righe
  ```
	download_dir directory
	rpc-whitelist ip_autorizzati
	rpc-username  utente 
	rpc-password password
  ```
- aggiungere l'utente `debian-transmission` ad un gruppo con permessi
  di scrittura sulla directory dove transmission deve salvare
- rifar partire il servizio
- connettersi mediante browser a ip_server:9091/
