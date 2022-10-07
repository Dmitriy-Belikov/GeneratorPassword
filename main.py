import random
import pyside6
#Словари для генерации
letters_l = 'abcdefghijklmnopqrstuvwxyz' #словарь 0
letters_b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #словарь 1
symbols = '!@#$%^&*()-_=+:;/?.,'#словарь 2
number = '0123456789'#словарь 3
letters = [letters_l, letters_b, symbols, number]
letters_use = '' #Пользовательские словари
password = '' #Готовый пароль
#Пользовательский ввод
f = int(input('Количество символов ')) #количество символов в пароле
h = str(input('Какие словари 0123 ')) #Какие словари будут использоваться 0123

for i in range(len(h)): #Цикл для создания словаря пользовательских символов для выборки
    y = h[i] #Получение номера словаря
    t = int(y) #Приведение номера к int
    letters_use = letters_use + letters[t] #Запись выбранного словаря в общий
for i in range(f): #Цикл для генерации случайного пароля из выбранных символов
    s = random.randint(0, len(letters_use)-1) #генерация случайного числа на основе количества символов в строке с пользовательским паролем
    password += letters_use[s] #получение символа из строки общего словаря и запись в переменную
print(password)