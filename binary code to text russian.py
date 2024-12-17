def binary_to_text(binary):
    """Конвертирует двоичный код в текст."""
    try:
        # Разделяем строку на 8-битные блоки и конвертируем в символы
        text = ''.join(chr(int(byte, 2)) for byte in binary.split())
        return text
    except ValueError:
        return "Ошибка: Некорректный двоичный код."

def main():
    binary = input("Введите двоичный код (разделённый пробелами): ")
    text = binary_to_text(binary)
    print(f"Текст: {text}")

if __name__ == "__main__":
    main()
