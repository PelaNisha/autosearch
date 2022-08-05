from itsdangerous import exc
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import csv
import json

li = []

input_file = input("Enter the input csv file name: (with .csv extension) ")
save_file = input("Enter the name of the file to save to : (with .csv extension)")

driver = webdriver.Firefox()
driver.get("https://www.google.com/maps/@27.6925138,85.2825928,15z")
sleep(2)


# search the place 
def searchplace(p):
	place = driver.find_element_by_class_name('tactile-searchbox-input')
	place.send_keys(p)
	sleep(5)
	submit = driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
	submit.click()
	sleep(3)
	try:
		get_text = driver.find_elements_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[1]/div/div/div/div[1]')
		sleep(2)
		name = get_text[0].text
		try:
			driver.find_element_by_xpath('//*[@id="searchboxinput"]').clear()
			sleep(2)
			searchplace(name)

		except:
			print("Error occured!")
		
	except:
		submit = driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
		submit.click()


# get the location and location link
def get_gogle_location():
	sleep(5)
	google_link = driver.find_elements_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[5]/button/span/img')
	google_link[0].click() 
	print("Clicked!")
	sleep(5)
	loc = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div[3]/div[2]/div[2]')
	for l in loc:
		final_location = l.text
	list_links=driver.find_elements_by_tag_name('input')
	final_location_link = list_links[0].get_attribute('value')
	final_name = list_links[2].get_attribute('value')

	di = {}
	di['name'] = final_name
	di['location'] = final_location
	di['google_map_location'] = final_location_link
	
	li.append(di)
	di = {}
	print(li)
	# back button to close the share 
	sleep(2)
	close_botton = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/div[2]/button')
	close_botton.click()
	sleep(5)
	try:
		driver.find_element_by_xpath('//*[@id="searchboxinput"]').clear()
	except:
		print("Error occured!")
	sleep(5)


# Function to save data into a file
def save_to_file(final_result,filename):
	with open(filename, "w+") as f:
		json.dump(final_result, f, indent = 2)


# convert to a csv file 
def conv_to_csv(json_file, csv_file):
	with open(json_file) as json_file:
		data = json.load(json_file)	
		fin_data = data
		data_file = open(csv_file, 'w')	
		csv_writer = csv.writer(data_file)	
		count = 0
		for f in fin_data:
			if count == 0:
				header = f.keys()
				csv_writer.writerow(header)
				count += 1
			csv_writer.writerow(f.values())
	
	data_file.close()


# main function 
def main(input_file, save_file):
	rows = []
	with open(input_file, 'r') as file:
		csvreader = csv.reader(file)
		for row in csvreader:
			rows.append(row)
	for i in rows[1:]:
		try:
			one = str(i[0])

			searchplace(one)
			get_gogle_location()
		except:
			print("Error occured!")
			pass

	save_to_file(li, 'mydata.json')
	conv_to_csv('mydata.json', save_file)


# calling main function
main(input_file, save_file)

# close the driver
driver.close()
  