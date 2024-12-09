# snake_case
import sys
import decimal

from Tools.scripts.generate_global_objects import Printer

print("Radek")  # wyswietl wydrukuj
print('Radek')

print(type("radek"))  # dane str, <class 'str>
print("39")
print(type("39"))  # <class 'str'>
print(39)
print(type(39))  # <class 'int'> liczby calkowite

print(type(40))
print(sys.int_info)

# print(" Radek') #
# C:\Users\cscomarch\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:\Users\cscomarch\PycharmProjects\pythonProject1\pierwszy.py
#   File "C:\Users\cscomarch\PycharmProjects\pythonProject1\pierwszy.py", line 16
#     print(" Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 16)


# ctrl / - komentarz
# ctrl alt l - formatuje

# print("59" 90)

# C:\Users\cscomarch\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:\Users\cscomarch\PycharmProjects\pythonProject1\pierwszy.py
#   File "C:\Users\cscomarch\PycharmProjects\pythonProject1\pierwszy.py", line 27
#     print("59" 90)
#           ^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

print(int("59") + 90)  # 149
print("59" + str(90))  # 5990 - konkatenacja - łączenie string
print(5 * "90")  # 9090909090 - daje 5 * "90"
print(type(3.99))  # <class 'float'>

print(sys.float_info)

# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.4)  # 0.5
print(0.1 + 0.2)  # 0.30000000000000004

# zmienna - pudełko
a = decimal.Decimal("10")
print(a)

a = decimal.Decimal("1.2345")
b = decimal.Decimal("2.2345")
print(a + b)  # 3.4690

precyzja = decimal.Decimal("0.00")
print((a + b).quantize(precyzja))  # 3.47

# typ logiczny
# prawda / fałsz
#True False

print(True)
print(False)
#ctrl d - kopiowanie linii
# True
# Fakse

print(int(True)) # 1
print(bool(1)) #true
print(bool(0)) # false
print(bool(100)) # true

print(bool(None)) # odpowienik null

tekst = "Radek"
print(tekst.upper()) #RADEK
print(tekst.lower()) #radek
print(tekst) # Radek

# kolekcja - zapamiętuje wiele elementów , różne typy na raz moga być

#lista, krotka (tuple) , zbiór(set), słownik (dict)

lista = [5,6,7,8,9]
print(lista) # [5, 6, 7, 8, 9]
lista2 = lista
lista_copy = lista.copy() # kopia elementów listy
print(lista2)
print(lista)

lista.clear() # usunięcie elementów listy
print(lista2)
print(lista)

# krotka tylko do odczytu
krotka = tuple(lista_copy)
print(krotka) # (5, 6, 7, 8, 9)

# przechowuje unikalne wartości - DISTINCT
zbior = {5,5,5,5,5,6,7,8,9,10}
print(zbior)   #{5, 6, 7, 8, 9, 10}

# json - czyli ma klucz
slownik = {"name" : "Radek" ,"age":45}
print(slownik)  #{'name': 'Radek', 'age': 45}









