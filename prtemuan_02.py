def my_function(fname):
    print(fname + "Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname):
    return fname + "Refsnes"

result = my_function("Emil")
print(result)
print(my_function("Tobias"))

def my_function(*kids):
    print(kids)
    for kid in kids:
        print(kid)

my_function("Emil", "Tobias")

#keyword arguments
def my_function(child3, chiled2, chiled1):
    print("The youngest child is" + child3)

my_function(chiled1="Emil", chiled2= "Tobies", child3="Linus")

#1
def full_name(first_name, last_name):
    print(first_name + " " + last_name)

full_name(last_name= "Tobias", first_name= "Emil")

#2
def full_name_2(**full_name):
    print(full_name)
    print("Last name is " + full_name['lname'])


full_name_2(lname="Tobias", fname="Emil", age=30)


#3
def detail_people(**data):
    print(data)

detail_people(nama_depan="Emil",
              nama_belakang="Tobias",
              umur="20",
              status="Bekerja")

#4
def upper_case_country(country = "Norway"):
    print(country.upper())

upper_case_country("Swiss")


#5
def my_function(country = "Norway"):
    print("I an from " + country)

my_function("Swedia")
my_function("India")
my_function()
my_function("Brazil")

print("")

#6

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#7
def multiply_by_two(a):
    return a * 2

assert(multiply_by_two(3)) == 0

def multiply_by_x(w, x = 2):
    "If not passed, than define the default value to 2"
    return w * x

assert(multiply_by_x(3)) == 6
assert(multiply_by_x(3, 1)) == 3

user_input = input('input dikali dengan 2:')
print(type(user_input))


