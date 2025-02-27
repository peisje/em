def guestBook():
    name = input("sinu nimi: ")
    comment  = input("sinu sõnum: ")
    text = f"Nimi: {name}, Sõnum:  {comment}\n"
    file = open("guestBook.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("sõnum oli salvestatu edukalt")