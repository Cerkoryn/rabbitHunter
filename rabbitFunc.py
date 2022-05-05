from pydoc import plain
from pyparsing import Word
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from sympy import true
from webdriver_manager.chrome import ChromeDriverManager

import hashlib
import enchant
import random
import pybel
import time
import os

def caesarCipher(plaintext, shift):
    result = ""
    # traverse text
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char=="\n":
            continue
        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    result+="\n"
    return result

def GenWordlist():
    if os.path.exists("wordlist.txt"):
        choice = input("This will overwrite your current wordlist.txt, are you sure? y/n: ")
        if choice=='y' or choice=='Y' or choice=='yes' or choice=='Yes':
            pass
        else:
            exit()

    #Initialize here to keep in scope.
    clue1ans=clue2ans=clue3ans=clue4ans=clue5ans=clue6ans=clue7ans=clue8ans=""
    try:
        with open("answers.txt", "r+") as answerFile:
            clue1Line=(answerFile.readline()).strip("\n")
            clue1ans=clue1Line.split(",")
            clue2Line=(answerFile.readline()).strip("\n")
            clue2ans=clue2Line.split(",")
            clue3Line=(answerFile.readline()).strip("\n")
            clue3ans=clue3Line.split(",")
            clue4Line=(answerFile.readline()).strip("\n")
            clue4ans=clue4Line.split(",")
            clue5Line=(answerFile.readline()).strip("\n")
            clue5ans=clue5Line.split(",")
            clue6Line=(answerFile.readline()).strip("\n")
            clue6ans=clue6Line.split(",")
            clue7Line=(answerFile.readline()).strip("\n")
            clue7ans=clue7Line.split(",")
            clue8Line=(answerFile.readline()).strip("\n")
            clue8ans=clue8Line.split(",")

    except:
        print("Error reading answers.txt.  Make sure each riddle has its own line and the answers are separated by commas.")
        print("Also remember that clues 7 and 8 take the whole \"word\", not just the first character.")
        return

    with open("tmpfile.txt", "w+") as tmpFile:
        #Taking just the first letter of the whole answer
        for part1 in clue1ans:
            for part2 in clue2ans:
                for part3 in clue3ans:
                    for part4 in clue4ans:
                        for part5 in clue5ans:
                            for part6 in clue6ans:
                                for part7 in clue7ans:
                                    for part8 in clue8ans:
                                        tmpFile.write(f"{part1[0]}{part2[0]}{part3[0]}{part4[0]}{part5[0]}{part6[0]}{part7}{part8}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}{part4[0]}{part5[0]}{part6[0]}{part7}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}{part4[0]}{part5[0]}{part6[0]}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}{part4[0]}{part5[0]}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}{part4[0]}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}\n")
                                        #file.write(f"{part1[1][0]}\n")

        #Taking just the first letter of EACH WORD in the answer
        for part1 in clue1ans:
            for part2 in clue2ans:
                for part3 in clue3ans:
                    for part4 in clue4ans:
                        for part5 in clue5ans:
                            for part6 in clue6ans:
                                for part7 in clue7ans:
                                    for part8 in clue8ans:
                                        line=""
                                        for splitPart1 in part1.split():
                                            line+=splitPart1[0]
                                            #tmpline=line+"\n"
                                            #wordlistFile.write(tmpline)
                                        for splitPart2 in part2.split():
                                            line+=splitPart2[0]
                                            #tmpline=line+"\n"
                                            #wordlistFile.write(tmpline)
                                        for splitPart3 in part3.split():
                                            line+=splitPart3[0]
                                            #tmpline=line+"\n"
                                            #wordlistFile.write(tmpline)
                                        for splitPart4 in part4.split():
                                            line+=splitPart4[0]
                                            #tmpline=line+"\n"
                                            #wordlistFile.write(tmpline)
                                        for splitPart5 in part5.split():
                                            line+=splitPart5[0]
                                            #tmpline=line+"\n"
                                            #wordlistFile.write(tmpline)
                                        for splitPart6 in part6.split():
                                            line+=splitPart6[0]
                                            #tmpline=line+"\n"
                                            #wordlistFile.write(tmpline)
                                        line+=part7
                                            #tmpline=line+"\n"
                                            #wordlistFile.write(tmpline)
                                        line+=part8
                                        tmpline=line+"\n"
                                        tmpFile.write(tmpline)

    caesarTrue=False
    shift=26
    caesar=input("Would you like to apply a Caesar Cipher to your wordlist? y/n: ")
    if caesar=='y' or caesar=='Y' or caesar=='yes' or caesar=='Yes':
        caesarTrue=True
        try:
            shift=int(input("Enter the shift you'd like to use.  (I.e., 13 for ROT13, 21 for ROT21, etc.): "))
            if shift>25 or shift<1:
                print("There was an error getting your desired shift.  Make sure you enter a number between 1 and 25.")
                exit()
        except:
            print("There was an error getting your desired shift.  Make sure you enter a number between 1 and 25.")
            exit()

    print("Elminating duplicates...")
    with open("tmpFile.txt", "r+") as tmpFile:
        with open("wordlist.txt", "w+") as wordlistFile:
            tmp=set()
            for line in tmpFile:
                if caesarTrue:
                    line=caesarCipher(line, shift)
                if line not in tmp:
                    wordlistFile.write(line)
                    tmp.add(line)
    
    os.remove("tmpfile.txt")
    print("Wrote wordlist to wordlist.txt.")

def genEmails():
    GenWordlist()
    fullString=""
    with open("wordlist.txt", "r+") as file:
        for line in file.readlines():
            tmpLine=line.strip()+"@protonmail.com; \n"
            fullString+=tmpLine

    with open("emailList.txt", "w+") as outFile:
        outFile.write(fullString)
    print("Wrote email list to emailList.txt.")

def searchProtonDrive():
    GenWordlist()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    random.seed(time.time())
    baseURL="https://drive.protonmail.com/urls/"
    rand = (random.randrange(1000, 5000, 1))/1000.0

    total=0
    found=0
    with open("wordlist.txt", "r+") as inFile:
        with open("results.txt", "w+") as outFile:
            for line in inFile.readlines():
                total+=1
                os.system("cls")
                rand = (random.randrange(1000, 5000, 1))/1000.0
                fullURL=baseURL+line.strip()+"\n"
                print(f"trying {fullURL} ...")
                driver.get(fullURL)
                time.sleep(6)
                if "The link either does not exist or has expired" in driver.page_source:
                    print(f"Doesn't exist, sleeping for {rand} seconds and trying the next one.")
                else:
                    found+=1
                    outFile.write(fullURL)
                time.sleep(rand)
            print(f"Searched {total} total URLs on {baseURL}.  Found {found} hits.")

    driver.close()

def searchDeadRabbitsIO():
    GenWordlist()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    random.seed(time.time())
    baseURL="https://deadrabbits.io/"
    rand = (random.randrange(1000, 5000, 1))/1000.0

    total=0
    found=0
    with open("wordlist.txt", "r+") as inFile:
        with open("results.txt", "w+") as outFile:
            for line in inFile.readlines():
                total+=1
                os.system("cls")
                rand = (random.randrange(1000, 5000, 1))/1000.0
                fullURL=baseURL+line.strip()+"\n"
                print(f"trying {fullURL} ...")
                driver.get(fullURL)
                time.sleep(6)
                if "404 Not Found" in driver.page_source:
                    print(f"Doesn't exist, sleeping for {rand} seconds and trying the next one.")
                else:
                    found+=1
                    outFile.write(fullURL)
                time.sleep(rand)
            print(f"Searched {total} total URLs on {baseURL}.  Found {found} hits.")

    driver.close()

def searchVLkSysCheck():
    GenWordlist()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    random.seed(time.time())
    baseURL="https://deadrabbits.io/VLk_SYS_Check/"
    rand = (random.randrange(1000, 5000, 1))/1000.0

    total=0
    found=0
    with open("wordlist.txt", "r+") as inFile:
        with open("results.txt", "w+") as outFile:
            for line in inFile.readlines():
                total+=1
                os.system("cls")
                rand = (random.randrange(1000, 5000, 1))/1000.0
                fullURL=baseURL+line.strip()+"\n"
                print(f"trying {fullURL} ...")
                driver.get(fullURL)
                time.sleep(7)
                #print(len(driver.page_source))
                #print(hashlib.md5(driver.page_source.encode('utf-8')).hexdigest())
                if (len(driver.page_source)!=109902):
                    found+=1
                    outFile.write(fullURL)                    
                else:
                    print(f"Doesn't exist, sleeping for {rand} seconds and trying the next one.")

                time.sleep(rand)
            print(f"Searched {total} total URLs on {baseURL}.  Found {found} hits.")

    driver.close()

def searchZombieCircusGoats():
    GenWordlist()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    random.seed(time.time())
    baseURL="https://zombiecircusgoats.com//"
    rand = (random.randrange(1000, 5000, 1))/1000.0

    total=0
    found=0
    with open("wordlist.txt", "r+") as inFile:
        with open("results.txt", "w+") as outFile:
            for line in inFile.readlines():
                total+=1
                os.system("cls")
                rand = (random.randrange(1000, 5000, 1))/1000.0
                fullURL=baseURL+line.strip()+"\n"
                print(f"trying {fullURL} ...")
                driver.get(fullURL)
                time.sleep(6)
                if "Looks like you've found a page that no longer exists" in driver.page_source:
                    print(f"Doesn't exist, sleeping for {rand} seconds and trying the next one.")
                else:
                    found+=1
                    outFile.write(fullURL)
                time.sleep(rand)
            print(f"Searched {total} total URLs on {baseURL}.  Found {found} hits.")

    driver.close()

def checkBabelLength(numbers):
    totalNames=0
    with open ("wordlist.txt", "r+") as answersCheck:
        for _ in answersCheck.readlines():
            totalNames+=1

    totalNumbers=0
    for wall in numbers:
        if (wall < 1) or (wall > 4):
            continue
        for shelf in numbers:
            if (shelf < 1) or (shelf > 5):
                continue
            for volume in range(1,32):
                if (volume < 1) or (volume > 32):
                    continue
                for page in numbers:
                    if (page < 1) or (page > 410):
                        continue
                    totalNumbers+=1

    total=totalNames*totalNumbers
    if total>100000:
        choice=input(f"Total pages to check is {total}.  This may take a while, do you wish to continue? y/n: ")
        if choice=='y' or choice=='Y' or choice=='yes' or choice=='Yes':
            pass
        else:
            exit()



def getWord() -> str:
    word=input("Type the word you are searching for and hit enter: ")
    return word

def getNumbers() -> list:
    numbers=[]
    choice=input("Do you have specific numbers to guess at? y/n: ")
    if choice=='y' or choice=='Y' or choice=='yes' or choice=='Yes':
        while True:
            numberChoice=input("Type a number and press enter.  Type \"done\" when done: ")
            try: 
                if numberChoice=='d' or numberChoice=='done' or numberChoice=='Done' or numberChoice=='' or numberChoice=='\n':
                    break
                else:
                    numbers.append(int(numberChoice))
            except:
                print("There was an error reading your numbers.  Make sure you typed a valid number.")
                exit()
    else:
        for i in range (1,410):
            numbers.append(i)
    return numbers

def babelSearchWord2(hexName, numbers, word):
    for wall in numbers:
        if (wall < 1) or (wall > 4):
            continue
        for shelf in numbers:
            if (shelf < 1) or (shelf > 5):
                continue
            for volume in numbers:
                if (volume < 1) or (volume > 32):
                    continue
                wholeBook = (pybel.getbook(hexName.lower(), str(wall), str(shelf), str(volume))).split("\n\n")
                for page in numbers:
                    os.system("cls")
                    try:
                        print(f"Trying... HexName: {hexName.lower()}\n\nWall: {wall}\t\tShelf: {shelf}\tVolume: {volume}\tPage: {page}")
                        if word in wholeBook[page-1]:
                            print(f"{wholeBook[page-1]}\n")
                            input("Press Enter to continue...\n")
                    except:
                        print(f"ERROR:\tHexName: {hexName.lower()}\n\nWall: {wall}\t\tShelf: {shelf}\tVolume: {volume}\tPage: {page}")
                        continue

def babelSearchWord():
    word=getWord()
    numbers=getNumbers()
    choice=input("Do you have a specific hex name? y/n: ")
    if choice=='y' or choice=='Y' or choice=='yes' or choice=='Yes':
        hexName=input("Paste your hexname here and press enter: ")
        if len(hexName)>3260:
            print("Hexname is too long.  Goodbye.")
            exit()
        babelSearchWord2(hexName, numbers, word)
    else:
        if os.path.exists("wordlist.txt"):
            print("Taking hex names from answers.txt.")
            checkBabelLength(numbers)

            with open ("wordlist.txt", "r+") as possibleNames:
                for hexName in possibleNames.readlines():
                    hexName=((hexName.strip(",")).strip("\n")).strip()
                    babelSearchWord2(hexName, numbers, word)
        else:
            print("wordlist.txt doesn't exist.  Need to get hex names from somewhere.  Try making a wordlist first.")
            exit()

def babelSearchEnglish2(hexName, numbers):
    d=enchant.Dict("en_US")
    for wall in numbers:
        if (wall < 1) or (wall > 4):
            continue
        for shelf in numbers:
            if (shelf < 1) or (shelf > 5):
                continue
            for volume in numbers:
                if (volume < 1) or (volume > 32):
                    continue
                wholeBook = (pybel.getbook(hexName.lower(), str(wall), str(shelf), str(volume))).split("\n\n")
                for page in numbers:
                    os.system("cls")
                    try:
                        print(f"Trying... HexName: {hexName.lower()}\n\nWall: {wall}\t\tShelf: {shelf}\tVolume: {volume}\tPage: {page}")
                        for word in wholeBook[page-1].split():
                            if d.check(word):
                                print(f"{wholeBook[page-1]}\n")
                                input("Press Enter to continue...\n")
                                break
                    except:
                        print(f"ERROR:\tHexName: {hexName.lower()}\n\nWall: {wall}\t\tShelf: {shelf}\tVolume: {volume}\tPage: {page}")
                        continue

def babelSearchEnglish():
    numbers=getNumbers()
    choice=input("Do you have a specific hex name? y/n: ")
    if choice=='y' or choice=='Y' or choice=='yes' or choice=='Yes':
        hexName=input("Paste your hexname here and press enter: ")
        if len(hexName)>3260:
            print("Hexname is too long.  Goodbye.")
            exit()
        babelSearchEnglish2(hexName, numbers)
    else:
        if os.path.exists("wordlist.txt"):
            print("Taking hex names from answers.txt.")
            checkBabelLength(numbers)

            with open ("wordlist.txt", "r+") as possibleNames:
                for hexName in possibleNames.readlines():
                    hexName=((hexName.strip(",")).strip("\n")).strip()
                    babelSearchEnglish2(hexName, numbers)
        else:
            print("wordlist.txt doesn't exist.  Need to get hex names from somewhere.  Try making a wordlist first.")
            exit()

def babelSearchManual2(hexName, numbers):
    for wall in numbers:
        if (wall < 1) or (wall > 4):
            continue
        for shelf in numbers:
            if (shelf < 1) or (shelf > 5):
                continue
            for volume in numbers:
                if (volume < 1) or (volume > 32):
                    continue
                wholeBook = (pybel.getbook(hexName.lower(), str(wall), str(shelf), str(volume))).split("\n\n")
                for page in numbers:
                    os.system("cls")
                    try:
                        print(f"Trying... HexName: {hexName.lower()}\n\nWall: {wall}\t\tShelf: {shelf}\tVolume: {volume}\tPage: {page}")
                        print(f"{wholeBook[page-1]}\n")
                        input("Press Enter to continue...\n")
                        continue
                    except:
                        print(f"ERROR:\tHexName: {hexName.lower()}\n\nWall: {wall}\t\tShelf: {shelf}\tVolume: {volume}\tPage: {page}")
                        continue            

def babelSearchManual():
    numbers=getNumbers()
    choice=input("Do you have a specific hex name? y/n: ")
    if choice=='y' or choice=='Y' or choice=='yes' or choice=='Yes':
        hexName=input("Paste your hexname here and press enter: ")
        if len(hexName)>3260:
            print("Hexname is too long.  Goodbye.")
            exit()
        babelSearchManual2(hexName, numbers)
    else:
        if os.path.exists("wordlist.txt"):
            print("Taking hex names from answers.txt.")
            checkBabelLength(numbers)

            with open ("wordlist.txt", "r+") as possibleNames:
                for hexName in possibleNames.readlines():
                    hexName=((hexName.strip(",")).strip("\n")).strip()
                    babelSearchManual2(hexName, numbers)
        else:
            print("wordlist.txt doesn't exist.  Need to get hex names from somewhere.  Try making a wordlist first.")
            exit()