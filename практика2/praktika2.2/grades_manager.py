import file_handler as fh

def add_grade():
    name = input("Name: ")
    grades = input("Grades: ")
    fh.append_data([f"Name: {name}\nGrades: {grades}\n---\n"])
    print("Student added successfully!")

def show_grades():
    data = fh.load_data()
    if data:
        print("".join(data))
    else:
        print("No student data available.")

def avg_grade():
    name = input("Enter the student's name to calculate the average grade: ")
    lines = fh.load_data()
    for i in range(len(lines)):
        if lines[i].startswith(f"Name: {name}"):
            grades = [int(g) for g in lines[i + 1].replace("Grades: ", "").split(", ")]
            avg = sum(grades) / len(grades)
            print(f"Average grade for {name}: {avg}")
            break
    else:
        print(f"{name} not found!")


def search_student():
    name = input("Enter the name to search for: ")
    lines = fh.load_data()
    found = False
    for i in range(len(lines)):
        if lines[i].startswith(f"Name: {name}"):
            print(f"{lines[i]}\n{lines[i + 1]}")
            found = True
            break
    if not found:
        print(f"{name} not found!")

