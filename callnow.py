### FREE
# Bulk call generator using asterisk
# Use Asterisk installer if not available
import argparse,subprocess,functions


parser = argparse.ArgumentParser(description="Generate automate calls using Asterisk")
group = parser.add_mutually_exclusive_group()
## Asterisk parameters OPTIONAL
group.add_argument("-ma",type=int,help="Max retries before giving up default is 0")
group.add_argument("-re",type=int,help="Seconds between retries, Default is 300 (5 min).")
group.add_argument("-wa",type=int,help="Seconds to wait for an answer. Default is 45")

## Asterisk parameters MANDATORY
parser.add_argument("-ch",help="Channel to use for the call. (i.e pjsip/101)",required=True)
parser.add_argument("-co",help="<context-name> Context in extensions.conf",required=True)
parser.add_argument("-ex",help="<ext> Extension definition in extensions.conf",required=True)
#parser.add_argument("-ex",type=int,help="<ext> Extension definition in extensions.conf",required=True)
parser.add_argument("-pr",type=int,help="Priority of extension to start with",required=True)

## Application parameters MANDATORY
parser.add_argument("-cps",type=int, help="Maximum calls per second, depends on OS file creation",required=True)
## Application parameters OPTIONAL
parser.add_argument("-ba",type=int,help="Number of batches")
parser.add_argument("-de",type=int,help="Delay between batches in seconds")


args = parser.parse_args()

def call_now():
	if args.de and args.ba > 1:
		de=0
		while args.ba > 0:
			functions.subprocess_cmd('touch -d "+%s sec" time_ref.file' % de)
			cps=args.cps
			print "%s st run delay is %s" % (cps,de)
			print "Batch number %s" % args.ba
			while cps > 0:
				print "call number %s" % cps
				call_file_name=str(de)+"-"+str(cps)+"-"+"callfile"+"."+"call"
				functions.subprocess_cmd('echo Channel:%s > %s' % (args.ch,call_file_name))
				functions.subprocess_cmd('echo Context:%s >> %s' % (args.co,call_file_name))
				functions.subprocess_cmd('echo Extension:%s >> %s' %(args.ex,call_file_name))
				functions.subprocess_cmd('echo Priority:%s >> %s' %(args.pr,call_file_name))
				functions.subprocess_cmd('touch -r time_ref.file %s' % call_file_name)	
				cps=cps-1
			args.ba=args.ba-1
			de=de+args.de
		functions.subprocess_cmd('rm -rf time_ref.file')
		answer=functions.userInput("\033[1;32mDo you wish to start calling now [Y/N]....\033[1;m")
		if answer=="Y":
			functions.subprocess_cmd('mv *.call /var/spool/asterisk/outgoing')
		else:
			functions.subprocess_cmd('rm -rf *.call')
	else:
		print "batches has to be more than one to define delay"
		print "Continuing without batch or delay"
				
		while args.cps > 0:
			call_file_name=str(args.cps)+"-"+"callfile"+"."+"call"
			args.cps=args.cps-1
			functions.subprocess_cmd('touch %s' % call_file_name)
			functions.subprocess_cmd('echo Channel:%s > %s' % (args.ch,call_file_name))
			functions.subprocess_cmd('echo Context:%s >> %s' % (args.co,call_file_name))
			functions.subprocess_cmd('echo Extension:%s >> %s' %(args.ex,call_file_name))
			functions.subprocess_cmd('echo Priority:%s >> %s' %(args.pr,call_file_name))
		answer=functions.userInput("\033[1;32mDo you wish to start calling now [Y/N]....\033[1;m")
		if answer=="Y":
			functions.subprocess_cmd('mv *.call /var/spool/asterisk/outgoing')
		else:
			functions.subprocess_cmd('rm -rf *.call')
	
#call_now01()
call_now()


