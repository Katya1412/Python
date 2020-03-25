def frange(start, end, step):
    while start < end:
        yield round(start, 3)
        start += step


for i in frange(1, 6, 0.1):
    print(i)
#Напишите генератор frange как аналог range(7) с дробным шагом.
#Пример вызова:
#yield генератор
#for x in frange(1, 5, 0.1):
#print(x)
# выводит 1 1.1 1.2 1.3 1.4 … 4.9