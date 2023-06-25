import random



def range_smaller(flag_smaller, smaler, top, word):
    for ix in range(len(word)):
        if comparing(word[ix], top) != 'меньше':
            flag_smaller[ix] = 0
    for ix in range(len(word)):
        if flag_smaller[ix] == 1:
            smaler.append(word[ix])


def method_nearest_bigger(biger, keywr, word):
    for word in word:
        if comparing(word, keywr) == 'больше':
            biger.append(word)



def method_nearest_smaller(keywr, smaler, word):
    for word in word:
        if comparing(word, keywr) == 'меньше':
            smaler.append(word)



def method_smallest(curr, word):
    for ix in range(len(word[0])):
        smallest = []
        for word in curr:
            if word[ix] == 0:
                smallest.append(word)
        if len(smallest) > 0:
            curr = smallest
    return curr


def find_the_nearest_smaller(word, keywr):
    smaler = []
    method_nearest_smaller(keywr, smaler, word)
    the_nearest = find_the_biggest(smaler)
    return the_nearest



def find_the_biggest(word):
    if word == []: return []
    curr = word.copy()
    curr = method_biggest(curr, word)
    return curr


def method_biggest(curr, word):
    for ix in range(len(word[0])):
        the_biggest = []
        for word in curr:
            if word[ix] == 1:
                the_biggest.append(word)
        if len(the_biggest) > 0:
            curr = the_biggest
    return curr



def to_compare(first_word, g, l, second_word, word_first, word_second):
    for ix in range(len(first_word)):
        if first_word[ix] == 0:
            word_first.append(False)
        else:
            word_first.append(True)
        if second_word[ix] == 0:
            word_second.append(False)
        else:
            word_second.append(True)
    for ix in range(len(first_word)):
        g1 = g or (not (word_second[ix]) and word_first[ix] and not (l))
        l1 = l or (word_second[ix] and not (word_first[ix]) and not (g))
        g = g1
        l = l1
    return g, l

def find_the_nearest_bigger(word, keywr):
    biger = []
    method_nearest_bigger(biger, keywr, word)
    the_nearest = find_the_smallest(biger)
    return the_nearest

def find_the_smallest(word):
    if word == []: return []
    curr = word.copy()
    curr = method_smallest(curr, word)
    return curr


def range_bigger(flag_bigger, into, low, smaler):
    for ix in range(len(smaler)):
        if comparing(smaler[ix], low) != 'больше':
            flag_bigger[ix] = 0
    for ix in range(len(smaler)):
        if flag_bigger[ix] == 1:
            into.append(smaler[ix])


def comparing(first_word, second_word):
    g = False
    l = False
    word_first, word_second = [],[]
    g, l = to_compare(first_word, g, l, second_word, word_first, word_second)
    if g and not(l): return 'больше'
    elif not(g) and l: return 'меньше'
    else: return 'равно'


def range_within(word, low, top):
    into = []
    smaler = []
    flag_smaller = [1 for ix in range(len(word))]
    range_smaller(flag_smaller, smaler, top, word)
    flag_bigger = [1 for ix in range(len(smaler))]
    range_bigger(flag_bigger, into, low, smaler)
    return into



word = []
while True:
    if word == []:
        words_num = int(input('number of word: '))
        word_len = int(input('length of word: '))
        word = [[random.randint(0, 1) for n in range(word_len)] for m in range(words_num)]
        for word in word:
            print(word)
    operation = input('\n1 - new array of word\n2 - find the nearest smaller\n3 - find the nearest bigger\n4 - find word in range\n\n')
    match operation:
        case '1':
            words_num = int(input('number of word: '))
            word_len = int(input('length of word: '))
            word = [[random.randint(0, 1) for n in range(word_len)] for m in range(words_num)]
            for word in word:
                print(word)
        case '2':
            keywr = input('enter your word: ')
            keywr = keywr.replace(' ', '')
            keywr = [int(el) for el in keywr.split(',')]
            the_nearest = find_the_nearest_smaller(word, keywr)
            if the_nearest == []:
                print('no word smaller than this')
            else:
                for word in the_nearest:
                    print(word)
        case '3':
            keywr = input('enter your word: ')
            keywr = keywr.replace(' ', '')
            keywr = [int(el) for el in keywr.split(',')]
            the_nearest = find_the_nearest_bigger(word, keywr)
            if the_nearest == []:
                print('no word bigger than this')
            else:
                for word in the_nearest:
                    print(word)
        case '4':
            lower_border = input('low border: ')
            lower_border = lower_border.replace(' ', '')
            lower_border = [int(el) for el in lower_border.split(',')]
            top_border = input('top border: ')
            top_border = top_border.replace(' ', '')
            top_border = [int(el) for el in top_border.split(',')]
            within = range_within(word, lower_border, top_border)
            if within == []:
                print('no word in this range')
            else:
                for word in within:
                    print(word)
