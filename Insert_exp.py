# -*- coding: utf-8 -*
#!/usr/bin/python
#####################################
##KILL THE NET##
#### PS: CHANGE Your Threads pool on line 186 to make script more faster :)
##############[LIBS]###################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time				   		
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m'        
#####################################
##########################################################################################
try:
		with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
				ooo = f.read().splitlines()
except IndexError:
		print (ktnred + '[+]================> ' + 'USAGE: '+sys.argv[0]+' listsite.txt' + CEND)
		pass
ooo = list((ooo))
##########################################################################################

def urlfix(url):
	if url[-1] == "/":
		pattern = re.compile('(.*)/')
		site = re.findall(pattern,url)
		url = site[0]
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url


def check_log(url):
	try:
		Agent2 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
		se2 = requests.session()
		log = url+'/wp-login.php?action=register'
		url = urlfix(url)
		ktn3 = se2.get(log, headers=Agent2, verify=False, timeout=20)
		if '<form name="registerform"' in ktn3.content.encode('utf-8'):
			print (ktn5purp + 'SITE VULN ..... [' + url + ']' + '\n' + CEND)
			open('SITE-VULN.txt', 'a').write(log+'\n')
			pass
		else:
			print (ktn7grey + 'SITE NOT VULN ..... [' + url + ']' + '\n' + CEND)

		pass
	except:
		pass
	pass

def plgn_check(url):
	try:
		url = urlfix(url)
		payload = url + '/wp-content/plugins/insert-or-embed-articulate-content-into-wordpress/readme.txt'
		Agent1 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
		se1 = requests.session()
		ktn2 = se1.get(payload, headers=Agent1, verify=False, timeout=20)
		if '=== Insert or Embed Articulate Content into Wordpress ====' in ktn2.content.encode('utf-8'):
			print (ktngreen + 'SEARCHING FOR VULN ..... [' + url + ']' + '\n' + CEND)
			open('Plugin-on.txt', 'a').write(payload+'\n')
			check_log(url)

		else:
			print (ktn7grey + 'SITE NOT VULN ..... [' + url + ']' + '\n' + CEND)
			pass    
	except:
		pass
	pass

def check(url):
		try:
				Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
				url = urlfix(url)
				se = requests.session()
				ktn1 = se.get(url, headers=Agent, verify=False, timeout=20)
				if ktn1.status_code == 200:
						plgn_check(url)
						pass
				else:
						print (ktnred + 'DEAD SITE: ' + url + CEND)

				pass
		except:
			pass

#####################################
def logo():
	clear = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37]
	x = ''' 
				 FEDERATION BLACK HAT SYSTEM | IG: @_gghost666_ 
<-.(`-')  _                      (`-')      (`-').-> (`-')  _<-. (`-')_  (`-')  _(`-')      
 __( OO) (_)      <-.      <-.   ( OO).->   (OO )__  ( OO).-/   \( OO) ) ( OO).-/( OO).->   
'-'. ,--.,-(`-'),--. )   ,--. )  /    '._  ,--. ,'-'(,------.,--./ ,--/ (,------./    '._   
|  .'   /| ( OO)|  (`-') |  (`-')|'--...__)|  | |  | |  .---'|   \ |  |  |  .---'|'--...__) 
|      /)|  |  )|  |OO ) |  |OO )`--.  .--'|  `-'  |(|  '--. |  . '|  |)(|  '--. `--.  .--' 
|  .   '(|  |_/(|  '__ |(|  '__ |   |  |   |  .-.  | |  .--' |  |\    |  |  .--'    |  |    
|  |\   \|  |'->|     |' |     |'   |  |   |  | |  | |  `---.|  | \   |  |  `---.   |  |    
`--' '--'`--'   `-----'  `-----'    `--'   `--' `--' `------'`--'  `--'  `------'   `--'    
									  KILL THE NET
									 FB: fb/KtN.1990  
			   Note! : We Accept any responsibility for any illegal usage :). '''

	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
		time.sleep(0.05)
		pass


logo()

##########################################################################################
def Main():
		try:
				
				start = timer()
				ThreadPool = Pool(100)
				Threads = ThreadPool.map(check, ooo)
				print('TIME TAKE: ' + str(timer() - start) + ' S')
		except:
				pass


if __name__ == '__main__':
		Main()