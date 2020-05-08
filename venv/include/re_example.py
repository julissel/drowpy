import re


# 1
# Найти все номера машин в тексте по следующему правилу:
# 3 цифры 2 буквы 2-3 цифры, буквы из списка [ABEKMHOPCTYX]
text = '''
Автомобиль с номером А123ВС77 подрезал автомобиль К654НЕ197,
спровоцировав ДТП с участием еще двух автомобилей М542ОР777 и О007ОО77
Cherif's car has number = A234BT45
'''
pattern = r"[ABEKMHOPCTYXАВЕКМНОРСТУХ]\d{3}[ABEKMHOPCTYXАВЕКМНОРСТУХ]{2}\d{2,3}"
match = re.findall(pattern, text)
print("Найдены номера автомобилей:")
print(match)


# 2
# Найти корректные nicknames
nicknames = ['sU3r_haXX0r', 'alёna', 'ivan ivanovich']
reg = re.compile(r'^\w+$', re.ASCII)
print()
print("проверка nicknames:")
for nick in nicknames:
    print('{} nickname: "{}"'.format(
        'valid' if reg.match(nick) else 'invalid',
        nick
    ))


# 3
# Найти значение курса Евро для любого регистра в названии валюты
# 3.1
text = "Курс евро на сегодня 81,7571, курс евро на завтра 80,4512"
match = re.search(r"Евро\D+(\d+,\d+)", text, re.IGNORECASE)
rate = match.group(1)
print()
print("Курс Евро (1):")
print(rate)

# 3.2
match = re.search(r"Евро.*(\d+,\d+)", text, re.IGNORECASE | re.DOTALL).group(1)
print("Курс Евро (2):")
print(match)


# 4
# Даны положительные числа. Уменьшить на единиицу каждое.
s = '9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9'
print()
print("Уменьшить на единиицу числа:", s)
print("Результат:", re.sub(r"\d+", lambda r: str(int(r.group(0))-1), s))


# 5
# Найти все действительные числа
test_str = '-100; 21.4; +5.3; -1.5; 0'
res = re.findall(r"[-+]?\d+(?:\.\d+)", test_str)
print()
print("Найдены действительные числа:")
print(res)


# 6
# Проверить, что строка это серийный номер вида 00XXX-XXXXX-XXXXX-XXXXX, где X - шестнадцатиричная цифра
serial_str = ["00afc-001bc-00110-4596e", "01pwd-sss11-w4846-13123", "00aka-47wr-tt", "00143-00111-00110-45969"]
print()
for item in serial_str:
    if re.match(r"^00[\da-f]{3}(?:-[\da-f]{5}){3}$", item, re.IGNORECASE):
        print(f"Correct serial number: {item}")


# 7
# Проверить, что строка является корректным IPv4 адресом
#  запись в виде четырёх десятичных чисел значением от 0 до 255, разделённых точками, например, 192.168.0.3
ip_str = '192.168.29.1'
print()
if re.match(r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(\.|$)){4}(?<!\.)$", ip_str):
    print("Correct IPv4 :", ip_str)


# 8
# Проверить, что логин содержит от 8 до 16 латинских букв, цифр и _
print()
str_login = 'brilliAnte_7mile'
if re.match(r"^\w{8,16}$", str_login):
    print(f"Login '{str_login}' is correct")



# 9
# Проверить, что пароль состоит не менее чем из 8 символов без пробелов.
# Пароль должен содержать хотя бы одну: строчную букву, заглавную, цифру
password = 'dfkw245A'
print()
if re.match(r"^(?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9])\S{8,}$", password):
    print(f"Password '{password}' is correct")


# 10
# Переформатировать код, убрав лишние пробелы между def, именем функции и
# (Например: def    myFunc   (x, y):  => def myFunc(x, y):
list_func = ['def    first_fun (par1, par2)', 'def   fun2(f1,f2,f3)', 'def  f3     ()']
print()
for fun in list_func:
    print('old string', fun)
    print('new string =', re.sub(r'def\s+(\w+)\s*\(', r'def \1(', fun))




# 11
# Заменить все "camel_case" на "сamelCase"
# Например: my_function_name, peer__2__peer  =>  myFunctionName, peer2Peer
f_name = 'my_fun__new_val'
new_name = re.sub('_+([a-zA-Z\d])', lambda x: x.group(1).upper(), f_name.lower())
print()
print(f'Old function name = {f_name}')
print('New function name = ', new_name)


# 12
'''
Напишите регулярное выражение, которое с помощью re.findall найдет все последовательности цифр в строке. 
Например, для строки a123b45с6d должно вернуться ['123', '45', '6']
'''

def find_all_digits(text):
    exp = r'\d+'
    return re.findall(exp, text)

print()
myString = 'a123b45c60O1d_9_1'
print(find_all_digits(myString))

