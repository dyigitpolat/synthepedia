import api_keys

import openai
import random

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def completion_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

class OpenAIClient:
    def __init__(self, model="gpt-3.5-turbo", system_prompt=""):
        openai.organization = "org-YyEX4wI80xFZTZY6IjsS59V5"
        openai.api_key = api_keys.openai_api_key

        self.model = model
        self.system_prompt = system_prompt

    def respond(self, text):
        chat_history = []
        print("Query: ", text)
        chat_history.append({"role": "system", "content": self.system_prompt})
        chat_history.append({"role": "user", "content": text})
        try:
            response = completion_with_backoff(
                model=self.model,
                messages=list(chat_history),
                user=str(random.randint(0, 1000000000)),
            ).choices[0].message

            return response.content
        
        except Exception as e:
            print("Error: ", e)
            chat_history.messages.pop(0)
            return "{{}}"