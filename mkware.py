import os
import random
os.system("clear")
print("""

███╗   ███╗██╗  ██╗██╗    ██╗ █████╗ ██████╗ ███████╗
████╗ ████║██║ ██╔╝██║    ██║██╔══██╗██╔══██╗██╔════╝
██╔████╔██║█████╔╝ ██║ █╗ ██║███████║██████╔╝█████╗  
██║╚██╔╝██║██╔═██╗ ██║███╗██║██╔══██║██╔══██╗██╔══╝  
██║ ╚═╝ ██║██║  ██╗╚███╔███╔╝██║  ██║██║  ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                     
Desenvolvido by >> IboySec
Telegram >> @iboy_w
Discord >> iboy #3048
Script para fins educacionais.
	""")

decisao = str(input("Com a execução deste código ele irá criar varias pastas. S/N: "))
if decisao=='s':
	while True:
	    ran = random.randint(10,55)
	    os.system(f"mkdir {ran}")
else:
	os.system("clear")
	print("goodbye amigo")
	exit()
	



