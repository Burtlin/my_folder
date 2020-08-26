from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time
#https://www.railbike.com.tw/cart/step1


email = "fox82421020@gmail.com"
password = "1i6cj/6"
name = u"林泊宏"
ID = "R124141183"


driver = webdriver.Chrome(os.path.abspath('chromedriver.exe'))
# 登入
driver.get("https://www.railbike.com.tw/login/normal")
driver.find_element_by_name("username").click()
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys(email)
driver.find_element_by_name("username").send_keys(Keys.TAB)
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("submit_login").click()
# Step 1
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='確定儲存'])[1]/following::div[3]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='I.路線'])[1]/following::button[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='I.路線'])[1]/following::button[1]").click()
time.sleep(0.5)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='II.起始站'])[1]/following::button[1]").click()
# driver.find_element_by_name("2019-01-23").click()
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::p[30]").click()
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::p[32]").click()
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::p[34]").click()
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::p[30]").click()
time.sleep(6)
# driver.find_element_by_name("to_station").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='V.張數(人)'])[1]/following::button[2]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='V.張數(人)'])[1]/following::button[2]").click()
driver.find_element_by_name("is_checked").click()
driver.find_element_by_id("submit_button").click()
time.sleep(1)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='新北市瑞芳區建基路2段121號'])[1]/following::button[1]").click()


driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::div[2]").click()
driver.find_element_by_id("same_member").click()
time.sleep(2)
driver.find_element_by_name("subscriber_id_card").click()
driver.find_element_by_name("subscriber_id_card").clear()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='請選擇訂購人資訊'])[1]/following::div[8]").click() #先生
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='先生'])[1]/following::div[2]").click() #小姐
driver.find_element_by_name("subscriber_id_card").send_keys(ID)

# 二聯式發票
driver.find_element_by_name("invoice_addressee").click()
driver.find_element_by_name("invoice_addressee").click()
driver.find_element_by_name("invoice_name").click()
driver.find_element_by_name("invoice_name").clear()
driver.find_element_by_name("invoice_name").send_keys(name)
driver.find_element_by_name("invoice_email").click()
driver.find_element_by_name("invoice_email").clear()
driver.find_element_by_name("invoice_email").send_keys(email)
driver.find_element_by_name("check_rule").click()

# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='自然人憑證'])[1]/following::div[1]").click()
# driver.find_element_by_name("mobile_barcode_carrier").click()
# driver.find_element_by_name("mobile_barcode_carrier").clear()
# driver.find_element_by_name("mobile_barcode_carrier").send_keys("/O1LV6OQ")
# driver.find_element_by_id("invoice_email_5").click()
# driver.find_element_by_id("invoice_email_5").click()
# driver.find_element_by_name("invoice_email_5").send_keys("fox82421020@gmail.com")

# 確認
# driver.find_element_by_id("cart_submit").click()