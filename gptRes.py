import openai

class ChatAssistant:
    def __init__(self, model, userMessages):
        self.model = model
        self.userMessages = userMessages

    def get_response(self, messages):
        message = openai.ChatCompletion.create(
            model=self.model,
            messages= self.userMessages
        )
        response = message["choices"][0]["message"]["content"]
        return response
