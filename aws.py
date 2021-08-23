import os 
import subprocess
global instance_name , count , sg_name , sg_description , key_name , ebs_name , ebs_size
yellow = "\033[1;33m" # for numbering
green = "\033[1;32m" # statements
cyan = "\033[1;36m"
red =  "\033[1;31m" # for enter choicelocal
end = "\033[00m"
def check():
  print("\033[1;33mChecking for AWS CLI tools\033[00m")
  x = subprocess.getstatusoutput("aws --version")
  if x[0] != 0 :
    print("\033[1;33mPlease connect to internet before doing yes!")
    x =input("\033[1;36mAWS CLI is not installed! do you want to install (yes/no)? \033[1;33m").lower()
    #print("\033[1;36m")
    print("\033[00m")
    if x == "yes":
      os.system(" curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip' ")
      os.system("unzip awscliv2.zip")
      os.system("sudo ./aws/install")
      check()
    else:
      print("\033[1;33m  [ + ] \033[1;31m AWS can't run\033[00m")
      os.system("exit()")
  else:
    print("\033[1;33m[+] Configure AWS CLI ! \033[00m")
    os.system("aws configure")
def menu():
  os.system("clear")
  os.system("tput setaf 4")
  os.system("figlet -f slant -c AWS Cloud") 
  os.system("tput setaf 7")
  yellow = "\033[1;33m"
  green = "\033[1;32m"
  end = "\033[00m"
    #new=input("Do you want to enter AWS Cloud (yes/no) ? ").lower()
  new="yes"
  if new == "yes":
    check()
    while True:
      os.system("clear")
      os.system("tput setaf 4")
      os.system("figlet -f slant -c Aws Cloud")
      os.system("tput setaf 7")  
      print("""\n{0}[1]{1} To create key pair for EC2 instance.
{0}[2]{1} To create security Group for EC2 instance.
{0}[3]{1} To launch instance on AWS with Amazon Linux.
{0}[4]{1} To describe EC2 instances on AWS.
{0}[5]{1} To stop/terminate an EC2 instance.
{0}[6]{1} To create Volume to create EBS volume.(limit 10GB).
{0}[7]{1} To attach the EBS volume to EC2 instance.
{0}[8]{1} TO enter into S3 section.
{0}[b]{1} go back to main menu"
{0}[q]{1} exit the program {2}\n""".format(yellow,green,end))
      x = input("\n\033[1;36mEnter your choice : \033[1;33m ")
      if x == "1":
        key_name = input("\033[1;36mEnter Key Name: \033[1;33m")
        print("\033[00m")
        os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
        print("\033[1;33mSuccess security key created : {} ".format(key_name ))
        input("\033[1;36mpress Enter to continue...")
      elif x == "2":
        sg_name=input("\033[1;36mEnter your security group name : \033[1;33m ")
        sg_description=input("\033[1;36mEnter your security group description : \033[1;33m")
        print("\033[00m")
        os.system("aws ec2 create-security-group --group-name {} --description {} --vpc-id vpc-e11afa8a ".format(sg_name,sg_description))
        print("\033[1;33mSuccess security group created: {} , description: {}".format(sg_name , sg_description))
        input("\033[1;36mpress Enter to continue...")
      elif x == "3":
                #name = 0
                #score = input("Enter your Instance Name")
                #instance_name = {}
                #instance_name[name] = score
        instance_name=input("\033[1;36mEnter instance name : \033[1;33m")
        count=int(input("\033[1;36mEnter instance count : \033[1;33m "))
        key_name = input("\033[1;36mEnter Key Name : \033[1;33m ")
        sg_name=input("\033[1;36mEnter your security group name: ")

        print(yellow+instance_name[0]+end)
        print("\033[00m")
        os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name {0} --security-groups {1} --count {2} ".format(key_name,sg_name,count))
        instance_id=input("\033[1;36mEnter Instance id : \033[1;33m ")
        print("\033[00m")
        os.system("aws ec2 create-tags --resources {} --tags  Key=Name,Value={}".format(instance_id,instance_name))
                #os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name p --security-groups p --count 1 --tag-specifications ResourceType=instance,Tags=[{{Key=Name,Value={}}}]".format(instance_name[0]))
      elif x == "4":
        while True:
          print("{0}[1]{1} To describe all instance \n{0}[2]{1 }To enter instance name\n{0}[b]{1} go back \n{0}[q}{1} exit the program{2} \n".format(yello,green,end))
          desc = input("\033[1;36mEnter instance name: \033[1;33m")
          if disc == "1":
            print("\033[00m")
            os.system("aws ec2 describe-instances")
            input("\033[1;36mpress Enter to continue...")
          elif disc == "2":
            name=input("\033[1;36mEnter instance name: \033[1;33m")
            print("\033[00m")
            os.system("aws ec2 describe-instances --filters Name=tag:Name,Values={}".format(name))
            input("\033[1;36mpress Enter to continue...")
          elif disc == "b":
            break
          elif disc == "q":
            print("\033[00m")
            exit()
          else:
            print (f'''
\033[1;33m  [ + ] \033[1;31m This option doesn't support.
\033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
            input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
          os.system("clear")
        print ("\033[1;33mGood bye!\033[1;33m") 
      elif x == "5":
        while True:
          print("\n{0}[1]{1} To stop an instance  \n{0}[2]{1} To terminate an instance \n{0}[b]{1} go back \n{0}[q]{1} exit the program{2}\n".format(yellow,green,end))
          inst = input("\033[1;36mEnter your choice : \033[1;33m")
          if inst == "1":
            Iid=input("\033[1;36mEnter the instance id of EC2 instance you want to stop : \033[1;33m")
            print("\033[00m")
            os.system("aws ec2 stop-instances --instance-ids {}".format(Iid))
            input("\033[1;36mpress Enter to continue...")
          elif inst == "2" :
            Iid=input("\033[1;36mEnter the instance id of EC2 instance you want to terminate : \033[1;33m")
            print("\033[00m")
            os.system("aws ec2 stop-terminates --instance-ids {}".format(Iid))
            input("\033[1;36mpress Enter to continue...")
          elif inst == "b":
            break
          elif inst == "q":
            print("\033[00m")
            exit()
          else:
            print (f'''
\033[1;33m  [ + ] \033[1;31m This option doesn't support.
\033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
            input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
          os.system("clear")
        
      elif x == "6":
        ebs_name=input("\033[1;36mEnter your EBS name : \033[1;33m ")
        ebs_size=int(input("\033[1;36mEnter your EBS size in GB : \033[1;33m "))
        print("\033[00m")
        os.system("aws ec2 create-volume --availability-zone ap-south-1a --size {}".format(ebs_size))
        ebs_id=input("\033[1;36mEnter EBS volume id : \033[1;33m")
        print("\033[00m")
        os.system("aws ec2 create-tags --resources {} --tags  Key=Name,Value={}".format(ebs_id,ebs_name))
        input("\033[1;36mpress Enter to continue...\033[1;33m")
      elif x == "7":
        Iid=input("\033[1;36mEnter the instance id of EC2 instance : \033[1;33m ")
        volid=input("\033[1;36mEnter the EBS volume id :\033[1;33m ")
        print("\033[00m")
        os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volid,Iid))
        input("\033[1;36mpress Enter to continue...")
      elif x == "8":
        while True:
          print("\n{0}[1]{1} To create S3 bucket\n{0}[2]{1} To delete S3 bucket\n{0}[3]{1} To list all S3 bucket.\n{0}[4]{1} To copy a file to S3 bucket \n{0}[b]{1} go back \n{0}[q]{1} Exit the program{2}\n".format(yellow,green,end))
          s3 = input("Enter your choice : ")
          if s3 == "1":
            bkName=input("\033[1;36mEnter unique bucket name : \033[1;33m ")
            print("\033[00m")
            os.system("aws s3 mb s3://{}".format(bkName))
            input("\033[1;36mpress Enter to continue...")
          elif s3 == "2":
            bkName=input("\033[1;36mEnter unique bucket name : \033[1;33m ")
            print("\033[00m")
            os.system("aws s3 rb --force s3://{}".format(bkName))
            input("\033[1;36mpress Enter to continue...\033[00m")
          elif s3 == "3":
            os.system("aws s3 ls: ")
            input("\033[1;36mpress Enter to continue...\033[00m")
          elif s3 == "4":   
            bkName=input("\033[1;36mEnter unique bucket name : \033[1;33m ")
            fname=input("\033[1;36mEnter file name : \033[1;33m")
            print("\033[00m")
            os.system("aws s3 cp {} s3://{}",fname,bkName)
            input("\033[1;36mpress Enter to continue...\033[00m")
          elif s3 == "b":
            break
          elif s3 == "q":
            print("\033[00m")
            exit()
          else:
            print (f'''
\033[1;33m  [ + ] \033[1;31m This option doesn't support.
\033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
            input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
          os.system("clear")
        print ("\033[1;33mGood bye!\033[1;33m") 
      elif x == "b":
        return x
                #import menu.py
      elif x == "q" or x == "Q":
        print ("\033[1;33mGood bye!\033[1;33m")
        print("\033[00m")
        exit()
      
      else:
        print (f'''
\033[1;33m  [ + ] \033[1;31m This option doesn't support.
\033[1;33m  [ + ] \033[1;31m Don't Worry.\033[00m''')
        input("\033[1;33m  [ + ] \033[1;34mPress Enter to try again...\033[00m")
      os.system("clear")
    







                    

                    

                    

                   
