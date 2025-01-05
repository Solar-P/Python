import openai

# Укажите ваш API-ключ
openai.api_key = "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"

# Функция для запроса
def get_response_from_gpt(prompt):
    try:
        # Новый формат для ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Убедитесь, что у вас есть доступ к этой модели
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        # Возвращаем ответ
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Ошибка API: {e}"

# Пример использования
if __name__ == "__main__":
    prompt = "Tell me a joke"
    print(get_response_from_gpt(prompt))
    