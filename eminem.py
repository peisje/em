muusika_andmebaas = [
    {"id":1, "artist": 'Eminem', "title":"The real slim shady"},
    {"id":2, "artist": 'NOEP',"title":"On my Way"},
    {"id":3, "artist": 'Karl-Erik Taukar',"title":"seitse pühapaeva"}
]

print(muusika_andmebaas[0]["title"])

def otsi_muusikat(par):
    result = []
    for muusika in muusika_andmebaas:
        if par in muusika["title"] or par in muusika["artist"]:
            result.append(muusika)
            
            
    if result:
        for muusika in result:
            print(muusika['artist'], muusika['title'])
    return result

# userInput = otsi_muusikat(input("sisesta muusikat"))
# print(userInput)

hinded = {
    "Mari": {
        "matemaatika": [4, 5, 3],
        "eesti keel": [5, 4],
        "keemia": [3]
    },
    "Jüri": {
        "matemaatika": [2, 3],
        "eesti keel": [3],
        "keemia": [4, 4, 5]
    },
    "Anna": {
        "matemaatika": [5, 5],
        "eesti keel": [5],
        "keemia": [5, 5]
    }
}

# print(hinded["Mari"]["matemaatika"][-1])
for person in hinded:
    keskmine = 0
    tulemus = 0
    count = 0
    for aine in hinded[person]:
        for hind in hinded[person][aine]:
            tulemus = tulemus + hind
            count += 1
    keskmine = tulemus / count

    print(person,keskmine)
