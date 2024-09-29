s = "Hi there!"
start = 0
end = 7

print(s.find("er", start, end)) # 5 = index
print(s.find("q")) # -1 = not found
print(s.rfind("er", start, end))
print(s.rfind('q'))

s = 'Some words'

print(s.find("o"))
print(s.rfind('o'))
print(s.index("o"))
print(s.rindex('o'))

lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Curabitur vulputate est risus, ut interdum nisl mattis sed. Aliquam \
vel vehicula lacus. Orci varius natoque penatibus et magnis dis \
parturient montes, nascetur ridiculus mus. Nulla ac hendrerit \
libero, et tincidunt tortor. Curabitur fringilla euismod \
augue, a pulvinar lacus facilisis vel. Vestibulum ut \
blandit nisl, eget fringilla tortor. Praesent felis arcu, \
ullamcorper quis pulvinar at, lobortis nec leo. Class aptent \
taciti sociosqu ad litora torquent per conubia nostra, per \
inceptos himenaeos. Aliquam sed purus vehicula, sollicitudin \
elit vitae, eleifend nisl."

print(lorem_ipsum)
for item in lorem_ipsum.split():
    print(item)

my_list1 = ['1', '2', '3', '4']
my_list2 = ['Hello', 'my', 'love', '!']
result1 = '±'.join(my_list1)
result2 = ' '.join(my_list2)
print(result1)
print(result2)