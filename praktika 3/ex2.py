try:
  
    with open('kasutajad.txt', 'r') as file:
   
        users = file.readlines()

    
    for user in users:
        user = user.strip()  

        
        forbidden_chars = "!@#$%^&*()"

        
        if any(char in forbidden_chars for char in user):
            print(f"{user} – vigane kasutajanimi")  
        else:
            print(f"{user} – korrektne")  

except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"Error: An unexpected error occurred! {e}")
