"""
	Class that allows for taking in a csv 
"""
import csv
import datetime
import time
import matplotlib.pyplot as mpl

class Csv_Parsing :
        data_set = []
        def __init__(self):
                pass
        
        def listAdd(self,XVal, YVal, DatasetTuple, XList, YList):
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
        
        def read_csv_file(self,file):
                Listt=([0],[0])
                with open(file) as csv_file:		
                        csv_reader = csv.reader(csv_file, delimiter=',')
                        label_names = []
                        data_set = []
                        line_count = 0
                        for row in csv_reader:
                                if line_count == 0 :
                                        #creates a list of all the y-value names 
                                        label_names = row
                                        print(row)
                                        line_count += 1
                        else :	
                                data_set = row
                                print(row)
                                line_count += 1
                        
                        Listt=self.listAdd('Date','Barometric Pressure',(label_names, data_set),Listt[0],Listt[1])
                        #return label_names, data_set
        """
        def read_csv_file(self,file) :
                data_set = []
                with open(file) as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',')
                        label_names = []
                        line_count = 0
                        for row in csv_reader:

                                if line_count == 0 :
                                        #creates a list of all the y-value names 
                                        label_names = row
                                        line_count += 1
                                if line_count != 0 :
                                        data_set.append(row)
                                        line_count += 1
                return label_names, data_set
        """

if __name__ == "__main__":
        while 1:
                file = "data.csv"
                csv_penis = Csv_Parsing()
                csv_penis.read_csv_file(file)
                time.sleep(10000)
