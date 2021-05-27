"""The valid phone number program.

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
Створіть програму, яка перевіряє, чи рядок відповідає правильному формату для телефонного номера.
Програма повинна перевірити, чи рядок містить лише числові символи та має довжину лише 10 символів.
Роздрукуйте відповідне повідомлення залежно від результату оцінки рядка. """

print('Write phone numbe use just numbers')
number = '1234567890'
number = input()
if len(number) == 10:
    print(number.isdigit(), 'phone number')
else:
    var = number != 10
    print(number, 'not corect')
