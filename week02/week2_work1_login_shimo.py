# coding:utf-8
from selenium import webdriver
import time

try:
    # 使用webdriver启动浏览器
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/welcome')
    # 延迟2秒
    time.sleep(1)

    # 模拟浏览器,使用find_element_by_xpath方法，采用标签属性去定位到“登录”
    clk_tag = browser.find_element_by_xpath('//*[@class="entries"]/a[2]')
    clk_tag.click()
    time.sleep(1)
    # 获得新的url
    # print(browser.current_url)
    # print(browser.page_source)

    # 再定位到帐号输入的位置，并传送登录帐号(帐号已隐掉)
    browser.find_element_by_xpath('//*[@class="input"]/input').send_keys('account@mail.com')
    # 这里有坑！'list' object has no attribute 'send_keys'(密码已隐掉)
    browser.find_elements_by_xpath('//*[@name="password"]')[0].send_keys('password')
    browser.find_element_by_xpath('//*[@type="black"]').click()
    time.sleep(5)
except Exception as e:
    print(e)

finally:
    browser.close()
