import os
import subprocess
import time as t

yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

def hadoopclient(userPass,userName,remoteIp):
  while True:
    os.system("clear")
    os.system("tput setaf 6")
    os.system("figlet -f slant -c hadoop Client")
    os.system("tput setaf 7")
    print("""\n{0}[1]{1} install hadoop                {0}[2]{1} hadoop client setup file\n{0}[3]{1} Block size fix set up in file {0}[4]{1} replication factor set up\n{0}[5]{1} make a remote direcory        {0}{0}[6]{1} report of hdfs\n{0}[7]{1} remove remote directory       {0}[8]{1} see current directry locally \n{0}[9]{1} download hdfs file            {0}[10]{1} show all files of hdfs\n{0}[11]{1} delete hdfs directory        {0}[12]{1} upload files on hdfs\n{0}[13]{1} delete file from hdfs        {0}[14]{1} read file \n{0}[15]{1} Fix block size on loading    {0}[16]{1} help\n{0}[17]{1} create a file                {0}[18]{1} read core-site.xml file \n{0}[19]{1} read hdfs-site.xml file      {0}[b]{1} Go back \n{0}[q]{1} to exit the program
    \n""".format(yellow,green,end))
    d = input("\033[1;36mPlease Enter your choice : \033[1;33m")
    if d == "1": 
      ldjdkFile = input("\033[1;36mEnter path name of jdk software whereit present in your local system : \033[1;33m")
      ldjdk = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {0} | grep jdk".format(userPass,userName,remoteIp,ldjdkFile)) 
      os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} ".format(userPass,userName,remoteIp,ldjdk[1]))
      javaVersion = input("\033[1;36mdo you want to check jdk is successfully installed or not (y/n) :\033[1;33m")
      if javaVersion == "y":
        os.system("sshpass -p '{0}' ssh {1}@{2} java -version".format(userPass,userName,remoteIp))
        t.sleep(2)
      ldhadoopFile = input(green+"Enter full path name of hadoop software where it is present in your system : "+yellow)
      ldhadoop = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {4} | grep hadoop".format(userPass,userName,remoteIp,ldhadoopFile)) 
      os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} --force".format(userPass,userName,remoteIp,ldhadoop[1]))
      print(green+"Are you want to check hadoop is  successfully installed or not (y/n) : "+yellow)
      ans = input()
      if ans == "y":
        os.system("sshpass -p '{0}' ssh {1}@{2} hadoop version".format(userPass,userName,remoteIp))
        t.sleep(2)
    elif d == "2": 
      nameIp = input(green+"Enter ip address of namenode : "+yellow)
      namePort = input(green+"Enter port number on which namenode binding hdfs : "+yellow)
      dataDir = input(green+"Enter directory name for creating directory to be shared datanode : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} mkdir /{0}".format(userPass,userName,remoteIp,dataDir))
      os.system("sshpass -p '{0}' ssh {1}@{2} /cat cored1.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
      
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>hdfs://{3}:{4}</value> ' >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp,nameIp,namePort))
      os.system("sshpass -p '{0}' ssh {1}@{2} /cat coren2.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
      print(f'''\033[1;33m  [ + ] \033[1;32mHadoop client is configured sucessfully !!''')
      t.sleep(2)
    elif d == "3":
      print(green+"Enter block size to be fixed on client : "+yellow, end = "") 
      lcblockSize = int(input())
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<property>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<name>dfs.block.size</name>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>{3}</value>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp,lcblockSize))
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '</property>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      print(f'''\033[1;33m  [ + ] \033[1;32mBlock size is fixed sucessfully !!''')
      t.sleep(2)
                  
    elif d == "4": 
      print(green+"Enter replication factor : "+yellow, end = "")
      rreplication = int(input())  
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<property>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} sshpass -p '{0}' ssh {1}@{2} echo '<name>dfs.replication</name>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>{3}</value>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp,rreplication))
      os.system("sshpass -p '{0}' ssh {1}@{2} echo '</property>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
      print(f'''\033[1;33m  [ + ] \033[1;32mReplication factor{rreplication} is fixed sucessfully !!''')
      t.sleep(2)
    elif d == "5": 
      rcDir = input(green+"Enter directory name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} mkdir {3}".format(userPass,userName,remoteIp,rcDir))
      print(f"\033[36m{rcDir} is removed...")
      t.sleep(2)
    elif d == "6": 
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -report".format(userPass,userName,remoteIp))
      input("\033[36mPress Enter to continue...")
    elif d == "7": 
      localDataDir = input(green+"Enter the Directory name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} rm -rvf {3} ".format(userPass,userName,remoteIp,locaDataDir))
      print(f"\033[36m{localDataDir} is removed...")
      t.sleep(2)
    elif d == "8": 
      os.system("sshpass -p '{0}' ssh {1}@{2} pwd".format(userPass,userName,remoteIp))
      t.sleep(2)
    elif d == "9": 
      rhadoopFile = input(green+"Enter hadoop file file name : "+yellow)
      rsavedLocalDir = input(green+"Enter the name of local directory where you want to save it : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -get {3} {4}".format(userPass,userName,remoteIp,rhadoopFile,rsaveLocalDir))
      print(f"{rhadoopFile} is downloaded...")
      t.sleep(2)
    elif d == "10": 
      fsDir = input(green+"Enter directory name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -ls /{4}".format(userPass,userName,remoteIp,fsDir))
      input("\033[36mPress Enter to continue...")
    elif d == "11": 
      rhadoopDir = input(green+"Enter the hadoop directroy to be deleted : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rmr {3} ".format(userPass,userName,remoteIp,rhadoopDir))
      print(f"{rhadoopDir} is removed...")
      t.sleep(2)
    elif d == "12": 
      loadFile = input(green+"Enter file name which you want to load : "+yellow)
      loadDir = input(green+"Enter directory name where you want to load :"+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -put {3} {4}".format(userPass,userName,remoteIp,loadFile,loadDir))
      print(f"{loadFile} is uploaded...")
      t.sleep(2)
    elif d == "13": 
      remFile = input(green+"Enter file name with full path name : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rm {4}".format(userPass,userName,remoteIp,remFile))
      print(f"{remFile} is removed...")
      t.sleep(2)
    elif d == "14":  
      readFile = input(green+"Enter file name with location : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -cat {4} ".format(userPass,userName,remoteIp,readFile))
      input("\033[36mPress Enter to continue...")
    elif d == "15":
      print(green+"Enter block size in bytes which you want to give :"+yellow, end = "") 
      blockSize = int(input())
      blockFile = input(green+"Enter file name which you want to upload :"+yellow)
      blockDir = input(green+"Enter the directory name in which you want to upload : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -Ddfs.block.size={3} -put {4} {5} ".format(userPass,userName,remoteIp,blockSize,blockFile,blockDir))                
      print(f"{blockFile} is uploaded...")
      t.sleep(2)
    elif d == "16": 
      help = input(green+"Enter hadoop command : "+yellow)
      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -help {3}".format(userPass,userName,remoteIp,help))
      input("\033[36mPress Enter to continue...")
    elif d == "17": 
      print(yellow+"for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
      dataFileName = input("enter file name : ")
      os.system("sshpass -p '{0}' ssh {1}@{2} vim {3}".format(userPass,userName,remoteIp,dataFileName))
    elif d == "18":
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
      input("\033[36mPress Enter to continue...")
    elif d == "19":
      os.system("sshpass -p '{0}' ssh {1}@{2} cat /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
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
            
