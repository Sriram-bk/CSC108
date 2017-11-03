# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the
# code that you submit.  Do not use break or continue statements.


def clean_message(message):
    """ (str) -> str

    Returns a string containing all the characters
    in message that were alphabets. All the caracters in the returned string
    are in uppercase.

    >>> clean_message('How are you ?')
        HOWAREYOU

    >>> clean_message('Great to see you, its been a while !')
        GREATTOSEEYOUITSBEENAWHILE

    """

    clean_text = ''

    for char in message:
        if char.isalpha():
            # if character is an alphabet, convert it to
            # uppercase and concatenate it to clean_text.
            clean_text = clean_text + char.upper()

    return clean_text


def encrypt_letter(letter, key_stream_value):
    """ (str, int) -> str

    Applies the key_stream_value to letter for encryption and
    returns the result.

    >>> encrypt_letter('P',12)
        'B'

    >>> encrypt_letter('D',5)
        'I'

    """

    # Converts letter to its ASCII value and applies keystream value.
    encrypted_letter = ord(letter) - 65
    encrypted_letter = (encrypted_letter + key_stream_value) % 26
    encrypted_letter = encrypted_letter + 65

    # Returns the character corresponding to the final ASCII value
    # that was calculated.
    return chr(encrypted_letter)


def decrypt_letter(letter, key_stream_value):
    """ (str, int) -> str

    Applies the key_stream_value to letter for decryption and
    returns the result.

    >>> decrypt_letter('Z',17)
        'G'

    >>> decrypt_letter('A',3)
        'X'

    """

    # Converts letter to its ASCII value and applies keystream value.
    decrypted_letter = ord(letter) - 65
    decrypted_letter = decrypted_letter - key_stream_value
    if decrypted_letter < 0:
        decrypted_letter = 26 + decrypted_letter
    decrypted_letter = decrypted_letter % 26
    decrypted_letter = decrypted_letter + 65

    # Returns the character corresponding to the final ASCII value
    # that was calculated.
    return chr(decrypted_letter)


def swap_cards(deck_of_cards, card_index):
    """ (list of int, int) -> NoneType

    Swaps the card at card_index in deck_of_cards with the card next to it.
    The deck is considered to be a circular deck i.e. if card_index
    refers to the card at the bottom of the deck it swaps
    places with the card on top of the deck.

    >>> deck = [5,7,3,2,6,1,9,8,4]
    >>> swap_cards(deck, 4)
    >>> deck
        [5, 7, 3, 2, 1, 6, 9, 8, 4]

    >>> deck = [15,5,2,12,9,4,7,11,10,1,3,13,14,8,6]
    >>> swap_cards(deck, 7)
    >>> deck
        [15, 5, 2, 12, 9, 4, 7, 10, 11, 1, 3, 13, 14, 8, 6]

    """

    # Stores the card at card_index in a temporary memory location.
    temp = deck_of_cards[card_index]

    # Swaps the card with the next card in 2 different methods depending on
    # whether the card is at the bottom or not.
    if card_index < len(deck_of_cards) - 1:
        deck_of_cards[card_index] = deck_of_cards[card_index + 1]
        deck_of_cards[card_index + 1] = temp
    else:
        deck_of_cards[card_index] = deck_of_cards[0]
        deck_of_cards[0] = temp


def get_small_joker_value(deck_of_cards):
    """ (list of int) -> int

    Returns the value of the small joker from deck_of_cards. The small
    joker is the second largest value in deck_of_cards.

    >>> deck = [5,7,3,2,6,1,9,8,4]
    >>> get_small_joker_value(deck)
        8

    >>> deck = [15,5,2,12,9,4,7,11,10,1,3,13,14,8,6]
    >>> get_small_joker_value(deck)
        14

    """

    small_joker_value = max(deck_of_cards) - 1
    return small_joker_value


def get_big_joker_value(deck_of_cards):
    """ (list of int) -> int

    Returns the value of the big joker from deck_of_cards. The big
    joker is the largest value in deck_of_cards.

    >>> deck = [5,7,3,2,6,1,9,8,4]
    >>> get_big_joker_value(deck)
        9

    >>> deck = [15,5,2,12,9,4,7,11,10,1,3,13,14,8,6]
    >>> get_big_joker_value(deck)
        15

    """

    big_joker_value = max(deck_of_cards)
    return big_joker_value


def move_small_joker(deck_of_cards):
    """ (list of int) -> NoneType

    Swaps the small joker in deck_of_cards with the card that follows it.
    The deck is treated to be circular.

    >>> deck = [5,7,3,2,6,1,9,8,4]
    >>> move_small_joker(deck)
    >>> deck
        [5, 7, 3, 2, 6, 1, 9, 4, 8]

    >>> deck = [15,5,2,12,9,4,7,11,10,1,3,13,6,8,14]
    >>> move_small_joker(deck)
    >>> deck
        [14, 5, 2, 12, 9, 4, 7, 11, 10, 1, 3, 13, 6, 8, 15]

    """

    small_joker = get_small_joker_value(deck_of_cards)
    small_joker_index = deck_of_cards.index(small_joker)
    swap_cards(deck_of_cards, small_joker_index)


def move_big_joker(deck_of_cards):
    """ (list of int) -> NoneType

    Moves the big joker in deck_of_cards two cards down the deck.
    The deck is treated to be circular.

    >>> deck = [5,7,3,2,6,1,9,8,4]
    >>> move_big_joker(deck)
    >>> deck
        [5, 7, 3, 2, 6, 1, 8, 4, 9]

    >>> deck = [14,5,2,12,9,4,7,11,10,1,3,13,6,8,15]
    >>> move_big_joker(deck)
    >>> deck
        [5, 15, 2, 12, 9, 4, 7, 11, 10, 1, 3, 13, 6, 8, 14]

    """

    big_joker = get_big_joker_value(deck_of_cards)
    big_joker_index = deck_of_cards.index(big_joker)
    swap_cards(deck_of_cards, big_joker_index)
    big_joker_index = deck_of_cards.index(big_joker)
    swap_cards(deck_of_cards, big_joker_index)


def triple_cut(deck_of_cards):
    """ (list of int) -> NoneType

    Does a triple cut on deck_of_cards i.e. Swaps the stack of values above
    the first joker with the stack of values below the second joker.

    >>> deck = [5,7,3,2,6,1,4,9,8]
    >>> triple_cut(deck)
    >>> deck
        [9, 8, 5, 7, 3, 2, 6, 1, 4]

    >>> deck = [9,5,2,12,4,14,7,11,10,1,3,15,6,8,13]
    >>> triple_cut(deck)
    >>> deck
        [6, 8, 13, 14, 7, 11, 10, 1, 3, 15, 9, 5, 2, 12, 4]

    """

    small_joker = get_small_joker_value(deck_of_cards)
    big_joker = get_big_joker_value(deck_of_cards)
    small_joker_index = deck_of_cards.index(small_joker)
    big_joker_index = deck_of_cards.index(big_joker)

    # Determines which joker is the first_joker and which joker is the
    # second joker by comparing the position of the jokers.
    if small_joker_index < big_joker_index:
        first_joker = small_joker
        second_joker = big_joker
    else:
        first_joker = big_joker
        second_joker = small_joker

    first_joker_index = deck_of_cards.index(first_joker)
    second_joker_index = deck_of_cards.index(second_joker)

    # Splits the deck into 3 sectors. Combines the 3 sectors in the appropriate
    # order in order to get a triple cut deck.
    top_sector = deck_of_cards[ : first_joker_index]
    middle_sector = deck_of_cards[first_joker_index : second_joker_index + 1]
    bottom_sector = deck_of_cards[second_joker_index + 1 : ]
    triple_cutted_deck = bottom_sector + middle_sector + top_sector

    # Empties the original deck and then extends triple_cutted_deck to the
    # original deck.
    while len(deck_of_cards) != 0:
        deck_of_cards.pop()
    deck_of_cards.extend(triple_cutted_deck)


def insert_top_to_bottom(deck_of_cards):
    """ (list of int) -> NoneType

    Gets the value of the card at the bottom of deck_of_cards. If this value
    is not the big joker then it moves the value number of cards from the
    top of deck_of_cards to the bottom, inserting the stack just above the
    bottom card. If the value is the big joker then it moves the small joker
    value number of cards from the top of deck_of_cards to the bottom,
    inserting the stack just above the bottom card.

    >>> deck = [5,7,3,2,6,1,9,8,4]
    >>> insert_top_to_bottom(deck)
    >>> deck
        [6, 1, 9, 8, 5, 7, 3, 2, 4]

    >>> deck = [9,5,2,12,4,14,7,11,10,1,3,15,6,8,13]
    >>> insert_top_to_bottom(deck)
    >>> deck
        [8, 9, 5, 2, 12, 4, 14, 7, 11, 10, 1, 3, 15, 6, 13]

    """

    # Gets the value of the bottom card and then changes this value if
    # the initial value obtained was the value of the big_joker.
    bottom_card_value = deck_of_cards[-1]

    if bottom_card_value == get_big_joker_value(deck_of_cards):
        number_of_cards = get_small_joker_value(deck_of_cards)
    else:
        number_of_cards = bottom_card_value

    # Splits the deck into 2 sectors and then rearranges the 2 sectors along
    # with the bottom_card_value to get a top_to_bottom_deck.
    top_sector = deck_of_cards[ : number_of_cards]
    bottom_sector = deck_of_cards[number_of_cards : -1]
    top_to_bottom_deck = bottom_sector + top_sector
    top_to_bottom_deck.append(bottom_card_value)

    # Empties the original deck and then extends the top_to_bottom_deck to
    # the original deck.
    while len(deck_of_cards) != 0:
            deck_of_cards.pop()

    deck_of_cards.extend(top_to_bottom_deck)


def get_card_at_top_index(deck_of_cards):
    """ (list of int) -> int

    Gets the value of the card at the top of deck_of_cards.
    Returns the card at the index of that value in deck_of_cards if it is
    not the big joker. If it is the big joker it returns the card at the index
    of the value of the small joker in deck_of_cards.

    >>> deck = [5,7,3,1,6,2,9,8,4]
    >>> get_card_at_top_index(deck_of_cards)
        2

    >>> deck = [15,5,2,12,9,4,7,11,10,1,6,13,14,8,3]
    >>> get_card_at_top_index(deck_of_cards)
        3

    """

    if deck_of_cards[0] == get_big_joker_value(deck_of_cards):
        card_index = get_small_joker_value(deck_of_cards)
    else:
        card_index = deck_of_cards[0]

    card = deck_of_cards[card_index]

    return card


def get_next_keystream_value(deck_of_cards):
    """ (list of int) -> int

    Gets a valid keystream value from deck_of_cards by performing a set of
    steps on deck_of_cards and returns the keystream value.

    >>> deck = [5,7,3,2,6,1,9,8,4]
    >>> get_next_keystream_value(deck)
        1

    >>> deck = [15,5,2,12,9,4,7,11,10,1,3,13,14,8,6]
    >>> get_next_keystream_value(deck)
        6

    """

    key_stream_value = get_big_joker_value(deck_of_cards)

    # Creates a list containing the values of the 2 jokers in the deck.
    jokers = []
    jokers.append(get_big_joker_value(deck_of_cards))
    jokers.append(get_small_joker_value(deck_of_cards))

    # Repeats the steps of the algorithm to generate a key_stream_value
    # until the key_stream_value generated is not a joker.
    while key_stream_value in jokers:
        move_small_joker(deck_of_cards)
        move_big_joker(deck_of_cards)
        triple_cut(deck_of_cards)
        insert_top_to_bottom(deck_of_cards)
        key_stream_value = get_card_at_top_index(deck_of_cards)

    return key_stream_value


def process_messages(deck_of_cards, messages, action):
    """ (list of int, list of str, str) -> list of str

    Performs action (either encryption or decryption)
    on the strings in messages using deck_of_cards. Returns a list of encrypted
    or decrypted strings in the same order that the strings appear in messages.

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
        21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> message = ['How are you ?', 'Great to see you, its been a while !']
    >>> process_messages(deck, messages,'e')
        ['SXTHBDJZB', 'OAPLTRTBYVQXKBQBYCYZTVHYDG']

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
        21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> messages = ['EQFZSRTEAPNXLSRJAMNGAT', 'GLCEGMOTMTRWKHAMGNME']
    >>> process_messages(deck, messages,'d')
        ['THISISITTHEMASTERSWORD', 'NOTHISCANTBEITTOOBAD']

    """

    encrypted_or_decrytpted_messages = []
    message_under_e_or_d = ""

    if action == ENCRYPT:
        for a_message in messages:
            a_clean_message = clean_message(a_message)

            # Iterates through every letter in a_clean_message and encrypts
            # that letter and concatenates it to message_under_e_or_d.
            for letter in a_clean_message:
                keystream_value = get_next_keystream_value(deck_of_cards)
                encrypted_letter = encrypt_letter(letter, keystream_value)
                message_under_e_or_d = message_under_e_or_d + encrypted_letter
            encrypted_or_decrytpted_messages.append(message_under_e_or_d)
            message_under_e_or_d = ""

    elif action == DECRYPT:
        for a_message in messages:
            a_clean_message = clean_message(a_message)

            # Iterates through every letter in a_clean_message and decrypts
            # that letter and concatenates it to message_under_e_or_d.
            for letter in a_clean_message:
                keystream_value = get_next_keystream_value(deck_of_cards)
                decrypted_letter = decrypt_letter(letter, keystream_value)
                message_under_e_or_d = message_under_e_or_d + decrypted_letter
            encrypted_or_decrytpted_messages.append(message_under_e_or_d)
            message_under_e_or_d = ""

    return encrypted_or_decrytpted_messages


def read_messages(file_of_messages):
    """ (file open for reading) -> list of str

    Reads an open file, file_of_messages, and returns a list containing
    every line of that file as a separate item in the list.

    """

    messages = []

    for line in file_of_messages:
        messages.append(line[ : -1])

    return messages


def is_valid_deck(deck_of_cards):
    """ (list of int) -> bool

    Checks whether deck_of_cards contains every integer from 1 to the number
    of values in deck_of_cards.

    >>> deck = [5,7,3,2,6,1,9,8,4]
    >>> is_valid_deck(deck)
        True

    >>> deck = [15,5,2,12,9,4,7,11,10,1,3,13,14,8]
    >>> is_valid_deck(deck)
        False

    """

    integer = 1
    while integer <= len(deck_of_cards):
        if not (integer in deck_of_cards):
            return False
        integer = integer + 1

    return True


def read_deck(deck_file):
    """ (file open for reading) -> list of int

    Reads an open file, deck_of_file, and returns a list of
    all the integers in that file.

    """

    card_deck = []
    number = 0
    digits = 0

    for line in deck_file:
        i = 0
        digit_position = 0
        while i < len(line):
            if not(line[i].isdigit()):
                if digits > 0:
                    number = int(line[digit_position : i])
                    card_deck.append(number)
                    digits = 0
                digit_position = i + 1
            else:
                digits = digits + 1
            i = i + 1

    return card_deck
