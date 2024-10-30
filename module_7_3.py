import io
from webbrowser import Error


class WordsFinder:
    def __init__(self, *files):
        self.filenames = []
        self.filenames.append(files)

    def get_all_words(self):
            all_words = {}



            for my_file in self.filenames:
                for my_str in my_file:
                    try:
                        with open(my_str, 'r', encoding="utf-8") as file1:

                            new_str = file1.read().lower()

                            string_punctuation =  [',', '.', '=', '!', '?', ';', ':', ' - ']

                            for p in string_punctuation:
                                if p in new_str:
                                    new_str = new_str.replace(p, '')

                                all_words[my_str] =   new_str.split()
                    except:
                        print('ошибка')



            return all_words








    def find(self, word):


        for name, word1 in self.get_all_words().items():

            # new_word1 = word1.split()

            word_index = 0

            for word2 in word1:
                word_index = word_index + 1
                if word.lower() in word2:

                    # print (name, word, word_index)

                    return {name: word_index}



    def count(self, word):
        for name, word1 in self.get_all_words().items():


            word_count = 0

            for word2 in word1:
                if word.lower() in word2:
                    word_count = word_count + 1
            return {name: word_count}




finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')

print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))








