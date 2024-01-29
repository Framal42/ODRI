# defs.py
from Packages.texttospeech import *
from Packages.dealwith import *


# This is a simple speech recognition + tts bot to act as your manual reader in keep talking and nobody explodes.
# By Framal


def base_loop():
    # Very scuffed "pre-warm" of playsound, so it doesn't cut my tts. Still got no clue why it does that.
    # output = "test"
    # text_to_speech(output)

    # Lowest level loop, out of game
    running = True
    while running:
        # O.D.R.I: Ordnance Defusal Reference "Intelligence"
        output = """O.D.R.I version 1.0 started. Say start to start a game or any of: 
quit, exit, or stop to close the program."""
        text_to_speech(output)
        request = read_input()
        matches_start = ["start", "bomb", "defusal"]
        matches_quit = ["quit", "exit", "stop"]

        if any(m in request for m in matches_start):
            game_loop()

        elif any(m in request for m in matches_quit):
            running = False
            output = "O.D.R.I shutting down."
            text_to_speech(output)
        else:
            output = "No recognized keywords in your input. Please try again."
            text_to_speech(output)


def game_loop():
    # 2nd lowest level loop, choosing what module to handle.
    game_running = True
    while game_running:
        output = """Bomb defusal in progress. Please state the name of a module or describe it, and I will assist you. 
You can also say: quit, exit, or stop to stop this defusal attempt."""
        text_to_speech(output)
        request = read_input()

        # 0
        matches_quit = [" quit ", " exit ", " stop "]
        # 1
        matches_wires = [" simple wire ", " wire ", " horizontal "]
        # 2
        matches_button = ["button", "large", "cover", "abort", "detonate", "hold"]
        # 3
        matches_keypad = ["keypad", "symbols", "four buttons", "four squares"]
        # 4
        matches_simon = ["simon", "lozenge", "colors", "red", "blue", "yellow", "green"]
        # 5
        matches_first = ["who's on first", "display", "six buttons"]
        # 6
        matches_memory = ["memory", "display", "big display", "four buttons", "five numbers"]
        # 7
        matches_morse = ["morse", "frequency", "hertz", "mhz", "flashing light", "light", "tx"]
        # 8
        matches_complex_wires = ["complex wire", "wire", "vertical", "star"]
        # 9
        matches_sequence_wires = ["wire sequence", "three wire", "wire", " b ", " c "]  # No "a" since "a" is a word
        # 10
        matches_maze = ["maze", "red triangle", "triangle", "green circle", "grid"]
        # 11
        matches_password = ["password", "lock", "submit", "letters"]
        # 12
        matches_gas = ["gas", "question", "yes", "no", " y ", " n "]
        # 13
        matches_capacitor = ["capacitor", "discharge", "lever", "bar"]
        # 14
        matches_knob = ["knob", "turn", "up", "timer", "twelve", "light"]
        # 15 is for failure to match any keywords

        matches_list = [matches_quit, matches_wires, matches_button, matches_keypad, matches_simon, matches_first,
                        matches_memory, matches_morse, matches_complex_wires, matches_sequence_wires, matches_maze,
                        matches_password, matches_gas, matches_capacitor, matches_knob]

        # Counts the number of keywords matched for each module
        module_score_array = module_score_calculator(request, matches_list)
        # If only one module got points in the scoring, select that one. Else ask for clarification.
        selected_module = select_module(module_score_array)
        if selected_module == 0:
            game_running = False
            output = "O.D.R.I stopping defusal attempt. Returning to standby state."
            text_to_speech(output)
        elif selected_module == 15:
            output = "No keywords detected in your input. Please try again with different wording."
            text_to_speech(output)
        elif selected_module == 16:
            output = "Module selection aborted."
            text_to_speech(output)
        else:
            module_dispatch(selected_module)


def module_dispatch(module_num):
    # Simply calls the correct module method for the module selected.
    match module_num:
        case 0:
            raise NameError("Warning: module num 0 entered module_dispatch")
        case 1:
            deal_with_simple_wire()
        case 2:
            deal_with_button()
        case 3:
            deal_with_keypad()
        case 4:
            deal_with_simon()
        case 5:
            deal_with_who_first()
        case 6:
            deal_with_memory()
        case 7:
            deal_with_morse()
        case 8:
            deal_with_complex_wire()
        case 9:
            deal_with_wire_sequence()
        case 10:
            deal_with_maze()
        case 11:
            deal_with_password()
        case 12:
            deal_with_gas()
        case 13:
            deal_with_capacitor()
        case 14:
            deal_with_knob()
        case _:
            raise NameError("No module matched in module_dispatch")


def module_score_calculator(request, matches_list):
    # This function takes a string and an array of arrays of strings.
    # It counts the number of matches to the keywords in the request for each module.
    # Results are returned in an array where index indicates the module.
    score_array = []
    # TODO there has to be a better way to do this
    for matches in matches_list:
        curr_module_score = 0
        for match in matches:
            curr_module_score += request.count(match)
        score_array.append(curr_module_score)
    return score_array


def select_module(module_score_array):
    flagged_modules = []
    index = 0
    for score in module_score_array:
        if score > 0:
            flagged_modules.append(index)
        index += 1

    if len(flagged_modules) == 0:
        return 15  # Failure to match any keywords

    elif len(flagged_modules) == 1:
        output = ("Your description matches the module: " + module_num_to_string(flagged_modules[0]) +
                  " Answer confirm or cancel")
        text_to_speech(output)
        request = read_input()

        if any(m in request for m in [" confirm ", " yes ", " ok "]):
            return flagged_modules[0]
        else:
            return 16

    else:
        text_to_speech("""Your description matches multiple modules. 
Please select from these option by speaking the associated number:""")
        number = 1
        for module in flagged_modules:
            output = str(number) + ": " + module_num_to_string(module)
            text_to_speech(output)
            number += 1

        selecting_flagged_module = True
        request_int = 0
        while selecting_flagged_module:
            request_int = read_input_int()
            if 0 < request_int <= len(flagged_modules):
                selecting_flagged_module = False
            else:
                output = "That number was not an option. Please try again."
                text_to_speech(output)

        return flagged_modules[request_int - 1]


def module_num_to_string(module_num):
    match module_num:
        case 0:
            return "exit"
        case 1:
            return "simple wires. Horizontal, monochrome wires."
        case 2:
            return "button. A single, large button."
        case 3:
            return "keypad. Four strange symbols on a keypad."
        case 4:
            return "simon says. A lozenge with four colors."
        case 5:
            return "who's on first. "
        case 6:
            return "memory. A large display with a number with four smaller buttons."
        case 7:
            return "morse code. A frequency selector and a small button saying tx."
        case 8:
            return "complex wires. Vertical, sometimes multicolored wires."
        case 9:
            return "wire sequence. Three wires that can cross, with labels A B C 1 2 3."
        case 10:
            return "maze. A grid of light gray squares with green circles and a red triangle."
        case 11:
            return "password. Five letter selectors."
        case 12:
            return "gas. A display with a question and yes and no buttons."
        case 13:
            return "capacitor. A lever, some wiring and a horizontal bar filling up."
        case 14:
            return "knob. A selector with up writen on it and 12 lights."
        case _:
            return "Module number to string method failed. This should not happen. Please file a bug report."
