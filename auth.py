import os
import socket
import subprocess
import getpass

yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"
def authentication():
  while True:
    remoteIp = input("\033[1;36mEnter your remote IP address :\033[1;33m ")
    try:
      socket.inet_aton(remoteIp)
      print("\033[1;33mValid IP addreess")
      live=subprocess.getstatusoutput("ping {0} -c 1".format(remoteIp))
      if live[0] == 0:
        while True:
          userName = input("\033[1;36mEnter your remote user name :\033[1;33m ")
          userPass = getpass.getpass("\033[1;36mEnter your remote password \033[00m: ")
          login = subprocess.getstatusoutput("sshpass -p '{0}' ssh -o 'StrictHostKeyChecking=no' {1}@{2} date".format(userPass,userName,remoteIp))
          if login[0] != 0:
            print("\033[1;33m  [ + ] \033[1;31m Sorry! Either userName or password is incorrect!")
            input(green+"Press enter to try again"+end)
            os.system("clear")
          else:
            break
        break
      else:
        print("\033[1;33m  [ + ] \033[1;31m Sorry ! This IP address is not live or in your network.")
        print("\033[1;36mPlease Enter Another IPadress.")
        input("\033[1;36mPress Enter to continue...\033[00m")
        os.system("clear")
    except socket.error:
      print("\033[1;33m  [ + ] \033[1;31m Sorry ! you have typed incorrect IP address.")
      input("\033[1;33mPress Enter to re-enter Ip address...\033[00m")
      os.system("clear")
  return userPass,userName,remoteIp
