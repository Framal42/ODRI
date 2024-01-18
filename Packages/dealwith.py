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

        request_array = request.split(" ")
        matches = [" white ", " blue ", " red ", " yellow ", " black "]
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
    car_indicator = lit_car_indicator()

    if button_text == "detonate" and batteries_num > 1:
        text_to_speech("""Press and immediately release the button.""")
        return

    if button_color == "white" and car_indicator:
        deal_with_held_button()
        return

    frk_indicator = lit_frk_indicator()

    if batteries_num > 2 and frk_indicator:
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
    return


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
    text_to_speech("""Is there a lit indcator with label F R K anywhere on the bomb?""")
    request = read_input()
    matches = [" yes ", " correct ", " indeed ", " confirm "]
    if any(m in request for m in matches):
        return True
    else:
        return False
    