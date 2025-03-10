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

for elem in range(0,len(logid)):
    print(logid[elem]['tüüp'])
    if logid[elem]['tüüp'] == "Info":
        infoCount = infoCount + 1
        
print(infoCount)
    
   
   #or   
# 
# for elem in logid:
#     print(elem['tüüp'])
    

    