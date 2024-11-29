import threading, random, time
from time import sleep


class Bank():

    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
       
        for _ in range(10):

                if self.lock.locked() and self.balance >= 500:
                    self.lock.release()

                rand1 =  random.randint(50, 500)
                self.lock.acquire()
                self.balance = self.balance + rand1
                print (f'Пополнение: {rand1}. Баланс: {self.balance}.')
                self.lock.release()

                sleep(0.001)



    def take(self):

            for _ in range(10):

                self.lock.acquire()
                rand1 =  random.randint(50, 500)
                print(f'Запрос на: {rand1}.')

                if rand1 > self.balance:
                    print('Запрос отклонён, недостаточно средств')
                else:
                    self.balance = self.balance - rand1
                    print ( f'Снятие: {rand1}. Баланс: {self.balance}.')
                self.lock.release()
                sleep(0.001)








bank1 = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bank1,))
th2 = threading.Thread(target=Bank.take, args=(bank1,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'\nИтоговый баланс: {bank1.balance}')







