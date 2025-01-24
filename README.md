## VISION: Your AI Assistant
## About VISION
VISION was created as a solution to a problem I encountered when I noticed visually impaired students struggling to give online exams during the COVID-19 pandemic. The lack of accessible tools to assist them with exams inspired me to develop this software, aiming to make online exams more inclusive for everyone. VISION combines Speech-to-Text (STT) and Text-to-Speech (TTS) technologies to create an interactive and user-friendly experience for students, especially for those with visual impairments.

## Technologies Used
Speech-to-Text (STT)
• SpeechRecognition: This library allows VISION to recognize speech from a microphone and convert it to text, which the AI assistant then processes.
Text-to-Speech (TTS)
• pyttsx3: This library converts text into speech, allowing VISION to interact with users by reading aloud instructions, questions, and feedback.
Streamlit
• Streamlit: Used to create the web interface for VISION. Streamlit allows the software to provide a dynamic and easy-to-use platform to run and interact with the assistant.

## Folder Structure
Below is a breakdown of the folder structure for VISION:

    VISION/
    │
    ├── app.py               # Main Python file to run the application
    │
    ├── vision/
    │   ├── questions.txt    # Text file containing the questions for the exam
    │   ├── answers.txt      # Text file containing the correct answers for the exam
    │
    ├── assets/              # Folder for storing assets like logos or images
    │
    ├── requirements.txt     # Python dependencies for VISION
    │
    └── README.md            # This README file
    
## Explanation of Files
• questions.txt: This file contains the set of questions that the assistant will ask the user during the exam. Each line represents a question. The questions are read aloud using the TTS technology and displayed in the UI for the user to respond to.
• answers.txt: This file contains the correct answers corresponding to the questions in `questions.txt`. The assistant uses this file to compare the user’s response to the correct answer. It provides feedback on whether the answer is correct or not.
How to Use VISION
Step 1: Install Dependencies
Ensure you have Python installed. Then, create a virtual environment and install the required dependencies by running the following commands:

    pip install -r requirements.txt
    
Step 2: Prepare the Questions and Answers
You need to prepare two text files:
1. questions.txt: Place your exam questions here. Each question should be on a new line.
2. answers.txt: Place the correct answers here, corresponding to each question. Answers should be in the same order as the questions.
Step 3: Run the Application
Once everything is set up, run the application by executing the following command:

    streamlit run app.py
    
Step 4: Interact with VISION
• The assistant will greet you and ask if you are ready to start the exam.
• VISION will read the questions aloud and listen to your spoken responses.
• After each question, it will provide feedback on whether your answer was correct or incorrect.
• Once all questions are answered, VISION will thank you for completing the exam.
Step 5: Access the Results
After the exam, you can see the results, including whether each answer was correct or incorrect. At the end of the exam, you’ll receive a message thanking you for completing the exam.
Troubleshooting
• If you face issues with the `SpeechRecognition` or `pyttsx3` libraries, make sure your microphone is working correctly and that your audio drivers are up to date.
• Ensure that the `questions.txt` and `answers.txt` files are properly formatted and placed in the correct folder (`vision/`).
## Conclusion
VISION is a powerful tool designed to enhance the online exam experience for visually impaired students, making it easier for them to take exams independently using voice-based interactions. By combining Speech-to-Text and Text-to-Speech technologies, VISION is paving the way for more inclusive and accessible education.

## Snapshots: 
![vision](https://github.com/user-attachments/assets/78dad51d-b7ed-4c96-a866-1110b22a05bf)
