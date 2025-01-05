import openai
import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext

# Настройка OpenAI API
openai.api_key = "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"  # Вставьте ваш ключ OpenAI API

# Функция для захвата и преобразования звука в текст
def transcribe_audio_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        log_text.insert(tk.END, "Говорите, я слушаю...\n")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="en-US")
            log_text.insert(tk.END, f"Вы сказали: {text}\n")
            return text
        except sr.UnknownValueError:
            log_text.insert(tk.END, "Не удалось распознать речь.\n")
            return None
        except sr.RequestError as e:
            log_text.insert(tk.END, f"Ошибка распознавания: {e}\n")
            return None

# Отправка запроса в ChatGPT
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
        return f"Ошибка: {e}"
    
# Обработка нажатия кнопки
def process_audio():
    user_input = transcribe_audio_to_text()
    if user_input:
        get_response_from_gpt(user_input)

# Создание интерфейса
window = tk.Tk()
window.title("Голосовой помощник GPT")
window.geometry("600x400")

# Лог
log_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=20)
log_text.pack(pady=10)

# Кнопка
start_button = tk.Button(window, text="Начать запись", command=process_audio, bg="green", fg="white", font=("Arial", 12))
start_button.pack(pady=10)

# Запуск приложения
window.mainloop()
