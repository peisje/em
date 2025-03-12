logid = [
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Server käivati"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Kasutaja sisselogimine edukas"},
  {"aeg": "2025-03-10", "tüüp": "error", "sõnum": "Andmebaasi ühenduse viga"},
  {"aeg": "2025-03-10", "tüüp": "warn", "sõnum": "Mälu kasutus ületab piirangut"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Serveris tehtud uuendus"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Taustaprotsess käivitati"},
  {"aeg": "2025-03-10", "tüüp": "error", "sõnum": "Võrguprobleem, ühendus katkestatud"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Kasutaja väljalogimine edukas"},
  {"aeg": "2025-03-10", "tüüp": "warn", "sõnum": "Kasutaja õigused piiratud"},
  {"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Logimine lõpetatud"}
]
print(logid[0]["aeg"])
print(logid[0]["tüüp"])
print(logid[-1])


   
   
def errorCount(data):
    errorCount = 0  
    for elem in range(0, len(data)): 
        if data[elem]["tüüp"] == "error":  
            errorCount += 1  
    return {"error": errorCount}  


error_result = errorCount(logid)
#print(error_result)

def warningCount(data):
    warnCount = 0  
    for elem in range(0, len(data)): 
        if data[elem]["tüüp"] == "warn":  
            warnCount += 1  
    return {"warn": warnCount}  

warn_result = warningCount(logid)
#print(warn_result) 
    
def infoCount(data):
    infoCount = 0  
    for elem in range(0, len(data)):  
        if data[elem]["tüüp"] == "info":  
            infoCount += 1  
    return {"info": infoCount}  
info_result = infoCount(logid)
#print(info_result)
    
    
myList = [errorCount(logid),warningCount(logid),infoCount(logid)]
print(myList)   
   #or   
# 
# for elem in logid:
#     print(elem['tüüp'])
    

    