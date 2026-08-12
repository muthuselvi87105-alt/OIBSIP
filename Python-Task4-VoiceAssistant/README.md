# 🎙️ Voice Assistant

## 📌 Project Description

The Voice Assistant is a Python-based application that listens to voice commands and responds to the user. It uses speech recognition to convert spoken words into text and text-to-speech technology to provide voice responses.

This project was developed as part of the Oasis Infobyte Python Programming Internship.

---

## 🚀 Features

- 🎤 Capture voice input using a microphone
- 🗣️ Convert speech into text
- 👋 Respond to "Hello" command
- 🕐 Tell the current time
- 📅 Tell the current date
- 🔎 Perform Google searches using voice commands
- 🔊 Respond using text-to-speech
- ❌ Handle voice recognition errors
- 🌐 Handle internet connection errors
- 🔁 Continue listening for multiple commands
- 🛑 Exit the application using the "exit" command

---

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- PyAudio
- datetime
- webbrowser

---

## 📂 Project Structure

```text
Python-Task4-VoiceAssistant/
│
├── voice.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 📦 Installation

Install the required Python libraries:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install PyAudio
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📄 requirements.txt

```text
SpeechRecognition
pyttsx3
PyAudio
```

---

## ▶️ How to Run

Open the project folder in VS Code and run:

```bash
python voice.py
```

The program will display:

```text
==============================
       Voice Assistant Started
==============================
Say: hello, time, date, search...
Say 'exit' to stop
==============================

Speak something...
```

---

## 🎤 Voice Commands

### 1. Hello

Say:

```text
Hello
```

Response:

```text
Hello! How can I help you?
```

---

### 2. Time

Say:

```text
What is the time?
```

The assistant displays and speaks the current time.

Example:

```text
Current Time: 07:56 PM
```

---

### 3. Date

Say:

```text
What is today's date?
```

The assistant displays and speaks the current date.

Example:

```text
Today's Date: 12-08-2026
```

---

### 4. Google Search

Say:

```text
Search Python tutorial
```

The assistant opens Google and searches for the requested topic.

---

### 5. Exit

Say:

```text
Exit
```

The voice assistant stops running.

---

## ⚠️ Error Handling

The application handles situations where the user's voice cannot be understood.

Example:

```text
Sorry, I could not understand your voice.
Please try again.
```

It also handles network errors when speech recognition cannot connect to the required service.

---

## 📸 Sample Output

```text
Voice Assistant Started

Speak something...
You said: hello

Hello! How can I help you?

Speak something...
You said: what is the time

Current Time: 07:56 PM

Speak something...
You said: what is today's date

Today's Date: 12-08-2026
```

---

## 📷 Screenshots

Add screenshots showing:

- Voice Assistant started
- Hello command
- Time command
- Date command
- Google Search command
- Exit command

---

## 🔮 Future Improvements

- Add weather information
- Add email sending functionality
- Add reminders
- Add general knowledge questions
- Add more voice commands
- Add a graphical user interface
- Improve natural language understanding

---

## 🔐 Privacy

This project uses speech recognition to process spoken commands. Voice input is converted into text for command processing. The application does not intentionally store voice recordings or personal conversations.

---

## 👩‍💻 Author

**Muthuselvi**

Python Developer | Full Stack Python Learner

---

## ⭐ Internship

Developed as part of the **Oasis Infobyte Python Programming Internship**.

**Track:** Python Programming

**Project:** Voice Assistant
