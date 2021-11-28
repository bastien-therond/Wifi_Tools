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

def VerifInt(opt):
    it_is = False
    while it_is == False:
        opt = input("\nEntrer une option valide !\nEntrer une nouvelle option : ")
        try:
            int(opt)
            it_is = True
        except ValueError:
            it_is = False
    return opt

def User():
    print("\u001b[31m1. Voir son IP et MAC")
    
    print("2. WPA (2) cracking")
    
    print("3. Attaque par dénie de service(Dos)")
    
    print("4. Déconecter un client de ton wifi (aireplay-ng)")


    opt = input("\nChoisisser une option : ")
    
    if opt == str('1'):
        print("\n************************************************************")
        print("\n*********** Bienvenue dans l'interface 1 *******************")
        print("\n************************************************************")
        if platform.system == "Windows":
            print(os.system('ipconfig'))
            time.sleep(15)


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
