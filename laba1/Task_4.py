#Напишите скрипт, который разделяет введенный с клавиатуры текст на
#слова и выводит сначала те слова, длина которых превосходит 7
#символов, затем слова размером от 4 до 7 символов, затем – все
#остальные

text = input("Введите текст: ")
splitted_text = text.split()
seven_simbols = ""
four_and_seven_simbols = ""
rest_words = ""

while True:
    for i in range(0, len(splitted_text)):
        if len(splitted_text[i]) > 7:
            seven_simbols += splitted_text[i] + " "
        elif 3 < len(splitted_text[i]) < 8:
            four_and_seven_simbols += splitted_text[i] + " "
        else:
            rest_words += splitted_text[i] + " "
    break

print(seven_simbols)
print(four_and_seven_simbols)
print(rest_words)
