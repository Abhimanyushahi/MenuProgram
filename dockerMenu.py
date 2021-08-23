yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"
import os
import time as t
def DockerMenu():
  while True:
  	os.system("clear")
  	os.system("tput setaf 6")
  	os.system("figlet -f slant -c Docker MENU")
  	os.system("tput setaf 7")
  	print("""\n{0}[1]{1} Install docker\n{0}[2]{1} Launch new container\n{0}[3]{1} Start docker\n{0}[4]{1} Show running containers\n{0}[5]{1} Show all containers either stop or running\n{0}[6]{1} Download docker image\n{0}[7]{1} Show all images\n{0}[8]{1} Go inside a docker container\n{0}[9]{1} To remove a container\n{0}[10]{1} To start a container\n{0}[11]{1} To stop a container \n{0}[b]{1} Go back to main menu\n{0}[q]{1} Exit the program{2}
  	\n""".format(yellow,green,end))
  	print("\033[1;33mWhat you want to do in docker?", end='\n')
  	d = input("\033[1;36mEnter your choice :\033[1;33m ")
  	if d == "1": 
  	  os.system("yum install docker-ce --nobest")
  	  os.system("systemctl enable docker")
  	  t.sleep(2)
  	elif d == "2": 
  	  dname = input("\033[1;36mEnter os name :\033[1;33m")
  	  os.system("docker run -dit --name {0} centos:latest".format(dname))
  	  print(green+f"{dname} is launched successfully!")
  	  t.sleep(2)
  	elif d == "3": 
  	  os.system("systemctl start docker ")
  	  print(green+"Docker is started !!")
  	  t.sleep(2)
  	elif d == "4": 
  	  os.system("docker ps ")
  	  input(green+"Press enter to continue...")
  	elif d == "5": 
  	  os.system("docker ps -a")
  	  input(green+"Press enter to continue...")
  	elif d == "6": 
  	  dpull == input("\033[1;36mEnter Docker image name :\033[1;33m : ")
  	  os.system("docker pull {0} ".format(dpull))
  	  t.sleep(2)
  	elif d == "7": 
  	  os.system("docker images") 
  	  input(green+"Press Enter to continue...")
  	elif d == "8":
  	  contName = input(green+"Enter the existed container name : "+yellow)
  	  os.system(f"docker exec -it {contName} /bin/bash")
  	elif d == "9":
  	  rmContainer = input(green+"Enter conatiner name to be removed : "+yellow)
  	  os.system(f"docker rm -f {rmContainer}")
  	  print(green+f"{rmcontainer} is removed!"+end)
  	  t.sleep(2)
  	elif d == "10":
  	  startCont = input(green+"Enter container name which you want to start : "+yellow)
  	  os.system(f"docker start {stCont}")
  	  print(green+f"{stCont} is started..."+end)
  	  t.sleep(2)
  	elif d == "11":
  	  stopCont = input(green+"Enter container name which you want to start : "+yellow)
  	  os.system(f"docker stop {stopCont}")
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

  
