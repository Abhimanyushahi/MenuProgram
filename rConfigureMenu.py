import os
import time as t

yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

def RConfigureMenu(userPass,userName,remoteIp):
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c ConFigure MENU")
    os.system("tput setaf 7")
    print("\n{0}[1]{1} Configure yum\n{0}[2]{1} Configure docker\n{0}[b]{1} Go back \n{0}[q]{1} Exit the program{2}\n".format(yellow,green,end))
    d = input("\033[1;36mEnter your choice :\033[1;33m ")
    if d == "1": 
      os.system("sshpass -p '{0}' ssh {1}@{2} touch /etc/yum.repos.d/menuyum.repo".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh /cat yum.repo >> /etc/yum.repos.d/menuyum.repo".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} systemctl enable docker".format(userPass,userName,remoteIp))
      print(green+"yum is configured sucessfully.")
      t.sleep(2)
    elif d == "2": 
      os.system("sshpass -p '{0}' ssh {1}@{2} touch /etc/yum.repos.d/menudocker.repo".format(userPass,userName,remoteIp))
      os.system("shpass -p '{0}' ssh {1}@{2} cat /docker.repo >> /etc/yum.repos.d/menudocker.repo".format(userPass,userName,remoteIp)) 
      print(green+"Docker is configured sucessfully.")
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
