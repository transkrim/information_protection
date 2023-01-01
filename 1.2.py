def decode(text, xkeys, ykeys):
    return ''.join(text[len(xkeys)*(x-1)+(y-1)] for y in ykeys for x in xkeys)

xkey = input("x keys: ").upper().split(',')
xkeys = tuple([int(x) for x in xkey])
ykey = input("y keys: ").upper().split(',')
ykeys = tuple([int(y) for y in ykey])
cryptWord = input("Word: ").upper()
print(decode(cryptWord, xkeys, ykeys))