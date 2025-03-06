def copy_grades():
    try:
        with open("grades.txt", "r", encoding="utf-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        print("grades.txt file not found!")
        return
    with open("grades2.txt", "w", encoding="utf-8") as file:
        file.writelines(data)

    print("Data has been copied to grades2.txt.")

            
        
        
    
    