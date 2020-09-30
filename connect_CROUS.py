#!/usr/bin/env python3

"""
    A python script allowing Students at UPS to connect easily to the campus WIFI.
"""

import requests
import syslog
import sys

def try_access_point(i):
    """
        Essaye de se connecter a un point d'accès du campus.
        Retourne l'url du point d'accès si celui si est disponible.
    """

    url = f'https://pftf0{i}.in.crous-toulouse.fr:8003/index.php?zone=lan'
    try:
        requests.post(url)
        return url
    except:
        return None


def try_all_access_point():
    """
        Essaye de se connecter à tous les points d'accès du campus.
        Retourne le premier point d'accès disponible.
    """

    i = 0
    url = None
    while i <= 5 and url is None:
        url = try_access_point(i)
        i += 1
    return url


def connect(url, login, password):
    """
        Connection via une URL valide
    """

    syslog.syslog(syslog.LOG_INFO, f"Connection to {url}…")

    data = {
        "auth_user": login, "auth_pass": password,
        "redirurl": "http://www.crous-toulouse.fr",
        "accept": "Continue"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": url
    }

    res = requests.post(url, data=data, headers=headers)

    if res.content == b'You are connected.':
        syslog.syslog(syslog.LOG_INFO, "You are already connected.")
    elif b'Erreur d\'Authentification !' in res.content[:224]:
        syslog.syslog(syslog.LOG_ERR, "Wrong credentials.")
        exit(2)
    elif b'Redir' in res.content[:50]:
        syslog.syslog(syslog.LOG_INFO, "Connected.")


if __name__ == '__main__':
    syslog.openlog("CROUS-autoconnect")
    if len(sys.argv) != 3:
        syslog.syslog(syslog.LOG_ERR, "Credentials not provided.")
        exit(1)
    login = sys.argv[1]
    password = sys.argv[2]
    url = try_all_access_point()
    if url is None:
        syslog.syslog(syslog.LOG_ERR, "No captive portal detected.")
        exit(3)
    connect(url, login, password)
