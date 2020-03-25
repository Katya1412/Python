#Напишите скрипт, генерирующий случайным образом число n в
#диапазоне от 1 до 10000. Скрипт должен создать массив из n целых
#чисел, также сгенерированных случайным образом, и дополнить
#массив нулями до размера, равного ближайшей сверху степени двойки.
#Например, если в массиве было n=100 элементов, то массив нужно
#дополнить 28 нулями, чтобы в итоге был массив из 28
#=128 элементов
#(ближайшая степень двойки к 100 – это число 128, к 35 – это 64 и т.д.).
import random
import math
import array
numbers = array.array('i', [random.randint(1, 9) for _ in range(1, random.randint(1, 10) + 1)])
the_power_of_two = math.ceil(math.log(len(numbers), 2))
print("Длина массива {}\n{}".format(len(numbers), numbers))
print("Степень двойки: {}\nДвойка в этой степени {}\nСколько надо добавить: {}".format(the_power_of_two, 2 ** the_power_of_two, 2 ** the_power_of_two - len(numbers)))
numbers += array.array('i', [0] * (2 ** the_power_of_two - len(numbers)))
print(numbers)
