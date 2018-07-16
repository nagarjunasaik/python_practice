import csv

def getData(fileobj):
	csv_reader = csv.DictReader(fileobj, delimiter=',')
	
	for dic in csv_reader:
		#print(dic)
		for i in range(len(dic)):
		print('person {}'.(format(i)))
		print(dic['Name'])
		print(dic['Class'])
		print(dic['Phno'])
		print(dic['address'])
		print(50*'-')



if __name__ == '__main__':
	fileobj = open('details.csv','r')
	getData(fileobj)