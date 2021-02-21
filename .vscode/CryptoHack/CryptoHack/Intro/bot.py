from selenium import webdriver
import time


driver1 = webdriver.Chrome(executable_path='/Users/Ummar Awan/Downloads/chromedriver')
driver2 = webdriver.Chrome(executable_path='/Users/Ummar Awan/Downloads/chromedriver')
driver3 = webdriver.Chrome(executable_path='/Users/Ummar Awan/Downloads/chromedriver')

driver1.get('https://youtu.be/Sj1T97UIbwM')
driver2.get('https://youtu.be/Sj1T97UIbwM')
driver3.get('https://youtu.be/Sj1T97UIbwM')

while True:
    sleep(60)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()