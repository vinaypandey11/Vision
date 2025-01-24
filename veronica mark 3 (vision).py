import streamlit as st
import pyttsx3
import speech_recognition as sr
import datetime

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    st.text(f"Assistant: {audio}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.text("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            st.text("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            st.text(f"User: {query}")
            return query.lower()
        except Exception as e:
            st.text("Say that again, please...")
            return "none"

# Streamlit UI
st.title("VISION: Your AI Assistant")

# Automatically start the assistant
speak("Initializing Vision...")

# Delay added for clarity in speech output
import time
time.sleep(1)

speak("Do you want to start the exam?")
query = takeCommand()

if "yes" in query:
    speak("Okay, all the best.")

    try:
        with open(r"C:\Users\DELL\OneDrive\Desktop\Vision\vision\questions.txt", "r") as q_file, \
             open(r"C:\Users\DELL\OneDrive\Desktop\Vision\vision\answers.txt", "r") as a_file:

            questions = q_file.readlines()
            answers = a_file.readlines()

            for i, question in enumerate(questions):
                speak(question.strip())
                user_answer = takeCommand()

                if i < len(answers):
                    correct_answer = answers[i].strip().lower()
                    if correct_answer == user_answer:
                        speak("Correct")
                    else:
                        speak("Incorrect")
                else:
                    speak("No answer found for this question.")

            speak("You have completed the exam. Thank you!")

    except FileNotFoundError:
        st.error("Questions or answers file not found.")
else:
    speak("Okay, let me know when you're ready.")
