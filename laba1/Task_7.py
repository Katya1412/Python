#Напишите скрипт, который обрабатывает список строк-адресов
#следующим образом: сначала определяет, начинается ли каждая строка
#в списке с префикса «www». Если условие выполняется, то скрипт
#должен вставить в начало этой строки префикс «http://», а затем
#роверить, что строка заканчивается на «.com». Если у строки другое
#окончание, то скрипт должен вставить в конец подстроку «.com». В
#итоге скрипт должен вывести на консоль новый список с измененными
#адресами. Используйте генераторы списков
addresses = ["www.address_1.com", "www.address_2", "address_3.com", "address_4"]
addresses = [i + ".com" if not i[-4:] == ".com" else i for i in ["http://" + i if i[:4] == "www." else i for i in addresses]]
addresses = [i + ".com" if not i[-4:] == ".com" else i for i in addresses]
print(addresses)

# for i in range(len(addresses)):
#     if addresses[i][:4] == "www.":
#        addresses[i] = "http://" + addresses[i]
#    if not addresses[i][-4:] == ".com":
#        addresses[i] = addresses[i] + ".com"
