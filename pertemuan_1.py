print("Hello World!")
#ini comment

x, y, z = "Banana", "Orange", "Apple"
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 6
print(x + y)
#(+) dalam angka berfungsi sama dengan operasi matematika

x = 5
y = "John"
print(type(x))
print(type(y))

#LOOPING TROUGTH STRING, teks ke bawah
for x in "Banana":
    print(x)

#(len) berfungsi untuk mengecek panjang dari string (STRING HEIGHT)
a = "hello, word"
print(len(a))

txt = "The best thing in life are free!"
print("free" in txt)

txt = "The best thing in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")

txt = "The best thing in life are free!"
print("expensive" not in txt)

#MODIFY STRING
#upper
a = "Hello, World!"
print(a.upper()) #kapital semua, returns, HELLO, WORLD!

#strip
a = "Hello, World!"
print(a.strip()) #returns, Hello World!

#split
a = "Hello, World!"
print(a.split()) #returns, ['Hello,', 'World!']

#lower
a = "Hello, World!"
print(a.lower()) #retuns, hello, world!

#replace
a = "Hello, World!"
print(a.replace("H", "J"))

print('Hello')
print("World") #('...') dan ("...") is the same

#EXAMPLE, ASSIGN STRING TO A VARIABLE
a = "Hello"
print(a)

#STRING ARE ARRAYS
a = "Hello, World!"
print(a[1])

a = "Hello, World!"
print(a[2])

a = "Hello, World!"
print(a[0])


#example
#1
def sum_int_or_str(a, b):
    return int(a) + int(b)

assert(sum_int_or_str(1, '2')) == 3

#2
def get_second_caracter(a):
    if len(a) > 1:
        return a[1]
    else:
        return 0

assert (get_second_caracter("ab")) == "b"
assert (get_second_caracter("a")) == 0

#3
car = {
    'brand': 'Toyota',
    'year': 2022
}

assert (car['brand']) == 'Toyota'

#4
cars =  [
    {
        'brand': 'Toyota'
    },
    {
        'brand': 'Honda',
        'products': [
            'civic'
        ]
    }
]
assert(cars[1]['products'][0]) == 'civic'

#5
raw_cars = 'toyota,honda,indiacar'
assert(raw_cars.split(',')) == ['toyota', 'honda', 'indiacar'] # turn raw_cars into a list

#6
raw_cars = raw_cars.upper()
assert(raw_cars.split(',')) == ['TOYOTA','HONDA','INDIACAR']

#STUDY CASE
raw_cars = "toyota,honda,indiacar,indiacar,indiacar"
raw_cars = raw_cars.split(',')
raw_cars = set(raw_cars)
raw_cars = len(raw_cars)
assert(raw_cars) == 3

print("Hello, World!")
print(a[1])

print("Hello, World!")
print(a[2])

print("Hello, World!")
print(a[0])

#TYPE DATA PYTHON

#Python memiliki tipe data bawaan berikut secara default, dalam kategori ini:

#Jenis Teks:	str
#Jenis Numerik:	int, float, complex
#Jenis urutan:	list, tuple, range
#Jenis Pemetaan:	dict
#Tipe Setel:	set,frozenset
#Tipe Boolean:	bool
#Jenis Biner:	bytes, bytearray, memoryview
#Tidak ada Tipe:	NoneType

x = 5
print(type(x))

#ANGKA PYTHON

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#INTEGER, int

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#FLOAT
#Float, atau "floating point number" adalah angka, positif atau negatif, 
# yang mengandung satu atau lebih desimal.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float juga bisa berupa bilangan ilmiah dengan huruf "e" untuk menunjukkan pangkat 10.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#KOMPLEKS (ditulis dengan "j")

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#KONVERSI

x = 1 #int
y = 2.8 #float
z = 1j #complex

#convert fron int to float
a = float(x)

#convert from float to int
b = int(y)

#convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))