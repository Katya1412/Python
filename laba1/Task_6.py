#Напишите программу, позволяющую ввести с клавиатуры текст
#предложения и вывести на консоль все символы, которые входят в этот
#текст ровно по одному разу.
text = input("Введите текст: ")
for i in text:
    if text.count(i) == 1:
        print(i)
