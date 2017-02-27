## Common functions file
import os,subprocess,shlex,datetime,time

current_working_dir=os.getcwd()
timenow=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

def error_msg(err):
        if err != 0:
                print "\033[1;31m------------------------------------------"
                print "Something went wrong, please check and FIX"
                print "1. Internet Connection"
                print "2. YUM settings / output"
                print "------------------------------------------\033[1;m \n"
                exit(0)
def qa(question):
        ans_status=True
        while True:
                answer=raw_input(question).upper()
                if answer == "Y":
                        ans_status=False
                        return answer
                elif answer == "N":
                        ans_status=False
                        print "Exiting......\n"
			exit(0)

def subprocess_cmd(command):
        process=subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
        proc_stdout=process.communicate()[0].strip()
        print proc_stdout
#	error_msg(process)

def checkNET():
        print "Probing for Internet Connection, please wait"
        subprocess_cmd('wget -q --spider -T 3 google.com')
def userInput(question):
	ans_status=True
	while True:
		answer=str(raw_input(question)).upper()
		if answer != "":
			ans_status=False
			return answer
			
				
		
