# CROUS-autoconnect
Connecte automatiquement aux réseau du CROUS si les bons identifiants sont donnés.

## Dépendances
[Python 3](https://www.python.org/downloads) doit être installé, ainsi que le module [`requests`](https://pypi.org/project/requests), installable par la commande `pip install requests` dans un terminal si [`pip`](https://pip.pypa.io/en/stable/installing) est installé ou bien par apt si vous êtes sous linux :

```bash
# apt install python3-requests
```

## Usage
```bash
./connect_CROUS.py login password
```

### Automatisation de la connexion avec Network Manager
Vous pouvez créer un script avec Network Manager pour automatiser la connexion.
1. `mkdir -p /etc/NetworkManager/scripts`
2. Clonner le dépôt dans `/etc/NetworkManager/scripts/CROUS-autoconnect`
3. Activer le service: `systemctl enable NetworkManager-dispatcher.service`
4. Trouver l’UUID de la connexion avec `nmcli connection`.
5. Créer `/etc/NetworkManager/dispatcher.d/10-script.sh` contenant :
```bash
#!/usr/bin/env bash
# Vos identifiants à remplacer ci-dessous
LOGIN='<LOGIN>'
PASSWORD='<PASSWORD>'
UUID='<UUID>'

# début du script
status=$2
if [ "$CONNECTION_UUID" = $UUID ]; then
	case $status in
		up)
		/etc/NetworkManager/scripts/CROUS-autoconnect/connect_CROUS.py "$LOGIN" "$PASSWORD"
		;;
		down)
		;;
	esac
fi
```
6. S’assurer que LOGIN, PASSWORD et UUID ont bien configurés.
7. S’assurer que les droits sont corrects (tout doit appartenir à root et les autres utilisateurs ne doivent avoir aucun droit), `/etc/NetworkManager/dispatcher.d/10-script.sh` doit être exécutable).
