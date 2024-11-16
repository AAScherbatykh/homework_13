import enchant


class CaesarsCipher:
    """ Класс для работы с шифром Цезаря.

    """

    def __init__(self, symbols: str):
        """ Конструктор класса CaesarsCipher.

        Args:
            symbols: Словарь символов.
        """
        self.symbols: str = symbols

    def decrypt(self, text: str, step: int):
        """ Дешифрование текста с указанным шагом.

        Args:
            text: Текст для дешифровки.
            step: Шаг.

        Returns: Дешифрованный текст.

        """
        new_text: list = []
        for char in text:
            index: int = self.symbols.index(char)
            new_index: int = index - step
            new_char: str = self.symbols[new_index]
            new_text.append(new_char)
        return ''.join(new_text)

    def encrypt(self, text: str, step: int):
        """ Шифрование текста с указанным шагом.

        Args:
            text: Текст для шифровки.
            step: Шаг.

        Returns: Зашифрованный текст.

        """
        new_text: list = []
        for char in text:
            index: int = self.symbols.index(char)
            new_index: int = index + step
            new_char: str = self.symbols[new_index]
            new_text.append(new_char)
        return ''.join(new_text)


cipher: CaesarsCipher = CaesarsCipher(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.')
dictionary = enchant.Dict("en_US")
step: int = 0
decrypted_text: str = ''
for step in range(len(cipher.symbols)):
    decrypted_text = cipher.decrypt(
        'o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D', step)
    if dictionary.check(decrypted_text.split(' ')[0]):
        print(f'{step}: {decrypted_text}')
        break

file_name: str = input('Введите имя файла для сохранения текста: ')
with open(file_name, 'w') as file:
    file.write(f'{step}: {decrypted_text}\n')
