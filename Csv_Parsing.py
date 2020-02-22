"""
	Class that allows for taking in a csv 
"""
import csv
import datetime

class Csv_Parsing :
	"""docstring for ClassName"""
	def __init__(self):
		pass


	"""
		Function writes all the data points into a 
		Parameters:
			file - csv file being written into by the function
			data - a dictionary of the form {x_data_point : y_data_points}
			where x data set is string of date-time and y data set is the barametric pressure
			at a certain position in a string of lat and long
		Returns:
			returns a list of the order of variables and a 2d list of the data set 
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




csv_parser = Csv_Parsing()
print(csv_parser.read_csv_file("barometric_vs_time_data.csv"))
