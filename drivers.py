from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from flask import current_app as app

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = app.config["GOOGLE_CHROME_BIN"]
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=app.config["CHROMEDRIVER_PATH"], chrome_options=chrome_options)

def flipkart(mob):
    browser.get('https://www.flipkart.com/account/login?ret=/')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input').send_keys(mob)
    browser.find_element_by_link_text('Forgot?').click()

def netmeds(mob):
    browser.get('https://www.netmeds.com/customer/account/login')
    browser.implicitly_wait(5)
    browser.find_element_by_id('loginfirst_mobileno').send_keys(mob)
    browser.find_element_by_class_name('btn-signpass').click()
    
def oyorooms(mob):
    browser.get('https://www.oyorooms.com/login?country=&retUrl=/')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/input').send_keys(mob)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/button').click()
    
def abhibus(mob):
    browser.get('https://www.abhibus.com/')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[3]/div[1]/div/form/div[3]/input').send_keys(mob)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[3]/div[1]/div/form/div[6]/input').click()
    
def uber(mob):
    browser.get('https://auth.uber.com/login/?breeze_local_zone=phx5&next_url=https%3A%2F%2Fm.uber.com%2F&state=bwJUXHglVGcAhuI3VVwLhbrgETDe_e9kq4T78d7Qacg%3D')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/form/div[1]/div/div[1]/div/div[2]/input').send_keys(mob)
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/form/div[2]/button/span').click()
 
def wynk(mob):
    browser.get('/html/body/ngb-modal-window/div/div/app-login/div/div/div[2]/div[1]/form/div[1]/input[2]')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/ngb-modal-window/div/div/app-login/div/div/div[2]/div[1]/form/div[1]/input[2]').send_keys(mob)
    browser.find_element_by_xpath('/html/body/ngb-modal-window/div/div/app-login/div/div/div[2]/div[1]/form/div[2]/button').click()

def amazon(mob):
    browser.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fie%3DUTF8%26tag%3Dgooginabkvernac-21%26ascsubtag%3D_k_Cj0KCQiA9orxBRD0ARIsAK9JDxSfmIfqU8juU4Fjz61SE4Imv3G3pZaikD28mdfzCcAghmF3LVxuddoaAp85EALw_wcB_k_%26ext_vrnc%3Dhi%26gclid%3DCj0KCQiA9orxBRD0ARIsAK9JDxSfmIfqU8juU4Fjz61SE4Imv3G3pZaikD28mdfzCcAghmF3LVxuddoaAp85EALw_wcB%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input').send_keys(mob)
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div[3]/form/span/span/input').click()
    
def tinder(mob):
    browser.get('https://tinder.com/')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span').click()
    browser.implicitly_wait(2)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]').click()
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/input').send_keys(mob)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button').click()
    
def lenskart(mob):
    browser.get('')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div/div/div[1]/div[3]/div/div[1]/div/div/div/span[1]').click()
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div/div/div[2]/div[2]/form/ul/li/div/input').send_keys(mob)
    browser.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div/div/div[2]/div[2]/form/div/div[1]/button').click() 
    
def goibibo(mob):
    browser.get('https://www.goibibo.com/')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/form/div/input').send_keys(mob)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/input').click()
    
def snapdeal(mob):
    browser.get('https://www.snapdeal.com/')
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div/div/div/div[6]/form/div/input').send_keys(mob)
    browser.find_element_by_xpath('/html/body/div/div/div/div[6]/form/button').click()

# def goibibo(mob):
#     browser.get('')
#     browser.implicitly_wait(5)
#     browser.find_element_by_xpath('/').send_keys(mob)
#     browser.find_element_by_xpath('/').click()
    