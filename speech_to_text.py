# File: speech_to_text.py

import speech_recognition as sr

def speech_to_text():
    """
    Captures audio from the microphone and converts it to text using speech recognition.
    """
    # Initialize recognizer
    recognizer = sr.Recognizer()

    try:
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for speech. Speak now...")
            
            # Capture audio from the microphone
            audio_data = recognizer.listen(source)

            # Recognize speech using Google's Web Speech API
            print("Processing the audio...")
            text = recognizer.recognize_google(audio_data)
            print(f"Recognized text: {text}")
    
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Request failed; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Speech-to-Text program!")
    speech_to_text()
