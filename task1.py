"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string
length is less than 2, return instead of the empty string.
Sample String: 'helloworld'
Expected Result : 'held'
Sample String: 'my'
Expected Result : 'mymy'
Sample String: ' x'  # тут помилка в завданні прообіл лишній тому і у багатьх були проблеми
Expected Result: Empty String """


print('helloworld'[0:2] + 'helloworld'[-2:])  # print('helloworld'[0:3]+'d')
print('my'[:2] + 'my' [-2:])
print('x'[:-2])
