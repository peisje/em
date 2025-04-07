class Patsient:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
        
class Arst:
    def __init__(self, nimi, vanus, eriala, aeg):
        self.nimi = nimi
        self.vanus =  vanus
        self.eriala = eriala
        self.aeg = aeg
       
class Record:
    def __init__(self, patsiendiNimi, arstiNimi, viisitiAeg):  
        self.patsiendiNimi = patsiendiNimi
        self.arstiNimi = arstiNimi
        self.viisitiAeg = viisitiAeg


class Haigla:
    def __init__(self):
        self.patsiendiList = []
        self.arstiList = []
        self.recordList = [] 
        
    def naitaPatsiendid(self):
        for index, elem in enumerate(self.patsiendiList):
            print(" id", index, " Patsienti nimi: ", elem.nimi, ' vanus: ', elem.vanus)


        
    def naitaArstid(self):
        for elem in self.arstiList:
            print("Arsti nimi: ", elem.nimi, ' vanus: ', elem.vanus, ' eriala: ', elem.eriala, ' aeg: ', elem.aeg)
            if len(elem.aeg)>0:
                print("Arsti kättesaadav aeg: ")
                for time in elem.aeg:
                    print(time)
                    
                    
    def naitaArst(self, arst):
        for elem in arst.aeg:
            print(elem)
                    
    def visitArst(self):
        sisestatudArstiNimi = input("sisesta arsti nimi: ")
        for elem in self.arstiList:
            if sisestatudArstiNimi == elem.nimi:
                self.naitaArst(elem)
                userInput = input("Milline aeg sulle sobib?")
                patsientInput = input("sisesta patsienti nimi: ")
                if userInput in elem.aeg:
                    elem.aeg.remove(userInput)
                    for elem2 in self.patsiendiList:
                        if elem2.nimi in patsientInput:
                            record = Record(patsientInput, sisestatudArstiNimi, userInput)
                            self.recordList.append(record)

                            print("record oli loodud")
                            print(self.recordList)
                else:
                    print('andmed oli lisatetud valesti')
                    
    def naitaRecords(self):
        for elem in self.recordList:
            print(f"Patsient: {elem.patsiendiNimi}, Arst: {elem.arstiNimi}, Aeg: {elem.viisitiAeg}")
    
   
pats1 = Patsient("igor", 17)
pats2 = Patsient("dasha", 16)
arst1 = Arst("allah", 1000, "kiirurg",['10:00', '10:30', '11:00', '11:30'])
arst2 = Arst("ahmed", 900, "kiirurgi-abi",['12:00', '12:30', '13:00', '13:30'])
haigla = Haigla()

haigla.patsiendiList.append(pats1)
haigla.patsiendiList.append(pats2)

haigla.arstiList.append(arst1)
haigla.arstiList.append(arst2)
haigla.naitaArstid()
haigla.visitArst()
haigla.naitaRecords()







