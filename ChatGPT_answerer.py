import openai
import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext

# Insert your OpenAI API key
openai.api_key = ""  

# A function for capturing and converting audio to text
def transcribe_audio_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        log_text.insert(tk.END, "Speak up, I'm listening...\n")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="en-US")
            log_text.insert(tk.END, f"You said: {text}\n")
            return text
        except sr.UnknownValueError:
            log_text.insert(tk.END, "Speech recognition failed.\n")
            return None
        except sr.RequestError as e:
            log_text.insert(tk.END, f"Recognition error: {e}\n")
            return None

# Sending a request to ChatGPT
def get_response_from_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"
    
# Button click processing
def process_audio():
    user_input = transcribe_audio_to_text()
    if user_input:
        get_response_from_gpt(user_input)

# Creating an interface
window = tk.Tk()
window.title("Voice Assistant GPT")
window.geometry("600x400")

# Log
log_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=20)
log_text.pack(pady=10)

# Button
start_button = tk.Button(window, text="Start recording", command=process_audio, bg="green", fg="white", font=("Arial", 12))
start_button.pack(pady=10)

# Launching the app
window.mainloop()
