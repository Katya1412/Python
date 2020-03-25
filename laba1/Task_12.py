def get_frames(signal, size, overlap):
    step = int(size * overlap)
    i = 0
    while i < len(signal):
        yield signal[i:i+size]
        i += step


signal = [i for i in range(10)]
print("Сигнал: {}".format(signal))
for i in get_frames(signal, 2, 3):
    print(i)



#Напишите генератор get_frames(), который производит «оконную
#декомпозицию» сигнала: на основе входного списка генерирует набор
#списков – перекрывающихся отдельных фрагментов сигнала размера
#size со степенью перекрытия overlap. Пример вызова:
#for frame in get_frames(signal, size=1024, overlap=0.5):
#print(frame)
