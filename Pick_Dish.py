from DataStructure import tags_map, Dish


#creating some data for testing
'''
data = [
		['1', 'clam noodle', 'Joy kitchen', 'main02'],
		['2', 'fried rice', 'Joy kitchen', 'main01'],
		['3', 'steam dumpling', 'Joy kitchen', 'main03']
		]
'''

temp_1 = Dish('1', 'clam noodle', 'Joy kitchen', 'main02')
temp_2 = Dish('2', 'fried rice', 'Joy kitchen', 'main01')
temp_3 = Dish('3', 'steam dumpling', 'Joy kitchen', 'main03')
#initialize the big list
data = []
data.append(temp_1)
data.append(temp_2)
data.append(temp_3)


#To see if data stores things correctly
for i in range(len(data)):
	print(data[i])

input_tags = ['main01', 'main03']

#Store all output into a huge list
output = []

for i in range(len(data)):
	for index in range(len(input_tags)):			#run through every data 
		if data[i].hasTag(input_tags[index]):
			output.append(data[i])
			break


#To see if output list stores the correct data
for i in range(len(output)):
	print(output[i])
