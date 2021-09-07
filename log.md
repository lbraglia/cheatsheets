## Amministrazione - Log

```
journalctl -b                   # log del boot corrente
journalctl -b -r                # log del boot corrente, reversed
journalctl --since "1 hour ago" # log timeframe specificato
journalctl -f                   # ultimi eventi in aggiornamento continuo
journalctl -u nginx.service     # log di una unit di systemd
journalctl _UID=1000            # log di un utente (uid ottenibile con id user)
```
