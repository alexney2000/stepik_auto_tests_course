from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(0.5)
link = 'http://suninjuly.github.io/cats.html'
browser.get(link)
browser.find_element(By.ID, "button")