import file_handler as file

def add_note(title, text):
    note = f"Pealkiri: {title}\nTekst: {text}"
    file.append_note(note)
    print("Märge lisatud!")

def view_notes():
    notes = file.read_notes()
    if not notes:
        print("Märkmeid ei leitud.")
    else:
        print("\nMärkmed:")
        for note in notes:
            print(note + "\n")

def delete_note(title):
    file.delete_note_by_title(title)
    print(f"Märge pealkirjaga '{title}' kustutatud.")
