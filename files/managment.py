def managmentId():
    idcount = int(input("kui palju sa tahad sisetada"))
    for i in range(idcount):
        
        name = input("sinu nimi: ")
        age  = input("sinu vanus: ")
        text = (f"ID: {i} Nimi: {name}, Vanus:  {age}\n")
        file = open("managmentId.txt", "a", encoding="utf-8")
        file.write(text)
        file.close()
    print("nimi ja vanus oli salvestatu edukalt")