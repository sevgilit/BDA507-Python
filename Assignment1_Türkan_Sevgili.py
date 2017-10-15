##Tasks #1: area of a triangle
height=6
base=10
area = (height * base)/2
print(area) #30

##Tasks #2: geneSequence
listy_geneSequence = list("AATCGGCATGCCGAATTTCCGCTATGTTGCATGCATCGTACGATGCATATGCATAGAGGxGCTTTTAACGATGCCCGATGATTTCATGCCCGTAACGACTCTGACGTACTG")
print(listy_geneSequence)

count_A=listy_geneSequence.count("A")
print(count_A) #26
count_C=listy_geneSequence.count("C")
print(count_C) #27
count_T=listy_geneSequence.count("T")
print(count_T) #31
count_G=listy_geneSequence.count("G")
print(count_G) #26

count_geneSequence=len(listy_geneSequence)
print(count_geneSequence) #111

print(count_A+count_C+count_T+count_G==count_geneSequence) #False

index_x = listy_geneSequence.index("x")
print(index_x) #59

listy_geneSequence.pop(index_x)
print(listy_geneSequence)

##Tasks #3: nameList

nameList = ["Utku", "Aynur", "Tarik", "Aktan", "Asli", "Ahmet", "Metin", "Funda", "Kemal", "Hayko", "Zelal", "Kenan", "Asli", "Atakan", "Umut"]
print(nameList)

print("Aktan" in nameList) #True

print("Ezgi" in nameList) #False

print("Total number of students:", len(nameList)) #Total number of students: 15

nameList.append("Yahya")
print(nameList)

nameList.remove("Ahmet")
print(nameList)

nameList.sort(key=None, reverse=False)
print(nameList)

print(nameList[-1]) #Zelal


##Tasks #4: Compare Listx1 and Listx2 if they have the same content

Listx1 = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(Listx1)
Listx2 = ("w", 3, "e", "r", "e", "s", "o", "u", "r", "c")
print(Listx1)

print (Listx1 == Listx2) #False

print(sorted(Listx1))
print(sorted(Listx2))

print("Compare: " ,sorted(Listx1) == sorted(Listx2)) #True

##Tasks #5: highest value, lowest value, average value,range, count of numbers of listx

listx=[5, 10, 3, 25, 7, 4, 15, 13, 8, 4, 6]
print(listx)


max_value = max(listx)
print(max_value) #25

min_value = min(listx)
print(min_value) #3


average=sum(listx)/len(listx)
print(average) #9

range=max(listx)-min(listx)
print(range) #22


print("Length:", len(listx)) #Length: 11
