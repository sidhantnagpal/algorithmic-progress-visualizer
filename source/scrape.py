'''
	Created by Sidhant Nagpal
	Feb 1, 2018
'''

from sys import stdout
import re, json, requests
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium import webdriver

def stat(judge,probs):
	print '{: <4}: {}'.format(judge,probs)
	return probs

def codechef(handle):
	usr='http://www.codechef.com/users/' + handle
	request=requests.get(usr)
	content=request.content
	soup=BeautifulSoup(content,'html.parser')
	element=soup.find('section',{'class':'rating-data-section problems-solved'})
	prb = int(re.findall(r'\d+',element.findAll('h5')[0].text)[0])
	return stat('CC',prb)

def codeforces(handle): # using codeforces api
	# http://codeforces.com/api/help/methods#user.info
	usr = 'http://codeforces.com/api/user.status?handle='
	usr += handle
	usr += '&from=1&count=100000'
	stdout.write('Wait 30s!')
	stdout.flush()
	stdout.write('\r')
	request=requests.get(usr)
	content=request.content
	data = json.loads(content)
	probs = set()
	for a in data['result']:
		if a['verdict']=='OK':
			probs.add(a['problem']['name'])
	return stat('CF',len(probs))

def spoj(handle):
	usr='http://www.spoj.com/users/' + handle
	request=requests.get(usr)
	content=request.content
	soup=BeautifulSoup(content,'html.parser')
	element=soup.find('dl',{'class':'dl-horizontal profile-info-data profile-info-data-stats'})
	prb = int(element.findAll('dd')[0].text)
	return stat('SP',prb)

def uri(jid):
	usr='https://www.urionlinejudge.com.br/judge/en/profile/' + jid
	request=requests.get(usr)
	content=request.content
	soup=BeautifulSoup(content,'html.parser')
	element=soup.find('span',string='Solved:')
	prb = int(re.findall(r'\d+',element.parent.text)[0])
	return stat('URI',prb)

def csacademy(handle,browser):
	usr='https://csacademy.com/user/' + handle
	
	browser.get(usr)

	wait = WebDriverWait(browser,8)
	by = By.CSS_SELECTOR
	sel = 'span[style="font-size: 1.3em; margin-bottom: 10px;"]'
	tup = (by,sel)
	wait.until(EC.visibility_of_element_located(tup))
	element = browser.find_element_by_css_selector(sel)
	
	prb = int(re.findall(r'\d+',element.text)[0])
	return stat('CSA',prb)

def timus(jid):
	usr='http://acm.timus.ru/author.aspx?id=' + jid
	request=requests.get(usr)
	content=request.content
	soup=BeautifulSoup(content,'html.parser')
	element=soup.findAll('td',{'class':'author_stats_value'})[1]
	prb = int(re.findall(r'\d+',element.text)[0])
	return stat('TI',prb)

def poj(handle):
	usr='http://poj.org/userstatus?user_id=' + handle
	request=requests.get(usr)
	content=request.content
	soup=BeautifulSoup(content,'html.parser')
	element=soup.find('a',href='status?result=0&user_id=' + handle)
	prb=int(element.string)
	return stat('PKU',prb)

def uhunt(judge,jid):
	if judge=='UVa':
		usr='https://uhunt.onlinejudge.org/api/subs-user-last/'
	elif judge=='LA':
		usr='https://icpcarchive.ecs.baylor.edu/uhunt/api/subs-user-last/'
	usr+=jid
	usr+='/100000' 
	request=requests.get(usr)
	content=request.content
	data = json.loads(content)
	s = set()
	for a in data['subs']:
		if a[-1]!=-1: s.add(a[1])
	return stat(judge,len(s))

def hackerrank(handle,browser):
	usr='https://www.hackerrank.com/' + handle
	browser.get(usr)

	wait = WebDriverWait(browser,8)
	by = By.CSS_SELECTOR
	sel = 'a[data-analytics="ProfileChallengesLoadMore"]'
	tup = (by,sel)
	while True:
		try:
			wait.until(EC.visibility_of_element_located(tup))
			browser.find_element_by_css_selector(sel).click()
		except Exception as e:
			break
	sel = 'a[data-analytics="ProfileChallengesLink"]'
	prb = len(browser.find_elements_by_css_selector(sel))
	return stat('HR',prb)

def hackerearth(handle,browser):
	usr='https://www.hackerearth.com/' + 'submissions/' + handle	
	browser.get(usr)

	wait = WebDriverWait(browser,8)
	by = By.CSS_SELECTOR
	page = 1
	probs = set()
	browser.find_element_by_xpath("//select[@name='result']/option[text()='Accepted']").click()
	while True:
		# prevent class="loader-overlay"
		wait.until(EC.visibility_of_element_located((by,'div[class=""]')))
		stdout.write('Page %d'%(page))
		stdout.flush()
		stdout.write('\r')
		page += 1
		content = browser.page_source
		soup=BeautifulSoup(content,'html.parser')
		element=soup.findAll('i',{'class':'fa fa-check-circle fa-green result-icon tool-tip'})
		for x in element:
			y=x.parent.find_previous_sibling()
			probs.add(y['title'])

		sel = 'i[class="fa fa-angle-right dark"]'
		el = browser.find_element_by_css_selector(sel)
		pel = el.find_element_by_xpath('..') 
		if pel.get_attribute('class')=='disabled-arrow arrow':
			break
		browser.find_element_by_css_selector(sel).click()
	return stat('HE',len(probs))

def main():
	print 'Total Problems Solved Statistics'
	print 'Press Enter to Skip'
	data = {}

	handle = raw_input('CodeChef Handle: ')
	if handle != '':
		data['CodeChef'] = codechef(handle)
	
	handle = raw_input('SPOJ Handle: ')
	if handle != '':
		data['SPOJ'] = spoj(handle)
	
	handle = raw_input('Codeforces Handle: ')
	if handle != '':
		data['Codeforces'] = codeforces(handle) 

	handle = raw_input('URI ID: ')
	if handle != '':
		data['URI'] = uri(handle)
	
	handle = raw_input('UVa ID: ')
	if handle != '':
		data['UVa'] = uhunt('UVa',handle) 

	handle = raw_input('LiveArchive ID: ')
	if handle != '':
		data['LiveArchive'] = uhunt('LA',handle) 

	handle = raw_input('Timus ID: ')
	if handle != '':
		data['Timus'] = timus(handle)
	
	handle = raw_input('POJ ID: ')
	if handle != '':
		data['POJ'] = poj(handle)

	display = Display(visible=0,size=(800,600))
	display.start()
	browser = webdriver.Chrome('/usr/local/bin/chromedriver')
	
	handle = raw_input('CSAcademy Handle: ')
	if handle != '':
		data['CSAcademy'] = csacademy(handle,browser)
	
	handle = raw_input('HackerRank Handle: ')
	if handle != '':
		data['HackerRank'] = hackerrank(handle,browser)

	handle = raw_input('HackerEarth Handle: ')
	if handle != '':
		data['HackerEarth'] = hackerearth(handle,browser) 
	
	browser.quit()
	display.stop()
	
	with open("data.json", "w") as outfile:
		json.dump(data, outfile, indent=4)

	probs = sum(data.itervalues()) 
	print 'TOT : {}'.format(probs)
main()
