from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

print (list(map(lambda x, y: x==y, first, second )))





def get_advanced_writer(file_name):

    def  write_everything(*data):
        file2 = open(file_name, "a", encoding='utf-8')
        for my_str in data:
            file2.writelines(str(my_str) + '\n')
        file2.close()
    return write_everything


write = get_advanced_writer('example.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *my_collection):
        self.words = []
        for words1 in my_collection:
            self.words.append(words1)

    def __call__(self):
        return  choice(self.words)





first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
