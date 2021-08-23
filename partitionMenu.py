import os
import time as t

def PartitionMenu():
  yellow = "\033[1;33m"
  green = "\033[1;36m"
  end = "\033[00m"
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c Partition MENU") 
    os.system("tput setaf 7")
    print("\n{0}[1]{1} Go to lvm menu\n{0}[2]{1} Create static partition\n{0}[b]{1} go back \n{0}[q]{1} exit the program{2}\n".format(yellow,green,end))
    p = input("\033[1;35mEnter your choice : \033[1;33m")
    if p == "1":
      while True:
        os.system("clear")
        os.system("tput setaf 6")
        os.system("figlet -f slant -c Lvm MENU") 
        os.system("tput setaf 7")
        print("""\n
        {0}[1]{1} To check number of storage attached to the OS
        {0}[2]{1} To create Physical Volume
        {0}[3]{1} To view Physical Volume
        {0}[4]{1} To create Volume Group
        {0}[5]{1} To view Volume Group
        {0}[6]{1} To create Logical Volume
        {0}[7]{1} To view Logical Volume
        {0}[8]{1} To format the LV
        {0}[9]{1} To extend Logical Volume(LV)
        {0}[10]{1} To Mount the Logical Volume to the Datanode Directory
        {0}[b]{1} Go back
        {0}[q]{1} Exit the program{2}\n""".format(yellow,green,end))

        i = input("\033[1;35mEnter your Choice : \033[1;33m")
        if i == "1":
          os.system("fdisk -l")
          input("\033[36mPress Enter to continue...")
        elif i == "2":
          pvcreate=input("\033[1;35mEnter the device or hardisk name :\033[1;33m")
          os.system("pvcreate {}".format(pvcreate))
          print(f"\033[36m{pvcreate} is successfully created...")
          input("\033[36mPress Enter to continue...") 
        elif i == "3":
          os.system("pvdisplay")
          input("\033[36mPress Enter to continue...")
        elif i == "4":
          vgcreate=input("\033[1;35mGive name to the Volume Group :\033[1;33m")
          pvn1=input("\033[1;35mEnter the name of  physical volume :\033[1;33m")
          #pvn2=input("\033[1;36mEnter the name of 2nd physical volume :\033[1;33m")
          os.system("vgcreate {} {} ".format(vgcreate,pvn1))
          print(f"\033[36m{vgcreate} is successfully created...")
          input("\033[36mPress Enter to continue...") 
        elif i == "5":
          os.system("vgdisplay")
          input("\033[36mPress Enter to continue...") 
        elif i == "6":
          size=input("\033[1;35mEnter size for your Logical Volume :\033[1;33m")
          lvcreate=input("\033[1;35mGive name to your Logical Volume :\033[1;33m")
          vg2=input("\033[1;36mEnter name of the Volume Group from which u want to create LV :\033[1;33m")
          os.system("lvcreate --size {} --name {} {}".format(size,lvcreate,vg2))
          print(f"\033[36m{lvcreate} is successfully created...")
          input("\033[36mPress Enter to continue...") 
        elif i == "7":
          os.system("lvdisplay")
          input("\033[36mPress Enter to continue...")
        elif i == "8":
          vg4=input("\033[1;35mEnter the name of Volume Group from which your LV belonging:\033[1;33m")
          lv2=input("\033[1;35mEnter the name of Logical Volume :\033[1;33m")
          os.system("mkfs.ext4 /dev/{0}/{1}".format(vg4,lv2))
          print(f"\033[36m{lv2} is successfully formated...")
          input("\033[36mPress Enter to continue...") 
        elif i == "9":
          size=input("\n\033[1;35m Tell me the size how much u want to increase :\033[1;33m ")
          lv=input("\033[1;35mEnter the name of your logical volume :\033[1;33m ")
          vgname=input("\033[1;35mEnter the name of volume group :\033[1;33m ")
          os.system("lvextend --size +{0} /dev/{1}/{2} ".format(size,vgname,lv))
          os.system("resize2fs /dev/{0}/{1}".format( vgname,lv))
          print(f"\033[36m{ lv} is successfully resized...")
          input("\033[36mPress Enter to continue...") 
          
        elif i == "10":
          datadir=input("\n\033[1;35mEnter the Directory Name : \033[1;33m")
          logicalVol=input("\n\033[1;36mEnter the Logical Volume Name to be mounted : \033[1;33m")
          datavgroup=input("\n\033[1;35mEnter the Volume group Name of this LV : \033[1;33m")
          os.system("mount /dev/{0}/{1} {2}".format(datavgroup,logicalVol,datadir))
          print(f"\033[36m{logicalVol} is successfully mounted...")
          input("\033[36mPress Enter to continue...") 
        elif i == "b":
          break
        elif i == "q":
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
                  
    elif p == "2":
      while True:
        os.system("clear")
        os.system("tput setaf 4")
        os.system("figlet -f slant -c Partition MENU") 
        os.system("tput setaf 7")
        print("""\n{0}[1]{1} Ceate a directory \n{0}[2]{1} Create or delete static Partiton \n{1}{0}[3]{1} Format partition \n{1}{0}[4]{1} Umount partition \n{0}[5]{1} Permamnent mount \n{0}[6]{1} Mount partion \n{0}[7]{1} Show hardisk and partitions name \n{0}[8]{1} Show partition mount point \n{1}{0}[9]{1} Resize the Partition after umount to be mount partition \n{0}[b]{1} go back \n{0}[q]{1} exit the program{2} \n""".format(yellow,green,end))
        d = input("\033[1;35mEnter your choice :\033[1;33m ")
        if d == "1": 
          partDir = input("\033[1;35mEnter the direcory name which you want to create :\033[1;33m")
          os.system("mkdir {0}".format(partDir))
          print(f"\033[36m{partDir} is created...")
          input("\033[36mPress Enter to continue...") 
        elif d == "2": 
          device=input("\033[1;35mEnter device or hardisk name : \033[1;33m")
          os.system("fdisk {0}".format(device)) 
          os.system("udevadm sttle") 
          print("\033[36mPartition is created successfully!!") 
          input("\033[36mPress Enter to continue...") 
        elif d == "3": 
          partName = input("\033[1;35mEnter the partion name :\033[1;33m ")
          os.system("mkfs.ext4 {0}".format(partName))
          print(f"\033[36m{partName} is formated...")
          input("\033[36mPress Enter to continue...") 
        elif d == "4":
          umount= input("\033[1;35mEnter the partion name :\033[1;33m ")
          os.system("umount {0}".format(umount))
          print(f"\033[36m{umount} is unmounted...")
          input("\033[36mPress Enter to continue...") 
        elif d == "5": 
          os.system("echo 'mount {0} {1}' >> /etc/rc.d/rc.local".format(partName,partDir))
          print("\033[36mPermanent mount is configureed successfully!!")
          input("\033[36mPress Enter to continue...") 
        elif d == "6": 
          mount= input("\033[1;35mEnter the partion name :\033[1;33m ")
          mountdir= input("\033[1;35mEnter the directory name :\033[1;33m ")
          os.system("mount {0} {1}".format(mount,mountdir))
          print(f"\033[36m{mount} is mounted...")
          input("\033[36mPress Enter to continue...") 
        elif d == "7": 
          os.system("fdisk -l")
          input("\033[36mPress Enter to continue...")
        elif d == "8": 
          os.system("lsblk")
          input("\033[36mPress Enter to continue...") 
        elif d == "9": 
          resize=input("\033[1;35mEnter the partion name :\033[1;33m ")
          os.system("resize2fs {0}".format(resize))
          print(f"\033[36m{resize} is resized...")
          input("\033[36mPress Enter to continue...") 
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

