from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
from kora.selenium import wd

def get_platinum_screener_list():
	result = {}
	while len(result) ==  0:
		url = "https://www.tradingview.com/forex-screener/"
	# options.add_argument("start-maximized")


		driver = wd
		driver.get(url)
		time.sleep(2)
		data = driver.find_element_by_xpath('//*[@id="js-screener-container"]/div[4]/table/tbody').text

		driver.quit()

		list_ticker = []
		list_currency = []
		list_rating = []

		data = data.splitlines()
		start_pt = 0
		end = len(data)
		while start_pt < end:
			# print("***")
			line_1 = data[start_pt]

			line_2 = data[start_pt+1]

			line_3 = data[start_pt+2]
			line_3 = line_3.split()
			line_3 = line_3[-1]

			list_ticker.append(line_1)
			list_currency.append(line_2)
			list_rating.append(line_3)

			start_pt = start_pt + 3


#	result = {}
		for i in range(len(list_ticker)):
			key = list_ticker[i][:3] + '/' + list_ticker[i][3:]
			result[key] = list_rating[i]


		print(len(result), ' recieved from forex screener')

	return result
