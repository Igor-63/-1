
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category


    def __str__(self):

        return f'{self.name}, {self.weight}, {self.category}'







class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):

        try:
            f = open(self.__file_name, 'r')
            rez = f.read()
            f.close()
        except:
            rez = ''
        return rez

    def add(self, *products):

        all_products = self.get_products()

        f = open(self.__file_name, 'a')

        for i in products:
            if i.name in all_products:
                print(f'Продукт {i} уже есть в магазине')

                continue
            else:
               str1 = i.__str__() + '\n'
               f.write(str1)

        f.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

