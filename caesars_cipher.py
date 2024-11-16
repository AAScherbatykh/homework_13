import enchant

class CaesarsCipher:


    def __init__(self, symbols):
        self.symbols = symbols

    def decrypt(self, text, step):
        new_text: list = []
        for char in text:
            index = self.symbols.index(char)
            new_index = index - step
            new_char = self.symbols[new_index]
            new_text.append(new_char)
        return ''.join(new_text)

    def encrypt(self, text, step):
        new_text: list = []
        for char in text:
            index = self.symbols.index(char)
            new_index = index + step
            new_char = self.symbols[new_index]
            new_text.append(new_char)
        return ''.join(new_text)



cipher = CaesarsCipher('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.')

# print(cipher.encrypt('HELLO', 2))
#
# print(cipher.decrypt('JGNNQ', 2))

dictionary = enchant.Dict("en_US")
step = 0
decrypted_text = ''
for step in range(len(cipher.symbols)):
    decrypted_text = cipher.decrypt('o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D', step)
    if dictionary.check(decrypted_text.split(' ')[0]) == True:
        print(f'{step}: {decrypted_text}')
        break

file_name = input('Введите имя файла для сохранения текста: ')
with open(file_name, 'w') as file:
    file.write(f'{step}: {decrypted_text}\n')
