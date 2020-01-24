#---- To console log its no longer console log but print ----#

print('hello world')

#---- in the console type 'python3 intro.py' to see results ----#

#---- Variables ----#
variable = 'Hello world'

print(variable)

#---- Lists [] (basically arrays) and Dictionaries {} (basically objects) ----#


#---- If/ else ----#
name = 'Sam'

#----- Python always cares about the type of the variable i.e. string or value ----#
if name == "Sam":
    print ('Great Name')
elif name == 'Jacob':
    print('Great Guy')
else:
    print('oh dear')

#---- for loops ----#
for i in range (5):
    print(i)

for i in ['Sam', 'Jacob', 'Dean', 'Dan']:
    print(i)

my_list = []

#---- non indented loop ----#
for i in range (5):
    my_list.append(i)

print (my_list)

#---- indented loop ----#
#---- Append is the python way of push ----#
for i in range (5):
    my_list.append(i)
    print (my_list)

#---- Functions ----#
def my_func(a_string):
    print(a_string)
my_func ('hello')

def my_func(a_string):
    return a_string
print(my_func('hello'))

#---- libraries are prewritten code ----#
import math
print(math.tau)
print(math.pow(5, 3))

import random
print(random.randint(5,10))