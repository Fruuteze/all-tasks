#Задание №1
#input()
name = input ("Введите имя: ")
print(f"Привет ,{name}!")

#input() > int
age_str = input ("Введите ваш возраст:")
age = int(age_str)
print(age)
print(age_str)

#input() > float
weight = float(input("Укажите рост (см)"))
t(weight)
t(type(weight))

#input() > bool
input:bool(1)
output: True
input:bool(0)
output:False
input:bool(True)
output:True
input:bool([1, 2, 3])
output:True
input:bool([])
output:False

#input() > str
str(object='')
str(object=b'', encoding='utf-8', errors='strict')

#input() > complex

c = complex(1, 1) print(c)
c = complex(1.5, -2.1) print(c)
c = complex(0xF) # hexadecimal print(c)
c = complex(0b1010, -1) # binary print(c)

#Задание №2

print("Максимальное значение типа int:", sys.maxsize)
print("Максимальное значение типа float:", sys.float_info.max)

#Задание №3
s = "я люблю динамическую типизацию"

# cp1251
cp1251_bytes = s.encode('cp1251')
cp1251_size = len(cp1251_bytes)
print("Размер в cp1251: ", cp1251_size, "байт")

# utf-8
utf8_bytes = s.encode('utf-8')
utf8_size = len(utf8_bytes)
print("Размер в utf-8: ", utf8_size, "байт")

# utf-16
utf16_bytes = s.encode('utf-16')
utf16_size = len(utf16_bytes)
print("Размер в utf-16: ", utf16_size, "байт")

# utf-32
utf32_bytes = s.encode('utf-32')
utf32_size = len(utf32_bytes)
print("Размер в utf-32: ", utf32_size, "байт")