#Python Datetime

import datetime

x = datetime.datetime.now() # return, 2023-04-03 10:16:32.402493
print(x)
print(type(x))
print(x.strftime("%A")) #hari

# creating data objecst
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%d/%m/%Y")) 

# example
import datetime

dt_now = datetime.datetime.now()
print(dt_now)
print(dt_now.strftime("%d/%m/%Y"))

arr_1 = [5, 78, 2, 0]
assert(min(arr_1)) == 0 # nilai terkecil
assert(max(arr_1)) == 78 # nilai terbesar

# function 5 pangkat 5
assert(pow(5, 5)) == 3125 # hasil nilai berpangkat (pangkat)

# Python try except

#1
try:
    print(x)
except:
    print("An exception occurred")

#2
try:
    print(x)
except NameError:
    print('Variable x is not defined')
except:
    print("Something else went wrong")

#3
try:
    print("Hello Wolrd")
except:
    print("Something went wrong")
else:
    print("Somenthing went wrong")


try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# Raise an exception



# Finally

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

print("=================================")
# Python JSON

import json
#somw JSON:
x = '{"name":"John", "age":30, "city":"New York"}'
#PARSE X:
y = json.loads(x)
#the result is a python dictionary:
print(y["age"])


import json

# a Python object (dict):
x = {
    "name": "Jhon",
    "age": 30,
    "city": "New York"
}
 # convert into JSON:
y = json.dumps(x)

#the result is a JSON string:
print(y)

a = {
    "name": "Jhon",
    "age": 30
}

print('DICT: ', x)
print(type(x))
print(x["age"])

print('DICT: ', y)
print(type(y))

print("======================")

# Python File Handling


f = open("demofile2.txt", 'a')
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", 'r')
print(f.read())

#Delete a file
#ex
import os
os.remove("demofile.txt")

#1 open file & read
f = open('./jhon_read.txt')

json_string = f.read()

print(json_string)

