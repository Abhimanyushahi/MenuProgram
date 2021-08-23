yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

import os
import time as t
def namenode():
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c Namenode")
    os.system("tput setaf 7")
    print("""\n{0}[1]{1} Install hadoop \t{0}[2]{1} Namenode setup file \n{0}[3]{1} Start  \t\t{0}[4]{1} Start permanent\n{0}[5]{1} Remove directory\t{0}[6]{1} Report of hdfs\n{0}[7]{1} Stop firewall\t{0}[8]{1} Show all files of hdfs\n{0}[9]{1} Load files on hdfs \t{0}[10]{1} Delete file from hdfs \n{0}[11]{1} Read hdfs file\t{0}[12]{1} Fix block size on loading \n{0}[13]{1} Safemode on\t{0}[14]{1} Safemode off \n{0}[15]{1} Read core-site.xml file \t{0}[16]{1} Read hdfs-site.xml file\n{0}[b]{1} Go back\t\t{0}[q]{1} Exit the program{2}
    \n""".format(yellow,green,end))
    lnd = input("\033[1;36mEnter your choice : \033[1;33m")
    if lnd == "1": 
      lnjdkFile = input("\033[1;36mEnter path name of jdk software where it present in your local system : \033[1;33m")
      lnjdk = subprocess.getstatusoutput("ls {0} | grep jdk".format(lnjdkFile))
      print(green) 
      os.system("rpm -ivh {0} ".format(lnjdk[1]))
      javaVersion = input("\033[1;36mDo you want to check jdk is successfully installed or not (y/n) : \033[1;33m")
      if javaVersion == "y":
        print(green) 
        os.system("java -version")
        t.sleep(2)
      lnhadoopFile = input("\033[1;36mEnter full path name of hadoop software where it is present in your system : \033[1;33m")
      lnhadoop = subprocess.getstatusoutput("ls {0} | grep hadoop".format(lnhadoopFile))
      print(green)  
      os.system("rpm -ivh {0} --force".format(lnhadoop[1]))
      print("\033[1;36mAre you want to check hadoop is  successfully installed or not (y/n) : \033[1;33m ", end = "")
      ans = input()
      if ans == "y":
        print(green) 
        os.system("hadoop version")
        input(green+"Press Enter to continue..."+end)
    elif lnd == "2" : 
      namePort = input("\033[1;36mEnter port number on which you want to bind namenode or hdfs : \033[1;33m")
      os.system("cat coren1.txt >> /etc/hadoop/core-site.xml")
      os.system("echo '<value>hdfs://0.0.0.0:{0}</value> ' >> /etc/hadoop/core-site.xml".format(namePort))
      os.system(" cat coren2.txt >> /etc/hadoop/core-site.xml")
      ##############namenode coref-site.xml############
      nameDir = input("\033[1;36mEnter new directory name of which you want to make hdfs file system in namenode : \033[1;33m")
      os.system("cat hdfsn1.txt >> /etc/hadoop/hdfs-site.xml")
      os.system("echo '<value>{0}</value>' >> /etc/hadoop/hdfs-site.xml".format(nameDir))
      os.system("cat coren2.txt >> /etc/hadoop/hdfs-site.xml")
      print(f'''\033[1;33m  [ + ] \033[1;32mNamenode is configured sucessfully !!''')
      t.sleep(2)
      #################namenode hdfs-site.xml#############
      formatAns = input("\033[1;36mDo you want to format namenode(y/n) : \033[1;33m")
      if formatAns == "y":
        print(green)
        os.system("hadoop namenode -format")
        input(cyan+"Press Enter to continue..."+end)
    elif  lnd == "3": 
      os.system("hadoop-daemon.sh start namenode")
      jpsNameCheck = input("\033[1;36mDo you want to see namenode start or not (y/n) :\033[1;33m ")
      if jpsNameCheck == "y":
        os.system("jps")
      t.sleep(2)
    elif lnd == "4":  
      os.system("echo ' ' >> /etc/rc.d/rc.local")
      os.system("echo ' hadoop daemon.sh start namenode' >> /etc/rc.d/rc.local")
      os.system("chmod +x /etc/rc.d/rc.local")
      print(f'''
      \033[1;33m  [ + ] \033[1;32mNamenode permanent start setup is configured sucessfully !!''')
      t.sleep(2)
    elif lnd == "5":  
      localDir = input("\033[1;36mEnter the directory name :\033[1;33m")
      os.system(f"rm -rvf {localDir} ")
      print(green+f"{localDir} is removed!"+end)
      t.sleep(2)
    elif lnd == "6": 
      os.system("hadoop dfsadmin -report")
      input(green+"Press enter to continue..."+end)
    elif lnd == "7":  
      os.system("systemctl stop firewalld")
      print(green+"Firewall is stopped!"+end)
      t.sleep(2)
    elif lnd == "8": 
       fsDir = input("\033[1;36mEnter directory name : \033[1;33m")
       os.system("hadoop fs -ls /{0}".format(fsDir))
       input(green+"Press Enter to continue..."+end)
    elif lnd == "9": 
      loadFile = input("\033[1;36mEnter file name which you want to load: \033[1;33m")
      loadDir = input("\033[1;36mEnter directory name where you want to load :\033[1;33m")
      os.system("hadoop fs -put {0} {1}".format(loadFile,loadDir))
      print(green+f"{loadFile} is uploaded successfully!!"+end)
      t.sleep(2)
    elif lnd == "10": 
      remFile = input("\033[1;36mEnter file name with full path name :\033[1;33m ")
      os.system("hadoop fs -rm {0}".format(remFile))
      print(green+f"{remFile} is removed !"+end)
    elif lnd == "11":  
      readFile = input("\033[1;36mEnter file name with location : \033[1;33m")
      os.system("hadoop fs -cat {0} ".format(readFile))
      input(cyan+"Press Enter to continue..."+end)
    elif lnd == "12" : 
      blockSize = int(input("\033[1;36mEnter block size in bytes which you want to give :\033[1;33m"))
      blockFile = input("\033[1;36mEnter file name which you want to upload :\033[1;33m")
      blockDir = input("\033[1;36mEnter the directory name in which you want to upload :\033[1;33m ")
      os.system("hadoop fs -Ddfs.block.size={0} -put {1} {2} ".format(blockSize,blockFile,blockDir))
      print(cyan+"{blockFile} is uploaded successfully !!"+end)
      t.sleep(2)
    elif lnd == "13":
      os.system("hadoop dfsadmin -safemode get")
      print(cyan+" safe mode is on!"+end)
      t.sleep(2)
    elif lnd == "14": 
      os.system("hadoop dfsadmin -safemode leave")
      print(cyan+" safe mode is off!"+end)
      t.sleep(2)
    elif lnd == "15":
      os.system("cat /etc/hadoop/core-site.xml")
      input(cyan+"Press Enter to continue..."+end)
    elif lnd == "16":
      os.system("cat /etc/hadoop/hdfs-site.xml")
      input(cyan+"Press Enter to continue..."+end)
    elif lnd == "b": 
      break
    elif lnd == "q":
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
