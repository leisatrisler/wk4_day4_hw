
# Exercise #1
# Filter out all of the empty strings from the list below

# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York", "DC"]
new_words = []
def is_empty(places):
    for p in places:
        if p != "":
            new_words.append(p)
    return list(new_words)
print(is_empty(places))

# Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
def sort_authors(my_authors):
    for author in my_authors:
        print(author)



list_of_authors = sort_authors(authors).sort(key = lambda author: author.spilt()[-1])
print(list(list_of_authors))

 
# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angeles', 111.2), ('Miami', 84.2)]

F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

def C_to_F(celsius): # C_to_F is Convert Celsius to Farhenheit
    farhenheit = (9/5) * celsius + 32
    return(farhenheit)

F_to_places = [C_to_F,places] # F_to_places is Farhenheit to PLaces
map = lambda C_to_F, places:
print(F_to_places)

# Exercise #4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.
def fib(f):
    if f <= 1
        return(F)
    else:
        return fib(f-1)
# fib(1) = 0
# fib(2) = 1
# fib(3) = 1
# fib(4) = 2
# fib(5) = 3
# fib(6) = 5
# fib(7) = 8
# fib(8) = 13
# fib(9) = 21
# fib(10) = 34
# fib(11) = 55
# fib(12) = 89
# fib(13) = 144
 
