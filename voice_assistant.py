import speech_recognition as sr
import sounddevice as sd
import pyttsx3
from datetime import datetime
import webbrowser


# Text-to-Speech
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# Voice input
def listen():
    recognizer = sr.Recognizer()

    print("\nListening...")

    try:
        # Record voice from microphone
        audio_data = sd.rec(
            int(5 * 16000),
            samplerate=16000,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        # Convert recording to SpeechRecognition format
        audio = sr.AudioData(
            audio_data.tobytes(),
            16000,
            2
        )

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand. Please try again.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

    except Exception as e:
        print("Error:", e)
        speak("Something went wrong. Please try again.")
        return ""


# Main assistant
def main():

    speak("Hello! I am your voice assistant.")

    while True:

        command = listen()

        # Hello
        if "hello" in command:
            speak("Hello! How can I help you?")

        # Time
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        # Date
        elif "date" in command:
            current_date = datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        # Web search
        elif "search" in command:

            topic = command.replace("search", "").strip()

            if topic:
                speak("Searching for " + topic)

                webbrowser.open(
                    "https://www.google.com/search?q="
                    + topic.replace(" ", "+")
                )

            else:
                speak("Please tell me what you want to search.")

        # Exit
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        # Unknown command
        else:
            speak("I did not understand. Please try again.")


if __name__ == "__main__":
    main()                                                          