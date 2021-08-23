yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" 
end = "\033[00m"

import os
import time as t

def UserMenu():
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c User MENU")
    os.system("tput setaf 7")
    print("""\n{0}[1]{1} create user \n{0}[2]{1} create password for a user \n{0}[b]{1} Go back \n{0}[q]{1} exit the program
    \n""".format(yellow,green,end))
    d = input("\033[1;36mEnter your choice : \033[1;33m")
    if d == "1":
      print("\033[1;36mEnter user name :\033[1;33m" , end='')
      createUser = input()
      os.system("useradd {}".format(createUser))
      t.sleep(2)
    elif d == "2":
      os.system("passwd {0} ".format(creatUser))
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
