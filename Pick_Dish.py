#input tags
List = ['apple', 'Joy kitchen', 'fruit']

#run through every dishes and print the line when the certain tag is included.

class Item:
 def __init__(self, Dish, Restaurant, tag):
  self.a = Dish
  self.b = Restaurant 
  self.c = tag
 
 def hasTag(self, temp):
   if temp in self.c:
    print(self.a + '   ' + self.b + "\n")
   else:
    print('You eat nothing tonight heehee')
  
 
 
