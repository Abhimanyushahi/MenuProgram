import rnamenode as rn
import rdatanode as rd
import rhadoopClient as rhc
import os
import time as t

yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"
def rhadoopMenu(userPass,userName,remoteIp):
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c hadoop MENU")
    os.system("tput setaf 7")
    print('''\n{0}[1]{1} Go to namenode terminal\n{0}[2]{1} Go to datanode terminal\n{0}[3]{1} Go to hadoop client terminal\n{0}[b]{1} Go back to main menu\n{0}[q]{1} Exit the program{2}\n'''.format(yellow,green,end))
    hd = input("\033[1;36mEnter your choice : \033[1;33m")
    if hd == "1":
      rn.namenode()
    elif hd == "2":
      rd.datanode()
    elif hd == "3":
      rhc.hadoopClient()
    elif hd == "b":
      break
    elif hd == "q" or hd =="Q":
      exit()
    else:
      print (f'''
      \033[1;33m  [ + ] \033[1;31m This option doesn't support.
      \033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
      input("\033[1;33m  [033[1;36m + ] \033[1;34mPress Enter to try again...\033[00m")
    os.system("clear")
