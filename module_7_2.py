

def custom_write(file_name: str, strings:list):

        rez = {}

        new_file = open(file_name, 'w', encoding="utf-8")
        nom_str = 1
        for i in strings:


            bite_begin = new_file.tell()
            key  = (nom_str, bite_begin)

            rez[key] = i
            nom_str = nom_str+1

            i = i + '\n'
            new_file.write(i)


        new_file.close()



        return rez

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

print(*result.items(), sep='\n')

