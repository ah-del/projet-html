import psutil

def connected_devices():
    # Récupération des informations de connexion réseau
    net_io_counters = psutil.net_io_counters()
    # Récupération des adresses IP des périphériques connectés
    ip_addresses = psutil.net_if_addrs()
    # Récupération des noms des interfaces réseau
    net_if_names = psutil.net_if_stats()
    print("Adresse IP : ",ip_addresses)
    print("Nom interface : ",net_if_names)

connected_devices()
