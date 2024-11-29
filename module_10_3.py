import threading, random, time
from time import sleep


class Bank():

    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        self.lock.acquire()
        for _ in range(5):

                rand1 =  random.randint(50, 500)
                self.balance = self.balance + rand1
                print (f'Пополнение: {rand1}. Баланс: {self.balance}.')


                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()

                sleep(0.001)


        if self.lock.locked(): self.lock.release()



    def take(self):

            for _ in range(5):


                rand1 =  random.randint(50, 500)
                print(f'Запрос на: {rand1}.')

                if rand1 > self.balance:
                    print('Запрос отклонён, недостаточно средств')
                    self.lock.acquire()
                else:
                    self.balance = self.balance - rand1
                    print ( f'Снятие: {rand1}. Баланс: {self.balance}.')

                sleep(0.001)

            if self.lock.locked(): self.lock.release()







bank1 = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bank1,))
th2 = threading.Thread(target=Bank.take, args=(bank1,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'\nИтоговый баланс: {bank1.balance}')







