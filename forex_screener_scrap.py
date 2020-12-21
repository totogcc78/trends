from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time

def get_platinum_screener_list():
	result = {}
	while len(result) ==  0:
		url = "https://www.tradingview.com/forex-screener/"
		options = Options()
	# options.add_argument("start-maximized")
		options.add_argument("--headless")
		options.add_argument("--window-size=1920x1080")

		driver = webdriver.Chrome(options=options)
		driver.get(url)

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
