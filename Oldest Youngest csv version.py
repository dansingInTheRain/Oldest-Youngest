#Oldest Youngest
#Daniel Seix
#09/03/2022

import csv

names=[]
ageList=[]

def getInputs():
        f=open("namesandages.csv")
        csvFile=csv.reader(f)
        for row in csvFile:
                names.append(row[0])
                ageList.append(row[1])
        f.close()
        return names,ageList

def calcOldest(ageList):
        #find oldest
        oldest=ageList[0]
        for counter in range(1,len(ageList)):
            if ageList[counter]>oldest:
                oldest=ageList[counter]
                oldestName=names[counter]
        return oldest,oldestName

def calcYoungest(ageList):
        #find youngest 
        youngest=ageList[0]
        for counter in range(1,len(ageList)):
            if ageList[counter]<youngest:
                youngest=ageList[counter]
                youngestName=names[counter]
        return youngest,youngestName

def displayOutputs(oldest,oldestName,youngest,youngestName):
        print("The youngest person is",youngestName,"who is",youngest,"years old")
        print("The oldest person is",oldestName,"who is",oldest,"years old")
        f=open("oldestyoungest.txt","w")
        f.write("The youngest person is"+" "+youngestName+" "+"who is"+" "+youngest+" "+"years old"+" ")
        f.write("The oldest person is"+" "+oldestName+" "+"who is"+" "+oldest+" "+"years old")
        f.close()

#main
names,ageList=getInputs()
oldest,oldestName=calcOldest(ageList)
youngest,youngestName=calcYoungest(ageList)
displayOutputs(oldest,oldestName,youngest,youngestName)
