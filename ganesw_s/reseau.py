import os 
import re

def aff_ip():
	ip_inf = os.popen("ifconfig eth0 | grep '^          inet addr'")
	now = ip_inf.read()
	res = re.split("          inet addr:", now)
	result = re.split(" ", res[1])
	print ("\t\033[0;36mVotre adresse IP : \033[0m", result[0])


def ifce_list():
	inf = os.popen("ifconfig -s")
	now = inf.read()
	print ("\t\033[0;36mInterface des informations\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n\033[0m", now)

def info_route():
	inf = os.popen("route")
	now = inf.read()
	print (now)

def nb_packet():
	inf_rx = os.popen("ifconfig eth0 | grep 'RX packets:' | cut -d: -f2 | awk '{ print $1}'")
	now_rx = inf_rx.read()
	inf_tx = os.popen("ifconfig eth0 | grep 'TX packets:' | cut -d: -f2 | awk '{ print $1}'")
	now_tx = inf_tx.read()
	print ("\t\033[0;36mNombre de paquets transmis : \033[0m", now_rx)
	print ("\t\033[0;36mNombre de paquets recus	   : \033[0m", now_tx)

def verif_ip_forward():
	inf = os.popen("cat /proc/sys/net/ipv4/ip_forward")
	now = inf.read()
	if int(now) == 0:
		print ("\t\033[0;36mL'IP_forward est désactivé\033[0m")
	else:
		print ("\t\033[0;36mL'IP_forward est actif\033[0m")