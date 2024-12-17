def text_to_binary(text):
    """Конвертирует текст в двоичный код."""
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

def main():
    text = input("Введите текст для конвертации в двоичный код: ")
    binary_code = text_to_binary(text)
    print(f"Двоичный код: {binary_code}")

if __name__ == "__main__":
    main()
