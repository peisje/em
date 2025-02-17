import sonastik as myDictionary
import tuples as myTuples
# opilane = {
#     #key     value
#     'nimi': "thomas",
#     'vanus': 18,
#     'klass': "12A"
# }

# # print(opilane['nimi'])
# # print(opilane.get('vanus'))

# # print(opilane.values())
# # print(opilane.keys())

# opilane["adress"] = "Tallinn" #add element by key
# # opilane.pop('nimi') #delete element by key
# # #another variant
# # del opilane['klass']

# print(opilane.values()) #result is list []
# print(opilane.keys())  #result is list []

# #for i in range(len(opilane)):
#     #print(opilane[i])

# for elem in opilane.keys():
#     print(opilane[elem])

# # for elem in opilane.keys():
# #     print(elem)

# # for elem in opilane.values():
# #     print(elem)

# for key, value in opilane.items():
#     print('see on võtti', key,'see on värtus', value)

grades = {
    "mari": [4,5,3,4],
    "jaan": [2,3,2,3,3],
    "thomas": [3,2,4]
}
#ex1
result = myDictionary.arvutaKeskmineHinne(grades)
print(result)
#ex2
word = "koodimine"
result2 = myDictionary.tahemargede_sagedus(word)
print(result2)






# tuples
tuple = (2,4,5)
print(tuple)
tuple2 = "oun", "pirn", "ploom"
print(tuple2)
print(tuple2[2])

#naide
andmed = (10, 15, 20, 25, 30, 35)
tulemus = myTuples.filtreeri_arvud(andmed)
print(tulemus)

#naide
andmed = ("Õun", "banaan", "apelsin", "viinamari")
result3 = myTuples.find_index(andmed, "apelsin")
print(result3)

