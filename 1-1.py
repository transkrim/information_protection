table = {
    'a': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'к': 10, 'л': 11,
    'м': 12, 'н': 13, 'о': 14, 'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19, 'ф': 20, 'х': 21,
    'ц': 22, 'ч': 23, 'ш': 24, 'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29, 'ю': 30, 'я': 31, ' ':32
}


def shif(word):
    word = word.replace(' ', '').strip()
    if len(word) % 2 != 0:
        word = f'{word}я'

    doubles = []
    answers = []

    while word:
        x = f'{word[0]}{word[1]}'
        word = word[2::]
        doubles.append(x)

    for pars in doubles:
        ans = 0

        x1 = pars[0]
        x2 = pars[1]

        ans += (table[x1] - 1) * 32
        ans += table[x2]

        answers.append(ans)

    return answers

answers = shif('привет мир')
print(answers)

def unshif(answers):
    b_list = list()
    for item in answers:
        a = (item//31)+1
        b_list.append(a)
        print(a)

unshif(answers)




