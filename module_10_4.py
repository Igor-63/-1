import queue
import random
import threading
import time


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(5, 20))


class Cafe:
    def __init__(self, *cafe_tables: Table):
        self.queue = queue.Queue()
        self.cafe_tables = []

        for tabl in cafe_tables:
            self.cafe_tables.append(tabl)

    def guest_arrival(self, *cafe_guests):

        for my_guest in cafe_guests:
            self.queue.put(my_guest)

        customers = 0

        for tabl in self.cafe_tables:
            if not tabl.guest:
                tabl.guest = self.queue.get()
                print(f'{tabl.guest.name} сел(-а) за стол номер {tabl.number}.')
                customers = customers + 1
                tabl.guest.start()

        temp_my_queue = []
        while not self.queue.empty():
            temp_my_queue.append(self.queue.get())

        for my_queue in temp_my_queue:
            print(f'{my_queue.name} в очереди')
            self.queue.put(my_queue)

        if customers == len(self.cafe_tables):
            print(f'все столы заняты')

    def discuss_guests(self):
        close_tabl = True
        while not self.queue.empty() or close_tabl:
            close_tabl = False
            for cur_table in self.cafe_tables:
                if not (cur_table.guest is None):
                    close_tabl = True
                    if not cur_table.guest.is_alive():
                        print(f'{cur_table.guest.name} покушал(а) и ушёл(ушла)')
                        print(f'Стол номер {cur_table.number}  свободен.')
                        if self.queue.empty():
                            cur_table.guest = None
                            print('В очереди никого нет')
                        else:
                            cur_table.guest = self.queue.get()
                            print(f'{cur_table.guest.name} вышел из очереди и сел(а) за стол номер {cur_table.number}.')
                            cur_table.guest.start()

        print('Все столы свободны')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey',
    'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
