import os
import re

def os_version():
	os_name = os.popen('uname')
	now = os_name.read()
	os_version = os.popen('uname -r')
	now2 = os_version.read()
	print ("\t\033[0;36mSysteme d'exploitation (OS) : \033[0m", now)
	print ("\t\033[0;36mVersion du systeme d'exploitation : \033[0m", now2)
	
def uptime():
	up = os.popen('uptime')
	now = up.read()
	print (now)

def kernel_version():
	os_name = os.popen('uname')
	now = os_name.read()
	kernel_version = os.popen('uname -v')
	now2 = kernel_version.read()
	print ("\033[0;36mSysteme d'exploitation 	: \033[0m", now)
	print ("\033[0;36mVersion du Kernel : \033[0m", now2)

def hardware_info():
	cpu_inf = os.popen('lscpu')
	now = cpu_inf.read()
	mem_inf = os.popen("free -t | grep -E '^ |^M'")
	now2 = mem_inf.read()
	disc_inf = os.popen("df -h | grep -E '^/|^F'")
	now3 = disc_inf.read()
	print ("\t\033[0;36mInformations sur le CPU\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n\033[0m")
	print (now)
	print ("\t\033[0;36mInformations sur la Memoire\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n\033[0m")
	print (now2)
	print ("\t\033[0;36mInformations sur le Disque\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n\033[0m")
	print (now3)

def file_max():
	top = os.popen('ulimit -n')
	now = top.read()
	now = re.split('\n', now)
	print ("\033[0;36mVous pouvez ouvrir %s fichiers au maximum.\n\033[0m" % (now[0]))

def proces_max():
	max = os.popen('ulimit -p')
	now = max.read()
	now = re.split('\n', now)
	print ("\033[0;36mVous pouvez ouvrir %s processus au maximum.\n\033[0m" % (now[0]))
	
def list_package():
	lis = os.popen("dpkg-query -l | grep '^ii' | awk '{ print $2 }'")
	now = lis.read()
	print (now)