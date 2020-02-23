import matplotlib.pyplot as mpl


"""
    x_axis = string of the first three from the keys 
    y_axis = multiple strings from the values of the dict, that will be taken in as a list of strings 
"""


def listAdd(XVal, YVal, DatasetTuple, ExistingData):
    XList=[]
    XPos =0
    YPos =3
    VarList = DatasetTuple[0]
    DataBlck = DatasetTuple[1]
    for i in range(3):
        if XVal == VarList[i]:
            XPos = i
    for i in range(len(VarList)):
        print (len(VarList))
        if YVal == VarList[i]:  
            YPos = i
    for i in range(len(DataBlck)):
        print(i)
        print( DataBlck[i][XPos])
        if not(DataBlck[i][XPos] in XList):
            XList.append(DataBlck[i][XPos])
    for i in range(len(DataBlck)):
        print(i)
        print(DataBlck[i][YPos])
        ExistingData.append(DataBlck[i][YPos])
   
    mpl.plot(XList, ExistingData)
    mpl.ylabel(YVal)
    mpl.xlabel(XVal)
    mpl.show()
    return ExistingData



if __name__ == "__main__":
    Data = (['Date', 'Model', 'Location', 'Barometric Pressure', 'Test1'], [['20 21 2020','Smangsmug', '-33,22', '1000', 'TEST A'], ['20 21 2020','Smangsmug', '-33,20', '3000', 'TEST B'], ['20 21 2020', 'ePhone', '-33,18', '2800', 'TEST C'], ['20 21 2020','Smol', '-34,27', '1200', 'TEST D']])
    ExistingData =[]
    while 1:
        a = input("Gib X Parameter, plz: ") 
        print("Thank.")
        b = input("Gib Y Parameter, plz: ")  
        print("Thank.")
        ExistingData = listAdd(a,b,Data, ExistingData)