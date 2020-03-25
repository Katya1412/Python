def extra_enumerate(x):
    cum = 0
    full_cum = sum(x)
    for i in x:
        cum += i
        frac = round(cum / full_cum, 1)
        yield i, cum, frac


lst = [1, 3, 4, 3]
for elem, cum, frac in extra_enumerate(lst):
    print("({}, {}, {})".format(elem, cum, frac), end="\t" * 4)


#Напишите собственную версию генератора enumerate под названием
#extra_enumerate. Пример вызова:

#$for i, elem, cum, frac in extra_enumerate(x):
#print(elem, cum, frac)
#В переменной cum хранится накопленная сумма на момент текущей
#итерации, в переменной frac – доля накопленной суммы от общей
#суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
#вывод будет таким:
 #(1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1)