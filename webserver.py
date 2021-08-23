yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

import os
import time as t

def WebserverMenu():
  while True:
    os.system("clear")
    os.system("tput setaf 4")
    os.system("figlet -f slant -c Webserver MENU")
    os.system("tput setaf 7")
    print("""\n{0}[1]{1} install apache webserver\n{0}[2]{1} start webserver\n{0}[3]{1} check status\n{0}[4]{1} stop webserver\n{0}[5]{1} show current directory \n{0}[6]{1} create or open a file\n{0}[7]{1} copy a file on webserver\n{0}[b]{1} Go back \n{0}[q]{1} exit the program{2}\n""".format(yellow,green,end))
    d = input("\033[1;36mEnter your choice :\033[1;33m ")
    if d == "1":
      print("\033[00m") 
      os.system("yum install httpd")
    elif d == "2":
      os.system("systemctl start httpd")
      print(green+"webserver is started..."+end)
      t.sleep(1)
    elif d == "3": 
      print("\033[1;33mPress q to come out from it\033[00m")
      os.system("systemctl status httpd")
    elif d == "4": 
      os.system("systemctl stop httpd")
      print(green+"webserver is stopped..."+end)
      t.sleep(1)
    elif d == "5": 
      print("\033[00m") 
      os.system("pwd")
      os.system("ls")
      input(green+"Press Enter to continue..."+end)
    elif d == "6": 
      print("\033[1;33mFor writting anything in file press i, and for saving press esc key and :wq, and only close file press esc key and :q\033[00m")
      webFileName = input("\033[1;36mEnter file name :\033[1;33m ")
      os.system("vim {0}".format(webFileName))
      print(green+f"{webFileName} is created..."+end)
      t.sleep(1)
    elif d == "7": 
      file = input("\033[1;36mEnter file name :\033[1;33m")
      os.system("cp {0} /var/www/html".format(file))
      print(green+f"{file} is coppied to webserver..."+end)
      t.sleep(1)
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
