from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import random

driver = webdriver.Firefox()
driver.get('http://play.typeracer.com')
check = 0
#kind of game: practice or competition
while check == 0:
    try:
        if sys.argv[1] == "practice":
        	result = driver.find_element_by_xpath('//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a').click()
        else:
        	result = driver.find_element_by_xpath('//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a').click()
        check = 1
    except:
         pass
#take the text
if sys.argv[1] == "practice":
	elem = driver.find_element_by_xpath('//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div')
	time.sleep(5)
else:
	elem = driver.find_element_by_xpath('//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div')
	time.sleep(12)
#input
text = driver.find_element_by_class_name('txtInput')

for k in elem.text:
	text.send_keys(k)
	time.sleep(0.02)
