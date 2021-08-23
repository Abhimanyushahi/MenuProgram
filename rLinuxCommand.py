yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"
import os
import time as t


def linuxCommand(userPass,userName,remoteIp):
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c RLinux MENU")
    os.system("tput setaf 7")
    print("""\n{0}[1]{1} run linux command\n{0}[b]{1} go back \n{0}[q]{1} exit the program
    \n""".format(yellow,green))
    rcmd = input("\033[1;36mEnter your choice : \033[1;33m")
    if rcmd == "1":
      linuxCommand = input(green+"Enter the command : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} {3}".format(userPass,userName,remoteIp,linuxCommand))
      input("\033[1;36mPress Enter to continue.."+end)
    elif rcmd == "b": 
      break
    elif rcmd == "q" or rcmd == "Q":
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
