import streamlit as st
import pyttsx3
import speech_recognition as sr
import time
from streamlit_chat import message

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak text
def speak(audio):
    """Speak the given audio using pyttsx3."""
    engine.say(audio)
    engine.runAndWait()

# Function to take voice input from the user
def takeCommand():
    """Take voice input from the user and return the text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.text("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            st.text("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            return query.lower()
        except Exception as e:
            st.text("Say that again, please...")
            return "none"

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>VISION</h1>", unsafe_allow_html=True)

# Initialize session state to store conversation
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

# Initialize a flag for exam completion
if 'exam_completed' not in st.session_state:
    st.session_state['exam_completed'] = False

# Automatically start the assistant
if not st.session_state['exam_completed']:
    speak("Initializing Vision...")
    st.session_state.conversation.append({"message": "Initializing Vision...", "is_user": False})

    # Wait for user to confirm to start the exam
    time.sleep(1)
    speak("Do you want to start the exam?")
    st.session_state.conversation.append({"message": "Do you want to start the exam?", "is_user": False})

# Render only if the exam is not completed
if not st.session_state['exam_completed']:
    for i, message_data in enumerate(st.session_state['conversation']):
        key = f"{i}_{message_data['message']}_{message_data['is_user']}"
        if message_data['is_user']:
            message(f"*{message_data['message']}*", is_user=True, key=key, avatar_style="lorelei")
        else:
            message(f"*{message_data['message']}*", is_user=False, key=key, avatar_style="bottts")  # Bot avatar

# Ask for user response and listen in real-time
if not st.session_state['exam_completed']:
    query = takeCommand()
    st.session_state.conversation.append({"message": query, "is_user": True})

    # Display the user response
    message(f"*{query}*", is_user=True, key=f"user_{len(st.session_state['conversation']) - 1}", avatar_style="lorelei")

    if "yes" in query:
        speak("Okay, all the best.")
        st.session_state.conversation.append({"message": "Okay, all the best.", "is_user": False})

        try:
            # Open questions and answers from files
            with open(r"C:\Users\DELL\OneDrive\Desktop\Vision\vision\questions.txt", "r") as q_file, \
                 open(r"C:\Users\DELL\OneDrive\Desktop\Vision\vision\answers.txt", "r") as a_file:

                questions = q_file.readlines()
                answers = a_file.readlines()

                for i, question in enumerate(questions):
                    speak(question.strip())
                    st.session_state.conversation.append({"message": question.strip(), "is_user": False})
                    message(f"*{question.strip()}*", is_user=False, key=f"assistant_q_{i}", avatar_style="bottts")  # Bot avatar

                    # Wait for user's response
                    user_answer = takeCommand()
                    st.session_state.conversation.append({"message": user_answer, "is_user": True})
                    message(f"*{user_answer}*", is_user=True, key=f"user_answer_{i}", avatar_style="lorelei")

                    if i < len(answers):
                        correct_answer = answers[i].strip().lower()
                        if correct_answer == user_answer:
                            speak("Correct")
                            st.session_state.conversation.append({"message": "Correct", "is_user": False})
                            message("*Correct*", is_user=False, key=f"assistant_correct_{i}", avatar_style="bottts")
                        else:
                            speak("Incorrect")
                            st.session_state.conversation.append({"message": "Incorrect", "is_user": False})
                            message("*Incorrect*", is_user=False, key=f"assistant_incorrect_{i}", avatar_style="bottts")
                    else:
                        speak("No answer found for this question.")
                        st.session_state.conversation.append({"message": "No answer found for this question.", "is_user": False})
                        message("*No answer found for this question.*", is_user=False, key=f"assistant_no_answer_{i}", avatar_style="bottts")

            # Exam completion message
            speak("You have completed the exam. Thank you!")
            st.session_state.conversation.append({"message": "You have completed the exam. Thank you!", "is_user": False})
            message("*You have completed the exam. Thank you!*", is_user=False, key="exam_end", avatar_style="bottts")

            # Mark the exam as completed
            st.session_state['exam_completed'] = True

        except FileNotFoundError:
            st.error("Questions or answers file not found.")
    else:
        speak("Okay, let me know when you're ready.")
        st.session_state.conversation.append({"message": "Okay, let me know when you're ready.", "is_user": False})

# Prevent re-rendering after exam completion
if st.session_state['exam_completed']:
    st.success("Exam is completed.")
