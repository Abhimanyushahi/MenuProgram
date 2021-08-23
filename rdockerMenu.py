import os
import time as t

yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

def rDockerMenu(userPass,userName,remoteIp):
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c Docker MENU")
    os.system("tput setaf 7")
    print("""\n{0}[1]{1} Install docker\n{0}[2]{1} Launch new container\n{0}[3]{1} Start docker\n{0}[4]{1} Show running containers\n{0}[5]{1} Show all containers either stop or running\n{0}[6]{1} Download docker image\n{0}[7]{1} Show all images\n{0}[8]{1} Go inside a docker container\n{0}[9]{1} To remove a container\n{0}[10]{1} To start a container\n{0}[11]{1} To stop a container \n{0}[b]{1} Go back\n{0}[q]{1} Exit the program{2}\n""".format(yellow,green,end))
    print("\033[1;33mWhat you want to do in docker?", end='\n')
    d = input("\033[1;36mEnter your choice :\033[1;33m ")
            
    if d == "1": #("docker" in d) and ("install" in d):
      os.system("sshpass -p '{0}' ssh {1}@{2} yum install docker-ce --nobest".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} systemctl enable docker".format(userPass,userName,remoteIp))
      t.sleep(2)
    elif d == "2": #("run" in d) and ("docker" in d):
      dname = input("Give OS name : ")
      os.system("sshpass -p '{0}' ssh {1}@{2} docker run -it --name {3} centos:latest".format(userPass,userName,remoteIp,dname))
      print(green+f"{dname} is launched successfully!")
      t.sleep(2)
    elif d == "3": #("start" in d) and ("docker" in d):
      os.system("sshpass -p '{0}' ssh {1}@{2} systemctl start docker ".format(userPass,userName,remoteIp))
      print(green+"Docker is started !!")
      t.sleep(2)
    elif d == "4": # ("status" in d) and ("running" in d):
      os.system("sshpass -p '{0}' ssh {1}@{2} docker ps ".format(userPass,userName,remoteIp))
      input(green+"Press enter to continue...")
    elif d == "5": #("status" in d) and ("all" in d):
      os.system("sshpass -p '{0}' ssh {1}@{2} docker ps -a".format(userPass,userName,remoteIp))
      input(green+"Press enter to continue...")
    elif d == "6": #("detail" in d):
      dpull == input("Enter docker image name : ")
      os.system("sshpass -p '{0}' ssh {1}@{2} docker pull {3} ".format(userPass,userName,remoteIp,dpull))
      t.sleep(2)
    elif d == "7": #("copy" in d) and ("os" in d):
      os.system("sshpass -p '{0}' ssh {1}@{2} docker images".format(userPass,userName,remoteIp))
      input(green+"Press Enter to continue...") 
    elif d == "8":
      contName = input(green+"Enter the existed container name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} docker exec -it {3} /bin/bash".format(userPass,userName,remoteIp,contName))
    elif d == "9":
      rmContainer = input(green+"Enter conatiner name to be removed : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} docker rm -f {3}".format(userPass,userName,remoteIp,rmContainer))
      print(green+f"{rmcontainer} is removed!"+end)
      t.sleep(2)
    elif d == "10":
      startCont = input(green+"Enter container name which you want to start : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} docker start {3}".format(userPass,userName,remoteIp,stCont))
      print(green+f"{stCont} is started..."+end)
      t.sleep(2)
    elif d == "11":
      stopCont = input(green+"Enter container name which you want to start : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} docker stop {3}".format(userPass,userName,remoteIp,stopCont))
      print(green+f"{stopCont} is stopped!"+end)
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
