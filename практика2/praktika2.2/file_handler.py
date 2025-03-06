def load_data(): 
    try:
        with open("grades.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def append_data(data): 
    with open("grades.txt", "a", encoding="utf-8") as f:
        f.writelines(data)



