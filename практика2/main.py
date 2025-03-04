import file_handler as file
import notes_manager as notes

def main():
    while True:
        print("Märkmete haldur")
        print("1. Lisa märge")
        print("2. Vaata märkmeid")
        print("3. Kustuta märge")
        print("4. Välju")
        
        choice = input("Vali toiming: ")
        
        if choice == "1":
            title = input("Sisesta pealkiri: ")
            text = input("Sisesta tekst: ")
            notes.add_note(title, text)
        elif choice == "2":
            notes.view_notes()
        elif choice == "3":
            title = input("Sisesta pealkiri, mida kustutada: ")
            notes.delete_note(title)
        elif choice == "4":
            print("Programmist väljumine...")
            break
        else:
            print("Vale valik, proovi uuesti.")

if __name__ == "__main__":
    main()
