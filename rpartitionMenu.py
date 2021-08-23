yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

import os
import time as t

def partition(userPass,userName,remoteIp):
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c RPartition MENU") 
    os.system("tput setaf 7")
    print("\n{0}[1]{1} Go to lvm menu\n{0}{0}[2]{1} Create partition\n{0}[b]{1} Go back \n{0}[q]{1} Exit the program\n".format(yellow,green))
    p = input("\033[1;36mEnter your choice : \033[1;33m")
    if p == "1":
      while True:
        os.system("clear")
        os.system("tput setaf 6")
        os.system("figlet -f slant -c RLvm MENU") 
        os.system("tput setaf 7")
        print("""\n{0}[1]{1} To check number of storage attached to the OS\n{0}[2]{1} To create Physical Volume\n{0}[3]{1} To view Physical Volume\n{0}[4]{1} To create Volume Group\n{0}[5]{1} To view Volume Group\n{0}[6]{1} To create Logical Volume\n{0}[7]{1} To view Logical Volume\n{0}[8]{1} To format the LV\n{0}[b]{1} go back\n{0}[q]{1} Exit the program\n""".format(yellow,green))

        i = input("\033[1;36mEnter your Choice : \033[1;33m")
        if i == "1":
          os.system("sshpass -p '{0}' ssh {1}@{2} fdisk -l".format(userPass,userName,remoteIp,creatUser))
          input("\033[36mPress Enter to continue...")
        elif i == "2":
          pv1=input("\033[1;36m Enter the name of storage 1 :\033[1;33m")
          pv2=input("\033[1;36m Enter the name of storage 2 :\033[1;33m")
          os.system("sshpass -p '{0}' ssh {1}@{2} pvcreate {3}".format(userPass,userName,remoteIp,creatUser,pv1))
          t.sleep(2)
          os.system("sshpass -p '{0}' ssh {1}@{2} pvcreate {3}".format(userPass,userName,remoteIp,creatUser,pv2))
          t.sleep(2)
        elif i == "3":
          pv=input("\033[1;36mEnter the name of storage :\033[1;33m")
          os.system("sshpass -p '{0}' ssh {1}@{2} pvdisplay {3}".format(userPass,userName,remoteIp,creatUserpv))
          input("\033[36mPress Enter to continue...")
        elif i == "4":
          vg=input("\033[1;36mGive name to the Volume Group :\033[1;33m")
          pvn1=input("\033[1;36mEnter the name of storage 1 :\033[1;33m")
          pvn2=input("\033[1;36mEnter the name of Storage 2 :\033[1;33m")
          os.system("sshpass -p '{0}' ssh {1}@{2} vgcreate {3} {4} {5}".format(userPass,userName,remoteIp,creatUser,vg,pvn1,pvn2))
          t.sleep(2)
        elif i == "5":
          vg1=input(green+"Enter the name of Volume Group :"+yellow)
          os.sytem("sshpass -p '{0}' ssh {1}@{2} vgdisplay {3}".format(userPass,userName,remoteIp,creatUser,vg1))
          input("\033[36mPress Enter to continue...")
        elif i == "6":
          size=input(green+"Enter size for your Logical Volume :"+yellow)
          lv=input(green+"Give name to your Logical Volume :"+yellow)
          vg2=input(green+"Enter name of the Volume Group :"+yellow)
          os.system("sshpass -p '{0}' ssh {1}@{2} lvcreate --size{3} --name{4} {5}".format(userPass,userName,remoteIp,creatUser,size,lv,vg2))
          t.sleep(2)
        elif i == "7":
          os.system("sshpass -p '{0}' ssh {1}@{2} lvdisplay".format(userPass,userName,remoteIp))
          input("\033[36mPress Enter to continue...")
        elif i == "8":
          vg4=input("\033[1;36mEnter the name of Volume Group :\033[1;33m")
          lv2=input("\033[1;36mEnter the name of Logical Volume :\033[1;33m")
          os.system("sshpass -p '{0}' ssh {1}@{2} mkfs.ext4  /dev{3}{4}".format(userPass,userName,remoteIp,creatUser,vg4,lv2))
          t.sleep(2)
        elif i == "b":
          break
        elif i == "q":
          print("\033[00m")
          print ("\033[1;33mGood bye!\033[00m") 
          t.sleep(1)
          exit()
        else:
          print("This option doesn't support")
          input("\nPress Enter to try again...")
        os.system("clear")
       
    elif p == "2":
      while True:
        os.system("clear")
        os.system("tput setaf 6")
        os.system("figlet -f slant -c RPartition MENU")
        os.system("tput setaf 7")
        print("""\n{0}[1]{1} Create a directory \n{0}[2]{1} Create a partition \n{0}[3]{1}{1} Format partition \n{0}[4]{1} Mount partion \n{0}{0}{0}[5]{1} Permamnent mount\n{0}{0}[6]{1} Show hardisk \n{0}[7]{1} Show partition \n{0}[b]{1} Go to back \n{0}[q]{1} Exit the program\n""".format(yellow,green))
        d = input("\033[1;36mEnter your choice : \033[1;33m")
        if d == "1": 
          partDir = input(green+"Enter the direcory name which you want to create :"+yellow)
          os.system("sshpass -p '{0}' ssh {1}@{2} mkdir {3}".format(userPass,userName,remoteIp,partDir))
          nt(f"{partDir} is created...")
          t.sleep(2)
        elif d == "2": 
          partitionName = input(green+"Give hardisk name : "+yellow)
          os.system("sshpass -p '{0}' ssh {1}@{2} fdisk {3} ".format(userPass,userName,remoteIp,partitionName)) 
          t.sleep(2) 
          os.system("sshpass -p '{0}' ssh {1}@{2} udevadm sttle".format(userPass,userName,remoteIp)) 
        elif d == "3": 
          partName = input(green+"Enter the partion name : "+yellow)
          os.system("sshpass -p '{0}' ssh {1}@{2} mkfs.ext4 {3}".format(userPass,userName,remoteIp,partName))
          t.sleep(2)
        elif d == "4": 
          os.system("sshpass -p '{0}' ssh {1}@{2} echo 'mount {3} {4}' >> /etc/rc.d/rc.local".format(userPass,userName,remoteIp,partName,partDir))
          print("Permanent mount is configureed successfully!!")
          t.sleep(2)
        elif d == "5": 
          os.system("sshpass -p '{0}' ssh {1}@{2} mount {3} {4}".format(userPass,userName,remoteIp,partName,partDir))
          print(f"{partName} is mounted...")
          t.sleep(2)
        elif d == "6": 
          os.system("sshpass -p '{0}' ssh {1}@{2} fdisk -l".format(userPass,userName,remoteIp))
          input("\033[36mPress Enter to continue...")
        elif d == "7": 
          os.system("sshpass -p '{0}' ssh {1}@{2} lsblk".format(userPass,userName,remoteIp))
          input("\033[36mPress Enter to continue...") 
        elif d == "b" or d == "B": 
          break
        elif d == "q" or d == "Q":
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
    elif p == "b":
      break
    elif p == "q":
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
