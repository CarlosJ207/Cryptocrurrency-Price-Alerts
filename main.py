from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
def get_driver(): 

  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver = webdriver.Chrome(options=options)
  driver.get("https://coinranking.com/")
  return driver

def float_txt(value):
 #Change the 24Hr percentage change from a string to a float object
 float_value = value.replace('%', '') 
 output = float(float_value)
 return output 


def main():
  driver = get_driver()
  #Click search button
  search_button = driver.find_element(by = 'xpath', value = "//*[@id='__layout']/div/header/div[2]/div[1]/button")
  search_button.click()

  #Type text into the search button
  val = input("Enter the name of the cryptocurrenct to monitor:")
  text_area = driver.find_element(by = 'xpath', value = "//*[@id='__layout']/div/header/div[2]/div[1]/div[1]/div[2]/input")
  text_area.send_keys(val + Keys.RETURN)
  while True:
    time.sleep(2)
    element = driver.find_element(by = 'xpath', value = "/html/body/div/div/div/div[3]/section/div[4]/div/div/table/tbody/tr/td[2]/div")
    str_value = element.text
    print(float_txt(str_value))
    


print(main())

