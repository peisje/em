import datetime
print(datetime.datetime.now())

def TegevusBook():
    name = input("sinu nimi: ")
    tegevus  = input("sinu tegevus: ")
    time = datetime.datetime.now()
    text = f"Date: {time}, Nimi: {name}, Tegevus:  {tegevus}\n"
    file = open("TegevusBook.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("tegevus oli salvestatu edukalt")
  



