fullString=""
with open("finalEmailROT13.txt", "r+") as file:
    for line in file.readlines():
        tmpLine=line.strip()+"@protonmail.com; \n"
        fullString+=tmpLine

with open("allROT13Emails.txt", "w+") as outFile:
    outFile.write(fullString)