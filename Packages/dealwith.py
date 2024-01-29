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

    text_to_speech("""No corresponding column found. Exiting.""")


def deal_with_simon():
    # 4
    text_to_speech("""Please speak the number of strikes or fails so far.""")
    while True:
        strikes_num = read_input_int()
        if 0 <= strikes_num <= 2:
            break
        else:
            text_to_speech("""Invalid number of strikes.""")
    color_not_found = True
    request_sanitized = []
    while color_not_found:
        text_to_speech("""Please state the color of the flashing button.""")
        request = read_input()
        request_sanitized = []
        matches = [" red ", " blue ", " green ", " yellow "]
        for index, match in enumerate(matches):
            if match in request:
                request_sanitized.append(match)
        if len(request_sanitized) != 1:
            text_to_speech("""Invalid input. Try again.""")
        else:
            color_not_found = False
    match strikes_num:
        case 0:
            match request_sanitized[0]:
                case 0:
                    text_to_speech("""Press the blue button, then simply copy the pattern that plays.""")
                case 1:
                    text_to_speech("""Press the yellow button,then simply copy the pattern that plays.""")
                case 2:
                    text_to_speech("""Press the green button, then simply copy the pattern that plays.""")
                case 3:
                    text_to_speech("""Press the red button, then simply copy the pattern that plays.""")
        case 1:
            match request_sanitized[0]:
                case 0:
                    text_to_speech("""Press the red button, then simply copy the pattern that plays.""")
                case 1:
                    text_to_speech("""Press the blue button,then simply copy the pattern that plays.""")
                case 2:
                    text_to_speech("""Press the yellow button, then simply copy the pattern that plays.""")
                case 3:
                    text_to_speech("""Press the green button, then simply copy the pattern that plays.""")
        case 2:
            match request_sanitized[0]:
                case 0:
                    text_to_speech("""Press the yellow button, then simply copy the pattern that plays.""")
                case 1:
                    text_to_speech("""Press the green button,then simply copy the pattern that plays.""")
                case 2:
                    text_to_speech("""Press the blue button, then simply copy the pattern that plays.""")
                case 3:
                    text_to_speech("""Press the red button, then simply copy the pattern that plays.""")


def deal_with_who_first():
    # 5

    # reference array
    step_1_display_array = [(" yes ", "middle left"),
                            (" first ", "top right"),
                            (" display ", "bottom right"),
                            (" okay ", "top right"),
                            (" says ", "bottom right"),
                            (" nothing ", "middle left"),
                            (" black ", "bottom left"),  # blank display
                            (" blank ", "middle right"),
                            (" no ", "bottom right"),
                            (" led ", "middle left"),   # Same pronunciation warning, handle
                            (" lead ", "bottom right"),
                            (" leed ", "bottom left"),
                            (" read ", "middle right"),  # same pronunciation warning, handle by giving
                            (" red ", "middle right"),   # options and spelling
                            (" reed ", "bottom left"),
                            (" hold on ", "bottom right"),
                            (" you are ", "bottom right"),
                            (" you ", "middle right"),
                            (" your ", "middle right"),   # Same pronunciation warning
                            (" you're ", "middle right"),
                            (" ur ", "top left"),
                            (" there ", "bottom right"),  # Same pronunciation warning
                            (" they're ", "bottom left"),
                            (" their ", "middle right"),
                            (" they are ", "middle left"),
                            (" see ", "bottom right"),   # Same pronunciation warning
                            (" c ", "top right"),
                            (" cee ", "bottom right")]

    step_2_display_array = [(" ready ", ["YES", "OKAY", "WHAT", "MIDDLE", "LEFT", "PRESS", "RIGHT", "BLANK", "READY",
                                         "NO", "FIRST", "UHHH", "NOTHING", "WAIT"]),
                            (" first ", ["LEFT", "OKAY", "YES", "MIDDLE", "NO", "RIGHT", "NOTHING", "UHHH", "WAIT",
                                         "READY", "BLANK", "WHAT", "PRESS", "FIRST"]),
                            (" no ", ["BLANK", "UHHH", "WAIT", "FIRST", "WHAT", "READY", "RIGHT", "YES", "NOTHING",
                                      "LEFT", "PRESS", "OKAY", "NO", "MIDDLE"]),
                            (" blank ", ["WAIT", "RIGHT", "OKAY", "MIDDLE", "BLANK", "PRESS", "READY", "NOTHING", "NO",
                                         "WHAT", "LEFT", "UHHH", "YES", "FIRST"]),
                            (" nothing ", ["UHHH", "RIGHT", "OKAY", "MIDDLE", "YES", "BLANK", "NO", "PRESS", "LEFT",
                                           "WHAT", "WAIT", "FIRST", "NOTHING", "READY"]),
                            (" yes ", ["OKAY", "RIGHT", "UHHH", "MIDDLE", "FIRST", "WHAT", "PRESS", "READY", "NOTHING",
                                       "YES", "LEFT", "BLANK", "NO", "WAIT"]),
                            (" what ", ["UHHH", "WHAT", "LEFT", "NOTHING", "READY", "BLANK", "MIDDLE", "NO", "OKAY",
                                        "FIRST", "WAIT", "YES", "PRESS", "RIGHT"]),
                            # To catch all possible lenghts of uh.
                            # TODO make sure this works when implementing voice input
                            (" uh", ["READY", "NOTHING", "LEFT", "WHAT", "OKAY", "YES", "RIGHT", "NO", "PRESS",
                                     "BLANK", "UHHH", "MIDDLE", "WAIT", "FIRST"]),
                            (" left ", ["RIGHT", "LEFT", "FIRST", "NO", "MIDDLE", "YES", "BLANK", "WHAT", "UHHH",
                                        "WAIT", "PRESS", "READY", "OKAY", "NOTHING"]),
                            (" right ", ["YES", "NOTHING", "READY", "PRESS", "NO", "WAIT", "WHAT", "RIGHT", "MIDDLE",
                                         "LEFT", "UHHH", "BLANK", "OKAY", "FIRST"]),
                            (" middle ", ["BLANK", "READY", "OKAY", "WHAT", "NOTHING", "PRESS", "NO", "WAIT", "LEFT",
                                          "MIDDLE", "RIGHT", "FIRST", "UHHH", "YES"]),
                            (" okay ", ["MIDDLE", "NO", "FIRST", "YES", "UHHH", "NOTHING", "WAIT", "OKAY", "LEFT",
                                        "READY", "BLANK", "PRESS", "WHAT", "RIGHT"]),
                            (" wait ", ["UHHH", "NO", "BLANK", "OKAY", "YES", "LEFT", "FIRST", "PRESS", "WHAT", "WAIT",
                                        "NOTHING", "READY", "RIGHT", "MIDDLE"]),
                            (" press ", ["RIGHT", "MIDDLE", "YES", "READY", "PRESS", "OKAY", "NOTHING", "UHHH", "BLANK",
                                         "LEFT", "FIRST", "WHAT", "NO", "WAIT"]),
                            (" you ", ["SURE", "YOU ARE", "YOUR", "YOU\'RE", "NEXT", "UH HUH", "UR", "HOLD", "WHAT?",
                                       "YOU", "UH UH", "LIKE", "DONE", "U"]),
                            (" you are ", ["YOUR", "NEXT", "LIKE", "UH HUH", "WHAT?", "DONE", "UH UH", "HOLD", "YOU",
                                           "U", "YOU\'RE", "SURE", "UR", "YOU ARE"]),
                            (" your ", ["UH UH", "YOU ARE", "UH HUH", "YOUR", "NEXT", "UR", "SURE", "U", "YOU\'RE",
                                        "YOU", "WHAT?", "HOLD", "LIKE", "DONE"]),
                            (" you\'re ", ["YOU", "YOU\'RE", "UR", "NEXT", "UH UH", "YOU ARE", "U", "YOUR", "WHAT?",
                                           "UH HUH", "SURE", "DONE", "LIKE", "HOLD"]),
                            (" ur ", ["DONE", "U", "UR", "UH HUH", "WHAT?", "SURE", "YOUR", "HOLD", "YOU\'RE", "LIKE",
                                      "NEXT", "UH UH", "YOU ARE", "YOU"]),
                            (" u ", ["UH HUH", "SURE", "NEXT", "WHAT?", "YOU\'RE", "UR", "UH UH", "DONE", "U", "YOU",
                                     "LIKE", "HOLD", "YOU ARE", "YOUR"]),
                            (" uh huh ", ["UH HUH", "YOUR", "YOU ARE", "YOU", "DONE", "HOLD", "UH UH", "NEXT", "SURE",
                                          "LIKE", "YOU\'RE", "UR", "U", "WHAT?"]),
                            (" uh uh ", ["UR", "U", "YOU ARE", "YOU\'RE", "NEXT", "UH UH", "DONE", "YOU", "UH HUH",
                                         "LIKE", "YOUR", "SURE", "HOLD", "WHAT?"]),
                            (" what ", ["YOU", "HOLD", "YOU\'RE", "YOUR", "U", "DONE", "UH UH", "LIKE", "YOU ARE",
                                        "UH HUH", "UR", "NEXT", "WHAT?", "SURE"]),
                            (" done ", ["SURE", "UH HUH", "NEXT", "WHAT?", "YOUR", "UR", "YOU\'RE", "HOLD", "LIKE",
                                        "YOU", "U", "YOU ARE", "UH UH", "DONE"]),
                            (" next ", ["WHAT?", "UH HUH", "UH UH", "YOUR", "HOLD", "SURE", "NEXT", "LIKE", "DONE",
                                        "YOU ARE", "UR", "YOU\'RE", "U", "YOU"]),
                            (" hold ", ["YOU ARE", "U", "DONE", "UH UH", "YOU", "UR", "SURE", "WHAT?", "YOU\'RE",
                                        "NEXT", "HOLD", "UH HUH", "YOUR", "LIKE"]),
                            (" sure ", ["YOU ARE", "DONE", "LIKE", "YOU\'RE", "YOU", "HOLD", "UH HUH", "UR", "SURE",
                                        "U", "WHAT?", "NEXT", "YOUR", "UH UH"]),
                            (" like ", ["YOU\'RE", "NEXT", "U", "UR", "HOLD", "DONE", "UH UH", "WHAT?", "UH HUH", "YOU",
                                        "LIKE", "SURE", "YOU ARE", "YOUR"])]

    text_to_speech("""Please read the word on the top display. If there is no word, say: black.""")
    # Get the last word in input that matches
    while True:
        request = read_input()

        request_sanitized_array = []

        for elem in step_1_display_array:
            word = elem[0]
            if word in request:
                request_sanitized_array.append(word)
        if len(request_sanitized_array) > 0:
            request_sanitized = request_sanitized_array[-1]
            break
        else:
            text_to_speech("No valid words recognized, try again.")

    # Deal with same pronunciation first
    if request_sanitized == " led " or request_sanitized == " lead " or request_sanitized == " leed ":
        while True:
            text_to_speech("""Did you mean: 1: l e d. 2: l e a d. 3: l e e d.""")
            request_int = read_input_int()
            if request_int == 1:
                for elem in step_1_display_array:
                    if elem[0] == " led ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 2:
                for elem in step_1_display_array:
                    if elem[0] == " lead ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 3:
                for elem in step_1_display_array:
                    if elem[0] == " leed ":
                        text_to_speech("Read out the " + elem[1] + " word.")

    elif request_sanitized == " led " or request_sanitized == " lead " or request_sanitized == " leed ":
        while True:
            text_to_speech("""Did you mean: 1: r e d. 2: r e a d. 3: r e e d.""")
            request_int = read_input_int()
            if request_int == 1:
                for elem in step_1_display_array:
                    if elem[0] == " red ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 2:
                for elem in step_1_display_array:
                    if elem[0] == " read ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 3:
                for elem in step_1_display_array:
                    if elem[0] == " reed ":
                        text_to_speech("Read out the " + elem[1] + " word.")

    elif request_sanitized == " your " or request_sanitized == " you're " or request_sanitized == " ur ":
        while True:
            text_to_speech("""Did you mean: 1: y o u r. 2: y o u \' r e. 3: u r.""")
            request_int = read_input_int()
            if request_int == 1:
                for elem in step_1_display_array:
                    if elem[0] == " your ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 2:
                for elem in step_1_display_array:
                    if elem[0] == " you're ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 3:
                for elem in step_1_display_array:
                    if elem[0] == " ur ":
                        text_to_speech("Read out the " + elem[1] + " word.")

    elif request_sanitized == " there " or request_sanitized == " they're " or request_sanitized == " their ":
        while True:
            text_to_speech("""Did you mean: 1: t h e r e. 2: t h e y ' r e. 3: t h e i r.""")
            request_int = read_input_int()
            if request_int == 1:
                for elem in step_1_display_array:
                    if elem[0] == " there ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 2:
                for elem in step_1_display_array:
                    if elem[0] == " they're ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 3:
                for elem in step_1_display_array:
                    if elem[0] == " their ":
                        text_to_speech("Read out the " + elem[1] + " word.")

    elif request_sanitized == " see " or request_sanitized == " c " or request_sanitized == " cee ":
        while True:
            text_to_speech("""Did you mean: 1: s e e. 2: c ' r e. 3: c e e.""")
            request_int = read_input_int()
            if request_int == 1:
                for elem in step_1_display_array:
                    if elem[0] == " see ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 2:
                for elem in step_1_display_array:
                    if elem[0] == " c ":
                        text_to_speech("Read out the " + elem[1] + " word.")
            elif request_int == 3:
                for elem in step_1_display_array:
                    if elem[0] == " cee ":
                        text_to_speech("Read out the " + elem[1] + " word.")

    # Now deal with the rest
    else:
        text_to_speech("I have heard the word: " + request_sanitized)
        for elem in step_1_display_array:
            if request_sanitized in elem[0]:
                text_to_speech("Read out the " + elem[1] + " word.")

    # Deal with step 2
    while True:
        request = read_input()

        request_sanitized_array = []
        for elem in step_2_display_array:
            word = elem[0]
            if word in request:
                request_sanitized_array.append(word)
        if len(request_sanitized_array) > 0:
            request_sanitized = request_sanitized_array[-1]
            break
        else:
            text_to_speech("No valid words recognized, try again.")

    # Deal with same pronunciation of step 2 words
    if (request_sanitized == " uh" or request_sanitized == " uh uh " or request_sanitized == " uh huh "
            or request_sanitized == " u " or request_sanitized == " you "):
        while True:
            text_to_speech("""Did you mean: 1: u h h h. 2: u h  u h. 3: u h h u h. 4: u 5: y o u""")
            request_int = read_input_int()
            if request_int == 1:
                for elem in step_2_display_array:
                    if elem[0] == " uh":
                        text_to_speech("Press the first button that matches one of these words: ")
                        for word in elem[1]:
                            text_to_speech(word)
            elif request_int == 2:
                for elem in step_2_display_array:
                    if elem[0] == " uh uh ":
                        text_to_speech("Press the first button that matches one of these words: ")
                        for word in elem[1]:
                            text_to_speech(word)
            elif request_int == 3:
                for elem in step_2_display_array:
                    if elem[0] == " uh huh ":
                        text_to_speech("Press the first button that matches one of these words: ")
                        for word in elem[1]:
                            text_to_speech(word)
            elif request_int == 4:
                for elem in step_2_display_array:
                    if elem[0] == " u ":
                        text_to_speech("Press the first button that matches one of these words: ")
                        for word in elem[1]:
                            text_to_speech(word)
            elif request_int == 5:
                for elem in step_2_display_array:
                    if elem[0] == " you ":
                        text_to_speech("Press the first button that matches one of these words: ")
                        for word in elem[1]:
                            text_to_speech(word)

    elif request_sanitized == " your " or request_sanitized == " you're " or request_sanitized == " ur ":
        while True:
            text_to_speech("""Did you mean: 1: y o u r. 2: y o u \' r e. 3: u r.""")
            request_int = read_input_int()
            if request_int == 1:
                for elem in step_2_display_array:
                    if elem[0] == " your ":
                        text_to_speech("Press the first button that matches one of these words: ")
                        for word in elem[1]:
                            text_to_speech(word)
            elif request_int == 2:
                for elem in step_2_display_array:
                    if elem[0] == " you\'re ":
                        text_to_speech("Press the first button that matches one of these words: ")
                        for word in elem[1]:
                            text_to_speech(word)
            elif request_int == 3:
                for elem in step_2_display_array:
                    if elem[0] == " ur ":
                        text_to_speech("Press the first button that matches one of these words: ")
                        for word in elem[1]:
                            text_to_speech(word)

    else:
        for elem in step_2_display_array:
            if elem[0] == request_sanitized:
                text_to_speech("Press the first button that matches one of these words: ")
                for word in elem[1]:
                    text_to_speech(word)


def deal_with_memory():
    # 6

    # Array of tuples, format (position, value)
    pressed_buttons = []
    # Stage 1
    while True:
        text_to_speech("Please read out the number on the display." +
                       "Make sure to remember the position and values of the buttons you press," +
                       " as ODRI can only help occasionally.")
        request_int = read_input_int()


        if request_int == 1:
            text_to_speech("Press the button in the 2 position.")
            pressed_buttons.append(("2", None))
            break
        elif request_int == 2:
            text_to_speech("Press the button in the 2 position.")
            pressed_buttons.append(("2", None))
            break
        elif request_int == 3:
            text_to_speech("Press the button in the 3 position.")
            pressed_buttons.append(("3", None))
            break
        elif request_int == 4:
            text_to_speech("Press the button in the 4 position.")
            pressed_buttons.append(("4", None))
            break

    # Stage 2
    while True:
        text_to_speech("Please read out the number on the display.")
        request_int = read_input_int()

        if request_int == 1:
            text_to_speech("Press the button labeled 4")
            pressed_buttons.append((None, "4"))
            break
        elif request_int == 2:
            if pressed_buttons[0][0] is not None:
                text_to_speech("Press the button in the " + pressed_buttons[0][0] + " position")
                pressed_buttons.append((pressed_buttons[0][0], None))
            else:
                text_to_speech("Press the button in the same position as stage 1.")
            break
        elif request_int == 3:
            text_to_speech("Press the button in the 1 position.")
            pressed_buttons.append(("1", None))
            break
        elif request_int == 4:
            if pressed_buttons[0][0] is not None:
                text_to_speech("Press the button in the " + pressed_buttons[0][0] + " position")
                pressed_buttons.append((pressed_buttons[0][0], None))
            else:
                text_to_speech("Press the button in the same position as stage 1.")
            break

    # Stage 3
    while True:
        text_to_speech("Please read out the number on the display.")
        request_int = read_input_int()

        if request_int == 1:
            if pressed_buttons[1][1] is not None:
                text_to_speech("Press the button with the " + pressed_buttons[1][1] + " label")
                pressed_buttons.append((None, pressed_buttons[1][1]))
            else:
                text_to_speech("Press the button with the same label as stage 2.")
            break
        elif request_int == 2:
            if pressed_buttons[0][1] is not None:
                text_to_speech("Press the button with the " + pressed_buttons[0][1] + " label")
                pressed_buttons.append((None, pressed_buttons[0][1]))
            else:
                text_to_speech("Press the button with the same label as stage 1.")
            break
        elif request_int == 3:
            text_to_speech("Press the button in the 3 position.")
            pressed_buttons.append(("3", None))
            break
        elif request_int == 4:
            text_to_speech("Press the button with the 4 label.")
            pressed_buttons.append((None, "4"))
            break

    # Stage 4
    while True:
        text_to_speech("Please read out the number on the display.")
        request_int = read_input_int()
        if request_int == 1:
            if pressed_buttons[0][0] is not None:
                text_to_speech("Press the button in the " + pressed_buttons[0][0] + " position")
                pressed_buttons.append((pressed_buttons[0][0], None))
            else:
                text_to_speech("Press the button in the same position as stage 1.")
            break
        elif request_int == 2:
            text_to_speech("Press the button in the 1 position.")
            pressed_buttons.append(("1", None))
            break
        elif request_int == 3:
            if pressed_buttons[1][0] is not None:
                text_to_speech("Press the button in the " + pressed_buttons[1][0] + " position")
                pressed_buttons.append((pressed_buttons[1][0], None))
            else:
                text_to_speech("Press the button in the same position as stage 2.")
            break
        elif request_int == 4:
            if pressed_buttons[1][0] is not None:
                text_to_speech("Press the button in the " + pressed_buttons[1][0] + " position")
                pressed_buttons.append((pressed_buttons[1][0], None))
            else:
                text_to_speech("Press the button in the same position as stage 2.")
            break

    # Stage 5
        while True:
            text_to_speech("Please read out the number on the display.")
            request_int = read_input_int()
            if request_int == 1:
                if pressed_buttons[0][1] is not None:
                    text_to_speech("Press the button with the " + pressed_buttons[0][1] + " label")
                    pressed_buttons.append((None, pressed_buttons[0][1]))
                else:
                    text_to_speech("Press the button with the same label as stage 1.")
                break
            elif request_int == 2:
                if pressed_buttons[1][1] is not None:
                    text_to_speech("Press the button with the " + pressed_buttons[1][1] + " label")
                    pressed_buttons.append((None, pressed_buttons[1][1]))
                else:
                    text_to_speech("Press the button with the same label as stage 2.")
                break
            elif request_int == 3:
                if pressed_buttons[3][1] is not None:
                    text_to_speech("Press the button with the " + pressed_buttons[3][1] + " label")
                    pressed_buttons.append((None, pressed_buttons[3][1]))
                else:
                    text_to_speech("Press the button with the same label as stage 4.")
                break
            elif request_int == 4:
                if pressed_buttons[2][1] is not None:
                    text_to_speech("Press the button with the " + pressed_buttons[2][1] + " label")
                    pressed_buttons.append((None, pressed_buttons[2][1]))
                else:
                    text_to_speech("Press the button with the same label as stage 3.")
                break


def deal_with_morse():
    # 7

    return


def deal_with_complex_wire():
    # 8

    return


def deal_with_wire_sequence():
    # 9
    red_wire_occurrences = ["C", "B", "A", "A or C", "B", "A or C", "A or B or C", "A or B", "B"]
    blue_wire_occurrences = ["B", "A or C", "B", "A", "B", "B or C", "C", "A or C", "A"]
    black_wire_occurrences = ["A or B or C", "A or C", "B", "A or C", "B", "B or C", "A or B", "C", "C"]

    possible_wires = ["red", "blue", "black"]

    red_wires_seen = 0
    blue_wires_seen = 0
    black_wires_seen = 0
    for i in range(1, 4):
        text_to_speech("""Please state the color of the three wires in order.""")
        request = read_input()
        request_sanitized = request.split(" ")
        request_sanitized.pop(0)
        request_sanitized.pop(-1)
        for word in request_sanitized:
            if word not in possible_wires:
                request_sanitized.remove(word)

        j = 0
        ref_number = ["first", "second", "third"]

        for wire in request_sanitized:
            if wire == "red":
                red_wires_seen += 1
                text_to_speech("Cut the " + ref_number[j] + " wire if connected to " + red_wire_occurrences[red_wires_seen-1])
            if wire == "blue":
                blue_wires_seen += 1
                text_to_speech("Cut the " + ref_number[j] + " wire if connected to " + blue_wire_occurrences[blue_wires_seen - 1])
            if wire == "black":
                black_wires_seen += 1
                text_to_speech("Cut the " + ref_number[j] + " wire if connected to " + black_wire_occurrences[black_wires_seen - 1])
            j += 1

        if i != 3:
            text_to_speech("""Go to the next panel""")

    return


def deal_with_maze():
    # 10

    return


def deal_with_password():
    # 11

    return


def deal_with_gas():
    # 12
    text_to_speech("""Respond to the questions before the timer runs out. This module cannot be defused,
     instead you must deal with it periodically until all other modules are defused.""")
    return


def deal_with_capacitor():
    # 13
    text_to_speech("""Discharge the capacitor before it fills up by pulling down the lever. This module cannot be defused,
    instead you must deal with it periodically until all other modules are defused.""")
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
