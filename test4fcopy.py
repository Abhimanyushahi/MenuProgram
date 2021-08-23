import os
import getpass
import socket
import subprocess
import time as t
import aws as a

while True:
  os.system("clear")
  print('''\007
\033[1;33m
    __  __________   ____  __ \033[01;34m     ____            \033[1;33m  ______                        
   /  |/  / ____/ | / / / / / \033[01;34m    / __ \_________  \033[1;33m / ____/________ _____ ___      
  / /|_/ / __/ /  |/ / / / /  \033[01;34m   / /_/ / ___/ __ \ \033[1;33m/ / __/ ___/ __ `/ __ `__ \     
 / /  / / /___/ /|  / /_/ /   \033[01;34m  / ____/ /  / /_/ / \033[1;33m /_/ / /  / /_/ / / / / / /     
/_/  /_/_____/_/ |_/\____/    \033[01;34m /_/   /_/   \____/  \033[1;33m\____/_/   \__,_/_/ /_/ /_/      
                                                                         \033[1;34mv2.0

\t\t\t\033[1;36m .........................................\033[1;m
\t\t\t\033[1;36m|\033[1;33m     Hey welcome to my menu program\033[1;36m      |
\t\t\t\033[1;36m .........................................\033[00m''')
  print('''\n\n\n\t\t\t\033[01;32m1. ---> Local
\t\t\t2. ---> Remote
\t\t\tq. ---> Quit\033[00m''')
  print("\n\033[1;33m\t\t\twhere you would like to perform your job (local/remote) \033[00m")
  print("\t\t\t\033[1;36m......................................................\n")
  
  location = input("\033[1;36m \t\t\tMenu \033[1;35m>>\033[01;32m ").lower()
  yellow = "\033[1;33m" # for numbering
  green = "\033[1;32m" # statements
  cyan = "\033[1;36m"
  red =  "\033[1;31m" # for enter choicelocal
  end = "\033[00m"

  if location == "1":
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
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c ConFigure MENU")
          os.system("tput setaf 7")
          print("\n{0}[1]{1} Configure yum\n{0}[2]{1} Configure docker\n{0}[b]{1} Go back to main menu\n{0}[q]{1} Exit the program{2}\n".format(yellow,green,end))
          d = input("\033[1;36mEnter your choice :\033[1;33m ")
          
          if d == "1": 
            os.system("touch /etc/yum.repos.d/menuyum.repo")
            os.system(" cat yum.repo >> /etc/yum.repos.d/menuyum.repo")
            os.system("systemctl enable docker")
            print(f'''
\033[1;33m  [ + ] \033[1;32myum is configured sucessfully !!''')
            t.sleep(2)
          elif d == "2": 
            os.system("touch /etc/yum.repos.d/menudocker.repo")
            os.system("cat docker.repo >> /etc/yum.repos.d/menudocker.repo")
            print(f'''
\033[1;33m  [ + ] \033[1;32mDocker is configured sucessfully !!''')
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
            
      elif ch == "2":
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
      elif ch == "3":
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c hadoop MENU")
          os.system("tput setaf 7")
          print('''\n{0}[1]{1} Go to namenode terminal\n{0}[2]{1} Go to datanode terminal\n{0}[3]{1} Go to hadoop client terminal\n{0}[b]{1} Go back to main menu\n{0}[q]{1} Exit the program{2}\n'''.format(yellow,green,end))
          hd = input("\033[1;36mEnter your choice : \033[1;33m")
          if hd == "1":
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
            
          elif hd == "2":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c Datanode MENU")
              os.system("tput setaf 7")
              print("""\n{0}[1]{1} install hadoop               {0}[2]{1} Datanode setup file\n{0}[3]{1} start                        {0}[4]{1} Stop\n{0}[5]{1} report of hdfs               {0}[6]{1} remove local directory\n{0}[7]{1} see current directry locally {0}[8]{1} download hdfs file\n{0}[9]{1} show all files of hdfs       {0}[10]{1} delete hdfs directory\n{0}[11]{1} upload files on hdfs        {0}[12]{1} delete file from hdfs\n{0}[13]{1} read file                   {0}[14]{1} Fix block size on loading\n{0}[15]{1} help                        {0}[16]{1} create a file\n{0}[17]{1} read core-site.xml file     {0}[18]{1} read hdfs-site.xml file\n{0}[b]{1} Go back                      {0}[q]{1} exit the program{2} \n""".format(yellow,green,end))
              d = input("\033[1;36mPlease Enter your choice : \033[1;33m")
              if d == "1": 
                ldjdkFile = input("\033[1;36mEnter path name of jdk software whereit present in your local system : \033[1;33m")
                ldjdk = subprocess.getstatusoutput("ls {0} | grep jdk".format(ldjdkFile)) 
                os.system("rpm -ivh {0} ".format(ldjdk[1]))
                javaVersion = input("\033[1;36mDo you want to check jdk is successfully installed or not (y/n) :\033[1;33m")
                if javaVersion == "y":
                  os.system("java -version")
                  t.sleep(2)
                ldhadoopFile = input("\033[1;36mEnter full path name of hadoop software where it is present in your system : \033[1;33m")
                ldhadoop = subprocess.getstatusoutput("ls {0} | grep hadoop".format(ldhadoopFile)) 
                os.system("rpm -ivh {0} --force".format(ldhadoop[1]))
                print("\033[1;36mAre you want to check hadoop is  successfully installed or not (y/n) : \033[1;33m")
                ans = input()
                if ans == "y":
                  os.system("hadoop version")
                  t.sleep(2)
              elif d == "2": 
                nameIp = input("\033[1;36mEnter ip address of namenode :\033[1;33m ")
                namePort = input("\033[1;36mEnter port number on which namenode binding hdfs : \033[1;33m")
                dataDir = input("\033[1;36mEnter directory name for creating directory to be shared datanode :\033[1;33m ")
                os.system("mkdir /{0}".format(dataDir))
                os.system("cat cored1.txt >> /etc/hadoop/core-site.xml")
                os.system("echo '<value>hdfs://{0}:{1}</value> ' >> /etc/hadoop/core-site.xml".format(nameIp,namePort))
                os.system("cat coren2.txt >> /etc/hadoop/core-site.xml")
                  
              ####datanode core-site.xml###########################
                os.system("cat hdfsd1.txt >> /etc/hadoop/hdfs-site.xml")
                
                os.system("echo '<value>/{0}</value>' >> /etc/hadoop/hdfs-site.xml".format(dataDir))
                os.system("cat coren2.txt >> /etc/hadoop/hdfs-site.xml")
                print(f'''\033[1;33m  [ + ] \033[1;32mDatanode is configured sucessfully !!''')
                t.sleep(2)
              
                ########datanode hdfs-site.xml##########################
              elif d == "3": 
                os.system("hadoop-daemon.sh start datanode")
                jpsDataCheck = input("\033[1;36mDo you want to see datanode start or not (y/n) :\033[1;33m ")
                if jpsDataCheck == "y":
                  os.system("jps")
                t.sleep(2)
              elif d == "4": 
                os.system("hadoop-daemon.sh stop datanode")
                print("\033[1;32mDatanode is stopped !!")
              elif d == "5": 
                os.system("hadoop dfsadmin -report")
                print(f'''\033[1;33m  [ + ] \033[1;32mPress enter to continue... !!'''+end)
              elif d == "6": 
                localDataDir = input("\033[1;36mEnter the Directory name :\033[1;33m")
                os.system("rm -rvf {0} ".format(locaDataDir))
                t.sleep(2)
              elif d == "7": 
                os.system("pwd")
                t.sleep(2)
              elif d == "8": 
                hadoopFile = input("\033[1;36mEnter hadoop file file name : \033[1;33m")
                savedLocalDir = input("Enter the name of local directory where you want to save it : \033[1;33m")
                os.system("hadoop fs -get {0} {1}".format(hadoopFile,saveLocalDir))
                t.sleep(2)
              elif d == "9": 
                fsDir = input("\033[1;36mEnter directory name :\033[1;33m")
                os.system("hadoop fs -ls /{0}".format(fsDir))
                input("\033[1;36mPress Enter to continue... !!")
              elif d == "10": 
                hadoopDir = input("\033[1;36mEnter the hadoop directroy to be deleted :\033[1;33m")
                os.system("hadoop fs -rmr {0} ".format(hadoopDir))
                print(f'''\033[1;36m {hadoopDir} is removed !!'''+end)
                t.sleep(2)
              elif d == "11": 
                loadFile = input("\033[1;36mEnter file name which you want to load:\033[1;33m ")
                loadDir = input("\033[1;36mEnter directory name where you want to load :\033[1;33m")
                os.system("hadoop fs -put {0} {1}".format(loadFile,loadDir))
                print(f'''\033[1;36m {loadFile} is uploaded!!'''+end)
                t.sleep(2)
              elif d == "12": 
                remFile = input("\033[1;36mEnter file name with full path name :\033[1;33m ")
                os.system("hadoop fs -rm {0}".format(remFile))
                print(f'''\033[1;36m {remFile} is removed !!'''+end)
                t.sleep(2)
              elif d == "13":  
                readFile = input("Enter file name with location : ")
                os.system("hadoop fs -cat {0} ".format(readFile))
                input("\033[36mPress Enter to continue...")
              elif d == "14" : 
                blockSize = int(input("\033[1;36mEnter block size in bytes which you want to give :\033[1;33m"))
                blockFile = input("\033[1;36mEnter file name which you want to upload :\033[1;33m")
                blockDir = input("\033[1;36mEnter the directory name in which you want to upload :\033[1;33m ")
                os.system("hadoop fs -Ddfs.block.size={0} -put {1} {2} ".format(blockSize,blockFile,blockDir))
                t.sleep(1)
              #os.system("hadoop fs -touchz /filename")
              elif d == "15": 
                help = input("\033[1;36mEnter hadoop command :\033[1;33m ")
                os.system("hadoop fs -help {0}".format(help))
                input("\033[36mPress Enter to continue...")
              elif d == "16": 
                print("\033[1;33mFor writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q\033[00m")
                dataFileName = input("\033[1;36mEnter file name : \033[1;33m")
                os.system("vim {0}".format(dataFileName))
              elif d == "17":
                os.system("cat /etc/hadoop/core-site.xml")
                input(cyan+"Press Enter to continue..."+end)
              elif d == "18":
                os.system("cat /etc/hadoop/hdfs-site.xml")
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
          elif hd == "3":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c hadoop Client")
              os.system("tput setaf 7")
              print("""{0}[1]{1} install hadoop                 {0}[2]{1} hadoop client setup file\n{0}[3]{1} Block size fix set up in file  {0}[4]{1} replication factor set up\n{0}[5]{1} make a local direcory          {0}[6]{1} report of hdfs\n{0}[7]{1} remove local directory         {0}[8]{1}see current directry localy\n{0}[9]{1} download hdfs file             {0}[10]{1} show all files of hdfs\n{0}[11]{1} delete hdfs directory         {0}[12]{1} upload files on hdfs \n{0}[13]{1} delete file from hdfs         {0}[14]{1} read file \n{0}[15]{1} Fix block size on loading     {0}[16]{1} help \n{0}[17]{1} create a file                 {0}[18]{1} Read core-site.xml file\n{0}[19]{1} Read hdfs-site.xml file       {0}[b]{1} Go back \n{0}[q]{1} exit the program{2}\n""".format(yellow,green,end))
              d = input("\033[1;36mEnter ip address of namenode : \033[1;33m")
              if d == "1": 
                ldjdkFile = input("\033[1;36mEnter path name of jdk software whereit present in your local system : \033[1;33m")
                ldjdk = subprocess.getstatusoutput("ls {0} | grep jdk".format(ldjdkFile)) 
                os.system("rpm -ivh {0} ".format(ldjdk[1]))
                javaVersion = input("\033[1;36mdo you want to check jdk is successfully installed or not (y/n) :\033[1;33m")
                if javaVersion == "y":
                  os.system("java -version")
                t.sleep(2)
                ldhadoopFile = input("\033[1;36mEnter full path name of hadoop software where it is present in your system :\033[1;33m ")
                ldhadoop = subprocess.getstatusoutput("ls {0} | grep hadoop".format(ldhadoopFile)) 
                os.system("rpm -ivh {0} --force".format(ldhadoop[1]))
                print("\033[1;36mAre you want to check hadoop is  successfully installed or not (y/n) :\033[1;33m ")
                ans = input()
                if ans == "y":
                  os.system("hadoop version")
                t.sleep(2)
              elif d == "2": 
                nameIp = input("\033[1;36mEnter ip address of namenode :\033[1;33m ")
                namePort = input("\033[1;36mEnter port number on which namenode binding hdfs :\033[1;33m ")
                dataDir = input("\033[1;36mEnter directory name for creating directory to be shared datanode :\033[1;33m ")
                os.system("mkdir /{0}".format(dataDir))
                os.system("cat cored1.txt >> /etc/hadoop/core-site.xml")
                
                os.system("echo '<value>hdfs://{0}:{1}</value> ' >> /etc/hadoop/core-site.xml".format(nameIp,namePort))
                os.system("cat coren2.txt >> /etc/hadoop/core-site.xml")
                print(f'''\033[1;33m  [ + ] \033[1;32mHadoop client is configured sucessfully !!''')
                #input("\033[1;33m  [ + ] \033[1;32mEnter to continue...")
                t.sleep(2)
              elif d == "3": 
                lcblockSize = int(input("\033[1;36mEnter block size to be fixed on client : \033[1;33m"))
                os.system("echo '<property>'>> /etc/hadoop/hdfs-site.xml")
                os.system("echo '<name>dfs.block.size</name>'>> /etc/hadoop/hdfs-site.xml")
                os.system("echo '<value>{0}</value>'>> /etc/hadoop/hdfs-site.xml".format(lcblockSize))
                os.system("echo '</property>'>> /etc/hadoop/hdfs-site.xml")
                print(f'''\033[1;33m  [ + ] \033[1;32mBlock size is configured sucessfully !!''')
                #input("\033[1;33m  [ + ] \033[1;32mEnter to continue...")
                t.sleep(2)
              elif d == "4": 
                lcreplication = int(input("\033[1;36mEnter replication factor : \033[1;33m"))  
                os.system("echo '<property>'>> /etc/hadoop/hdfs-site.xml")
                os.system("echo '<name>dfs.replication</name>'>> /etc/hadoop/hdfs-site.xml")
                os.system("echo '<value>2</value>'>> /etc/hadoop/hdfs-site.xml".format(lcreplication))
                os.system("echo '</property>'>> /etc/hadoop/hdfs-site.xml")
                print(f'''\033[1;33m  [ + ] \033[1;32mReplication factor is configured sucessfully !!''')
                #input("\033[1;33m  [ + ] \033[1;32mEnter to continue...")
                t.sleep(2)
                    ####hadoop client core-site.xml###########################
              elif d == "5": 
                cDir = input("\033[1;36mEnter directory name : \033[1;33m")
                os.system("mkdir {0}".format(cDir))
                print(f"\033[36m{cDir} is removed...")
                t.sleep(2)
              elif d == "6": 
                os.system("hadoop dfsadmin -report")
                input("\033[36mPress Enter to continue...")
              elif d == "7": 
                localDataDir = input("\033[1;36mEnter the Directory name :\033[1;33m")
                os.system("rm -rvf {0} ".format(locaDataDir))
                print(f"\033[36m{localDataDir} is removed...")
                t.sleep(2)
              elif d == "8": 
                os.system("pwd")
                t.sleep(2)
              elif d == "9": 
                hadoopFile = input("\033[1;36mEnter hadoop file file name :\033[1;33m ")
                savedLocalDir = input("\033[1;36mEnter the name of local directory where you want to save it :\033[1;33m ")
                os.system("hadoop fs -get {0} {1}".format(hadoopFile,saveLocalDir))
                print(f"{hadoopFile} is downloaded...")
                t.sleep(2)
              elif d == "10": 
                fsDir = input("\033[1;36mEnter directory name :\033[1;33m")
                os.system("hadoop fs -ls /{0}".format(fsDir))
                input("\033[36mPress Enter to continue...")
              elif d == "11": 
                hadoopDir = input("\033[1;36mEnter the hadoop directroy to be deleted :\033[1;33m")
                os.system("hadoop fs -rmr {0} ".format(hadoopDir))
                print(f"{hadoopDir} is removed...")
                t.sleep(2)
              elif d == "12": 
                loadFile = input("\033[1;36mEnter file name which you want to load :\033[1;33m ")
                loadDir = input("\033[1;36mEnter directory name where you want to load : \033[1;33m")
                os.system("hadoop fs -put {0} {1}".format(loadFile,loadDir))
                print(f"{loadFile} is uploaded...")
                t.sleep(2)
              elif d == "13": 
                remFile = input("\033[1;36mEnter file name with full path name : \033[1;33m ")
                os.system("hadoop fs -rm {0}".format(remFile))
                print(f"{remFile} is removed...")
                t.sleep(2)
              elif d == "14":  
                readFile = input("\033[1;36mEnter file name with location : \033[1;33m ")
                os.system("hadoop fs -cat {0} ".format(readFile))
                input("\033[36mPress Enter to continue...")
              elif d == "15": 
                blockSize = int(input("\033[1;36mEnter block size in bytes which you want to give : \033[1;33m"))
                blockFile = input("\033[1;36mEnter file name which you want to upload : \033[1;33m")
                blockDir = input("\033[1;36mEnter the directory name in which you want to upload :\033[1;33m ")
                os.system("hadoop fs -Ddfs.block.size={0} -put {1} {2} ".format(blockSize,blockFile,blockDir))
                print(f"{blockFile} is uploaded...")
                t.sleep(2)
                #os.system("hadoop fs -touchz /filename")
              elif d == "16": 
                help = input("\033[1;36mEnter hadoop command : \033[1;33m ")
                os.system("hadoop fs -help {0}".format(help))
                input("\033[36mPress Enter to continue...")
              elif d == "17": 
                print("\033[1;33mFor writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q\033[00m")
                dataFileName = input("\033[1;36mEnter file name : \033[1;33m")
                os.system("vim {0}".format(dataFileName))
              elif d == "18":
                os.system("cat /etc/hadoop/core-site.xml")
                input("\033[36mPress Enter to continue...")
              elif d == "19":
                os.system("cat /etc/hadoop/hdfs-site.xml")
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
          elif hd == "b":
            break
          elif hd == "q":
            print("\033[00m")
            print ("\033[1;33mGood bye!\033[00m") 
            t.sleep(1)
            exit()
          else:
            print (f'''
\033[1;33m  [ + ] \033[1;31m This option doesn't support.
\033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
            input("\033[1;33m  [033[1;36m + ] \033[1;34mPress Enter to try again...\033[00m")
          os.system("clear")       
      elif ch == "4":
        while True:
          os.system("clear")
          os.system("tput setaf 4")
          os.system("figlet -f slant -c Webserver MENU")
          os.system("tput setaf 7")
          print("""\n{0}[1]{1} install apache webserver\n{0}[2]{1} start webserver\n{0}[3]{1} check status\n{0}[4]{1} stop webserver\n{0}[5]{1} show current directory \n{0}[6]{1} create or open a file\n{0}[7]{1} copy a file on webserver\n{0}[b]{1} Go back \n{0}[q]{1} exit the program{2}\n""".format(yellow,green,end))
          d = input("\033[1;36mEnter your choice :\033[1;33m ")
          if d == "1":
            print("\033[00m") 
            os.system("yum install httpd")
          elif d == "2":
            os.system("systemctl start httpd")
            print(green+"webserver is started..."+end)
            t.sleep(1)
          elif d == "3": 
            print("\033[1;33mPress q to come out from it\033[00m")
            os.system("systemctl status httpd")
          elif d == "4": 
            os.system("systemctl stop httpd")
            print(green+"webserver is stopped..."+end)
            t.sleep(1)
          elif d == "5": 
            print("\033[00m") 
            os.system("pwd")
            os.system("ls")
            input(green+"Press Enter to continue..."+end)
          elif d == "6": 
            print("\033[1;33mFor writting anything in file press i, and for saving press esc key and :wq, and only close file press esc key and :q\033[00m")
            webFileName = input("\033[1;36mEnter file name :\033[1;33m ")
            os.system("vim {0}".format(webFileName))
            print(green+f"{webFileName} is created..."+end)
            t.sleep(1)
          elif d == "7": 
            file = input("\033[1;36mEnter file name :\033[1;33m")
            os.system("cp {0} /var/www/html".format(file))
            print(green+f"{file} is coppied to webserver..."+end)
            t.sleep(1)
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
      elif ch == "5":
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c User MENU")
          os.system("tput setaf 7")
          print("""\n{0}[1]{1} create user \n{0}[2]{1} create password for a user \n{0}[b]{1} Go back \n{0}[q]{1} exit the program
          \n""".format(yellow,green,end))
          d = input("\033[1;36mEnter your choice : \033[1;33m")
          if d == "1":
            print("\033[1;36mEnter user name :\033[1;33m" , end='')
            createUser = input()
            os.system("useradd {}".format(createUser))
            t.sleep(2)
          elif d == "2":
            os.system("passwd {0} ".format(creatUser))
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
            
      elif ch == "6":
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c Partition MENU") 
          os.system("tput setaf 7")
          print("\n{0}[1]{1} go to lvm menu\n{0}[2]{1} Create partition\n{0}[b]{1} go back\n{0}[q]{1} exit the program{2}\n".format(yellow,green,end))
          p = input("\033[1;36mEnter your choice : \033[1;33m")
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
{0}[b]{1} go back 
{0}[q]{1} Exit the program{2}\n""".format(yellow,green,end))

              i = input("\033[1;36mEnter your Choice : \033[1;33m")
              if i == "1":
                os.system("fdisk -l")
                input("\033[36mPress Enter to continue...")
              elif i == "2":
                pv1=input("\033[1;36mEnter the name of storage 1:\033[1;33m")
                pv2=input("\033[1;36mEnter the name of storage 2:\033[1;33m")
                os.system("pvcreate {}".format(pv1))
                t.sleep(2)
                os.system("pvcreate {}".format(pv2))
                t.sleep(2)
              elif i == "3":
                pv=input("\033[1;36mEnter the name of storage:\033[1;33m")
                os.system("pvdisplay {}".format(pv))
                input("\033[36mPress Enter to continue...")
              elif i == "4":
                vg=input("\033[1;36mGive name to the Volume Group :\033[1;33m")
                pvn1=input("\033[1;36mEnter the name of storage 1 :\033[1;33m")
                pvn2=input("\033[1;36mEnter the name of Storage 2 :\033[1;33m")
                os.system("vgcreate {} {} {}".format(vg,pvn1,pvn2))
                t.sleep(2)
              elif i == "5":
                vg1=input("\033[1;36mEnter the name of Volume Group :\033[1;33m")
                os.sytem("vgdisplay {}".format(vg1))
                input("\033[36mPress Enter to continue...")
                t.sleep(2)
              elif i == "6":
                size=input("\033[1;36mEnter size for your Logical Volume :\033[1;33m")
                lv=input("\033[1;36mGive name to your Logical Volume :\033[1;33m")
                vg2=input("\033[1;36mEnter name of the Volume Group :\033[1;33m")
                os.system("lvcreate --size{} --name{} {}".format(size,lv,vg2))
                t.sleep(2)
              elif i == "7":
                os.system("lvdisplay")
                input("\033[36mPress Enter to continue...")
              elif i == "8":
                vg4=input("Enter the name of Volume Group:")
                lv2=input("Enter the name of Logical Volume:")
                os.system("mkfs.ext4  /dev{}{}".format(vg4,lv2))
                t.sleep(2)
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
              print("""\n{0}[1]{1} create a directory \n{0}[2]{1}{0}[3]{1} format partition \n{0}[4]{1} mount partion \n{0}[5]{1} permamnent mount \n{0}[6]{1} show hardisk \n{0}[7]{1} show partition \n{0}[b]{1} go back \n{0}[q]{1} exit the program{2} \n""".format(yellow,green,end))
              d = input("\033[1;36mEnter your choice :\033[1;33m ")
              if d == "1": 
                partDir = input("\033[1;36mEnter the direcory name which you want to create :\033[1;33m")
                os.system("mkdir {0}".format(partDir))
                print(f"{partDir} is created...")
                t.sleep(2)
              elif d == "2": 
                partitionName = input("\033[1;36mEnter hardisk name : \033[1;33m")
                os.system("fdisk {0} ".format(partitionName))
                t.sleep(2) 
                os.system("udevadm sttle") 
              elif d == "3": 
                partName = input("\033[1;36mEnter the partion name :\033[1;33m ")
                os.system("mkfs.ext4 {0}".format(partName))
                t.sleep(2)
              elif d == "4": 
                os.system("echo 'mount {0} {1}' >> /etc/rc.d/rc.local".format(partName,partDir))
                print("Permanent mount is configureed successfully!!")
                t.sleep(2)
              elif d == "5": 
                os.system("mount {0} {1}".format(partName,partDir))
                print(f"{partName} is mounted...")
                t.sleep(2)
              elif d == "6": 
                os.system("fdisk -l")
                input("\033[36mPress Enter to continue...")
              elif d == "7": 
                os.system("lsblk")
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
      elif ch == "7":
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c Linux MENU")
          os.system("tput setaf 7")
          print("""\n{0}[1]{1} run linux command\n{0}[b]{1} go back\n{0}[q]{1} exit the program
            {2}\n""".format(yellow,green,end))
          ch = input("\033[1;36mEnter your choice :\033[1;33m ")
          if ch == "1":
            linuxCommand = input("\033[1;36mEnter the command :\033[1;33m ")
            print("\033[00m")
            os.system("{0}".format(linuxCommand))
            input(green+"Press Enter to continue.."+end)
          elif ch == "b": 
            break
          elif ch == "q":
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
      elif ch == "8":
        os.system("clear")
        os.system(a.menu())
      elif ch == "m":
        break    
      elif ch == "q" or ch == "Q":
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
          
  elif location == "2":
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
            login = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} date".format(userPass,userName,remoteIp))
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
    while True:
      os.system("clear")
      os.system("tput setaf 4")
      os.system("figlet -f slant -c RMENU ProGram")
      os.system("tput setaf 7")
      print (f"""\n
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
      \033[00m\n""")
      print("\033[1;36mEnter your choice : \033[1;33m" , end="")
      ch = input()
      if ch == "1":
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c ConFigure MENU")
          os.system("tput setaf 7")
          print("\n{0}[1]{1} Configure yum\n{0}[2]{1} Configure docker\n{0}[b]{1} Go back \n{0}[q]{1} Exit the program{2}\n".format(yellow,green,end))
          d = input("\033[1;36mEnter your choice :\033[1;33m ")
          if d == "1": 
            os.system("sshpass -p '{0}' ssh {1}@{2} touch /etc/yum.repos.d/menuyum.repo".format(userPass,userName,remoteIp))
            os.system("sshpass -p '{0}' ssh /cat yum.repo >> /etc/yum.repos.d/menuyum.repo".format(userPass,userName,remoteIp))
            os.system("sshpass -p '{0}' ssh {1}@{2} systemctl enable docker".format(userPass,userName,remoteIp))
            print(green+"yum is configured sucessfully.")
            t.sleep(2)
          elif d == "2": 
            os.system("sshpass -p '{0}' ssh {1}@{2} touch /etc/yum.repos.d/menudocker.repo".format(userPass,userName,remoteIp))
            os.system("shpass -p '{0}' ssh {1}@{2} cat /docker.repo >> /etc/yum.repos.d/menudocker.repo".format(userPass,userName,remoteIp)) 
            print(green+"Docker is configured sucessfully.")
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
      elif ch == "2":
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
      elif ch == "3":
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c hadoop MENU")
          os.system("tput setaf 7")
          print("""\n{0}[1]{1} Go to namenode terminal\n{0}[2]{1} Go to datanode terminal\n{0}[3]{1} go to hadoop client terminal\n{0}[4]{1} send requirement files for hadoop file configuration for onetime setup\n{0}[b]{1} Go back \n{0}[q]{1} exit the program
          \n""".format(yellow,green,end))
          hd = input("\033[1;36mEnter your choice : \033[1;33m")
          if hd == "1":
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
          elif hd == "2":
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
          elif hd == "3":
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
          elif hd == "4":
            os.system("sshpass -p '{0}' scp  coren1.txt coren2.txt cored1.txt hdfsn1.txt hdfsd1.txt {1}@{2}:/ ".format(userPass,userName,remoteIp))
          elif hd == "b":
            break
          elif hd == "q":
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
      elif ch == "4":
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c Webserver MENU")
          os.system("tput setaf 7")
          
          print("""\n{0}[1]{1} install webserver\n{0}[2]{1} Check status\n{0}[3]{1} stop webserver\n{0}[4]{1} show current directory \n{0}[5]{1} create or open a file\n{0}[6]{1}{1} copy a file on webserver\n{0}[7]{1} Start the webserver \n{0}[b]{1} Go back\n{0}[q]{1} exit the program\n""".format(yellow,green))
          d = input("\033[1;36mPlease Enter your choice : \033[1;33m")
          if d == "1": 
            os.system("sshpass -p '{0}' ssh {1}@{2} yum install httpd".format(userPass,userName,remoteIp))
          elif d == "2":
            print(yellow+"Press q to come out from it")
            os.system("sshpass -p '{0}' ssh {1}@{2} systemctl status httpd".format(userPass,userName,remoteIp))
            input("\033[36mPress Enter to continue..."+end)
          elif d == "3": 
            os.system("sshpass -p '{0}' ssh {1}@{2} systemctl stop httpd".format(userPass,userName,remoteIp))
            print("webserver is stopped...")
            t.sleep(2)
          elif d == "4": 
            os.system("sshpass -p '{0}' ssh {1}@{2} pwd".format(userPass,userName,remoteIp))
            os.system("sshpass -p '{0}' ssh {1}@{2} ls".format(userPass,userName,remoteIp))
            input("[36mPress Enter to continue..."+end)
          elif d == "5":
            print(yellow+"for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
            webFileName = input(green+"Enter file name : "+yellow)
            os.system("sshpass -p '{0}' ssh {1}@{2} vim {0}".format(userPass,userName,remoteIp,webFileName))
          elif d == "6": 
            file = input(green+"Enter file name : "+yellow)
            os.system("sshpass -p '{0}' ssh {1}@{2} cp {0} /var/www/html".format(userPass,userName,remoteIp,webFileName))
            print(f"{webFile} is coppied to webserver...")
            t.sleep(2)
          elif d == "7":
            os.system("sshpass -p '{0}' ssh {1}@{2} systemctl start httpd".format(userPass,userName,remoteIp))
            print("webserver is started...")
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
        
            
      elif ch == "5":
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c User MENU")
          os.system("tput setaf 7")
          print("""\n{0}[1]{1} create user \n{0}[2]{1} create password for a user \n{0}[b]{1} Go back\n{0}[q]{1} exit the program
          \n""".format(yellow,green))
          d = input("\033[1;36mEnter your choice : \033[1;33m")
          if d == "1":
            print(green+"Enter username : "+yellow , end='')
            createUser = input()
            os.system("sshpass -p '{0}' ssh {1}@{2} useradd {3}".format(userPass,userName,remoteIp,createUser))
            t.sleep(2)
          elif d == "2":
            os.system("sshpass -p '{0}' ssh {1}@{2} passwd {3} ".format(userPass,userName,remoteIp,creatUser))
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
        
                         
      elif ch == "6":
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
            print ("\033[1;33mGood bye!\033[00m")
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
    
      elif ch == "7":
        while True:
          os.system("clear")
          os.system("tput setaf 6")
          os.system("figlet -f slant -c RLinux MENU")
          os.system("tput setaf 7")
          print("""\n{0}[1]{1} run linux command\n{0}[b]{1} go back \n{0}[q]{1} exit the program
          \n""".format(yellow,green))
          rcmd = input("\033[1;36mEnter your choice : \033[1;33m")
          if rcmd == "1":
            linuxCommand = input(green+"Enter the command : "+yellow)
            os.system("sshpass -p '{0}' ssh {1}@{2} {3}".format(userPass,userName,remoteIp,linuxCommand))
            input("\033[1;36mPress Enter to continue.."+end)
          elif rcmd == "b": 
            break
          elif rcmd == "q" or rcmd == "Q":
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
            
      elif ch == "8":
        
        global instance_name , count , sg_name , sg_description , key_name , ebs_name , ebs_size
          #new=input("Do you want to enter AWS Cloud (yes/no) ? ").lower()
        def remoteCheck():
          print(yellow+"Checking for AWS CLI tools")
          x = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} aws --version".format(userPass,userName,remoteIp))
          if x[0] != 0 :
            x =input(green+"AWS CLI is not installed! do you want to install (yes/no)? "+yellow).lower()
            if x == "yes":
              print("\033[00m")
              os.system("sshpass -p '{0}' ssh {1}@{2} curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip' ".format(userPass,userName,remoteIp))
              os.system("sshpass -p '{0}' ssh {1}@{2} unzip awscliv2.zip".format(userPass,userName,remoteIp))
              os.system("sshpass -p '{0}' ssh {1}@{2} sudo ./aws/install".format(userPass,userName,remoteIp))
              remoteCheck()
            else:
              print(red+"Sorry AWS can't run")
              os.system("exit()")
          else:
            print(green+"Configure AWS CLI ! "+end)
            os.system("sshpass -p '{0}' ssh {1}@{2} aws configure".format(userPass,userName,remoteIp))
        os.system("clear")
        os.system("tput setaf 4")
        os.system("figlet -f slant -c AWS Cloud") 
        os.system("tput setaf 7")
        new="yes" 
        if new == "yes":
          remoteCheck()
          while True:
            os.system("clear")
            os.system("tput setaf 4")
            os.system("figlet -f slant -c AWS Cloud") 
            os.system("tput setaf 7")
            print("""\n{0}[1]{1} To create key pair for EC2 instance\n{0}[2]{1} To create security Group for EC2 instance\n{0}[3]{1} To launch instance on AWS with Amazon Linux\n{0}[4]{1} To describe EC2 instances on AWS\n{0}[5]{1} To stop/terminate an EC2 instance\n{0}[6]{1} To create Volume to create EBS volume(limit 10GB)\n{0}[7]{1} To attach the EBS volume to EC2 instance\n{0}[8]{1} TO enter into S3 section\n{0}[b]{1} Go back\n{0}[q]{1} Exit the program {2}\n""".format(yellow,green,end))
            x = input("\n\033[1;36mEnter your choice :\033[1;33m ")
            if x == "1":
              key_name = input(green+"Enter Key Name: "+yellow)
              print("\033[00m")
              os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 create-key-pair --key-name {3}".format(userPass,userName,remoteIp,key_name))
              print(green+"Success security key created : {} ".format(key_name ))
              input(green+"press Enter to continue...")
            elif x == "2":
              sg_name=input(green+"Enter your security group name: "+yellow)
              sg_description=input("Enter your security group description: ")
              print("\033[00m")
              os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 create-security-group --group-name {3} --description {4} --vpc-id vpc-e11afa8a ".format(userPass,userName,remoteIp,sg_name,sg_description))
              print(green+"Success security group created: {0} , description: {1}".format(sg_name , sg_description))
              input(green+"press Enter to continue...")
            elif x == "3":
              instance_name=input(green+"Enter instance name :"+yellow)
              count=int(input(green+"Enter instance count : "+yellow))
              key_name = input(green+"Enter Key Name : "+yellow)
              sg_name=input(green+"Enter your security group name : "+yellow)
              print(cyan+"{0}".format(instance_name[0]))
              print("\033[00m")
              os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name {3} --security-groups {4} --count {5} ".format(userPass,userName,remoteIp,key_name,sg_name,count))
              instance_id=input(green+"Enter Instance id : "+yellow)
              print("\033[00m")
              os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 create-tags --resources {3} --tags  Key=Name,Value={4}".format(userPass,userName,remoteIp,instance_id,instance_name))
              t.sleep(2)
            elif x == "4":
              while True:
                print("{0}[1]{1} To describe all instance \n{0}[2]{1} To enter instance name\n{0}[b]{1} go back \n{0}[q}{1} exit the program{2} ".format(yello,green,end))
                desc = input("\033[1;36mEnter instance name : \033[1;33m")
                if disc == "1":
                  print("\033[00m")
                  os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 describe-instances".format(userPass,userName,remoteIp))
                  input("\033[1;36mpress Enter to continue...")
                elif disc == "2":
                  name=input("\033[1;36mEnter instance name : \033[1;33m")
                  print("\033[00m")
                  os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 describe-instances --filters Name=tag:Name,Values={}".format(userPass,userName,remoteIp,name))
                  input("\033[1;36mpress Enter to continue...")
                elif disc == "b":
                  break
                elif disc == "q":
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
                      
            elif x == "5":
              while True:
                print("\n{0}[1]{1} To stop an instance  \n{0}[2]{1} To terminate an instance \n{0}[b]{1} go back \n{0}[q]{1} exit the program{2}\n".format(yellow,green,end))
                inst = input("\033[1;36mEnter your choice : \033[1;33m ")
                if inst == "1":
                  Iid=input("\033[1;36mEnter the instance id of EC2 instance you want to stop : \033[1;33m")
                  print("\033[00m")
                  os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 stop-instances --instance-ids {2}".format(userPass,userName,remoteIp,Iid))
                  input("\033[1;36mpress Enter to continue...")
                elif inst == "2" :
                  Iid=input("\033[1;36mEnter the instance id of EC2 instance you want to terminate : \033[1;33m")
                  print("\033[00m")
                  os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 stop-terminates --instance-ids {}".format(userPass,userName,remoteIp,Iid))
                  input("\033[1;36mpress Enter to continue...")
                elif inst == "b":
                  break
                elif inst == "q":
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
              
            elif x == "6":
              ebs_name=input(green+"Enter your EBS name : "+yellow)
              ebs_size=int(input(green+"Enter your EBS size in GB : "+yellow))
              print("\033[00m")
              os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 create-volume --availability-zone ap-south-1a --size {3}".format(userPass,userName,remoteIp,ebs_size))
              ebs_id=input(green+"Enter EBS volume id : "+yellow)
              print("\033[00m")
              os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 create-tags --resources {3} --tags  Key=Name,Value={4}".format(userPass,userName,remoteIp,ebs_id,ebs_name))
              input(green+"press Enter to continue...")
            elif x == "7":
              Iid=input(green+"Enter the instance id of EC2 instance : "+yellow)
              volid=input(green+"Enter the EBS volume id : "+yellow)
              print("\033[00m")
              os.system("sshpass -p '{0}' ssh {1}@{2} aws ec2 attach-volume --volume-id {3} --instance-id {4} --device /dev/sdf".format(userPass,userName,remoteIp,volid,Iid))
              input(green+"Press Enter to continue..."+end)
            elif x == "8":
              while True:
                print("\n{0}[1]{1} To create S3 bucket\n{0}[2]{1} To delete S3 bucket\n{0}[3]{1} To list all S3 bucket.\n{0}[4]{1} To copy a file to S3 bucket \n{0}[b]{1} go back \n{0}[q]{1} Exit the program{2}\n".format(yellow,green,end))
                s3 = input(green+"Enter your choice : "+yellow)
                if s3 == "1":
                  bkName=input("\033[1;36mEnter unique bucket name : \033[1;33m ")
                  print("\033[00m")
                  os.system("sshpass -p '{0}' ssh {1}@{2} aws s3 mb s3://{}".format(userPass,userName,remoteIp,bkName))
                  input("\033[1;36mpress Enter to continue..."+end)
                elif s3 == "2":
                  bkName=input("\033[1;36mEnter unique bucket name : \033[1;33m ")
                  print("\033[00m")
                  os.system("sshpass -p '{0}' ssh {1}@{2} aws s3 rb --force s3://{}".format(userPass,userName,remoteIp,bkName))
                  input("\033[1;36mpress Enter to continue..."+end)
                elif s3 == "3":
                  print("\033[00m")
                  os.system("sshpass -p '{0}' ssh {1}@{2} aws s3 ls: ".format(userPass,userName,remoteIp))
                  input("\033[1;36mpress Enter to continue..."+end)
                elif s3 == "4":   
                  bkName=input("\033[1;36mEnter unique bucket name : \033[1;33m ")
                  fname=input("\033[1;36mEnter file name : "+yellow)
                  print("\033[00m")
                  os.system("sshpass -p '{0}' ssh {1}@{2} aws s3 cp {3} s3://{4}".format(userPass,userName,remoteIp,fname,bkName))
                  input("\033[1;36mpress Enter to continue..."+end)
                elif s3 == "b":
                  break
                elif s3 == "q":
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
            elif x == "b":
              break
            elif x == "q" or x == "Q":
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
   
      elif ch == "m":
        break             
      elif ch == "q" or ch == "Q":
        print("\033[00m")
        print ("\033[1;33mGood bye!\033[00m") 
        t.sleep(1)
        exit()
      else:
        print (f'''
\033[1;33m  [ + ] \033[1;31m This location doesn't support.
\033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
        input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
      os.system("clear")
  elif location == "q" or location == "Q":
    print("\033[00m")
    print ("\033[1;33mGood bye!\033[00m") 
    t.sleep(1)
    exit()  
  else:
    print (f'''
\033[1;33m  [ + ] \033[1;31m This location doesn't support.
\033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
    input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
  os.system("clear")

