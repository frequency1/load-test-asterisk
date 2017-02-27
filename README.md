# load-test-asterisk

Command line tool for asterisk stress test



python callnow.py -h
usage: callnow.py [-h] [-ma MA | -re RE | -wa WA] -ch CH -co CO -ex EX -pr PR
                  -cps CPS [-ba BA] [-de DE]

Generate automate calls using Asterisk

optional arguments:
  -h, --help  show this help message and exit
  -ma MA      Max retries before giving up default is 0
  -re RE      Seconds between retries, Default is 300 (5 min).
  -wa WA      Seconds to wait for an answer. Default is 45
  -ch CH      Channel to use for the call. (i.e pjsip/101)
  -co CO      <context-name> Context in extensions.conf
  -ex EX      <ext> Extension definition in extensions.conf
  -pr PR      Priority of extension to start with
  -cps CPS    Maximum calls per second, depends on OS file creation
  -ba BA      Number of batches
  -de DE      Delay between batches in seconds


