#Написать скрипт, который выводит на экран «True», если элементы
#программно задаваемого списка представляют собой возрастающую
#последовательность, иначе – «False»
lst = [7, 9, 2, 4, 1, 6, 5, 8, 3, 10]
lst = list(range(11))
lst_copy = sorted(lst)
print("TRUE" if lst == lst_copy else "FALSE")

#lst = [7, 9, 2, 4, 1, 6, 5, 8, 3, 10]
#lst = list(range(11))
#for i in range(1, len(lst)):
#   if lst[i - 1] > lst[i]:
#     print("FALSE")
#   break
#else:
#     print("TRUE")


