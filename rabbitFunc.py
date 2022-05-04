import os

def GenWordlist():
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

    print("Elminating duplicates...")
    with open("tmpFile.txt", "r+") as tmpFile:
        with open("wordlist.txt", "w+") as wordlistFile:
            tmp=set()
            for line in tmpFile:
                if line not in tmp:
                    wordlistFile.write(line)
                    tmp.add(line)
    
    os.remove("tmpfile.txt")
    print("Wrote wordlist to wordlist.txt.")

