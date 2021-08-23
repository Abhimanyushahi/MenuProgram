yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"
import os
import time as t

def datanode():
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
