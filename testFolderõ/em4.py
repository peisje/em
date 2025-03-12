# myList = [5,4,3]
# print(myList[5])

try:
    myList = [5,4,3]
    print(myList[2])
    x=10
    x/0
except IndexError:
    print("Viga: pandnud indexid")
except ZeroDivisionError:
    print("Viga: me ei sa jagad nuliks")
except ValueError:
    print("Viga: me ei sa jagad nuliks")
finally:
     print("Programm lõpetab oma töö")
 