import os
import getpass
import socket
import subprocess
import time as t
import configureMenu
import dockerMenu
import hadoopMenu
import datanode
import namenode
import hadoopClient
import webserver
import userMenu
import partitionMenu
import linuxMenu
import aws
import rConfigureMenu
import rdockerMenu
import rhadoopMenu
import rdatanode
import rnamenode
import rhadoopClient
import rwebserver
import ruserMenu
import rpartitionMenu
import rLinuxCommand
import remoteAws
from auth import *

yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"
while True:
  os.system("clear")
  print('''\007
\033[1;33m
    __  __________   ____  __ \033[01;34m     ____            \033[1;33m  ______                        
   /  |/  / ____/ | / / / / / \033[01;34m    / __ \_________  \033[1;33m / ____/________ _____ ___      
  / /|_/ / __/ /  |/ / / / /  \033[01;34m   / /_/ / ___/ __ \ \033[1;33m/ / __/ ___/ __ `/ __ `__ \     
 / /  / / /___/ /|  / /_/ /   \033[01;34m  / ____/ /  / /_/ / \033[1;33m /_/ / /  / /_/ / / / / / /     
/_/  /_/_____/_/ |_/\____/    \033[01;34m /_/   /_/   \____/  \033[1;33m\____/_/   \__,_/_/ /_/ /_/      
                                                                         \033[1;34mv2.0

\t\t\t\033[1;36m .........................................\033[1;m
\t\t\t\033[1;36m|\033[1;33m     Hey welcome to my menu program\033[1;36m      |
\t\t\t\033[1;36m .........................................\033[00m''')
  print('''\n\n\n\t\t\t\033[01;32m1. ---> Local
\t\t\t2. ---> Remote
\t\t\tq. ---> Quit\033[00m''')
  print("\n\033[1;33m\t\t\twhere you would like to perform your job (local/remote) \033[00m")
  print("\t\t\t\033[1;36m......................................................\n")
  
  location = input("\033[1;36m \t\t\tMenu \033[1;35m>>\033[01;32m ").lower()
  yellow = "\033[1;33m" # for numbering
  green = "\033[1;32m" # statements
  cyan = "\033[1;36m"
  red =  "\033[1;31m" # for enter choicelocal
  end = "\033[00m"

  if location == "1":
    while True:
      os.system("clear")
      os.system("tput setaf 6")
      os.system("figlet -f slant -c LMENU ProGram")
      os.system("tput setaf 7")
      
      print (f'''
    \033[1;33m  [ 1 ] \033[1;32myou want to configure yum or docker
    \033[1;33m  [ 2 ] \033[1;32myou want to use docker
    \033[1;33m  [ 3 ] \033[1;32myou want to use hadoop
    \033[1;33m  [ 4 ] \033[1;32myou want to use webserver
    \033[1;33m  [ 5 ] \033[1;32myou want to create new user
    \033[1;33m  [ 6 ] \033[1;32myou want to do partion
    \033[1;33m  [ 7 ] \033[1;32myou want to run linux commands
    \033[1;33m  [ 8 ] \033[1;32mTo enter AWS CLOUD
    \033[1;33m  [ m ] \033[1;32mGo to main screen
    \033[1;33m  [ q ] \033[1;32mTo exit
          \033[00m''')
      ch=input("\033[1;36mEnter your choice : \033[1;33m")  
      print(ch)
      if ch == "1":
        configureMenu.ConfigureMenu()
      elif ch == "2":
        dockerMenu.DockerMenu()
      elif ch == "3":
        hadoopMenu.hadoopMenu()
      elif ch == "4":
        webserver.WebserverMenu()
      elif ch == "5":
        userMenu.UserMenu()
      elif ch == "6":
        partitionMenu.PartitionMenu()
      elif ch == "7":
        linuxMenu.linuxMenu()
      elif ch == "8":
        aws.menu()
      elif ch == "m":
        break
      elif ch == "q" or ch == "Q":
        print("\033[00m")
        print ("\033[1;33mGood bye!\033[00m") 
        t.sleep(1)
        exit()
      else :
        print (f'''
        \033[1;33m  [ + ] \033[1;31m This option doesn't support.
        \033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
        input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
      os.system("clear")
  elif location == "2":
    os.system("clear")
    userPass, userName,remoteIp=authentication()
    while True:
      os.system("clear")
      os.system("tput setaf 4")
      os.system("figlet -f slant -c RMENU ProGram")
      os.system("tput setaf 7")
      print (f"""\n
      \033[1;33m  [ 1 ] \033[1;32myou want to configure yum or docker
      \033[1;33m  [ 2 ] \033[1;32myou want to use docker
      \033[1;33m  [ 3 ] \033[1;32myou want to use hadoop
      \033[1;33m  [ 4 ] \033[1;32myou want to use webserver
      \033[1;33m  [ 5 ] \033[1;32myou want to create new user
      \033[1;33m  [ 6 ] \033[1;32myou want to do partion
      \033[1;33m  [ 7 ] \033[1;32myou want to run linux commands
      \033[1;33m  [ 8 ] \033[1;32mTo enter AWS CLOUD
      \033[1;33m  [ m ] \033[1;32mGo to main screen
      \033[1;33m  [ q ] \033[1;32mTo exit
      \033[00m\n""")
      print("\033[1;36mEnter your choice : \033[1;33m" , end="")
      ch = input()
      if ch == "1":
        rConfigureMenu.RConfigureMenu(userPass,userName,remoteIp)
      elif ch == "2":
        rdockerMenu.rDockerMenu(userPass,userName,remoteIp)
      elif ch == "3":
        rhadoopMenu.rhadoopMenu(userPass,userName,remoteIp)
      elif ch == "4":
        rwebserver.webserver(userPass,userName,remoteIp)
      elif ch == "5":
        ruserMenu.userMenu(userPass,userName,remoteIp)
      elif ch == "6":
        rpartitionMenu.partition(userPass,userName,remoteIp)
      elif ch == "7":
        rLinuxCommand.linuxCommand(userPass,userName,remoteIp)
      elif ch == "8":
        remoteAws.raws(userPass,userName,remoteIp)
      elif ch == "m":
        break
      elif ch == "q" or ch == "Q":
        print("\033[00m")
        print ("\033[1;33mGood bye!\033[00m") 
        t.sleep(1)
        exit()
      else :
        print (f'''
        \033[1;33m  [ + ] \033[1;31m This location doesn't support.
        \033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
        input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
      os.system("clear")
  elif location == "q" or location == "Q":
    print("\033[00m")
    print ("\033[1;33mGood bye!\033[00m") 
    t.sleep(1)
    exit()
  else :
    print (f'''
    \033[1;33m  [ + ] \033[1;31m This location doesn't support.
    \033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
    input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
  os.system("clear")


