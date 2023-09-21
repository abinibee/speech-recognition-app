import streamlit as st
import speech_recognition as sr
import pyttsx3
import time
import pandas as pd

# Create a function for Speech Trancription
def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:

        # create a streamlit spinner that shows progress
        with st.spinner(text='Silence pls, Caliberating background noise.....'):
            time.sleep(2)

        r.adjust_for_ambient_noise(source, duration = 1) # ..... Adjust the sorround noise
        st.info("Speak now...")

        audio_text = r.listen(source) #........................ listen for speech and store in audio_text variable
        with st.spinner(text='Transcribing your voice to text'):
            time.sleep(2)

        try:
            # using Google speech recognition to recognise the audio
            text = r.recognize_google(audio_text)
            # print(f' Did you say {text} ?')
            return text
        except:
            return "Sorry, I did not get that."

# # Create a function for text Talkback
# def Text_Speaker(your_command):
#     speaker_engine = pyttsx3.init() #................ initiate the talkback engine
#     speaker_engine.say(your_command) #............... Speak the command
#     speaker_engine.runAndWait() #.................... Run the engine



def main():
    st.markdown("<h1 style = ' color: #176B87'>SPEECH RECOGNITION APP</h1>", unsafe_allow_html = True)
    st.markdown("<h6 style = 'top-margin: 0rem; color: F8FF95'>built by Gbenga Olaosebikan</h1>", unsafe_allow_html = True)
    
    st.write("Click on the microphone to start speaking:")

    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        your_words_in_text = transcribe_speech()
        st.write("Transcription: ", your_words_in_text)
if __name__ == "__main__":
    main()

    #.....................................................


# import streamlit as st
# import speech_recognition as sr
# import pyttsx3
# import time
# import pandas as pd

# # Initialize the recognizer
# recognizer = sr.Recognizer()

# # Function to transcribe speech
# def transcribe_speech(audio_source, language="en-US"):
#     try:
#         with sr.AudioFile(audio_source) as source:
#             recognizer.adjust_for_ambient_noise(source)
#             st.write("Recording...")

#             # Record audio
#             audio = recognizer.listen(source)

#             st.write("Transcribing...")

#             # Recognize speech using the selected API and language
#             if language == "en-US":
#                 text = recognizer.recognize_google(audio)
#             elif language == "fr-FR":
#                 text = recognizer.recognize_google(audio, language="fr-FR")
#             # Add more languages as needed

#             return text
#     except sr.RequestError as e:
#         return f"Error: Could not request results; {e}"
#     except sr.UnknownValueError:
#         return "Error: Unable to recognize speech"

# # Streamlit app
# st.title("Speech Recognition App")

# # Choose speech recognition API
# selected_api = st.selectbox("Select Speech Recognition API", ["Google Speech Recognition"])

# # Choose language
# selected_language = st.selectbox("Select Language", ["en-US", "fr-FR"])

# # Upload audio file
# uploaded_audio = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

# if uploaded_audio:
#     st.audio(uploaded_audio)

#     if st.button("Transcribe Speech"):
#         # Transcribe speech and display result
#         result = transcribe_speech(uploaded_audio, language=selected_language)
#         st.write("Transcribed Text:")
#         st.write(result)

#         if st.button("Save Transcription"):
#             # Save transcribed text to a file
#             with open("transcription.txt", "w") as file:
#                 file.write(result)
#             st.write("Transcribed text saved as 'transcription.txt'")

# # Add pause and resume functionality (not implemented here)
# if st.button("Pause Recording"):
#     # Implement pause functionality here
#     pass

# if st.button("Resume Recording"):
#     # Implement resume functionality here
#     pass


#.................................................................

# import streamlit as st
# import speech_recognition as sr
# import pyttsx3
# import time
# import pandas as pd

# # Initialize the recognizer
# recognizer = sr.Recognizer()

# # Function to transcribe speech
# def transcribe_speech(language, selected_api):
#     try:
#         # Configure the recognizer for the selected language
#         if language:
#             recognizer.recognize_google(audio, language=language)
        
#         # Choose the API
#         if selected_api == "Google Speech Recognition":
#             text = recognizer.recognize_google(audio)
#         # Add more APIs as needed

#         st.write(f"Transcription: {text}")
#         return text
#     except sr.RequestError as e:
#         st.error(f"Could not request results; {e}")
#     except sr.UnknownValueError:
#         st.warning("No speech detected or could not understand audio")

# def main():
#     st.title("Speech Recognition App")

#     # Select the language
#     language = st.selectbox("Select Language", ["en-US", "fr-FR"])  # Add more languages as needed

#     # Select the speech recognition API
#     api_options = ["Google Speech Recognition"]
#     selected_api = st.selectbox("Select Speech Recognition API", api_options)

#     # Initialize the microphone
#     microphone = sr.Microphone()

#     # Record audio from the microphone
#     st.write("Click 'Start Recording' to begin.")
#     if st.button("Start Recording"):
#         with microphone as source:
#             audio = recognizer.listen(source)
#         st.success("Recording completed. Click 'Transcribe' to transcribe.")

#     # Transcribe speech
#     if st.button("Transcribe"):
#         text = transcribe_speech(language, selected_api)

#         # Save the transcribed text to a file
#         if st.button("Save to File"):
#             with open("transcribed_text.txt", "w") as file:
#                 file.write(text)
#             st.success("Transcribed text saved to 'transcribed_text.txt'.")

# if __name__ == "__main__":
#     main()


#..........................................


# import streamlit as st
# import speech_recognition as sr
# import pyttsx3
# import time
# import pandas as pd


# # Function to transcribe speech from the microphone
# def transcribe_speech():
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()

#     with microphone as source:
#         st.write("Listening... (Speak or Stop)")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source, timeout=10)

#     try:
#         text = recognizer.recognize_google(audio)
#         st.write(f"Transcription: {text}")
#     except sr.UnknownValueError:
#         st.write("No speech detected.")
#     except sr.RequestError as e:
#         st.error(f"Could not request results from Google Web Speech API; {e}")
#     except Exception as e:
#         st.error(f"An error occurred: {e}")

# def main():
#     st.title("Speech Recognition App")
#     st.markdown("Click the 'Start Recording' button to transcribe your speech.")

#     if st.button("Start Recording"):
#         transcribe_speech()

# if __name__ == "__main__":
#     main()

