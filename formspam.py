from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

### Change the Chrome Webdriver .exe location
path = 'C:\\Users\\kalok\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
service = Service(executable_path=path)

### Webdriver Configuration
option = webdriver.ChromeOptions()
option.add_argument("-incognito") # Uncomment to open the chrome in incognito mode
option.add_experimental_option("excludeSwitches", ['enable-automation'])
# option.add_argument('log-level=3') # Uncomment to hide every type of warning message
option.add_argument("disable-infobars")
option.add_argument("--disable-extensions")
# option.add_argument("--headless") # Uncomment to make it run in background
# option.add_argument("start-maximized") # Uncomment to start in maximize window
# option.add_argument("disable-gpu") # Uncomment to disable GPU

browser = webdriver.Chrome(service=service, options=option)

### Change the Google Form link
GForm_link = "https://docs.google.com/forms/d/e/xxx/viewform" # example Google Form, replace with your Google Form
browser.get(GForm_link) 

### Web Input section
## Setup page 1
time.sleep(0.3)

# Next button click with CSS Selector
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span')  
nextbutton.click()


## Setup page 2 ---------
pick = '//*[@id="i5"]'
radiobuttons_page_1 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, pick))
)
radiobuttons_page_1.click()

nextbutton = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2) > span'))
)
nextbutton.click()


## Setup page 3 ---------
time.sleep(0.3)

# //*[@id="i9"] #Durasi Operasi
pick = ['//*[@id="i9"]','//*[@id="i12"]','//*[@id="i15"]']
radiobuttons_page_2 = browser.find_element("xpath", random.choice(pick))

# //*[@id="i25"] #Peran Perusahaan
pick = ['//*[@id="i25"]','//*[@id="i28"]','//*[@id="i31"]']
radiobuttons_page_3 = browser.find_element("xpath", random.choice(pick))

# //*[@id="i38"] #Average income
pick = ['//*[@id="i38"]','//*[@id="i41"]','//*[@id="i44"]']
radiobuttons_page_4 = browser.find_element("xpath", random.choice(pick))

# Page 2 answer
radiobuttons_page_2.click()
radiobuttons_page_3.click()
radiobuttons_page_4.click()

# Next button click with CSS Selector
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2) > span')
nextbutton.click()


## Setup page 4 ---------
time.sleep(0.3)

# Linear scale input with CSS Selector
#! What we don't want : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div > div.vd3tt'
#! What we want       : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div'
linearscale_page_4_no_1 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')  

linearscale_page_4_no_2 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_4_no_3 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(4) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_4_no_4 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(5) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_4_no_5 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(6) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_4_no_6 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(7) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_4_no_7 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(8) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

x = random.randrange(2,5)
linearscale_page_4_no_1.click()
linearscale_page_4_no_1.send_keys(Keys.ARROW_DOWN * x)

x = random.randrange(2,5)
linearscale_page_4_no_2.click()
linearscale_page_4_no_2.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_4_no_3.click()
linearscale_page_4_no_3.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_4_no_4.click()
linearscale_page_4_no_4.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_4_no_5.click()
linearscale_page_4_no_5.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_4_no_6.click()
linearscale_page_4_no_6.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_4_no_7.click()
linearscale_page_4_no_7.send_keys(Keys.ARROW_RIGHT * x)

# Next button click with CSS Selector
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2) > span')
nextbutton.click()


## Setup page 5 ---------
time.sleep(0.3)

# Linear scale input with CSS Selector
#! What we don't want : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div > div.vd3tt'
#! What we want       : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div'
linearscale_page_5_no_1 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')  

linearscale_page_5_no_2 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_5_no_3 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(4) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_5_no_4 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(5) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_5_no_5 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(6) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_5_no_6 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(7) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_5_no_7 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(8) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

x = random.randrange(2,5)
linearscale_page_5_no_1.click()
linearscale_page_5_no_1.send_keys(Keys.ARROW_DOWN * x)

x = random.randrange(2,5)
linearscale_page_5_no_2.click()
linearscale_page_5_no_2.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_5_no_3.click()
linearscale_page_5_no_3.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_5_no_4.click()
linearscale_page_5_no_4.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_5_no_5.click()
linearscale_page_5_no_5.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_5_no_6.click()
linearscale_page_5_no_6.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_5_no_7.click()
linearscale_page_5_no_7.send_keys(Keys.ARROW_RIGHT * x)

# Next button click with CSS Selector
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2) > span')
nextbutton.click()


## Setup page 6 ---------
time.sleep(0.3)

# Linear scale input with CSS Selector
#! What we don't want : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div > div.vd3tt'
#! What we want       : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div'
linearscale_page_6_no_1 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')  

linearscale_page_6_no_2 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_6_no_3 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(4) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_6_no_4 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(5) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_6_no_5 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(6) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_6_no_6 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(7) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_6_no_7 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(8) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

x = random.randrange(2,5)
linearscale_page_6_no_1.click()
linearscale_page_6_no_1.send_keys(Keys.ARROW_DOWN * x)

x = random.randrange(2,5)
linearscale_page_6_no_2.click()
linearscale_page_6_no_2.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_6_no_3.click()
linearscale_page_6_no_3.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_6_no_4.click()
linearscale_page_6_no_4.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_6_no_5.click()
linearscale_page_6_no_5.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_6_no_6.click()
linearscale_page_6_no_6.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_6_no_7.click()
linearscale_page_6_no_7.send_keys(Keys.ARROW_RIGHT * x)

# Next button click with CSS Selector
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2) > span')
nextbutton.click()


## Setup page 7 ---------
time.sleep(0.3)

# Linear scale input with CSS Selector
#! What we don't want : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div > div.vd3tt'
#! What we want       : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div'
linearscale_page_7_no_1 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')  

linearscale_page_7_no_2 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_7_no_3 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(4) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_7_no_4 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(5) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_7_no_5 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(6) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_7_no_6 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(7) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

x = random.randrange(2,5)
linearscale_page_7_no_1.click()
linearscale_page_7_no_1.send_keys(Keys.ARROW_DOWN * x)

x = random.randrange(2,5)
linearscale_page_7_no_2.click()
linearscale_page_7_no_2.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_7_no_3.click()
linearscale_page_7_no_3.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_7_no_4.click()
linearscale_page_7_no_4.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_7_no_5.click()
linearscale_page_7_no_5.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_7_no_6.click()
linearscale_page_7_no_6.send_keys(Keys.ARROW_RIGHT * x)

# Next button click with CSS Selector
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2) > span')
nextbutton.click()


## Setup page 8 ---------
time.sleep(0.3)

# Linear scale input with CSS Selector
#! What we don't want : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div > div.vd3tt'
#! What we want       : '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div.lLfZXe.fnxRtf.BpKDyb > span > div > label:nth-child(2) > div.eRqjfd > div > div'
linearscale_page_8_no_1 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')  

linearscale_page_8_no_2 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_8_no_3 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(4) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_8_no_4 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(5) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_8_no_5 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(6) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_8_no_6 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(7) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')

linearscale_page_8_no_7 = browser.find_element(By.CSS_SELECTOR,'#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(8) > div > div > div.PY6Xd > div > span > div > label:nth-child(2) > div.eRqjfd > div > div')


x = random.randrange(2,5)
linearscale_page_8_no_1.click()
linearscale_page_8_no_1.send_keys(Keys.ARROW_DOWN * x)

x = random.randrange(2,5)
linearscale_page_8_no_2.click()
linearscale_page_8_no_2.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_8_no_3.click()
linearscale_page_8_no_3.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_8_no_4.click()
linearscale_page_8_no_4.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_8_no_5.click()
linearscale_page_8_no_5.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_8_no_6.click()
linearscale_page_8_no_6.send_keys(Keys.ARROW_RIGHT * x)

x = random.randrange(2,5)
linearscale_page_8_no_7.click()
linearscale_page_8_no_7.send_keys(Keys.ARROW_RIGHT * x)

# Next button click with CSS Selector
nextbutton = browser.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2) > span')
nextbutton.click()

submitbutton = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')))
submitbutton.click()

# Close the browser
browser.close()