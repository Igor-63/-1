


import threading
import time
import random


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        rand1 = random.randint(1, 100)
        time.sleep(rand1/1000)
        # запуск потоков  с небольшой случайной разницей во времени (менее 0,1 секунды)
        # чтобы не мешали друг другу выводить на экран сообщения
        #  если этого не сделать иногда не происходит переход на новую строку при печати следующего сообщения
        print(f'{self.name}, на нас напали!.')

        cout_enimi =100
        time1 = 0
        while cout_enimi>0:
            cout_enimi = cout_enimi - self.power
            time.sleep(1)
            time1 = time1 + 1
            print(f'{self.name} сражается {time1} дней(дня), осталось {cout_enimi} воинов.')
        print (f"{self.name} одержал победу спустя {time1} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)



first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()


print ('Все битвы закончились!')




