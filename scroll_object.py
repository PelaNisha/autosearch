from itsdangerous import exc
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from sqlalchemy import true


li = []


driver = webdriver.Firefox()
driver.get("https://www.google.com/maps/@27.6924389,85.2825928,15z")
sleep(3)


def change_language():
	sleep(3)
	menu_button = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[1]/button')
	menu_button.click()
	sleep(3)
	sel_lan_button = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[25]/div/div[2]/ul/div[7]/li[1]/button')
	sel_lan_button.click()
	sleep(3)
	click_eng = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/div[3]/div/div/div/div[2]/div[2]/ul[1]/li[11]')
	click_eng.click()
	sleep(3)

# search the place 
def searchplace():
	place = driver.find_element_by_class_name('tactile-searchbox-input')
	place.send_keys("NIC Asia Bank in Kathmandu")
	sleep(3)
	submit = driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
	submit.click()
	sleep(3)


def scroll_to_bottom():  
	set_func = True
	sleep(4)
	while set_func == True:
		print("inside while!")
		try:
			
			print("TRY try !")
			div_locator = "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]"
			div_el = driver.find_element_by_xpath(div_locator)
			driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div_el)
			print(" DRiver Execute : ", div_el)
			sleep(3)
			try:
				print("her last words! ")
				limit_text = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[145]/div/p/span/span[1]')
				print(limit_text.text)
				set_func = False
				break
			except:
				pass
		except:
			print("INto the except case!")
			break
	sleep(2)
	back_to_top = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button/span[1]")
	back_to_top.click()
	sleep(2)
	get_names()
	

def get_names():
	print("Names are getting extracted")
	list_ = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')

	try:
		for item in list_.find_elements_by_class_name('NrDZNb'):
			print(item.text)

		sleep(2)
	except:
		print("Error occured!")



# change_language()
searchplace()
sleep(3)
scroll_to_bottom()

# close the driver
# driver.close()
