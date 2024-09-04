def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if (i.upper().find(root_word.upper()) + 1) > 0:
            same_words.append(i)
        if (root_word.upper().find(i.upper()) + 1) > 0:
            same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'disaBle', 'Bagel')
print(result1)
print(result2)
