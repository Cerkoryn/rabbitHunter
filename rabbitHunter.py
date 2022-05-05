from rabbitFunc import *
import os

banner="""
----------------------------------------------------------------------------------
Rabbit hunter will help you find Yamarashi by trying a lot of answers VERY quickly.

Make sure to put all your answers in answers.txt separated by a comma.  
Line 1 has answers to Riddle 1, line two has answers to Riddle 2, etc.

HIGHLY RECOMMEND USING A VPN SO YOU DON'T GET YOUR IP BLOCKED!!!
---------------------------------------------------------------------------------"""

mainMenu="""
What would you like to try your answers against?

Looking for hidden web pages:
1) https://drive.protonmail.com/urls/<AnswerGoesHere>
2) https://deadrabbits.io/<AnswerGoesHere>
3) https://deadrabbits.io/VLk_SYS_Check/<AnswerGoesHere>
4) https://zombiecircusgoats.com/<AnswerGoesHere>

Library of Babel:
5) I have a specific word or string I'd like to search for with a set of given hex names/numbers.
6) Look for any English words in a set of Hex names/numbers.
7) Manually check many pages quickly with a set of given hex names/numbers.

Other:
8) Output a list of emails in the format <AnswerGoesHere>@protonmail.com;
9) I just want a to make a new wordlist.

0) Exit.
"""

if __name__ == "__main__":
    while True:
        os.system("cls")
        print(banner)
        print(mainMenu)
        choice=0
        while True:
            try:
                choice=int(input("Enter choice: "))
                break
            except:
                print("That's not a valid option.")

        if choice == 1:
            os.system("cls")
            searchProtonDrive()
            print("Goodbye.")
            exit()

        elif choice == 2:
            os.system("cls")
            searchDeadRabbitsIO()
            print("Goodbye.")
            exit()

        elif choice == 3:
            os.system("cls")
            searchVLkSysCheck()
            print("Goodbye.")
            exit()

        elif choice == 4:
            os.system("cls")
            searchZombieCircusGoats()
            print("Goodbye.")
            exit()

        elif choice == 5:
            os.system("cls")
            babelSearchWord()
            print("Goodbye.")
            exit()

        elif choice == 6:
            os.system("cls")
            babelSearchEnglish()
            print("Goodbye.")
            exit()

        elif choice == 7:
            os.system("cls")
            babelSearchManual()
            print("Goodbye.")
            exit()

        elif choice == 8:
            os.system("cls")
            genEmails()
            print("Goodbye.")
            exit()

        elif choice == 9:
            os.system("cls")
            GenWordlist()
            print("Goodbye.")
            exit()

        elif choice == 0:
            print("Goodbye.")
            exit()

        else:
            print("That's not a valid option.")