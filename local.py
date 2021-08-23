import os

def local():
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
    elif ch == "2":
    elif ch == "3":
    elif ch == "4":
    elif ch == "5":
    elif ch == "6":
    elif ch == "7":
    elif ch == "8":
    elif ch == "m":
    elif ch == "q" or ch == "Q":
    else :
      print (f'''
      \033[1;33m  [ + ] \033[1;31m This option doesn't support.
      \033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
      input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
    os.system("clear")
