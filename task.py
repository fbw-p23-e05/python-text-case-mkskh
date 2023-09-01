string = 'The Quick BroWnFoX jumps over the laZy Dog!'

print('Original String: ', string)
print('String in uppercase: ', string.upper())
print('String in lowercase: ', string[:18].lower().replace('nf', 'n f').replace('fox', 'fox!'))