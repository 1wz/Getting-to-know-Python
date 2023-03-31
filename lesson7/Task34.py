vowels={'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'}
def vowelsInWord(word):
    count=0
    for letter in word:
        if letter in vowels:
            count+=1
    return count


input="пара-ра-рам рам-пам-папам па-ра-па-да"
print("Парам пам-пам" if len(set(map(vowelsInWord,input.split())))==1 else "Пам парам")
