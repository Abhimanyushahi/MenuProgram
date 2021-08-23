import os
import time as t
import subprocess
yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

def datanode(userPass,userName,remoteIp):
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c Datanode MENU")
    os.system("tput setaf 7")
    print("""\n{0}[1]{1} install hadoop \t\t{0}[2]{1} Datanode setup file\n{0}[3]{1} start \t\t\t{0}[4]{1} stop\n{0}[5]{1} report of hdfs\t\t{0}[6]{1}remove local directory\n{0}[7]{1} see current directry locally{0}[8]{1} download hdfs file \n{0}[9]{1} show all files of hdfs \t{0}[10]{1} delete hdfs directory\n{0}[11]{1} upload files on hdfs \t{0}[12]{1} delete file from hdfs\n{0}[13]{1} read file \t\t\t{0}[14]{1} Fix block size on loading\n{0}[15]{1} help \t\t\t{0}[16]{1} create a file\n{0}[17]{1} read core-site.xml file \t{0}[18]{1} read hdfs-site.xml file\n{0}[b]{1} Go back \t\t\t{0}[q]{1} to exit the program\n""".format(yellow,green,end))
    d = input("\033[1;36mPlease Enter your choice : \033[1;33m")
    if d == "1":               
      rdjdkFile = input(green+"Enter path name of jdk software whereit present in your remote system : "+yellow)
      rdjdk = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {3} | grep jdk".format(userPass,userName,remoteIp,rdjdkFile))                
      os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} ".format(userPass,userName,remoteIp,rjddk[1]))   
      javaVersion = input("\033[1;33mdo you want to check jdk is successfully installed or not (y/n) :"+yellow)
      if javaVersion == "y":
        os.system("sshpass -p '{0}' ssh {1}@{2} java -version".format(userPass,userName,remoteIp))
        t.sleep(2)
      rdhadoopFile = input("Enter full path name of hadoop software where it is present in your remote system : ")
      rnhadoop = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {3} | grep hadoop".format(userPass,userName,remoteIp,rdhadoopFile))   
      os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} --force".format(userPass,userName,remoteIp,rdhadoop[1]))   
      print("\033[1;33mAre you want to check hadoop is  successfully installed or not (y/n) : \033[1;33m")
      ans = input()
      if ans == "y":
        os.system("sshpass -p '{0}' ssh {1}@{2} hadoop version".format(userPass,userName,remoteIp))
        t.sleep(2)
    elif d == "2": 
      nameIp = input("\033[1;36mEnter ip address of namenode : \033[1;33m")
      namePort = input("\033[1;36mEnter port number on which namenode binding hdfs : \033[1;33m")
      dataDir = input("\033[1;36mEnter directory name for creating directory to be shared datanode : \033[1;33m")
      os.system("sshpass -p '{0}' ssh {1}@{2} mkdir /{3}".format(userPass,userName,remoteIp,dataDir))
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /cored1.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
      
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>hdfs://{3}:{4}</value> ' >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp,nameIp,namePort))
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /coren2.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
    
                  ####datanode core-site.xml###########################
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /hdfsd1.txt >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>/{3}</value>' >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp,dataDir))
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /coren2.txt >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      print(f'''\033[1;33m  [ + ] \033[1;32mDatanode is configured sucessfully !!''')
      t.sleep(2)
                              ########datanode hdfs-site.xml##########################
    elif d == "3": 
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop-daemon.sh start datanode".format(userPass,userName,remoteIp,remoteIp))
      jpsDataCheck = input("\033[1;36mDo you want to see datanode start or not (y/n) : \033[1;33m")
      if jpsDataCheck == "y":
        os.system("sshpass -p '{0}' ssh {1}@{2} jps".format(userPass,userName,remoteIp))
        t.sleep(2)
    elif d == "4": 
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop-daemon.sh stop datanode".format(userPass,userName,remoteIp))
      print("\033[1;32mDatanode is stopped !!")
      t.sleep(2)
    elif d == "5": 
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -report".format(userPass,userName,remoteIp,remoteIp))
      input("\033[1;32mPress enter to continue... !!")
    elif d == "6": 
      rlocalDataDir = input(green+"Enter the Directory name :"+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} rm -rvf {3} ".format(userPass,userName,remoteIp,remoteIp,rlocaDataDir))
      t.sleep(2)
    elif d == "7": 
      os.system("sshpass -p '{0}' ssh {1}@{2} pwd".format(userPass,userName,remoteIp))
      t.sleep(2)
    elif d == "8": 
      rhadoopFile = input(green+"Enter hadoop file file name : "+yellow)
      rsavedLocalDir = input(green+"Enter the name of local directory where you want to save it : "+yellow)
      os.system("st.sleep(2)shpass -p '{0}' ssh {1}@{2} hadoop fs -get {3} {4}".format(userPass,userName,remoteIp,rhadoopFile,rsaveLocalDir))
      print(f'''\033[1;36m {rhadoopFile} is uploaded !!'''+end)
      t.sleep(2)
    elif d == "9": 
      fsDir = input(green+"Enter directory name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -ls /{3}".format(userPass,userName,remoteIp,fsDir))
      input("\033[1;36mPress Enter to continue... !!")
    elif d == "10": 
      rhadoopDir = input(green+"Enter the hadoop directroy to be deleted : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rmr {3} ".format(userPass,userName,remoteIp,rhadoopDir))
      print(f'''\033[1;36m {rhadoopDir} is removed !!'''+end)
      t.sleep(1)
    elif d == "11":
      rloadFile = input(green+"Enter file name which you want to load : "+yellow)
      rloadDir = input(green+"Enter directory name where you want to load : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -put {1} {2}".format(userPass,userName,remoteIp,rloadFile,rloadDir))
      print(f'''\033[1;36m {rloadFile} is uploaded!!'''+end)
      t.sleep(1)
    elif d == "12": 
      rremFile = input(green+"Enter file name with full path name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rm {3}".format(userPass,userName,remoteIp,rremFile))
      print(f'''\033[1;36m {remFile} is removed !!'''+end)
      t.sleep(1)
    elif d == "13": 
      rreadFile = input(green+"Enter file name with location : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -cat {3} ".format(userPass,userName,remoteIp,rreadFile))
      input("\033[1;36mPress Enter to continue... !!")
    elif d == "14" :
      print(+green+"Enter block size in bytes which you want to give : "+yellow, end = "") 
      blockSize = int(input())
      blockFile = input(green+"Enter file name which you want to upload :"+yellow)
      blockDir = input(green+"Enter the directory name in which you want to upload : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -Ddfs.block.size={1} -put {3} {4} ".format(userPass,userName,remoteIp,blockSize,blockFile,blockDir))
      t.sleep(1)
    elif d == "15": 
      help = input("\033[1;36mEnter hadoop command : \033[1;33m")
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -help {3}".format(userPass,userName,remoteIp,help))
      input("\033[36mPress Enter to continue...")
    elif d == "16":
      print(yellow+"for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
      dataFileName = input("\033[1;36menter file name : \033[1;36m")
      os.system("sshpass -p '{0}' ssh {1}@{2} vim {3}".format(userPass,userName,remoteIp,dataFileName))
    elif d == "17":
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
      input(cyan+"Press Enter to continue..."+end)
    elif d == "18":
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
