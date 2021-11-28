#!/usr/bin/python3
import os
import time
import sys
import platform

#------------------ Couleur --------------------
# rouge    \u001b[31m
# bleu     \u001b[34m
# annuler  \u001b[0m
# vert     \u001b[32m
#-----------------------------------------------

def Chargement():
    toolbar_width = 90

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.001) # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar

def Clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def Finish():
    input("Appuyer sur entrée pour terminer")
    Clear()

def Help_NMAP():
    print('''
        SPÉCIFICATIONS DES CIBLES:
        Les cibles peuvent être spécifiées par des noms d'hôtes, des adresses IP, des adresses de réseaux, etc.
        Exemple: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0-255.0-255.1-254
        -iL <inputfilename>: Lit la liste des hôtes/réseaux cibles à partir du fichier
        -iR <num hosts>: Choisit les cibles au hasard
        --exclude <host1[,host2][,host3],...>: Exclut des hôtes/réseaux du scan 
        --excludefile <exclude_file>: Exclut des hôtes/réseaux des cibles à partir du fichier

        DÉCOUVERTE DES HÔTES:
        -sL: List Scan - Liste simplement les cibles à scanner
        -sP: Ping Scan - Ne fait que déterminer si les hôtes sont en ligne -P0: Considère que tous les hôtes sont en ligne -- évite la découverte des hôtes
        -PN: Considérer tous les hôtes comme étant connectés -- saute l'étape de découverte des hôtes
        -PS/PA/PU [portlist]: Découverte TCP SYN/ACK ou UDP des ports en paramètre
        -PE/PP/PM: Découverte de type requête ICMP echo, timestamp ou netmask 
        -PO [num de protocole]: Ping IP (par type)
        -n/-R: Ne jamais résoudre les noms DNS/Toujours résoudre [résout les cibles actives par défaut]
        --dns-servers <serv1[,serv2],...>: Spécifier des serveurs DNS particuliers

        TECHNIQUES DE SCAN:
        -sS/sT/sA/sW/sM: Scans TCP SYN/Connect()/ACK/Window/Maimon 
        -sN/sF/sX: Scans TCP Null, FIN et Xmas
        -sU: Scan UDP
        --scanflags <flags>: Personnalise les flags des scans TCP
        -sI <zombie host[:probeport]>: Idlescan (scan passif)
        -sO: Scan des protocoles supportés par la couche IP
        -b <ftp relay host>: Scan par rebond FTP
        --traceroute: Détermine une route vers chaque hôte
        --reason: Donne la raison pour laquelle tel port apparait à tel état

        SPÉCIFICATIONS DES PORTS ET ORDRE DE SCAN:
        -p <plage de ports>: Ne scanne que les ports spécifiés
        Exemple: -p22; -p1-65535; -pU:53,111,137,T:21-25,80,139,8080
        -F: Fast - Ne scanne que les ports listés dans le fichier nmap-services
        -r: Scan séquentiel des ports, ne mélange pas leur ordre
        --top-ports <nombre>: Scan <nombre> de ports parmis les plus courants
        --port-ratio <ratio>: Scan <ratio> pourcent des ports les plus courants
            
        DÉTECTION DE SERVICE/VERSION:
        -sV: Teste les ports ouverts pour déterminer le service en écoute et sa version
        --version-light: Limite les tests aux plus probables pour une identification plus rapide
        --version-intensity <niveau>: De 0 (léger) à 9 (tout essayer)
        --version-all: Essaie un à un tous les tests possibles pour la détection des versions
        --version-trace: Affiche des informations détaillées du scan de versions (pour débogage)

        SCRIPT SCAN:
        -sC: équivalent de --script=safe,intrusive
        --script=<lua scripts>: <lua scripts> est une liste de répertoires ou de scripts séparés par des virgules
        --script-args=<n1=v1,[n2=v2,...]>: passer des arguments aux scripts
        --script-trace: Montre toutes les données envoyées ou recues
        --script-updatedb: Met à jour la base de données des scripts. Seulement fait si -sC ou --script a été aussi donné.

        DÉTECTION DE SYSTÈME D'EXPLOITATION:
        -O: Active la détection d'OS
        --osscan-limit: Limite la détection aux cibles prometteuses
        --osscan-guess: Devine l'OS de façon plus agressive

        TEMPORISATION ET PERFORMANCE:
        Les options qui prennent un argument de temps sont en milisecondes a moins que vous ne spécifiiez 's'
        (secondes), 'm' (minutes), ou 'h' (heures) à la valeur (e.g. 30m).

        -T[0-5]: Choisit une politique de temporisation (plus élevée, plus rapide)
        --min-hostgroup/max-hostgroup <nombre>: Tailles des groupes d'hôtes à scanner en parallèle
        --min-parallelism/max-parallelism <nombre>: Parallélisation des paquets de tests (probes)
        --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <msec>: Spécifie le temps d'aller-retour des paquets de tests
        --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <msec>: Spécifie le temps d'aller-retour des paquets de tests
        --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Précise
        le round trip time des paquets de tests.
        --max-retries <tries>: Nombre de retransmissions des paquets de tests des scans de ports.
        --host-timeout <msec>: Délai d'expiration du scan d'un hôte --scan-delay/--max-scan-delay <msec>: Ajuste le délai de retransmission entre deux paquets de tests
        --scan-delay/--max-scan-delay <time>: Ajuste le delais entre les paquets de tests.

        ÉVASION PARE-FEU/IDS ET USURPATION D'IDENTITÉ
        -f; --mtu <val>: Fragmente les paquets (en spécifiant éventuellement la MTU)
        -D <decoy1,decoy2[,ME],...>: Obscurci le scan avec des leurres
        -S <IP_Address>: Usurpe l'adresse source
        -e <iface>: Utilise l'interface réseau spécifiée
        -g/--source-port <portnum>: Utilise le numéro de port comme source
        --data-length <num>: Ajoute des données au hasard aux paquets émis
        --ip-options <options>: Envoi des paquets avec les options IP spécifiées. 
        --ttl <val>: Spécifie le champ time-to-live IP
        --spoof-mac <adresse MAC, préfixe ou nom du fabriquant>: Usurpe une adresse MAC
        --badsum: Envoi des paquets TCP/UDP avec une somme de controle erronnée.

        SORTIE:
        -oN/-oX/-oS/-oG <file>: Sortie dans le fichier en paramètre des résultats du scan au format normal, XML, s|<rIpt kIddi3 et Grepable, respectivement
        -oA <basename>: Sortie dans les trois formats majeurs en même temps
        -v: Rend Nmap plus verbeux (-vv pour plus d'effet)
        -d[level]: Sélectionne ou augmente le niveau de débogage (significatif jusqu'à 9)
        --packet-trace: Affiche tous les paquets émis et reçus
        --iflist: Affiche les interfaces et les routes de l'hôte (pour débogage)
        --log-errors: Journalise les erreurs/alertes dans un fichier au format normal
        --append-output: Ajoute la sortie au fichier plutôt que de l'écraser 
        --resume <filename>: Reprend un scan interrompu
        --stylesheet <path/URL>: Feuille de styles XSL pour transformer la sortie XML en HTML
        --webxml: Feuille de styles de références de Insecure.Org pour un XML plus portable
        --no-stylesheet: Nmap n'associe pas la feuille de styles XSL à la sortie XML

        DIVERS:
        -6: Active le scan IPv6
        -A: Active la détection du système d'exploitation et des versions
        --datadir <dirname>: Spécifie un dossier pour les fichiers de données de Nmap
        --send-eth/--send-ip: Envoie des paquets en utilisant des trames Ethernet ou des paquets IP bruts
        --privileged: Suppose que l'utilisateur est entièrement privilégié 
        -V: Affiche le numéro de version
        --unprivileged: Suppose que l'utilisateur n'a pas les privilèges d'usage des raw socket
        -h: Affiche ce résumé de l'aide

        EXEMPLES:
        nmap -v -A scanme.nmap.org
        nmap -v -sP 192.168.0.0/16 10.0.0.0/8
        nmap -v -iR 10000 -P0 -p 80 ''')

def User():
    print("\u001b[31m1. Découverte de réseaux")
    
    print("2. WPA (2) cracking")
    
    print("3. Attaque par dénie de service(Dos)")
    
    print("4. Déconecter un client de ton wifi (aireplay-ng)")


    opt = input("\nChoisisser une option : ")
    
    if opt == str('1'):
        print("\n************************************************************")
        print("\n*************** Bienvenue dans l'interface 1 ***************")
        print("\n************************************************************")
        accpt = input("Vouler vous continuez ? (o ou N)")

        if accpt == str("o"):
            dependence = input("Vouler vous installer les dépendences ? (o ou N)")
            if dependence == str("o"):
                os.system('sudo apt install nmap -y')
                print('nmap installed')

            print('\n************************************************************')
            print('\n*************************** NMAP ***************************')
            print('\n************************************************************')

            user = input("\nEntrer l'adresse que vous voulez scanner\nSi vous ne connaissait pas les commandes écrires help.\n")
            if user == "help":
                print("\nPour scanner un réseaux il suffit de mettre une adresse en paramètre suivit d'un slash avec le masque de sous réseaux.")
                print("\nPour scanner tout un réseau vous pouvez mettre un * a la fin de l'adresse.")
                Help_NMAP()
            
            req = "sudo nmap "+user
            print(os.system(req))
    
    if opt == str('2'):
        print("\n************************************************************")
        print("\n*************** Bienvenue dans l'interface 2 ***************")
        print("\n************************************************************")
        accpt = input("Vouler vous continuez ? (o ou N)")
        if accpt == str("o"):
            dependence = input("Vouler vous installer les dépendences ? (o ou N)")
            if dependence == str("o"):

    Finish()

z = '''
                           ██           ██    
                           ░░           ░░                                  ██████████
        ██░░=░░███░░=░░██  ██   ██████  ██  ██████   ████    ████   ██     ██╝
        ╚██░░░██╩██░░░██╝  ██   ██═╝    ██   ╚██╝   ██░░██  ██░░██  ██     ╚████  
         ╚██░██╝ ╚██░██╝   ██   ████    ██    ██    ██░░██  ██░░██  ██        ╚██ 
          ╚███╝   ╚███╝    ██   ██╝     ██    ██    ╚████╝  ╚████╝  ██████  ████╝
''' 
Clear()
print(z)
Chargement()
User()
