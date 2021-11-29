#DON'T COPY MY CODE DO YOUR SELF BE ETHICAL
import os
import time

def banner():
	print('\n\033[1;32;40m¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
	print('\033[1;32;40m¤   Network Scanner    ¤')
	print('\033[1;32;40m¤   Happy Hacking      ¤')
	print('\033[1;31;40m¤   coder:D4RK W0lF    ¤')
	print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')

def home():
    print('\033[1;32;40m[1] scan all ports [x] ::')
    print('[2] scan normal    [x] ::')
    print('[3] scan target os [x] ::')
    print('[4] scan DNS       [x] ::')
    print('[5] about          [x] ::')
    print('[\033[1;31;40m6] exit           [x] ::\n')


    #print('[x]    D4RK_W0lF    [x]\n')


banner()
time.sleep(3)
home()

choose = int(input('choose scan type ::'))  
while choose != 0:
    if choose == 1:
        url = input('\n[x] Enter your Target url [x] ::')
        cmd = "nmap "+url+" -p-"
        os.system(cmd)
        break
    elif choose == 2:
        url = input('\nx] Enter Your Target url [x] ::')
        cmd = "nmap "+url
        os.system(cmd)
        break
    elif choose == 3:
        url = input('\n[x] Enter Your Target url [x] ::')
        cmd = "nmap -o "+url
        os.system(cmd)
        break
    elif choose == 4:
        url = input('\n[x] Enter Your Target url [x] ::')
        cmd = "nmap --script dns-brute "+url
        os.system(cmd)
        break
    elif choose == 5:
        print('\n[x]   ABOUT THIS SCRIPT   [x]')
        print('\n[x] Coder::D4RK W0LF [x]')
        print('[x] Base on NMAP     [x]')
        break
    elif choose == 6:
        print('\nbye bye')
        exit()
    else:
        print('something wrong try again')
        exit()