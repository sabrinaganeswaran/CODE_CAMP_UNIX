import os
import re

def list_process():
	inf = os.popen("ps aux")
	now = inf.read()
	print (now)

def detail_process():
	pattern = input("\033[0;32mEntrez le nom du processus > \033[0m")
	verif = os.popen("ps aux | grep '" + pattern + "$'")
	n_verif = verif.read()
	if (n_verif != ""):
		inf = os.popen("ps aux | grep '" + pattern + "' | awk '{ print $1 }'")
		User = inf.read()
		User = re.split("\n", User)
		inf = os.popen("ps aux | grep '" + pattern + "' | awk '{ print $2 }'")
		PID = inf.read()
		PID = re.split("\n", PID)
		inf = os.popen("ps aux | grep '" + pattern + "' | awk '{ print $11 }'")
		l_cmd = inf.read()
		l_cmd = re.split("\n", l_cmd)
		inf = os.popen("ps aux | grep '" + pattern + "' | awk '{ print $8 }'")
		stat = inf.read()
		stat = re.split("\n", stat)
		inf = os.popen("ps -f | grep '" + pattern + "' | awk '{ print $3 }'")
		Ppid = inf.read()
		Ppid = re.split("\n", Ppid)
		print ("""\nUtilisateur          : """ + User[0] + """\nPID                  : """ + PID[0] + 
			""" \nLigne de commande    : """ + l_cmd[0] + """\nStatut               : """+ stat[0] + """\nParent ID            : """ + Ppid[0])
	elif n_verif:
		print("\033[31m∆ Veuillez entrer un nom de processus! ∆\033[0m")

	else:
		print("\033[31m∆ Le nom du processus n'existe pas. Veuillez essayer un autre nom ! ∆\033[0m\n")
