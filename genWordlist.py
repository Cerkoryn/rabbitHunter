clue1ans=["Da Tung"]
clue2ans=["Aurora Bridge", "bridge", "roof", "George Washington Bridge", "George Washington Memorial Bridge"]
clue3ans=["charm", "charm person", "cure wounds", "open sesame"]
clue4ans=["Holowan Labs"]
clue5ans=["Malindi"]
clue6ans=["Saruman, your staff is broken", "your staff is broken"]
clue7ans=["13", "9", "t", "n"]
clue8ans=["42", "f", "ft"]

def interateAnswers():
    with open("latestAnswers.txt", "w+") as file:
        for fullName in clue1ans:
            part1 = fullName.split()
            for part2 in clue2ans:
                for part3 in clue3ans:
                    for part4 in clue4ans:
                        for part5 in clue5ans:
                            for part6 in clue6ans:
                                for part7 in clue7ans:
                                    for part8 in clue8ans:
                                        file.write(f"{part1[0][0]}{part2[0]}{part3[0]}{part4[0]}{part5[0]}{part6[0]}{part7}{part8}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}{part4[0]}{part5[0]}{part6[0]}{part7}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}{part4[0]}{part5[0]}{part6[0]}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}{part4[0]}{part5[0]}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}{part4[0]}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}{part3[0]}\n")
                                        #file.write(f"{part1[1][0]}{part2[0]}\n")
                                        #file.write(f"{part1[1][0]}\n")

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
                                            #file.write(tmpline)
                                        for splitPart2 in part2.split():
                                            line+=splitPart2[0]
                                                #tmpline=line+"\n"
                                                #file.write(tmpline)
                                        for splitPart3 in part3.split():
                                            line+=splitPart3[0]
                                                #tmpline=line+"\n"
                                                #file.write(tmpline)
                                        for splitPart4 in part4.split():
                                            line+=splitPart4[0]
                                                #tmpline=line+"\n"
                                                #file.write(tmpline)
                                        for splitPart5 in part5.split():
                                            line+=splitPart5[0]
                                                #tmpline=line+"\n"
                                                #file.write(tmpline)
                                        for splitPart6 in part6.split():
                                            line+=splitPart6[0]
                                                #tmpline=line+"\n"
                                                #file.write(tmpline)
                                        line+=part7
                                            #tmpline=line+"\n"
                                            #file.write(tmpline)
                                        line+=part8
                                        tmpline=line+"\n"
                                        file.write(tmpline)

interateAnswers()