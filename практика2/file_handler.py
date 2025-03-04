import os

def read_notes(file_name="notes.txt"):
    if not os.path.exists(file_name):
        return []
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().strip().split("---\n")

def write_notes(notes, file_name="notes.txt"):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("---\n".join(notes) + "\n" if notes else "")

def append_note(note, file_name="notes.txt"):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(note + "\n---\n")

def delete_note_by_title(title, file_name="notes.txt"):
    notes = read_notes(file_name)
    new_notes = [note for note in notes if not note.startswith(f"Pealkiri: {title}")]
    write_notes(new_notes, file_name)