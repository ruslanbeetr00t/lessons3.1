"""The valid phone number program.
Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
Напишіть програму, яка має змінну із збереженим вашим іменем (малими літерами), а потім запитує ваше ім’я як введення.
Програма повинна перевірити, чи дорівнює ваше введення збереженому імені, навіть якщо в даному імені є інший регістр,
наприклад,якщо ваше введення - "Антон", а збережене ім'я - "антон", воно повинно повернути True. """

name = 'ruslan'
print('input you are name')
s = input()
if print(name == s.lower()):
    print('This is correct name')
