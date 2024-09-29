import sys

my_string = "Lorem Ipsum is my favorite text pattern"

print(my_string.startswith('Lorem'))
print(my_string.startswith('lorem'))
print(my_string.endswith('pattern'))
print(my_string.endswith('PaTtErN'))


print(sys.getrefcount(my_string))

this_is_string = "Hi there!"
the_same_string = 'Hi there!'
print(this_is_string == the_same_string)  # True
print(id(this_is_string))
print(id(the_same_string))

text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

print(text)
print(song)

implicit_concatenation = "some text " "and other text"
print(implicit_concatenation)