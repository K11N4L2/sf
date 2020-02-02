# vowel counter

mystr = input('Please enter a string').lower()


def vowel_count(mystr):
    count = 0
    for i in mystr:
        if i in "aeiou":
            count = count + 1
    return count

print(str(vowel_count(mystr)))

# combine with letter counter