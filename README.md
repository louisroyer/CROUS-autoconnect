# CROUS-autoconnect
Connecte automatiquement aux réseau du CROUS si les bons identifiants sont donnés.

# Requis
[Python 3](https://www.python.org/downloads) doit être installé, ainsi que le module [`requests`](https://pypi.org/project/requests), installable par la commande `pip install requests` dans un terminal si [`pip`](https://pip.pypa.io/en/stable/installing) est installé ou par apt :

```bash
# apt install python3-requests
```

# Usage
```bash
./connect_CROUS.py login password
```

Vous pouvez créer un script avec Network Manager pour automatiser la connexion.
