from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "https://onestop.ucas.edu.cn/home/index"
driver.get(url)

username = driver.find_element_by_id("menhuusername").send_keys("你的账户")
pwd = driver.find_element_by_id("menhupassword").send_keys("你的密码")
click = driver.find_element_by_class_name("loginbtn").click()
time.sleep(3)
click2 = driver.find_element_by_xpath('//*[@id="main-metro"]/div/div[1]/a').click()

