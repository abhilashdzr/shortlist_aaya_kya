from datetime import datetime
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import re
import sys

class Hack:
  def __init__(self,username,password,name,m,ts):

    user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    # options.headless = True
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    self.password = password
    self.username = username  
    self.name = name  
    self.m = m  
    self.driver = driver
    self.last_stamp = ts



  def login_to_erp(self):

    driver = self.driver

    url = "https://erp.iitkgp.ac.in/" 
    driver.get(url)
    time.sleep(3)

    if self.name in driver.page_source:
      self.get_to_notice_board()

    else:
      # find username/email field and send the username itself to the input field
      driver.find_element(By.ID,"user_id").send_keys(self.username)
      time.sleep(1)

      # find password input field and insert password as well
      driver.find_element(By.ID,"password").send_keys(self.password)
      time.sleep(3)

      try:
        #find question asked
        question = driver.find_element(By.ID,"question").text
        driver.find_element(By.ID,"answer").send_keys((self.m)[question])
      
        # click login button
        driver.find_element(By.ID,"loginFormSubmitButton").click()

      except:
        print("Wrong credentials, try again")
        hack = take_input()
        hack.login_to_erp()

      time.sleep(4)

      #call noticeboard function
      self.get_to_notice_board()



  def get_to_notice_board(self):
    try:
      driver = self.driver

      html_tree=html.fromstring(self.driver.page_source)
      cdc_module_link = html_tree.xpath(".//div[@class='navbar navbar-default']/div[2]/ul/li[3]/a/@href")[0]

      #get into cdc module
      driver.get("https://erp.iitkgp.ac.in/IIT_ERP3/"+cdc_module_link)
      time.sleep(2)

      #click on STUDENT
      driver.find_element(By.CLASS_NAME,"text-primary").click()
      time.sleep(2)

      #click on application for placement/internship
      driver.find_element(By.XPATH,".//div[@class='panel-body']/div/a").click()
      time.sleep(2)


      while(True):
        self.check_jsp()
        time.sleep(300)

    except:
      #start from loggin in again
      print("exception found")
      print("Oops!", sys.exc_info()[0], "occurred.")
      self.login_to_erp()



  def check_jsp(self):

    print("into jsp checking")
    #go to the notice board jsp
    self.driver.get("https://erp.iitkgp.ac.in/TrainingPlacementSSO/Notice.jsp")
    time.sleep(2)

    html_tree = html.fromstring(self.driver.page_source)

    i = 3 
    while(True):
      try:
        notice_text = html_tree.xpath(f"(.//tr[@role='row'])[{i}]/td[6]/a/@title")[0]
        if re.search(self.username, notice_text, re.IGNORECASE) or re.search(self.name, notice_text, re.IGNORECASE):
          print(notice_text)
          print("found")
          # print('\007')
          os.system('play -nq -t alsa synth {} sine {}'.format(10, 220))
          
        notice_time = html_tree.xpath(f"(.//tr[@role='row'])[{i}]/td[8]/@title")[0]
        date = notice_time.split(" ")[0]
        t = notice_time.split(" ")[1]
        yy = int(date.split("-")[2])
        mm = int(date.split("-")[1])
        dd = int(date.split("-")[0])
        h = int(t.split(":")[0])
        minute = int(t.split(":")[1])

        time_stamp = datetime(yy,mm,dd,h,minute,0)
        if(time_stamp<=self.last_stamp):
          self.last_stamp = time_stamp
          break   
        
        i+=1
          
      except:
        break  



#main function
# username,password,roll_no,name,m

def take_input():
  username = input("Give the username ")
  password = input("Give the password ")
  name = input("Give your name ")
  f_q = input("Input 1st question ")
  f_ans = input("Input 1st answer ")
  s_q = input("Input 2nd question ")
  s_ans = input("Input 2nd answer ")
  t_q = input("Input 3rd question ")
  t_ans = input("Input 3rd answer ")

  m = {}
  m[f_q] = f_ans
  m[s_q] = s_ans 
  m[t_q] = t_ans 

  ts = datetime(2022, 9, 3, 12, 0, 0, 0)
  return Hack(username,password,name,m,ts)
#datetime can be set to right now using datetime.now()

hack = take_input()
hack.login_to_erp()

















