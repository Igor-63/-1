
def all_variants(s):
    i =0

    for _ in range (i, len(s)):
        j = i + 1
        for _ in range(j, len(s) +1):
            s2 = s[i:j]
            yield s2
            j = j + 1
        i = i + 1


a = all_variants("abdc")


for i in a:
    print(i)





