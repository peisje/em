"""
file = open("myFile.txt", "w")
file.write("myText")
file.close()
"""


import bookCreator as bookCreator
import tegevusGuest as tegevusGuest
import filereader as filereader
import managment as managment


def main():
    print("1 - külalisteraamat")
    print("2 -  luua tegevus")
    print("3 -  lugeda faili")
    print("4 - managment id sustem")
    userInput = input("sinu valik: ")
    if userInput == "1":
        bookCreator.guestBook()
    elif userInput == "2":
        tegevusGuest.TegevusBook()
    elif userInput == "3":
        userFile = input("Milline file sa tahad lugeda: ")
        filereader.readFile(userFile)
    elif userInput == "4":
        i = 0
        i = i + 1
        managment.managmentId()
    else:
        print("vale valik")
        
            
main()