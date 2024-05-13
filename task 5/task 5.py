word_input = input('Введите слово: ')
new_words = []

with open('text.txt','r',encoding='utf-8') as f:
    for word in f.read().split():
        if word_input == word or word_input+word.split(word_input)[-1] == word or word_input[-1] == word[0]:
            continue
        for i in range(1,len(word_input)):
            if word_input[(len(word_input)*-1)+i:] == word[:len(word_input[(len(word_input)*-1)+i:])]:
                new_words.append(word_input[:i]+word[:])
print('\n'.join(new_words))

