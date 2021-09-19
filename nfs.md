# NFS

## Lato server
Installare `nfs-kernel-server`, poi per l'ultima versione (4):
- in `/etc/default/nfs-common:`
  ```
  NEED_STATD="no"
  NEED_IDMAPD="yes"
  ```
- in `/etc/default/nfs-kernel-server`
  ```
  RPCNFSDOPTS="-N 2 -N 3 -H ip_da_ascoltare"
  RPCMOUNTDOPTS="--manage-gids -N 2 -N 3"
  ```
- per evitare un demone aggiuntivo inutile 
  ```
  sudo systemctl mask rpcbind.service
  sudo systemctl mask rpcbind.socket
  ```

## Lato client
