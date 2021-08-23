yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

import os
import time as t

def webserver(userPass,userName,remoteIp):
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c Webserver MENU")
    os.system("tput setaf 7")
    
    print("""\n{0}[1]{1} install webserver\n{0}[2]{1} Check status\n{0}[3]{1} stop webserver\n{0}[4]{1} show current directory \n{0}[5]{1} create or open a file\n{0}[6]{1}{1} copy a file on webserver\n{0}[7]{1} Start the webserver \n{0}[b]{1} Go back\n{0}[q]{1} exit the program\n""".format(yellow,green))
    d = input("\033[1;36mPlease Enter your choice : \033[1;33m")
    if d == "1": 
      os.system("sshpass -p '{0}' ssh {1}@{2} yum install httpd".format(userPass,userName,remoteIp))
    elif d == "2":
      print(yellow+"Press q to come out from it")
      os.system("sshpass -p '{0}' ssh {1}@{2} systemctl status httpd".format(userPass,userName,remoteIp))
      input("\033[36mPress Enter to continue..."+end)
    elif d == "3": 
      os.system("sshpass -p '{0}' ssh {1}@{2} systemctl stop httpd".format(userPass,userName,remoteIp))
      print("webserver is stopped...")
      t.sleep(2)
    elif d == "4": 
      os.system("sshpass -p '{0}' ssh {1}@{2} pwd".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} ls".format(userPass,userName,remoteIp))
      input("[36mPress Enter to continue..."+end)
    elif d == "5":
      print(yellow+"for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
      webFileName = input(green+"Enter file name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} vim {0}".format(userPass,userName,remoteIp,webFileName))
    elif d == "6": 
      file = input(green+"Enter file name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} cp {0} /var/www/html".format(userPass,userName,remoteIp,webFileName))
      print(f"{webFile} is coppied to webserver...")
      t.sleep(2)
    elif d == "7":
      os.system("sshpass -p '{0}' ssh {1}@{2} systemctl start httpd".format(userPass,userName,remoteIp))
      print("webserver is started...")
      t.sleep(2)
    elif d == "b": 
      break
    elif d == "q":
      print("\033[00m")
      print ("\033[1;33mGood bye!\033[00m") 
      t.sleep(1)
      exit()    
    else:
      print (f'''
  \033[1;33m  [ + ] \033[1;31m This option doesn't support.
  \033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
      input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
      os.system("clear")
