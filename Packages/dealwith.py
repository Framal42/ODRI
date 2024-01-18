from Packages.texttospeech import *


# This is a simple speech recognition + tts bot to act as your manual reader in keep talking and nobody explodes.
# By Framal


def deal_with_simple_wire():
    # module 1
    module_active = True
    while module_active:
        text_to_speech("""Please read out the color of the wires in order. Recognized colors are: white, blue,
red, yellow, black.""")
        request = read_input()
        print(request)
        request_array = request.split(" ")
        print(request_array)
        matches = ["white", "blue", "red", "yellow", "black"]
        request_array_sanitized = []
        for word in request_array:
            if word in matches:
                request_array_sanitized.append(word)
        print(request_array_sanitized)
        match len(request_array_sanitized):
            case 3:
                if "red" not in request_array_sanitized:
                    text_to_speech("""Cut the second wire.""")

                elif request_array_sanitized[2] == "white":
                    text_to_speech("""Cut the last wire.""")

                elif request_array_sanitized.count("blue") > 1:
                    text_to_speech("""Cut the last blue wire.""")

                else:
                    text_to_speech("""Cut the last wire.""")

                module_active = False
            case 4:
                odd = serial_number_odd()
                if (request_array_sanitized.count("red") > 1) and odd:
                    text_to_speech("""Cut the last red wire.""")

                elif (request_array_sanitized[3] == "yellow") and ("red" not in request_array_sanitized):
                    text_to_speech("""Cut the last wire.""")

                elif request_array_sanitized.count("blue") == 1:
                    text_to_speech("""Cut the first wire.""")

                elif request_array_sanitized.count("yellow") > 1:
                    text_to_speech("""Cut the last wire.""")

                else:
                    text_to_speech("""Cut the second wire.""")

                module_active = False
            case 5:
                odd = serial_number_odd()
                if request_array_sanitized[4] == "black" and odd:
                    text_to_speech("""Cut the fourth wire.""")

                elif (request_array_sanitized.count("red") == 1) and (request_array_sanitized.count("yellow") > 1):
                    text_to_speech("""Cut the first wire.""")

                elif "black" not in request_array_sanitized:
                    text_to_speech("""Cut the second wire.""")

                else:
                    text_to_speech("""Cut the first wire.""")

                module_active = False
            case 6:
                odd = serial_number_odd()
                if "yellow" not in request_array_sanitized and odd:
                    text_to_speech("""Cut the third wire.""")

                elif (request_array_sanitized.count("yellow") == 1) and (request_array_sanitized.count("white") > 1):
                    text_to_speech("""Cut the fourth wire.""")

                elif "red" not in request_array_sanitized:
                    text_to_speech("Cut the last wire.")

                else:
                    text_to_speech("""Cut the fourth wire.""")

                module_active = False
            case _:
                text_to_speech("""The number of wires spoken is not valid. Please try again.""")


def deal_with_button():
    # 2
    text_to_speech("""Please state the color and text on the button.""")
    request = read_input()
    matches_color = [" white ", " red ", " blue ", " yellow "]
    matches_text = [" abort ", " detonate ", " hold "]
    button_color = ""
    button_text = ""

    for match in matches_color:
        if match in request:
            button_color = match.split(" ")[1]

    for match in matches_text:
        if match in request:
            button_text = match.split(" ")[1]

    if button_color == "blue" and button_text == "abort":
        deal_with_held_button()
        return

    batteries_num = number_of_batteries()

    if button_text == "detonate" and batteries_num > 1:
        text_to_speech("""Press and immediately release the button.""")
        return

    if button_color == "white" and lit_car_indicator():
        deal_with_held_button()
        return

    if batteries_num > 2 and lit_frk_indicator():
        text_to_speech("""Press and immediately release the button.""")
        return

    if button_color == "yellow":
        deal_with_held_button()
        return

    if button_color == "red" and button_text == "hold":
        text_to_speech("""Press and immediately release the button.""")
        return

    deal_with_held_button()
    return


def deal_with_held_button():
    text_to_speech("""Please keep the button held. What color is the light strip?""")
    request = read_input()
    matches = [" blue ", " white ", " yellow "]
    strip_color = "other"
    for match in matches:
        if match in request:
            strip_color = match.split(" ")[1]
    match strip_color:
        case "blue":
            text_to_speech("""When the countdown timer has 4 in any position, release the button.""")
            return
        case "white":
            text_to_speech("""When the countdown timer has 1 in any position, release the button.""")
            return
        case "yellow":
            text_to_speech("""When the countdown timer has 5 in any position, release the button.""")
            return
        case "other":
            text_to_speech("""When the countdown timer has 1 in any position, release the button.""")
            return
        case _:
            text_to_speech("""Fatal error in deal with held button. Please file a bug report.""")
            raise NameError("Fatal Error in deal_with_held_button")


def deal_with_keypad():
    # 3
    symbols_array = [[" o with a bar ", " q ", " magnifying glass "],  # 0
                     [" pyramid ", " A "],  # 1
                     [" lambda ", " n with bar "],  # 2
                     [" weird n ", " sideways n ", " zig zag "],  # 3
                     [" sideways t ", " triangle ", " strange "],  # 4
                     [" h "],  # 5
                     [" reverse c "],  # 6
                     [" reverse e ", " reverse epsilon ", " diaeresis "],  # 7
                     [" loop ", " c q "],  # 8
                     [" white star ", " empty star "],  # 9
                     [" question ", " mark "],  # 10
                     [" copyright "],  # 11
                     [" comma ", " cat ", " cat's "],  # 12
                     [" i k ", " i ", " k "],  # 13
                     [" r ", " unfinished three "],  # 14
                     [" six ", " 6 "],  # 15
                     [" paragraph ", " p "],  # 16
                     [" b ", " upside down p "],  # 17
                     [" smile ", " smiley "],  # 18
                     [" psi ", " chandelier ", " candelabra "],  # 19
                     [" c with a dot ", " c "],  # 20
                     [" three ", " 3 ", " antenna ", "antennae"],  # 21
                     [" black star ", " filled star "],  # 22
                     [" not equal ", " ki "],  # 23
                     [" a e ", " ae "],  # 24
                     [" capital n ", " large n "],  # 25
                     [" omega "]]  # 26

    # Hardcoded columns in the manual
    columns_array = [[0, 1, 2, 3, 4, 5, 6],
                     [7, 0, 6, 8, 9, 5, 10],
                     [11, 12, 8, 13, 14, 2, 9],
                     [15, 16, 17, 4, 13, 10, 18],
                     [19, 18, 17, 20, 16, 21, 22],
                     [15, 7, 23, 24, 19, 25, 26]]

    text_to_speech("""Please list the four symbols on the keypad. If you need a refresher of the names of symbols,
say help. Caution, this takes a while.""")
    request = read_input()
    if " help " in request:
        for index, symbols in enumerate(symbols_array):
            text_to_speech("symbol " + str(index) + ": " + " : ".join(symbols))
        text_to_speech("""Please list the four symbols on the keypad.""")
        request = read_input()

    request_sanitized = []
    for index, array in enumerate(symbols_array):
        if any(m in request for m in array):
            request_sanitized.append(index)
    request_sanitized = set(request_sanitized)
    if len(request_sanitized) != 4:
        while len(request_sanitized) != 4:
            if len(request_sanitized) < 4:
                while len(request_sanitized) < 4:
                    text_to_speech("""Only these symbols were recognized: """)
                    for index, symbol_index in enumerate(request_sanitized):
                        text_to_speech(str(index + 1) + ": " + symbols_array[symbol_index][0])
                    text_to_speech("""Please speak the missing symbols or help.""")
                    request = read_input()
                    if " help " in request:
                        for index, symbols in enumerate(symbols_array):
                            text_to_speech("symbol " + index + ": " + " : ".join(symbols))
                    else:
                        for index, array in enumerate(symbols_array):
                            if any(m in request for m in array):
                                request_sanitized.add(index)

            elif len(request_sanitized) > 4:
                while len(request_sanitized) > 4:
                    text_to_speech("""Too many symbols were recognized: """)
                    for index, symbol_index in enumerate(request_sanitized):
                        text_to_speech(str(index + 1) + ": " + symbols_array[symbol_index][0])
                    text_to_speech("""Please speak the symbols to remove.""")
                    request = read_input()

                    # if " help " in request:
                    #     text_to_speech("""These are the symbols currently selected: """)
                    #     for index, symbols_index in enumerate(request_sanitized):
                    #         text_to_speech(index + ": " + symbols_array[symbol_index][0])
                    # else:

                    for index, array in enumerate(symbols_array):
                        if any(m in request for m in array):
                            request_sanitized.remove(index)

    for index, column in enumerate(columns_array):
        if request_sanitized.issubset(column):
            text_to_speech("""Column found. Press the buttons in this order,
ignoring symbols you do not recognize:""")
            for symbol in column:
                text_to_speech(symbols_array[symbol][0])
            break
            return
    text_to_speech("""No corresponding column found. Exiting.""")


def deal_with_simon():
    # 4
    return


def deal_with_who_first():
    # 5
    return


def deal_with_memory():
    # 6
    return


def deal_with_morse():
    # 7
    return


def deal_with_complex_wire():
    # 8
    return


def deal_with_wire_sequence():
    # 9
    return


def deal_with_maze():
    # 10
    return


def deal_with_password():
    # 11
    return


def deal_with_gas():
    # 12
    return


def deal_with_capacitor():
    # 13
    return


def deal_with_knob():
    # 14
    return


def serial_number_odd():
    output = """Is the last digit of the serial number odd?"""
    text_to_speech(output)

    request = input("Input: ")
    request = request.lower()

    if any(m in request for m in ["yes", "confirm", "correct"]):
        return True
    else:
        return False


def number_of_batteries():
    text_to_speech("""How many batteries are there on the bomb?""")
    request_int = read_input_int()
    return request_int


def lit_car_indicator():
    text_to_speech("""Is there a lit indicator with label C A R anywhere on the bomb?""")
    request = read_input()
    matches = [" yes ", " correct ", " indeed ", " confirm "]
    if any(m in request for m in matches):
        return True
    else:
        return False


def lit_frk_indicator():
    text_to_speech("""Is there a lit indicator with label F R K anywhere on the bomb?""")
    request = read_input()
    matches = [" yes ", " correct ", " indeed ", " confirm "]
    if any(m in request for m in matches):
        return True
    else:
        return False
