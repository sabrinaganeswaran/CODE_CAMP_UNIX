#!/usr/bin/env python
import sys, os
import reseau
import infgen
import processus 

import os
os.system('clear')

text = """\033[0;36m
         __  __ _____ _   _ _____ _______ ______ _        ____   ___                       _____              
        |  \/  |_   _| \ | |_   _|__   __|  ____| |      |___ \ / _ \                     |     |             
        | \  / | | | |  \| | | |    | |  | |__  | |        __) | | | |                    |     |             
        | |\/| | | | | . ` | | |    | |  |  __| | |       |__ <| | | |                    |  ,__|_____        
        | |  | |_| |_| |\  |_| |_   | |  | |____| |____   ___) | |_| |                    |     |             
        |_|  |_|_____|_| \_|_____|  |_|  |______|______| |____(_)___/                       arck|_____        
                                                                                            consulting        
            \033[0m"""
aff = text.center(50, '\t')
print (aff)

login = input("\033[0;34mEntrez votre login > \033[0m")
if login == "":
    login = "user"

menu_actions  = {}
menu_actions1 = {}
menu_actions2 = {}
menu_actions3 = {}

# Main menu
def main_menu():
    os.system('clear')
    print("""\033[0;36m
        Bienvenue dans notre Shell Interactif!\033[0m\n
        ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬●\n
    Veuillez choisir une option :
    \033[0;34m1. Informations générales\033[0m
    \033[0;33m2. Réseau\033[0m
    \033[0;32m3. Processus\033[0m
    \033[0;35m4. Aide\033[0m
    0. Quitter""")
    choice = input(login + ' > ')
    exec_menu(choice)
    main_menu()
 
# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("\033[31m∆ Entrée erronée, merci de vouloir réessayer.∆\033[0m\n")
            menu_actions['main_menu']()
    return

#Execute menu1
def exec_menu1(choice1):
    os.system('clear')
    ch1 = choice1.lower()
    if ch1 == '':
        menu_actions1['menu1']()
        
    else:
        try:
            menu_actions1[ch1]()
        except KeyError:
            print("\033[31m\033[5m∆ Entrée erronée, réessayez.∆\033[0m\n")
            menu_actions1['menu1']()
    return

#Execute menu2
def exec_menu2(choice2):
    os.system('clear')
    ch2 = choice2.lower()
    if ch2 == '':
        menu_actions2['menu2']()
    else:
        try:
            menu_actions2[ch2]()
        except KeyError:
            print("\033[31m\033[5m∆Entrée erronée, réessayez.\033[0m\n")
            menu_actions2['menu2']()
    return

   
#Execute menu3
def exec_menu3(choice3):
    os.system('clear')
    ch3 = choice3.lower()
    if ch3 == '':
        menu_actions3['menu3']()
    else:
        try:
            menu_actions3[ch3]()
        except KeyError:
            print("\033[31m\033[5m∆Entrée erronée, réessayez.∆\033[0m\n")
            menu_actions3['menu3']()
    return

def exec_menu4(choice4):
    os.system('clear')
    ch4 = choice4.lower()
    if ch4 == '':
        menu_actions4['menu4']()
    else:
        try:
            menu_actions4[ch4]()
        except KeyError:
            print("\033[31m\033[5m∆Entrée erronée, réessayez.∆\033[0m\n")
            menu_actions4['menu4']()
    return

# Menu 1
def menu1():
    print ("""\t\033[0;34mMenu des informations générales.\033[0m\n\t●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬●\n
    1. \033[0;33mVersion du systeme\033[0m
    2. \033[0;34mUptime\033[0m 
    3. \033[0;33mVersion de Kernel\033[0m
    4. \033[0;34mInformations Hardware (CPU, Memoire, Disque dur..)\033[0m
    5. \033[0;33mLimite des fichiers ouverts\033[0m
    6. \033[0;34mLimite des processeurs ouverts\033[0m
    7. \033[0;33mListe des paquets installés\033[0m
    9. Back
    0. Quitter""")
    choice1 = input(login + ' > ')
    exec_menu1(choice1)
    menu1()

# Menu 2
def menu2():
    print ("""\t\033[0;33m Menu Reseau.\033[0m\n\t●▬▬▬▬๑۩۩๑▬▬▬▬●\n
   1. \033[0;34mAdresse IP\033[0m
   2. \033[0;33mInterfaces existantes\033[0m
   3. \033[0;34mNombre de paquets recus & transmis\033[0m
   4. \033[0;33mRoutes\033[0m
   5. \033[0;34mForward du paquet activé ?\033[0m
   9. Back
   0. Quitter""")
    choice2 = input(login + ' > ')
    exec_menu2(choice2)
    menu2()
    return

# Menu 3
def menu3():
    print ("""\t\033[0;32mMenu Processus.\033[0m\n\t●▬▬▬▬๑۩۩๑▬▬▬▬●\n 
    1. \033[0;34mListe des processus\033[0m
    2. \033[0;32mDétails sur un processus\033[0m
    9. Back
    0. Quitter""") 
    choice3 = input(login + ' > ')
    exec_menu3(choice3)
    menu3()
    return

def menu4():
    print ("""\t\033[0;35m Aide.\033[0m\n\t●▬▬๑۩۩๑▬▬●\n
    \033[0;32mVous avez sollicité l'aide ? Ce Shell interactif permet, à vous, de simples utilisateurs, d'accéder aux données de votre ordinateur. \nL'utilisation est simple: vous avez seulement à vous laisser guider par le menu en tapant les chiffres correspondant aux menus et aux détails désirés et suivre les instructions de votre technicien !\nRien de plus simple!\033[0m 
    9. Back
    0. Quitter""") 
    choice4 = input(login + ' > ')
    exec_menu4(choice4)
    menu4()
    return
 
# Back to main menu
def Back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    print("\033[0;32mMerci d'avoir utilise le Shell Interactif. A bientot!\033[0m")
    sys.exit()
  
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '9': Back,
    '0': exit,
}

menu_actions1 = {
    'menu1': menu1,
    '1': infgen.os_version,
    '2': infgen.uptime,
    '3': infgen.kernel_version,
    '4': infgen.hardware_info,
    '5': infgen.file_max,
    '6': infgen.proces_max,
    '7': infgen.list_package,
    '9': Back,
    '0': exit,
}

menu_actions2 = {
    'menu2': menu2,
    '1': reseau.aff_ip,
    '2': reseau.ifce_list,
    '3': reseau.nb_packet,
    '4': reseau.info_route,
    '5': reseau.verif_ip_forward,
    '9': Back,
    '0': exit,
}

menu_actions3 = {
    'menu3': menu3,
    '1': processus.list_process,
    '2': processus.detail_process,
    '9': Back,
    '0': exit,
}

menu_actions4 = {
    'menu4': menu4,
    '9': Back,
    '0': exit,
}


# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()