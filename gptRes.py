import openai

class ChatAssistant:
    def __init__(self, model):
        self.model = model

    def get_response(self, messages):
        message = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )
        response = message["choices"][0]["message"]["content"]
        return response
