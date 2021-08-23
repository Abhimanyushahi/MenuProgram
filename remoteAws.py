import os
import subprocess
import time as t
yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"

def raws(userPass,userName,remoteIp):
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
