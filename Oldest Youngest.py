#Oldest Youngest
#Daniel Seix
#09/03/2022

names=[]
ageList=[]

def getInputs():
        for counter in range(0,10):
            firstName=input("What is their first name? ")
            names.append(firstName)
            age=int(input("Please enter their age "))
            ageList.append(age)
        return names,ageList

def calcOldest(ageList):
        #find oldest
        oldest=ageList[0]
        oldestName=names[0]
        for counter in range(1,len(ageList)):
            if ageList[counter]>oldest:
                oldest=ageList[counter]
                oldestName=names[counter]
        return oldest,oldestName

def calcYoungest(ageList):
        #find youngest 
        youngest=ageList[0]
        youngestName=names[0]
        for counter in range(1,len(ageList)):
            if ageList[counter]<youngest:
                youngest=ageList[counter]
                youngestName=names[counter]
        return youngest,youngestName

def displayOutputs(oldest,oldestName,youngest,youngestName):
        print("The youngest person is",youngestName,"They are",youngest,"years old")
        print("The oldest person is",oldestName,"They are",oldest,"years old")

#main
names,ageList=getInputs()
oldest,oldestName=calcOldest(ageList)
youngest,youngestName=calcYoungest(ageList)
displayOutputs(oldest,oldestName,youngest,youngestName)
