from ollama import Client

from app.config import Config


class AIClient:

    def __init__(self):
        self.client = Client(host=Config.OLLAMA_HOST)

    def chat(self, prompt: str) -> str:

        response = self.client.chat(
            model=Config.CHAT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    def embed(self, text: str):

        response = self.client.embed(
            model=Config.EMBEDDING_MODEL,
            input=text
        )

        return response["embeddings"][0]