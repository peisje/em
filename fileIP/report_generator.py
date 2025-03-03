def generate_report(data):
    ip_count = data[0]
    error_counts = data[1]
    with open("report.txt", "w") as file:
        file.write("loogiamalüüs raport \n")
        file.write("kõige aktivsem ip oli: \n")
        for ip, count in ip_count.items():
            file.write(f"{ip}: {count} korda \n"  )
            
    with open("report.txt", "a") as file:
        
        file.write("loogiamalüüs raport \n")
        file.write("kõige aktivsem ip oli: \n")
        for error, count in error_counts.items():
            file.write(f"{error}: {count} korda \n"  )