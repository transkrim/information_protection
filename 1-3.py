alphabeth1 = {
    'a': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ё': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12,
    'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22,
    'ц': 23, 'ч': 24, 'ш': 25, 'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32
}

alphabeth = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
             'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def encrypt(text, gamma):
    textLen = len(text)
    gammaLen = len(gamma)

    text_arr = []
    while text:
        x = f'{text[0]}'
        text = text[1:]
        text_arr.append(x)
    print(text_arr[0])
    #Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(textLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(textLen % gammaLen):
        keyText.append(gamma[i])
    print(keyText)
    #Шифрование
    i = 0
    code = []
    for i in range(textLen):
        code.append(alphabeth[(alphabeth.index(text_arr[i]) + alphabeth.index(keyText[i])) % 33])
        print(code)
    return code

if __name__ == '__main__':
    text = input("text: ")
    gamma = input("gamma: ")
    encrypt(text, gamma)