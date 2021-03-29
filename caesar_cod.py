from alpha import abc


def ceasar_codding(file_name):
    # Открываем файл который необходимо закодировать
    file = open(file_name, "r")
    shift = int(input("Введите велечину сдвига:"))
    # Считываем информацию находящуюся в файле
    text = file.read()
    file.close()
    print(text)
    text_list = list(text)
    """
    for letters in text_list:
        try:
            text_list[text_list.index(letters)] = abc[(abc.index(letters) + shift) % len(abc)]
        except ValueError:
            continue
    """
    for letter_index, letters in enumerate(text_list):
        try:
            text_list[letter_index] = abc[(abc.index(letters) + shift) % len(abc)]
        except ValueError:
            continue
    print(text_list)
    cod_text = "".join(text_list)
    file = open(file_name, "w")
    file.write(cod_text)
    file.close()
    print("Kодирование завершено!")


def ceasar_decoding(file_name):
    shift = int(input("Введите велечину сдвига для расшифровки:"))
    file = open(file_name, "r")
    text = file.read()
    file.close()
    print(text)
    text_list = list(text)
    """
    for letters in text_list:
        try:
            text_list[text_list.index(letters)] = abc[(abc.index(letters) - shift) % len(abc)]
        except ValueError:
            continue
    """
    for letter_index, letters in enumerate(text_list):
        try:
            text_list[letter_index] = abc[(abc.index(letters) - shift) % len(abc)]
        except ValueError:
            continue
    print(text_list)
    cod_text = "".join(text_list)
    file = open(file_name, "w")
    file.write(cod_text)
    file.close()
    print("Декодирование завершено!")


def main():
    #file_name = input("Введите имя файла для кодирования:")
    file_name = "test.txt"
    ceasar_codding(file_name)
    #file_name = input("Введите имя файла для декодирования:")
    ceasar_decoding(file_name)


main()
