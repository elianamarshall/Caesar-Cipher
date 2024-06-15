def encrypt_letter(letter: str, key: int) -> str:
    """
    Encrypt the letter by shifting it key places to the right and returning
    that value. Assume len(letter) == 1.

    >>> encrypt_letter("a", 1)
    "b"
    >>> encrypt_letter("a", 3)
    "d"
    >>> encrypt_letter("t", 2)
    """
    return chr(ord(letter) + key)



def encrypt_message(message: str, key: int) -> str:
    """
Return the given message encrypted using encrypt_letter on each
alphabetic character in the word.

    >>> encrypt_messsage("cat", 3)
    "fdw"
    >>> encrypt_message("cat", 0)
    "cat"
    >>> encrypt_message("", 3)
    ""
    """
    new_message = ""
    for char in message:
        new_message = new_message + encrypt_letter(char, key)
    return new_message

def most_common (s:str) -> str:
    current_max = 0
    current_common = ""
    for char in s:
        if s.count(char) > current_max:
            current_max = s.count(char)
            current_common = char
    return current_common



def decrypt_letter(letter: str, key: int) -> str:
    return chr(ord(letter) - key)


def decrypt_message(message: str, key: int) -> str:
    new_message = ""
    for char in message:
        new_message = new_message + decrypt_letter(char, key)
    return new_message
