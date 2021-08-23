yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"
def hadoopClient():
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
              
