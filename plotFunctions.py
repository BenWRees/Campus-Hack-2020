import matplotlib.pyplot as mpl


"""
    x_axis = string of the first three from the keys 
    y_axis = multiple strings from the values of the dict, that will be taken in as a list of strings 
"""


def listAdd(XVal, YVal, DatasetTuple, XList, YList):
    XPos =0
    YPos =3
    VarList = DatasetTuple[0]
    DataBlck = DatasetTuple[1]
    for i in range(3):
        if XVal == VarList[i]:
            XPos = i
    for i in range(len(VarList)):
        if YVal == VarList[i]:  
            YPos = i
    for i in range(len(DataBlck)):
        
        if not(DataBlck[i][XPos] in XList):
            XList.append(DataBlck[i][XPos])
            YList.append(DataBlck[i][YPos])
       
    mpl.plot(XList, YList)
    mpl.ylabel(YVal)
    mpl.xlabel(XVal)
    mpl.show()
    return XList,YList



if __name__ == "__main__":
    Data = (['Date', 'Model', 'Location', 'Barometric Pressure', 'Test1'], [['20 21 2020 1PM','Smangsmug', '-33,22', '1000', 'TEST A'], ['20 21 2020 2PM','Smangsmug', '-33,20', '3000', 'TEST B'], ['20 21 2020 3PM', 'ePhone', '-33,18', '2800', 'TEST C'], ['20 21 2020 4PM','Smol', '-34,27', '1200', 'TEST D']])
    ExistingData=([],[])
    while 1:
        a = input("Gib X Parameter, plz: ")
        print("Thank.")
        b = input("Gib Y Parameter, plz: ")  
        print("Thank.")
        ExistingData = listAdd(a,b,Data, ExistingData[0], ExistingData[1])
        c = input("Gib X Parameter, plz: ")
        print("Thank.")
        d = input("Gib Y Parameter, plz: ")
        print("Thank.")
        ExistingData = listAdd(a,b,Data, ExistingData[0], ExistingData[1])
        if (a != c or b !=d):
            ExistingData=([],[])
         
