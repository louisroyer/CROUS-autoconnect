# CROUS-autoconnect
Connecte automatiquement au portail captif du CROUS.

## Dépendances
```bash
apt install python3 python3-requests
```

## Usage
```bash
./connect_CROUS.py login password
```

### Automatisation de la connexion avec Network Manager
Vous pouvez créer un script avec Network Manager pour automatiser la connexion.
1. Pour être sûr de créer les fichiers avec les bons droits : `sudo su - && umask 077`
2. `mkdir -p /etc/NetworkManager/scripts`
3. Cloner le dépôt : `cd /etc/NetworkManager/scripts/ && git clone https://github.com/louisroyer/CROUS-autoconnect.git`
4. Activer le service : `systemctl enable NetworkManager-dispatcher.service`
5. Trouver l’UUID de la connexion avec `nmcli connection`.
6. Créer `/etc/NetworkManager/dispatcher.d/10-script.sh` contenant :
```bash
#!/usr/bin/env bash
set -e
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
7. S’assurer que `LOGIN`, `PASSWORD` et `UUID` ont bien configurés.
8. `chmod +x /etc/NetworkManager/dispatcher.d/10-script.sh`
