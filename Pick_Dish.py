#input tags
List = ['apple', 'Joy kitchen', 'fruit']

#run through every dishes and print the line when the certain tag is included.

class Item:
 def __init__(self, Dish, Restaurant, tag):
  self.a = Dish
  self.b = Restaurant 
  self.c = tag
 
 def hasTag(self, temp):
  n = len(temp)
  i = 0
  while i < n:
   if temp[i] in self.c:
    print(self.a + '   ' + self.b + "\n")
    break
   else:
    print('You eat nothing tonight heehee')
   i = i + 1
  
 
#reading from input
list = []

# number of elements as input
#n = input("Enter how many tags u r gonna type: ")

#iterating till the end, could only read two tags for now
for i in range (0, 2):
 temp = input()
 list.append(temp)
 
#creating some data for testing
Apple = Item('apple', 'Joy kitchen', 'fruit')
Banana = Item('banana', 'Joy kitchen', 'fruit')

Apple.hasTag('fruit')
input_tags = ['fruit', 'rice']
Banana.hasTag(input_tags)

print(list)
Apple.hasTag(list)
Banana.hasTag(list)
