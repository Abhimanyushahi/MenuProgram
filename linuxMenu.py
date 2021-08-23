yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

import os
import time as t
def linuxMenu():
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c Linux MENU")
    os.system("tput setaf 7")
    print("""\n{0}[1]{1} run linux command\n{0}[b]{1} go back\n{0}[q]{1} exit the program
      {2}\n""".format(yellow,green,end))
    ch = input("\033[1;36mEnter your choice :\033[1;33m ")
    if ch == "1":
      linuxCommand = input("\033[1;36mEnter the command :\033[1;33m ")
      print("\033[00m")
      os.system("{0}".format(linuxCommand))
      input(green+"Press Enter to continue.."+end)
    elif ch == "b": 
      break
    elif ch == "q":
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
