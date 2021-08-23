yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

import os
import subprocess
import time as t

def namenode(userPass,userName,remoteIp):
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c Namenode MENU")
    os.system("tput setaf 7")
    print("""\n{0}[1]{1} install hadoop           {0}[2]{1} Namenode setup file \n{0}[3]{1} start                    {0}[4]{1} start permanent\n{0}[5]{1} remove directory         {0}[6]{1} report of hdfs\n{0}[7]{1} stop firewall            {0}[8]{1} show all files of hdfs\n{0}[9]{1} load files on hdfs       {0}[10]{1} delete file from hdfs \n{0}[11]{1} read file               {0}[12]{1} Fix block size on loading \n{0}[13]{1} safemode on             {0}[14]{1} safemode off\n{0}[15]{1} read core-site.xml file {0}[16]{1} read hdfs-site.xml file \n{0}[b]{1} Go back                  {0}[q]{1} to exit the program\n""".format(yellow,green,end))
    d = input("\033[1;36mPlease Enter your choice : \033[1;33m")
    if d == "1": 
      rnjdkFile = input(green+"Enter path name of jdk software whereit present in your remote system : "+end)
      rnjdk = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {3} | grep jdk".format(userPass,userName,remoteIp,rnjdkFile))   
      os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} ".format(userPass,userName,remoteIp,rnjdk[1]))
      javaVersion = input(green+"do you want to check jdk is successfully installed or not (y/n) :"+yellow)
      if javaVersion == "y":
        os.system("sshpass -p '{0}' ssh {1}@{2} java -version".format(userPass,userName,remoteIp))
      t.sleep(2)
      rnhadoopFile = input(green+"Enter full path name of hadoop software where it is present in your remote system : ")
      rnhadoop = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {3} | grep hadoop".format(userPass,userName,remoteIp,rnhadoopFile))  
      os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} --force".format(userPass,userName,remoteIp,rnhadoop[1]))
      print(green+"Are you want to check hadoop is  successfully installed or not (y/n) : "+yellow)
      ans = input()
      if ans == "y":
        os.system("sshpass -p '{0}' ssh {1}@{2} hadoop version".format(userPass,userName,remoteIp))
      t.sleep(2)
    elif d == "2" : 
      namePort = input(green+"Enter port number on which namenode binding hdfs : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /coren1.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>hdfs://0.0.0.0:{3}</value> ' >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp,namePort))
      os.system(" sshpass -p '{0}' ssh {1}@{2} cat /coren2.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
      ##############namenode coref-site.xml############
      nameDir = input(green+"Enter directory name for creating directory to be made hdfs file system in namenode : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /hdfsn1.txt >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>/{3}</value>' >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp,nameDir))
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /coren2.txt >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      print(f'''\033[1;33m  [ + ] \033[1;32mNamenode is configured sucessfully !!''')
      t.sleep(2)
          
      formatAns = input(green+"Do you want to format namenode : "+yellow)
      if formatAns == "y":
        os.system("sshpass -p '{0}' ssh {1}@{2} hadoop namenode -format".format(userPass,userName,remoteIp))
      print(green+"Namenode is formated..."+end)
      t.sleep(2)
    elif  d == "3": 
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop-daemon.sh start namenode".format(userPass,userName,remoteIp))
      jpsNameCheck = input(green+"Do you want to see namenode start or not (y/n) : "+yellow)
      if jpsNameCheck == "y":
        os.system("sshpass -p '{0}' ssh {1}@{2} jps".format(userPass,userName,remoteIp))
        t.sleep(2)
    elif d == "4":  
      os.system("sshpass -p '{0}' ssh {1}@{2} echo ' ' >> /etc/rc.d/rc.local".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} echo ' hadoop daemon.sh start namenode' >> /etc/rc.d/rc.local".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} chmod +x /etc/rc.d/rc.local".format(userPass,userName,remoteIp))
      print(f'''
      \033[1;33m  [ + ] \033[1;32mNamenode permanent start setup is configured sucessfully !!''')
      input("\033[1;33m  [ + ] \033[1;32mEnter to continue..."+end)
    elif d == "5":  
      remoteDir = input(green+"Enter the directory name :"+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} rm -rvf {3} ".format(userPass,userName,remoteIp,remoteDir))
      print(green+f"{remoteDir} is removed!"+end)
      t.sleep(2)
    elif d == "6": 
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -report".format(userPass,userName,remoteIp))
      input(green+"Press enter to continue..."+end)
      #os.system("sshpass -p '{0}' ssh {1}@{2} hadoop-daemon.sh stop namenode".format(userPass,userName,remoteIp))
    elif d == "7":  
      os.system("sshpass -p '{0}' ssh {1}@{2} systemctl stop firewalld".format(userPass,userName,remoteIp))
      print(green+"Firewall is stopped!"+end)
      t.sleep(2)
    elif d == "8": 
       fsDir = input(green+"Enter directory name :"+yellow)
       os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -ls /{3}".format(userPass,userName,remoteIp,fsDir))
       input(green+"Press Enter to continue..."+end)
    elif d == "9": 
      rloadFile = input(green+"Enter file name which you want to load : "+yellow)
      rloadDir = input(green+"Enter directory name where you want to load :"+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -put {3} {4}".format(userPass,userName,remoteIp,rloadFile,rloadDir))
      print(green+f"{rloadFile} is uploaded successfully!!"+end)
      t.sleep(2)
    elif d == "10": 
      rremFile = input(green+"Enter file name with full path name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rm {3}".format(userPass,userName,remoteIp,rremFile))
      print(green+f"{rremFile} is removed !"+end)
      t.sleep(2)
    elif d == "11":  
      readFile = input(green+"Enter file name with location : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -cat {3} ".format(userPass,userName,remoteIp,readFile))
      input(cyan+"Press Enter to continue..."+end)
    elif d == "12" : 
      print(green+"Enter block size in bytes which you want to give :"+yellow, end= "")
      blockSize = int(input())
      blockFile = input(green+"Enter file name which you want to upload :"+yellow)
      blockDir = input(green+"Enter the directory name in which you want to upload : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -Ddfs.block.size={3} -put {4} {5} ".format(userPass,userName,remoteIp,blockSize,blockFile,blockDir))
      print(cyan+"{blockFile} is uploaded successfully !!"+end)
      t.sleep(2)
    elif d == "13": 
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -safemode get".format(userPass,userName,remoteIp))
      print(cyan+" safe mode is on!"+end)
      t.sleep(2)           
    elif d == "14": 
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -safemode leave".format(userPass,userName,remoteIp))
      print(cyan+" safe mode is off!"+end)
      t.sleep(2)
    elif d == "15":
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp).format(userPass,userName,remoteIp))
      input(cyan+"Press Enter to continue..."+end)
    elif d == "16":
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      input(cyan+"Press Enter to continue..."+end)
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
