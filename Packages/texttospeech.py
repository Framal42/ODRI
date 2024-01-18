from gtts import gTTS
from playsound import playsound


# This is a simple speech recognition + tts bot to act as your manual reader in keep talking and nobody explodes.
# By Framal


def text_to_speech(text):
    try:
        print(text)
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save("output.mp3")
        playsound("output.mp3")
    except Exception as e:
        print(f"Error: {str(e)}")


def read_input():
    request = input("Input: ")
    request = " " + request.lower() + " "
    return request


def read_input_int():
    no_valid_input = True

    # Just to shut up the warning, this should never be used. It is set to 1000 so its obvious if it is used
    request_int = 1000
    while no_valid_input:
        request = read_input()

        # Take the last word/single thing
        request = request.split(" ")[-1]
        try:
            request_int = int(request)
            no_valid_input = False
        except ValueError:
            text_to_speech("""I did not recognize that as a number. Please try again.""")
    return request_int
