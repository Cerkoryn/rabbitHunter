from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import requests
import random
import time
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

random.seed(time.time())
baseURL="https://deadrabbits.io/"
rand = (random.randrange(1000, 5000, 1))/1000.0

total=0
found=0
with open("latestAnswers.txt", "r+") as inFile:
    with open("protonDrive.txt", "w+") as driveFile:
        for line in inFile.readlines():
            total+=1
            os.system("cls")
            random.seed(time.time())
            fullURL=baseURL+line.strip()+"\n"
            print(f"trying {fullURL} ...")
            #driveFile.write(fullURL)
            #response = requests.get(fullURL)
            #print(response.text)
            driver.get(fullURL)
            time.sleep(8)
            if "404 Not Found" in driver.page_source:
            #if "The link either does not exist or has expired" in response.text:
                print(f"Doesn't exist, sleeping for {rand} seconds and trying the next one.")
            else:
                found+=1
                driveFile.write(fullURL)
            time.sleep(rand)
        driver.close()
        print(f"Searched {total} total URLs on {baseURL}.  Found {found} hits.")



#with open("latestAnswers.txt", "r+") as inFile:
#    with open("protonMail.txt", "w+") as mailFile:
#        for line in inFile.readlines():
#            tmpLine=line.strip()+"@protonmail.com; \n"
#            mailFile.write(tmpLine)
            