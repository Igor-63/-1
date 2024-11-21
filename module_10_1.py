import time
from time import sleep
#from threading import Thread

import threading


def write_words(word_count, file_name):

    new_file = open(file_name, 'w', encoding="utf-8")
    for word_order in range(word_count):
        new_file.write(f'Какое-то слово № {word_order+1}')
        new_file.write('\n')
        sleep(0.1)
    new_file.close()

    print(f'Завершилась запись в файл {file_name}')


time1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time2 = time.time()

print (f'время работы программ последовательно {time2-time1} \n')








time1 = time.time()

th1 = threading.Thread(target=write_words, args = (10, 'example5.txt'))
th2 = threading.Thread(target=write_words, args =(30, 'example6.txt'))
th3 = threading.Thread(target=write_words, args = (200, 'example7.txt'))
th4 = threading.Thread(target=write_words, args = (100, 'example8.txt'))



th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()

time2 = time.time()
print (f'время работы потоков {time2-time1}')







